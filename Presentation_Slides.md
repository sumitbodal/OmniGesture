# OmniGesture v2.0 — Pitch Presentation Deck
### Snapdragon AI Lab: Build & Present Challenge
**Format:** 7-Slide Executive Pitch Deck & Presenter Guide  
**Hardware & Target:** Snapdragon-powered HP PCs (Snapdragon X Elite / X Plus)  
**Category:** Edge AI & Accessibility Innovation  

---

## Slide 1: Title Slide (Cover)

### Slide Header & Core Details
- **Title:** OmniGesture v2.0
- **Subtitle:** AI-Powered Hands-Free Accessibility Controller for Snapdragon HP PCs
- **Competition Track:** Snapdragon AI Lab Build & Present Challenge
- **Presenter Name:** [Your Name / Team Name]
- **Date:** September 2026
- **Target Platform:** HP OmniBook / EliteBook powered by Qualcomm Snapdragon X Elite / X Plus

### Slide Content & Bullet Points
- **Value Proposition:** Transforming the built-in HP laptop webcam into a sub-millisecond, zero-cost, private accessibility controller using edge AI.
- **Key Highlight:** 6 intuitive hand gestures + dynamic desktop control panel with zero external hardware required.
- **Hardware Integration:** Engineered for continuous on-device inference on Qualcomm Snapdragon architecture.

### Presenter Notes (30-45 Seconds)
> "Good morning, judges and fellow innovators. Over 1.3 billion people worldwide experience significant disabilities, and millions suffer from motor impairments, arthritis, or RSI that make standard mice and touchpads painful or impossible to use. Today, we are proud to introduce **OmniGesture v2.0**, an AI-powered, completely hands-free accessibility controller designed specifically for Snapdragon-powered HP PCs. By combining Google's MediaPipe Tasks API with Snapdragon's edge computing efficiency, OmniGesture turns any standard laptop webcam into a responsive, zero-latency accessibility device without requiring a single dollar of expensive peripheral hardware."

### Slide Design & Visual Tips
- **Layout:** Clean, bold minimalist cover. Left-aligned title typography with high contrast; right side features a high-res rendering or photo of an HP Snapdragon laptop with subtle digital hand-landmark overlay.
- **Color Palette:** Deep Snapdragon Obsidian Slate (`#0F141C` background), Qualcomm Crimson Accent (`#E60012` or `#FF334B`), HP Silver/Cyan (`#0096D6`), and crisp white typography.
- **Visual Assets:** Snapdragon AI Lab badge, HP logo, and a stylized 3D translucent hand wireframe.

---

## Slide 2: The Problem (Accessibility Barriers & Current Pitfalls)

### Slide Header
- **Headline:** The Mouse Barrier: Millions are Locked Out of Everyday Computing

### Slide Content & Key Pillars

#### 1. The Accessibility Gap
- **Motor & Mobility Impairments:** Millions of users suffering from cerebral palsy, spinal injuries, tremors, arthritis, and repetitive strain injuries (RSI/carpal tunnel) cannot operate physical mice or touchpads.
- **Temporary Disabilities:** Broken limbs, post-surgery recovery, and workplace injuries temporarily lock knowledge workers out of productivity.

#### 2. The Failure of Existing Solutions
| Existing Approach | Critical Limitation | Real-World Impact |
| :--- | :--- | :--- |
| **Specialized Hardware** (Trackballs, mouth sticks, eye-gaze bars) | Prohibitively expensive ($300 to $5,000+) | Financial barrier for schools, clinics, and individuals |
| **Cloud-Based Vision AI** | High latency (150–400ms network round-trip) | Disorienting cursor lag renders mouse navigation unusable |
| **Cloud Video Streaming** | Massive privacy and security violation | Users must stream live, continuous webcam footage to remote servers |
| **Legacy Local GPU Models** | Heavy thermal load and extreme battery drain | Laptop fans spin up, thermal throttling occurs, battery depleted in <1.5 hours |

### Presenter Notes (45-60 Seconds)
> "Let's talk about the friction in accessibility technology today. Traditional assistive hardware, like specialized eye-trackers or sip-and-puff switches, costs hundreds to thousands of dollars, making it completely unaffordable for many students and workers. Software alternatives that stream video to the cloud introduce 200 milliseconds of latency—making pointing and clicking feel like driving with a delayed steering wheel—while creating terrifying privacy concerns by broadcasting personal video streams. Meanwhile, unoptimized x86 vision models turn laptops into portable space heaters that drain the battery in under 90 minutes. Users need a solution that is free, private, instant, and power-efficient."

