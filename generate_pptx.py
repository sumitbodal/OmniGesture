"""
Generate Pitch Presentation as PPTX.
Run this script once to create the PowerPoint file for submission.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color scheme
DARK_BG = RGBColor(30, 30, 46)
ACCENT_BLUE = RGBColor(137, 180, 250)
ACCENT_GREEN = RGBColor(166, 227, 161)
ACCENT_RED = RGBColor(243, 139, 168)
ACCENT_PEACH = RGBColor(250, 179, 135)
ACCENT_MAUVE = RGBColor(203, 166, 247)
ACCENT_YELLOW = RGBColor(249, 226, 175)
WHITE = RGBColor(205, 214, 244)
GRAY = RGBColor(108, 112, 134)
SURFACE = RGBColor(49, 50, 68)


def set_slide_bg(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_textbox(slide, left, top, width, height, text, font_size=18,
                color=WHITE, bold=False, alignment=PP_ALIGN.LEFT, font_name="Segoe UI"):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox


# ============================================================
# SLIDE 1: Title Slide
# ============================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
set_slide_bg(slide1, DARK_BG)

add_textbox(slide1, 1.5, 1.5, 10, 1.5, "OmniGesture v2.0",
            font_size=48, color=ACCENT_BLUE, bold=True, alignment=PP_ALIGN.CENTER)
add_textbox(slide1, 1.5, 3.0, 10, 1, "AI-Powered Hands-Free PC Controller",
            font_size=28, color=WHITE, alignment=PP_ALIGN.CENTER)
add_textbox(slide1, 1.5, 4.0, 10, 0.8, "Built for Snapdragon-Powered HP PCs",
            font_size=20, color=ACCENT_GREEN, alignment=PP_ALIGN.CENTER)
add_textbox(slide1, 1.5, 5.5, 10, 0.5, "Snapdragon AI Lab Build & Present Challenge | September 2026",
            font_size=14, color=GRAY, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 2: The Problem
# ============================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide2, DARK_BG)

add_textbox(slide2, 0.8, 0.4, 11, 0.8, "The Problem",
            font_size=36, color=ACCENT_RED, bold=True)
add_textbox(slide2, 0.8, 1.1, 11, 0.5, "Standard PC navigation is not accessible to everyone",
            font_size=18, color=GRAY)

problems = [
    ("1.3B+ people worldwide", "live with disabilities affecting motor function"),
    ("Assistive hardware costs $1,500-$10,000+", "making it inaccessible in developing economies"),
    ("Cloud AI tracking has 200-500ms latency", "making real-time cursor control impossible"),
    ("Streaming video to cloud servers", "creates massive privacy violations"),
    ("Heavy GPU models drain batteries", "and cause thermal throttling on laptops"),
]

y_pos = 1.8
for title, desc in problems:
    add_textbox(slide2, 1.2, y_pos, 10, 0.35, f">>  {title}", font_size=18, color=ACCENT_PEACH, bold=True)
    add_textbox(slide2, 1.7, y_pos + 0.35, 9.5, 0.3, desc, font_size=15, color=WHITE)
    y_pos += 0.85

# ============================================================
# SLIDE 3: The Solution
# ============================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide3, DARK_BG)

add_textbox(slide3, 0.8, 0.4, 11, 0.8, "The Solution: OmniGesture v2.0",
            font_size=36, color=ACCENT_GREEN, bold=True)
add_textbox(slide3, 0.8, 1.1, 11, 0.5, "Turn your webcam into a zero-latency gesture controller",
            font_size=18, color=GRAY)

gestures = [
    ("Point (Index Up)", "Move Cursor", ACCENT_BLUE),
    ("Pinch (Thumb+Index)", "Left Click", ACCENT_GREEN),
    ("Peace (Index+Middle)", "Double Click", ACCENT_MAUVE),
    ("Fist (All Closed)", "Right Click", ACCENT_RED),
    ("Open Palm (All Up)", "Scroll Up/Down", ACCENT_PEACH),
    ("Thumbs Up", "Toggle Drag Lock", ACCENT_YELLOW),
]

y_pos = 1.9
for gesture, action, color in gestures:
    add_textbox(slide3, 1.2, y_pos, 5, 0.4, gesture, font_size=18, color=color, bold=True)
    add_textbox(slide3, 6.5, y_pos, 5, 0.4, action, font_size=18, color=WHITE)
    y_pos += 0.55

add_textbox(slide3, 0.8, 5.8, 11, 0.8,
            "Plus: Dark-themed Control Panel | Live FPS Counter | Sensitivity Slider | Activity Log",
            font_size=14, color=GRAY, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 4: Why Snapdragon
# ============================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide4, DARK_BG)

add_textbox(slide4, 0.8, 0.4, 11, 0.8, "Why Snapdragon?",
            font_size=36, color=ACCENT_BLUE, bold=True)
add_textbox(slide4, 0.8, 1.1, 11, 0.5, "Edge AI is not optional for real-time gesture control - it is mandatory",
            font_size=18, color=GRAY)

# Comparison headers
headers = ["", "Cloud AI", "Snapdragon Edge AI"]
cols_x = [1.2, 4.5, 8.5]
for i, header in enumerate(headers):
    color = GRAY if i == 0 else (ACCENT_RED if i == 1 else ACCENT_GREEN)
    add_textbox(slide4, cols_x[i], 1.9, 3.5, 0.4, header, font_size=16, color=color, bold=True)

comparisons = [
    ("Latency", "200-500ms (unusable)", "<15ms (fluid)"),
    ("Privacy", "Video sent to servers", "100% on-device"),
    ("Internet", "Required always", "Fully offline"),
    ("Battery", "Heavy drain", "NPU-optimized"),
    ("Cost", "Per-API-call charges", "Free forever"),
]

y_pos = 2.5
for metric, cloud, snap in comparisons:
    add_textbox(slide4, cols_x[0], y_pos, 3, 0.35, metric, font_size=15, color=WHITE, bold=True)
    add_textbox(slide4, cols_x[1], y_pos, 3.5, 0.35, cloud, font_size=15, color=ACCENT_RED)
    add_textbox(slide4, cols_x[2], y_pos, 3.5, 0.35, snap, font_size=15, color=ACCENT_GREEN)
    y_pos += 0.55

# ============================================================
# SLIDE 5: Technical Architecture
# ============================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide5, DARK_BG)

add_textbox(slide5, 0.8, 0.4, 11, 0.8, "Technical Architecture",
            font_size=36, color=ACCENT_MAUVE, bold=True)

# Pipeline
pipeline_text = (
    "HP Webcam  -->  OpenCV 4.10  -->  MediaPipe HandLandmarker  -->  "
    "Gesture Engine  -->  PyAutoGUI  -->  OS Mouse Events"
)
add_textbox(slide5, 0.8, 1.5, 11.5, 0.6, pipeline_text,
            font_size=16, color=ACCENT_YELLOW, bold=True, alignment=PP_ALIGN.CENTER,
            font_name="Consolas")

tech_items = [
    ("MediaPipe Tasks API", "Open-source edge AI model detecting 21 hand landmarks at 30+ FPS"),
    ("Gesture Recognition", "Finger state vectors (tip vs PIP elevation) + Euclidean pinch distance"),
    ("EMA Cursor Smoothing", "Exponential Moving Average filter eliminates tremors and micro-jitter"),
    ("Multi-threaded Design", "Vision engine runs in background thread; Tkinter UI on main thread"),
    ("Temporal Cooldowns", "State machine prevents accidental double-triggers during transitions"),
    ("Adjustable Sensitivity", "User-configurable smoothing factor via slider (1-10 range)"),
]

y_pos = 2.5
for title, desc in tech_items:
    add_textbox(slide5, 1.2, y_pos, 4.5, 0.35, title, font_size=16, color=ACCENT_BLUE, bold=True)
    add_textbox(slide5, 5.8, y_pos, 6.5, 0.35, desc, font_size=14, color=WHITE)
    y_pos += 0.55

add_textbox(slide5, 0.8, 6.0, 11, 0.5,
            "Tech Stack: Python 3.10+ | MediaPipe (Open Source) | OpenCV 4.10 | PyAutoGUI | Tkinter",
            font_size=14, color=GRAY, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 6: Demo / Screenshots
# ============================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide6, DARK_BG)

add_textbox(slide6, 0.8, 0.4, 11, 0.8, "Live Demo & Screenshots",
            font_size=36, color=ACCENT_PEACH, bold=True)

add_textbox(slide6, 1.5, 2.0, 4.5, 0.5, "Camera View (Hand Tracking HUD)",
            font_size=18, color=ACCENT_BLUE, bold=True, alignment=PP_ALIGN.CENTER)

# Placeholder box for camera screenshot
shape1 = slide6.shapes.add_shape(1, Inches(1.5), Inches(2.6), Inches(4.5), Inches(3.5))
shape1.fill.solid()
shape1.fill.fore_color.rgb = SURFACE
shape1.line.color.rgb = ACCENT_BLUE
shape1.line.width = Pt(2)
add_textbox(slide6, 2.0, 3.8, 3.5, 0.5, "[Insert Camera Screenshot Here]",
            font_size=14, color=GRAY, alignment=PP_ALIGN.CENTER)

add_textbox(slide6, 7.0, 2.0, 4.5, 0.5, "Tkinter Control Panel",
            font_size=18, color=ACCENT_GREEN, bold=True, alignment=PP_ALIGN.CENTER)

# Placeholder box for control panel screenshot
shape2 = slide6.shapes.add_shape(1, Inches(7.0), Inches(2.6), Inches(4.5), Inches(3.5))
shape2.fill.solid()
shape2.fill.fore_color.rgb = SURFACE
shape2.line.color.rgb = ACCENT_GREEN
shape2.line.width = Pt(2)
add_textbox(slide6, 7.5, 3.8, 3.5, 0.5, "[Insert Control Panel Screenshot Here]",
            font_size=14, color=GRAY, alignment=PP_ALIGN.CENTER)

add_textbox(slide6, 0.8, 6.5, 11, 0.5,
            "Both windows run simultaneously - Camera HUD shows landmarks, Control Panel shows status",
            font_size=14, color=GRAY, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 7: Future Roadmap
# ============================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide7, DARK_BG)

add_textbox(slide7, 0.8, 0.4, 11, 0.8, "Future Roadmap & Vision",
            font_size=36, color=ACCENT_YELLOW, bold=True)

phases = [
    ("Phase 1: Qualcomm AI Hub NPU Deployment",
     "Compile and INT8-quantize the hand landmark model for the Snapdragon Hexagon NPU "
     "via Qualcomm AI Hub. Target: sub-watt inference with near-zero CPU overhead.",
     ACCENT_BLUE),
    ("Phase 2: Custom Gesture Macro Builder",
     "Allow users to record custom hand poses and map them to any keyboard shortcut "
     "or system action (e.g., Peace Sign = Copy, Swipe Left = Switch Window).",
     ACCENT_GREEN),
    ("Phase 3: Multimodal Head & Gaze Tracking",
     "Add head-pose estimation and iris gaze tracking for users with severe mobility "
     "impairments who cannot use their hands at all (e.g., quadriplegia).",
     ACCENT_MAUVE),
]

y_pos = 1.5
for title, desc, color in phases:
    add_textbox(slide7, 1.2, y_pos, 10, 0.4, title, font_size=20, color=color, bold=True)
    add_textbox(slide7, 1.5, y_pos + 0.45, 9.5, 0.6, desc, font_size=15, color=WHITE)
    y_pos += 1.3

add_textbox(slide7, 0.8, 5.8, 11, 0.8,
            "OmniGesture makes every Snapdragon HP PC universally accessible - "
            "no extra hardware, no cloud, no compromise.",
            font_size=20, color=ACCENT_GREEN, bold=True, alignment=PP_ALIGN.CENTER)

add_textbox(slide7, 0.8, 6.6, 11, 0.5,
            "Thank You! | GitHub: github.com/YOUR_USERNAME/omnigesture",
            font_size=16, color=GRAY, alignment=PP_ALIGN.CENTER)

# Save
output_path = r"C:\Users\sumit\Downloads\OmniGesture_Project\OmniGesture_Pitch.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
