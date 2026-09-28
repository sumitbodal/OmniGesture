"""
OmniGesture v2.0 - AI-Powered Hands-Free PC Controller
=======================================================
An advanced accessibility tool that uses edge AI to control
your Snapdragon-powered HP PC entirely through hand gestures.

Supported Gestures:
  - Point (Index finger)  -> Move cursor
  - Pinch (Thumb + Index) -> Left Click
  - Peace (Index + Middle) -> Double Click  
  - Fist (All fingers closed) -> Right Click
  - Open Palm (All fingers up) -> Scroll Mode
  - Thumbs Up -> Toggle Drag Lock

Built with: MediaPipe (Edge AI) + OpenCV + PyAutoGUI
Target: Snapdragon-powered HP PCs
"""

import cv2
import mediapipe as mp
import pyautogui
import math
import time
import threading
import tkinter as tk
from tkinter import ttk

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

# ============================================================
# MediaPipe Setup
# ============================================================
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# ============================================================
# Gesture Recognition Engine
# ============================================================

class GestureRecognizer:
    """Recognizes hand gestures from MediaPipe landmarks."""

    def __init__(self):
        self.prev_gesture = "NONE"

    def is_finger_up(self, landmarks, finger_tip, finger_pip):
        """Check if a finger is extended (tip above PIP joint)."""
        return landmarks[finger_tip].y < landmarks[finger_pip].y

    def is_thumb_up(self, landmarks):
        """Check if thumb is extended (using x-axis for thumb)."""
        return landmarks[4].x < landmarks[3].x  # For right hand (mirrored)

    def get_finger_states(self, landmarks):
        """Get the up/down state of all 5 fingers."""
        thumb = self.is_thumb_up(landmarks)
        index = self.is_finger_up(landmarks, 8, 6)
        middle = self.is_finger_up(landmarks, 12, 10)
        ring = self.is_finger_up(landmarks, 16, 14)
        pinky = self.is_finger_up(landmarks, 20, 18)
        return [thumb, index, middle, ring, pinky]

    def get_pinch_distance(self, landmarks, img_w, img_h):
        """Calculate pixel distance between thumb tip and index tip."""
        ix = int(landmarks[8].x * img_w)
        iy = int(landmarks[8].y * img_h)
        tx = int(landmarks[4].x * img_w)
        ty = int(landmarks[4].y * img_h)
        return math.hypot(tx - ix, ty - iy)

    def recognize(self, landmarks, img_w, img_h):
        """Recognize the current gesture from hand landmarks."""
        fingers = self.get_finger_states(landmarks)
        thumb, index, middle, ring, pinky = fingers
        pinch_dist = self.get_pinch_distance(landmarks, img_w, img_h)

        # Pinch: Thumb and Index very close together
        if pinch_dist < 35:
            return "PINCH"

        # Thumbs Up: Only thumb is up
        if thumb and not index and not middle and not ring and not pinky:
            return "THUMBS_UP"

        # Fist: All fingers are down
        if not thumb and not index and not middle and not ring and not pinky:
            return "FIST"

        # Peace: Index and Middle up, others down
        if index and middle and not ring and not pinky:
            return "PEACE"

        # Open Palm: All fingers are up
        if thumb and index and middle and ring and pinky:
            return "OPEN_PALM"

        # Point: Only Index finger up
        if index and not middle and not ring and not pinky:
            return "POINT"

        return "NONE"


# ============================================================
# OmniGesture Controller (Camera + Gesture Processing Thread)
# ============================================================