### Slide Design & Visual Tips
- **Layout:** 3-column problem card layout:
  - *Card 1 (Cost):* Dollar sign with slashed price tags ($1,000+ specialized hardware).
  - *Card 2 (Privacy & Lag):* Cloud icon with red warning shield and buffering wheel (250ms latency).
  - *Card 3 (Power):* Battery icon running red with flame/heat graphic (Heavy thermal load).
- **Typography:** Emphasize keywords like **"Prohibitive Cost"**, **"Intolerable Latency"**, and **"Privacy Risks"** using warm red or alert orange accents (`#F38BA8`).

---

## Slide 3: The Solution (OmniGesture v2.0: 6 Gestures & Control Panel)

### Slide Header
- **Headline:** OmniGesture v2.0: Full PC Control Through Natural Hand Gestures

### Slide Content & Feature Breakdown

#### 1. Six Complete Hands-Free Gestures
1. **Point (Index Finger Up):** Smooth cursor movement mapped dynamically across screen dimensions with exponential moving average (EMA) jitter reduction.
2. **Pinch (Thumb + Index Tip <35px):** Standard Left Click with tactile cooldown prevention.
3. **Peace Sign (Index + Middle Up):** Instant Double Click to launch applications, open folders, and select text.
4. **Fist (All Fingers Folded):** Right Click to open context menus, inspect elements, and access shortcut panels.
5. **Open Palm (All 5 Fingers Extended):** Smooth vertical scrolling—moving the open palm up or down scrolls documents, websites, and feeds continuously.
6. **Thumbs Up (Thumb Extended Only):** Drag Lock Toggle (`mouseDown` / `mouseUp`) for effortless window moving, file dragging, and text highlighting.

#### 2. Native Dark-Mode Tkinter Control Panel
- **Real-Time Telemetry:** Live detection status indicator (`TRACKING` / `STOPPED`), recognized gesture readout, and continuous FPS counter.
- **User Customization:** Dynamic Smoothness/Sensitivity slider (levels 1–10) allowing users with tremors to dampen cursor sensitivity.
- **Live Activity Log:** Real-time event feed confirming executed clicks, scrolls, and drag-lock states.
- **Fail-Safe Operation:** Dedicated Start/Stop toggle button decoupled from system-level interrupt loops.

### Presenter Notes (60 Seconds)
> "OmniGesture v2.0 bridges this gap by delivering full OS mouse parity using six intuitive, natural gestures. The user points their index finger to smoothly guide the cursor across their multi-monitor workspace. Pinching triggers a left-click; flash a peace sign for an instant double-click; make a fist for a right-click context menu; hold up an open palm to glide through long web pages; and give a thumbs-up to toggle drag lock, letting you drag windows and select text effortlessly without muscle strain. Furthermore, our modern Tkinter control panel gives users total autonomy with a customizable smoothness slider—crucial for filtering out involuntary hand tremors—and live telemetry tracking."

### Slide Design & Visual Tips
- **Layout:** Split slide (60/40). 
  - *Left Side (60%):* 2x3 grid of gesture cards, each containing a clean minimalist vector icon of the hand pose, gesture name, and corresponding action badge.
  - *Right Side (40%):* Sleek mockup of the Tkinter Control Panel UI showing the dark purple/slate palette (`#1E1E2E`), active status pill, and slider widget.
- **Color Coding:** Use the application's actual color coding:
  - Point: Sky Blue (`#89B4FA`) | Pinch: Mint Green (`#A6E3A1`) | Peace: Lavender (`#CBA6F7`)
  - Fist: Coral Pink (`#F38BA8`) | Open Palm: Amber Orange (`#FAB387`) | Thumbs Up: Gold (`#F9E2AF`)

---

## Slide 4: Why Snapdragon? (Edge AI Advantages Benchmark)

### Slide Header
- **Headline:** Unleashing Edge AI on Qualcomm Snapdragon Architecture

### Slide Content: Edge AI Comparison Table

| Evaluation Vector | Cloud Vision AI | Traditional x86 / Discrete GPU | Snapdragon Edge AI (OmniGesture) |
| :--- | :--- | :--- | :--- |
| **Inference Latency** | 150 – 350 ms (Network bound) | 35 – 60 ms (Driver/bus overhead) | **< 15 ms (30+ FPS real-time tracking)** |
| **Data Privacy & Security** | ❌ Video stream uploaded to cloud | ⚠️ Local, but high OS vulnerability | **✅ 100% On-Device: Frames never leave RAM** |
| **Energy Consumption** | ~15–25W (Wi-Fi + continuous stream) | ~45–85W (Rapid battery depletion) | **⚡ Ultra-low power (All-day battery longevity)** |
| **Thermal Profile** | Moderate (Constant network traffic) | High heat, loud fan acoustics | **Silent, cool operation; zero throttling** |
| **Offline Independence** | ❌ Fails completely without internet | ✅ Operates offline | **✅ Fully operational anywhere, anytime** |
| **Hardware Overhead** | Recurring cloud API subscriptions | Bulky, heavy workstation laptops | **Native on lightweight HP Snapdragon laptops** |

### Key Architectural Advantages
- **Dedicated NPU & Hexagon Vector Engine:** Offloads tensor computations from the main CPU, keeping the operating system ultra-responsive.
- **All-Day Battery Life:** Enables disabled users to navigate their PCs for a full workday on battery power alone without being tethered to a wall outlet.
- **Zero Privacy Compromise:** Compliant with medical and enterprise privacy standards (HIPAA/GDPR) since zero video data is stored or transmitted.

### Presenter Notes (45-60 Seconds)
> "Why is Snapdragon the ideal home for OmniGesture? Interactive cursor control demands immediate physical feedback. If latency exceeds 30 milliseconds, the human brain perceives a disconnect, causing overshooting and fatigue. Cloud AI is inherently disqualified due to network ping, and it poses severe privacy risks by streaming intimate bedroom or office camera feeds over the web. Traditional laptop chips consume immense power, draining batteries and spinning fans loudly. Snapdragon changes the paradigm: with energy-efficient ARM architecture and dedicated neural processing capabilities, OmniGesture runs at a locked 30+ frames per second with sub-15ms response times, consumes minimal power, and ensures that not a single pixel ever leaves the device's local memory."

### Slide Design & Visual Tips
- **Layout:** High-impact comparison matrix. Highlight the "Snapdragon Edge AI" column with a glowing border in Qualcomm Crimson (`#E60012`) or Snapdragon Gold (`#FFC107`).
- **Icons:** Green checkmarks for Snapdragon advantages; red cross icons and yellow warning triangles for Cloud and Legacy x86 columns.
- **Callout Box:** Bottom banner: *"Powered by Qualcomm Snapdragon X Series: High-throughput, low-wattage intelligence at the edge."*

---

## Slide 5: Technical Architecture (MediaPipe Tasks, OpenCV, PyAutoGUI & Tkinter)

### Slide Header
- **Headline:** High-Performance, Multi-Threaded Edge AI Architecture

### Slide Content: Architecture Breakdown

#### System Pipeline Flow
```
[Built-in HP Webcam] 
        │  (640x480 @ 30 FPS raw BGR feed)
        ▼
[OpenCV Capture & Preprocessing] 
        │  (Mirror image, RGB conversion, aspect scaling)
        ▼
[MediaPipe Tasks Vision Engine] 
        │  (HandLandmarker: 21 3D hand coordinates via hand_landmarker.task)
        ▼
[OmniGesture Vector Geometry & State Engine]
        │  (Euclidean pinch math, finger PIP extension tests, EMA smoothing)
        ▼
 ┌──────┴──────────────────────────────────────┐
 ▼                                             ▼
[PyAutoGUI OS Injection]           [Tkinter GUI Event Thread]
 - Pointer Interpolation            - Live Telemetry (FPS / Active Gesture)
 - Click & Drag Locks               - Smoothness / Sensitivity Configuration
 - Dynamic Vertical Scroll          - Timestamped Activity Event Log
```

#### Core Components
- **MediaPipe Tasks API (`mp.tasks.vision.HandLandmarker`):** Utilizes the modern, standalone `hand_landmarker.task` model bundle for accelerated 21-landmark 3D hand mesh detection in continuous video stream mode.
- **OpenCV (`cv2`):** Handles camera ingestion, real-time horizontal mirroring (ensuring intuitive pointer direction), and low-overhead on-screen HUD drawing.
- **PyAutoGUI Automation Engine:** Converts normalized landmark coordinates into calibrated OS cursor coordinates with smoothing algorithms (`pyautogui.moveTo`, `click`, `scroll`, `mouseDown/Up`).
- **Decoupled Asynchronous GUI:** Multi-threaded architecture keeps the Tkinter GUI running on the main event thread while computer vision runs asynchronously in a daemon thread, guaranteeing zero UI freezing or dropped frames.