class OmniGestureController:
    """Main controller that processes the camera feed and maps gestures to actions."""

    def __init__(self):
        self.running = False
        self.thread = None
        self.gesture_recognizer = GestureRecognizer()

        # Screen info
        self.screen_w, self.screen_h = pyautogui.size()

        # Mouse smoothing
        self.prev_x = 0
        self.prev_y = 0
        self.smoothening = 5

        # Click cooldowns
        self.last_click_time = 0
        self.last_right_click_time = 0
        self.last_double_click_time = 0
        self.last_scroll_time = 0
        self.last_thumbsup_time = 0
        self.click_cooldown = 0.5

        # Drag state
        self.drag_active = False

        # Scroll tracking
        self.scroll_base_y = None

        # Stats
        self.current_gesture = "NONE"
        self.fps = 0
        self.frame_count = 0

        # Callbacks for UI updates
        self.on_gesture_change = None
        self.on_fps_update = None
        self.on_status_change = None
        self.on_log_event = None

        # Settings
        self.sensitivity = 5
        self.click_cooldown = 0.5

    def start(self):
        """Start the gesture tracking in a background thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
            if self.on_status_change:
                self.on_status_change("TRACKING")

    def stop(self):
        """Stop the gesture tracking."""
        self.running = False
        if self.drag_active:
            pyautogui.mouseUp()
            self.drag_active = False
        if self.on_status_change:
            self.on_status_change("STOPPED")

    def _log(self, message):
        """Log an event to the UI."""
        if self.on_log_event:
            self.on_log_event(message)

    def _run(self):
        """Main processing loop (runs in background thread)."""
        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
            running_mode=VisionRunningMode.VIDEO,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        with HandLandmarker.create_from_options(options) as landmarker:
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                self._log("ERROR: Cannot open webcam!")
                if self.on_status_change:
                    self.on_status_change("ERROR")
                return

            self._log("Camera connected successfully")
            start_time = time.time()
            fps_timer = time.time()
            frame_count = 0

            while self.running and cap.isOpened():
                success, img = cap.read()
                if not success:
                    break

                img = cv2.flip(img, 1)
                h, w, c = img.shape
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
                frame_timestamp_ms = int((time.time() - start_time) * 1000)

                result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)

                # FPS calculation
                frame_count += 1
                if time.time() - fps_timer >= 1.0:
                    self.fps = frame_count
                    frame_count = 0
                    fps_timer = time.time()
                    if self.on_fps_update:
                        self.on_fps_update(self.fps)

                if result and result.hand_landmarks:
                    for hand_landmarks in result.hand_landmarks:
                        # Draw hand skeleton on camera feed
                        self._draw_landmarks(img, hand_landmarks, w, h)

                        # Recognize gesture
                        gesture = self.gesture_recognizer.recognize(hand_landmarks, w, h)

                        if gesture != self.current_gesture:
                            self.current_gesture = gesture
                            if self.on_gesture_change:
                                self.on_gesture_change(gesture)

                        # Execute gesture action
                        self._execute_gesture(gesture, hand_landmarks, w, h)

                        # Draw gesture label on camera feed
                        self._draw_gesture_label(img, gesture)
                else:
                    if self.current_gesture != "NONE":
                        self.current_gesture = "NONE"
                        self.scroll_base_y = None
                        if self.on_gesture_change:
                            self.on_gesture_change("NO HAND")

                # Draw FPS on camera feed
                cv2.putText(img, f"FPS: {self.fps}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                cv2.imshow("OmniGesture v2.0 - Press Q to quit", img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False
                    break

            cap.release()
            cv2.destroyAllWindows()
            if self.on_status_change:
                self.on_status_change("STOPPED")

    def _draw_landmarks(self, img, landmarks, w, h):
        """Draw hand landmarks and connections on the image."""
        # Define hand connections
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),      # Thumb
            (0, 5), (5, 6), (6, 7), (7, 8),       # Index
            (0, 9), (9, 10), (10, 11), (11, 12),   # Middle
            (0, 13), (13, 14), (14, 15), (15, 16),  # Ring
            (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky
            (5, 9), (9, 13), (13, 17)               # Palm
        ]

        # Draw connections
        for start_idx, end_idx in connections:
            x1 = int(landmarks[start_idx].x * w)
            y1 = int(landmarks[start_idx].y * h)
            x2 = int(landmarks[end_idx].x * w)
            y2 = int(landmarks[end_idx].y * h)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2)

        # Draw landmark points
        for i, lm in enumerate(landmarks):
            cx, cy = int(lm.x * w), int(lm.y * h)
            color = (255, 0, 255)
            if i in [4, 8]:  # Thumb and Index tips
                color = (0, 255, 0)
                cv2.circle(img, (cx, cy), 8, color, -1)
            else:
                cv2.circle(img, (cx, cy), 4, color, -1)

    def _draw_gesture_label(self, img, gesture):
        """Draw the current gesture name on the camera feed."""
        gesture_labels = {
            "POINT": "POINTING - Moving Cursor",
            "PINCH": "PINCH - Left Click",
            "PEACE": "PEACE - Double Click",
            "FIST": "FIST - Right Click",
            "OPEN_PALM": "OPEN PALM - Scroll Mode",
            "THUMBS_UP": "THUMBS UP - Toggle Drag",
            "NONE": "No Gesture Detected",
        }
        label = gesture_labels.get(gesture, gesture)
        
        # Background rectangle
        cv2.rectangle(img, (10, 440), (400, 475), (0, 0, 0), -1)
        
        # Gesture color
        colors = {
            "POINT": (255, 255, 0),
            "PINCH": (0, 255, 0),
            "PEACE": (255, 0, 255),
            "FIST": (0, 0, 255),
            "OPEN_PALM": (255, 165, 0),
            "THUMBS_UP": (0, 255, 255),
            "NONE": (128, 128, 128),
        }
        color = colors.get(gesture, (255, 255, 255))
        cv2.putText(img, label, (15, 465), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    def _execute_gesture(self, gesture, landmarks, img_w, img_h):
        """Execute the system action corresponding to the detected gesture."""
        current_time = time.time()

        if gesture == "POINT" or gesture == "PINCH" or gesture == "OPEN_PALM":
            # Move cursor using index finger position
            index_x = landmarks[8].x
            index_y = landmarks[8].y

            screen_x = int(index_x * self.screen_w)
            screen_y = int(index_y * self.screen_h)

            # Smooth movement
            self.prev_x += (screen_x - self.prev_x) / self.sensitivity
            self.prev_y += (screen_y - self.prev_y) / self.sensitivity

            try:
                pyautogui.moveTo(self.prev_x, self.prev_y)
            except Exception:
                pass

        if gesture == "PINCH":
            if current_time - self.last_click_time > self.click_cooldown:
                pyautogui.click()
                self._log("Left Click")
                self.last_click_time = current_time

        elif gesture == "FIST":
            if current_time - self.last_right_click_time > self.click_cooldown:
                pyautogui.rightClick()
                self._log("Right Click")
                self.last_right_click_time = current_time

        elif gesture == "PEACE":
            if current_time - self.last_double_click_time > self.click_cooldown:
                pyautogui.doubleClick()
                self._log("Double Click")
                self.last_double_click_time = current_time

        elif gesture == "OPEN_PALM":
            # Scroll based on hand vertical movement
            palm_y = landmarks[9].y  # Middle finger base
            if self.scroll_base_y is None:
                self.scroll_base_y = palm_y
            else:
                diff = self.scroll_base_y - palm_y
                if abs(diff) > 0.03 and current_time - self.last_scroll_time > 0.1:
                    scroll_amount = int(diff * 10)
                    pyautogui.scroll(scroll_amount)
                    self.last_scroll_time = current_time

        elif gesture == "THUMBS_UP":
            if current_time - self.last_thumbsup_time > 1.0:
                if self.drag_active:
                    pyautogui.mouseUp()
                    self.drag_active = False
                    self._log("Drag Released")
                else:
                    pyautogui.mouseDown()
                    self.drag_active = True
                    self._log("Drag Started")
                self.last_thumbsup_time = current_time

        if gesture != "OPEN_PALM":
            self.scroll_base_y = None


# ============================================================
# Tkinter Control Panel UI
# ============================================================

class ControlPanel:
    """A simple control panel window for OmniGesture."""

    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("OmniGesture v2.0 - Control Panel")
        self.root.geometry("420x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        # Wire up callbacks
        self.controller.on_gesture_change = self._update_gesture
        self.controller.on_fps_update = self._update_fps
        self.controller.on_status_change = self._update_status
        self.controller.on_log_event = self._add_log

        self._build_ui()

    def _build_ui(self):
        """Build the entire UI."""
        bg = "#1e1e2e"
        fg = "#cdd6f4"
        accent = "#89b4fa"

        # Title
        title_frame = tk.Frame(self.root, bg=bg)
        title_frame.pack(fill="x", padx=15, pady=(15, 5))
        tk.Label(title_frame, text="OmniGesture v2.0", font=("Segoe UI", 18, "bold"),
                 bg=bg, fg=accent).pack()
        tk.Label(title_frame, text="AI-Powered Hands-Free PC Controller",
                 font=("Segoe UI", 9), bg=bg, fg="#6c7086").pack()

        # Status Section
        status_frame = tk.LabelFrame(self.root, text=" Status ", font=("Segoe UI", 10, "bold"),
                                      bg=bg, fg=fg, bd=1, relief="groove")
        status_frame.pack(fill="x", padx=15, pady=10)

        row1 = tk.Frame(status_frame, bg=bg)
        row1.pack(fill="x", padx=10, pady=5)
        tk.Label(row1, text="Status:", font=("Segoe UI", 10), bg=bg, fg=fg).pack(side="left")
        self.status_label = tk.Label(row1, text="STOPPED", font=("Segoe UI", 10, "bold"),
                                      bg=bg, fg="#f38ba8")
        self.status_label.pack(side="right")

        row2 = tk.Frame(status_frame, bg=bg)
        row2.pack(fill="x", padx=10, pady=5)
        tk.Label(row2, text="Gesture:", font=("Segoe UI", 10), bg=bg, fg=fg).pack(side="left")
        self.gesture_label = tk.Label(row2, text="---", font=("Segoe UI", 10, "bold"),
                                       bg=bg, fg="#a6e3a1")
        self.gesture_label.pack(side="right")

        row3 = tk.Frame(status_frame, bg=bg)
        row3.pack(fill="x", padx=10, pady=(5, 10))
        tk.Label(row3, text="FPS:", font=("Segoe UI", 10), bg=bg, fg=fg).pack(side="left")
        self.fps_label = tk.Label(row3, text="0", font=("Segoe UI", 10, "bold"),
                                   bg=bg, fg="#fab387")
        self.fps_label.pack(side="right")

        # Controls
        ctrl_frame = tk.LabelFrame(self.root, text=" Controls ", font=("Segoe UI", 10, "bold"),
                                    bg=bg, fg=fg, bd=1, relief="groove")
        ctrl_frame.pack(fill="x", padx=15, pady=5)

        btn_frame = tk.Frame(ctrl_frame, bg=bg)
        btn_frame.pack(fill="x", padx=10, pady=10)

        self.start_btn = tk.Button(btn_frame, text="START TRACKING", font=("Segoe UI", 11, "bold"),
                                    bg="#a6e3a1", fg="#1e1e2e", relief="flat", padx=15, pady=8,
                                    command=self._start_tracking)
        self.start_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.stop_btn = tk.Button(btn_frame, text="STOP", font=("Segoe UI", 11, "bold"),
                                   bg="#f38ba8", fg="#1e1e2e", relief="flat", padx=15, pady=8,
                                   command=self._stop_tracking, state="disabled")
        self.stop_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))

        # Sensitivity slider
        sens_frame = tk.Frame(ctrl_frame, bg=bg)
        sens_frame.pack(fill="x", padx=10, pady=(0, 10))
        tk.Label(sens_frame, text="Smoothness:", font=("Segoe UI", 9), bg=bg, fg=fg).pack(side="left")
        self.sens_slider = tk.Scale(sens_frame, from_=1, to=10, orient="horizontal",
                                     bg=bg, fg=fg, highlightthickness=0, troughcolor="#313244",
                                     command=self._update_sensitivity)
        self.sens_slider.set(5)
        self.sens_slider.pack(side="right", expand=True, fill="x", padx=(10, 0))

        # Gesture Reference
        ref_frame = tk.LabelFrame(self.root, text=" Gesture Guide ", font=("Segoe UI", 10, "bold"),
                                   bg=bg, fg=fg, bd=1, relief="groove")
        ref_frame.pack(fill="x", padx=15, pady=5)

        gestures = [
            ("Point (Index Up)", "Move Cursor", "#89b4fa"),
            ("Pinch (Thumb+Index)", "Left Click", "#a6e3a1"),
            ("Peace (Index+Middle)", "Double Click", "#cba6f7"),
            ("Fist (All Down)", "Right Click", "#f38ba8"),
            ("Open Palm (All Up)", "Scroll Up/Down", "#fab387"),
            ("Thumbs Up", "Toggle Drag", "#f9e2af"),
        ]

        for gesture_name, action, color in gestures:
            row = tk.Frame(ref_frame, bg=bg)
            row.pack(fill="x", padx=10, pady=2)
            tk.Label(row, text=gesture_name, font=("Segoe UI", 9), bg=bg, fg=color,
                     anchor="w", width=22).pack(side="left")
            tk.Label(row, text=action, font=("Segoe UI", 9, "bold"), bg=bg, fg=fg,
                     anchor="e").pack(side="right")

        # Add padding at bottom of gesture guide
        tk.Frame(ref_frame, bg=bg, height=5).pack()

        # Activity Log
        log_frame = tk.LabelFrame(self.root, text=" Activity Log ", font=("Segoe UI", 10, "bold"),
                                   bg=bg, fg=fg, bd=1, relief="groove")
        log_frame.pack(fill="both", expand=True, padx=15, pady=(5, 15))

        self.log_text = tk.Text(log_frame, height=5, font=("Consolas", 9),
                                 bg="#313244", fg="#cdd6f4", relief="flat",
                                 wrap="word", state="disabled")
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _start_tracking(self):
        self.controller.start()
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self._add_log("Tracking started")

    def _stop_tracking(self):
        self.controller.stop()
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self._add_log("Tracking stopped")

    def _update_sensitivity(self, val):
        self.controller.sensitivity = int(val)

    def _update_gesture(self, gesture):
        try:
            self.root.after(0, lambda: self.gesture_label.config(text=gesture))
        except Exception:
            pass

    def _update_fps(self, fps):
        try:
            self.root.after(0, lambda: self.fps_label.config(text=str(fps)))
        except Exception:
            pass

    def _update_status(self, status):
        colors = {"TRACKING": "#a6e3a1", "STOPPED": "#f38ba8", "ERROR": "#f38ba8"}
        try:
            self.root.after(0, lambda: self.status_label.config(
                text=status, fg=colors.get(status, "#cdd6f4")))
        except Exception:
            pass

    def _add_log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        try:
            def _insert():
                self.log_text.config(state="normal")
                self.log_text.insert("end", log_entry)
                self.log_text.see("end")
                self.log_text.config(state="disabled")
            self.root.after(0, _insert)
        except Exception:
            pass

    def _on_close(self):
        self.controller.stop()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


# ============================================================
# Main Entry Point
# ============================================================

if __name__ == "__main__":
    print("OmniGesture v2.0 - Starting Control Panel...")
    controller = OmniGestureController()
    panel = ControlPanel(controller)
    panel.run()