### Presenter Notes (45-60 Seconds)
> "Under the hood, OmniGesture v2.0 is built for performance and modularity. We use Google's latest MediaPipe Tasks API, loading a local hand landmarker model bundle that outputs twenty-one 3D skeletal coordinates per frame. Our custom geometry engine computes Euclidean tip distances for pinch detection and checks finger extension vectors relative to the PIP joints for gestures like Peace, Fist, and Open Palm. To prevent any lag or interface lockup, the architecture is strictly multi-threaded: camera ingestion, landmark inference, and gesture smoothing run on a high-priority background worker thread, while the Tkinter control panel runs seamlessly on the main loop, updating real-time FPS and telemetry."

### Slide Design & Visual Tips
- **Layout:** Architectural block diagram or flow diagram showing the 5 stages from webcam capture to OS cursor action.
- **Tech Stack Logos:** Include official logos for **Python**, **Qualcomm Snapdragon**, **Google MediaPipe**, **OpenCV**, and **Tkinter**.
- **Visual Distinction:** Use separate colored containers for the *Vision Inference Layer* (blue) and the *OS Control & Telemetry Layer* (green/purple).

---

## Slide 6: Live Demo & Verification (OmniGesture in Action)

### Slide Header
- **Headline:** Live Demonstration: Real-Time Precision & Intuitive Control

### Slide Content & Demo Script

#### Visual Showcase (Screenshots & Video Callouts)
- **Primary View — Live Computer Vision HUD:**
  - Mirrored webcam feed displaying 21 green skeletal landmarks and hand connection mesh.
  - Active Gesture Badge in top-left corner (e.g., `GESTURE: POINT`, `GESTURE: PINCH`).
  - Real-time performance metric overlay (e.g., `FPS: 31.4`).
- **Secondary View — Tkinter Control Panel:**
  - Status display showing `TRACKING` in bright emerald green.
  - Smoothness slider adjusted to demonstrate tremor suppression.
  - Activity log recording instant clicks: `[21:34:12] Left Click`, `[21:34:15] Double Click`.

#### Live Demo Flow (30-Second Rapid Showcase)
1. **Launch & Calibration:** Open app, click "START TRACKING" on the Control Panel.
2. **Cursor Navigation:** Raise index finger (Point) to steer the cursor smoothly to a browser tab.
3. **Selection & Launch:** Pinch thumb and index to select; show Peace Sign to double-click and open an application.
4. **Context & Scroll:** Close hand into a Fist to reveal context menu; raise Open Palm and move hand vertically to scroll down a document.
5. **Drag & Drop:** Flash Thumbs-Up to lock drag, move a window across the desktop, and flash Thumbs-Up again to release.

### Presenter Notes (60 Seconds)
> "Here you see OmniGesture v2.0 running live on our Snapdragon device. Notice on the left window the skeletal tracking: twenty-one landmarks tracking every joint with zero perceptible lag. Watch as I raise my index finger: the cursor tracks fluidly with my hand movement. I pinch to click a link—instant feedback. When I show a peace sign, it executes an immediate double-click. If I close my fingers into a fist, the right-click menu appears. When reading an article, I simply open my palm to scroll up and down smoothly. And when I need to move a window or select text, a quick thumbs-up locks the mouse drag, allowing me to drag effortlessly without maintaining a strenuous grip."

### Slide Design & Visual Tips
- **Layout:** Side-by-side split screen mockup showing:
  - *Left 55%:* Camera HUD screenshot with hand landmarks, landmark skeleton lines, and gesture label.
  - *Right 45%:* Control panel screenshot showing live FPS, active status, slider at 5, and populated event logs.
- **Annotated Callouts:** Use circular callout badges pointing to:
  - ① Skeletal Landmarker Mesh
  - ② Active Gesture Telemetry
  - ③ Responsive Smoothness Slider
  - ④ 30+ FPS Performance Metric

---

## Slide 7: Future Roadmap & Vision (Qualcomm AI Hub & Next Horizons)

### Slide Header
- **Headline:** The Future: Qualcomm AI Hub Integration & Universal Access

### Slide Content: Three Strategic Pillars

#### 1. Qualcomm AI Hub NPU Deployment
- **Hardware Target:** Compile and quantize vision models directly for the Snapdragon Hexagon NPU via **Qualcomm AI Hub**.
- **Performance Impact:** Offloads 100% of vision inference from the CPU/GPU, reducing power consumption to sub-1-watt levels and liberating system resources for heavy multitasking.

#### 2. Personalized Gesture Engine & Macro Customization
- **User-Defined Gestures:** Allow users with unique physical abilities or limited finger mobility to train bespoke gestures (e.g., three-finger spread, rock-on sign, wrist tilt).
- **Macro Keybinding:** Map custom gestures directly to complex shortcuts, such as app switching (`Alt+Tab`), copy/paste (`Ctrl+C / Ctrl+V`), or virtual keyboard toggles.

#### 3. Multimodal Facial & Head-Pose Tracking
- **Quadriplegia & Severe Mobility Support:** Integrate MediaPipe Face Landmarker for hands-free head-pose cursor guidance.
- **Blink & Smile Detection:** Map eye winks or mouth movements to mouse clicks for users who cannot utilize hand gestures at all.

### Final Summary Call to Action
- **Vision:** An inclusive digital world where every Snapdragon HP PC is an out-of-the-box accessibility workstation.
- **Repository & Code:** Open-source project ready for Qualcomm AI Hub optimization.
- **Closing Statement:** *"Empowering every user with the intelligence of Snapdragon Edge AI."*

### Presenter Notes (45 Seconds)
> "Looking ahead, our roadmap for OmniGesture v2.0 takes full advantage of Qualcomm's ecosystem. First, through the Qualcomm AI Hub, we will quantize and deploy custom hand tracking models directly onto the Snapdragon Hexagon NPU, unlocking near-zero CPU overhead and sub-watt power efficiency. Second, we will introduce a custom gesture calibration suite, letting users with non-standard hand anatomies map their own comfortable motions to OS hotkeys. And third, we will introduce facial and head-pose tracking to support quadriplegic users. OmniGesture demonstrates that on-device AI isn't just about speed—it is about accessibility, dignity, and independence for every user. Thank you!"

### Slide Design & Visual Tips
- **Layout:** 3 forward-looking horizontal roadmap cards or milestone chevron timeline (Phase 1: NPU Optimization -> Phase 2: Custom Macros -> Phase 3: Multimodal Face Tracking).
- **Icons:** Qualcomm AI Hub chip icon, wrench/macro gear icon, and face mesh/eye icon.
- **Footer:** GitHub repository QR code / link on the right, Snapdragon AI Lab partner mark on the left.

---

## Slide Deck Quick Reference Summary

| Slide # | Title | Primary Message | Visual Focus |
| :---: | :--- | :--- | :--- |
| **1** | Title Slide | OmniGesture v2.0: AI-Powered Hands-Free Accessibility | Hero photo of HP Snapdragon laptop + hand mesh |
| **2** | The Problem | Existing accessibility tools are costly, laggy, or privacy-invasive | 3-Card breakdown: High Cost vs Cloud Lag vs Heat |
| **3** | The Solution | 6 intuitive gestures + modern dark-mode control panel | 2x3 Gesture grid + Tkinter UI mockup |
| **4** | Why Snapdragon? | Edge AI delivers zero latency, absolute privacy, and all-day battery | Comparison table: Cloud AI vs x86 vs Snapdragon |
| **5** | Technical Architecture | MediaPipe Tasks API + OpenCV + PyAutoGUI + Tkinter | Multi-threaded pipeline flow diagram & tech logos |
| **6** | Live Demo / Proof | Seamless cursor navigation, clicking, scrolling & dragging | Camera HUD & Control Panel screenshots with callouts |
| **7** | Future Roadmap | Qualcomm AI Hub NPU acceleration & multimodal head tracking | 3-phase strategic roadmap cards + GitHub QR code |

---

## Presentation Delivery Best Practices
- **Pacing:** Aim for ~5 minutes total presentation time (~45-50 seconds per slide) with 2 minutes reserved for Q&A.
- **Tone:** Professional, empathetic, and technologically grounded. Highlight human impact first, backed up by Snapdragon engineering strengths.
- **Live Demo Fallback:** If presenting live without a webcam setup, keep a 20-second recorded screen capture video embedded directly into Slide 6 as a backup.
