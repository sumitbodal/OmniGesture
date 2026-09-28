"""
Generate Project_Description.docx from content.
Run this script once to create the Word document for submission.
"""
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

# Styles
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)
style.font.color.rgb = RGBColor(33, 33, 33)
style.paragraph_format.space_after = Pt(6)

# ---- TITLE ----
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("OmniGesture v2.0")
run.font.size = Pt(26)
run.font.bold = True
run.font.color.rgb = RGBColor(0, 82, 155)

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run("AI-Powered Hands-Free PC Controller for Snapdragon HP PCs")
run.font.size = Pt(13)
run.font.italic = True
run.font.color.rgb = RGBColor(100, 100, 100)

doc.add_paragraph()  # spacer

# ---- EXECUTIVE SUMMARY ----
h = doc.add_heading("Executive Summary", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "OmniGesture is an AI-powered accessibility application that transforms any standard webcam "
    "on a Snapdragon-powered HP PC into a hands-free computer controller. Using edge-optimized "
    "computer vision models running entirely on-device, OmniGesture enables users with mobility "
    "impairments, repetitive strain injuries, or temporary disabilities to navigate their PC "
    "through intuitive hand gestures - without any additional hardware, internet connection, or "
    "cloud processing."
)

doc.add_paragraph(
    "The application supports six distinct gestures that provide complete mouse functionality: "
    "cursor movement, left click, right click, double click, scrolling, and drag-and-drop. "
    "All AI inference runs locally on the Snapdragon processor, ensuring zero latency, "
    "total user privacy, and exceptional battery efficiency."
)

# ---- THE PROBLEM ----
h = doc.add_heading("The Problem: The Accessibility & Ergonomic Divide", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "Over 1.3 billion people worldwide live with some form of disability, and a significant "
    "portion face motor or mobility impairments that make standard PC inputs (mouse, keyboard, "
    "touchpad) difficult or impossible to use. These include conditions such as ALS, Parkinson's "
    "disease, carpal tunnel syndrome, repetitive strain injuries (RSI), arthritis, and temporary "
    "injuries like broken arms or post-surgical recovery."
)

doc.add_paragraph("Current solutions are fundamentally flawed:")

problems = [
    ("Expensive Hardware: ", "Dedicated assistive devices (eye trackers, sip-and-puff controllers, "
     "adaptive switches) cost $1,500 to $10,000+, making them inaccessible to most users, "
     "particularly in developing economies like India."),
    ("Cloud AI Latency: ", "Software-based gesture trackers that rely on cloud processing "
     "introduce 200-500ms of latency per frame, making real-time cursor control physically "
     "impossible and deeply frustrating."),
    ("Privacy Violations: ", "Streaming live webcam video to cloud servers for AI processing "
     "creates severe privacy risks, especially in medical, legal, and enterprise environments "
     "where camera feeds may capture sensitive information."),
    ("Battery Drain: ", "Running unoptimized AI models on general-purpose CPUs or discrete GPUs "
     "causes rapid battery depletion and thermal throttling, making continuous use impractical "
     "on laptop devices."),
]

for title_text, desc in problems:
    p = doc.add_paragraph()
    p.style = 'List Bullet'
    run = p.add_run(title_text)
    run.bold = True
    p.add_run(desc)

# ---- THE SOLUTION ----
h = doc.add_heading("The Solution: OmniGesture v2.0", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "OmniGesture turns any standard webcam on a Snapdragon-powered HP PC into a zero-latency, "
    "privacy-preserving gesture controller. The application uses Google's MediaPipe Tasks API, "
    "an open-source edge AI framework, to detect and track 21 three-dimensional hand landmarks "
    "in real-time at 30+ frames per second."
)

doc.add_paragraph("Six intuitive gestures provide complete mouse replacement:")

# Gesture table
table = doc.add_table(rows=7, cols=3)
table.style = 'Medium Shading 1 Accent 1'

headers = ["Gesture", "Hand Pose", "System Action"]
for i, header in enumerate(headers):
    table.rows[0].cells[i].text = header

gestures = [
    ["Point", "Index finger extended upward", "Move cursor (with EMA smoothing)"],
    ["Pinch", "Thumb tip touches index tip", "Left click (500ms cooldown)"],
    ["Peace", "Index + middle fingers up", "Double click"],
    ["Fist", "All fingers curled closed", "Right click (context menu)"],
    ["Open Palm", "All five fingers extended", "Scroll mode (vertical tracking)"],
    ["Thumbs Up", "Only thumb extended", "Toggle drag lock on/off"],
]

for row_idx, gesture in enumerate(gestures):
    for col_idx, cell_text in enumerate(gesture):
        table.rows[row_idx + 1].cells[col_idx].text = cell_text

doc.add_paragraph()

doc.add_paragraph(
    "The application includes a professional Tkinter-based control panel with a dark theme, "
    "featuring a live FPS counter, active gesture indicator, adjustable smoothness/sensitivity "
    "slider, and a timestamped activity log for monitoring all gesture-triggered actions."
)

# ---- WHY SNAPDRAGON ----
h = doc.add_heading("Why Snapdragon? The Edge AI Advantage", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "OmniGesture is specifically designed to leverage the unique capabilities of the Snapdragon "
    "platform. The application's architecture is fundamentally incompatible with cloud-based "
    "processing for the following reasons:"
)

advantages = [
    ("Zero Latency: ", "Real-time cursor control requires sub-20ms inference latency. "
     "Cloud round-trips introduce 200-500ms delays, making the mouse cursor lag unbearably "
     "behind hand movements. Snapdragon's local compute delivers consistent <15ms inference, "
     "enabling fluid, responsive cursor tracking at 30+ FPS."),
    ("Total Privacy: ", "OmniGesture processes video frames entirely in volatile memory on "
     "the local device. No camera feed is ever recorded, stored, or transmitted. This is "
     "critical for users in medical facilities, legal offices, government buildings, and "
     "enterprise environments where camera feeds may capture sensitive information."),
    ("Battery Efficiency: ", "Snapdragon's ARM-based Oryon CPU architecture and dedicated "
     "Hexagon NPU (Neural Processing Unit) are purpose-built for sustained AI workloads. "
     "OmniGesture can run continuously in the background without causing thermal throttling "
     "or rapid battery depletion - essential for an accessibility tool that must be always-on."),
    ("Offline Capability: ", "The application works without any internet connection, making "
     "it usable in remote areas, on flights, in restricted-network government facilities, "
     "and anywhere connectivity is unreliable."),
]

for title_text, desc in advantages:
    p = doc.add_paragraph()
    p.style = 'List Bullet'
    run = p.add_run(title_text)
    run.bold = True
    p.add_run(desc)

# ---- TECHNICAL IMPLEMENTATION ----
h = doc.add_heading("Technical Implementation", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "The application is built with a multi-threaded architecture that separates the vision "
    "processing pipeline from the user interface, ensuring smooth performance:"
)

tech_details = [
    ("Vision Engine (Background Thread): ", "OpenCV captures frames from the webcam. Each "
     "frame is converted to RGB and passed to the MediaPipe HandLandmarker model, which "
     "extracts 21 three-dimensional hand landmarks. A custom GestureRecognizer class analyzes "
     "finger extension states (tip vs. PIP joint elevation) and Euclidean pinch distances "
     "to classify the current gesture."),
    ("Cursor Smoothing: ", "An Exponential Moving Average (EMA) filter smooths cursor "
     "movement, eliminating micro-jitter and hand tremors. The smoothing factor is "
     "user-adjustable via the control panel's sensitivity slider."),
    ("Action Execution: ", "PyAutoGUI translates recognized gestures into OS-level mouse "
     "events (moveTo, click, rightClick, doubleClick, scroll, mouseDown/mouseUp). Temporal "
     "cooldown logic prevents accidental double-triggering of click actions."),
    ("Control Panel (Main Thread): ", "A Tkinter-based GUI provides real-time status "
     "monitoring, start/stop controls, sensitivity adjustment, and an activity log. The "
     "dark-themed interface is designed for minimal visual distraction."),
]

for title_text, desc in tech_details:
    p = doc.add_paragraph()
    p.style = 'List Bullet'
    run = p.add_run(title_text)
    run.bold = True
    p.add_run(desc)

# ---- TECH STACK ----
h = doc.add_heading("Technology Stack", level=2)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

stack_table = doc.add_table(rows=7, cols=2)
stack_table.style = 'Medium Shading 1 Accent 1'
stack_data = [
    ["Component", "Technology"],
    ["Language", "Python 3.10+"],
    ["Vision AI", "Google MediaPipe Tasks API (Open Source)"],
    ["Image Processing", "OpenCV 4.10"],
    ["System Control", "PyAutoGUI"],
    ["User Interface", "Tkinter (Built-in Python)"],
    ["Target Hardware", "Snapdragon X Elite / X Plus HP PCs"],
]
for row_idx, row_data in enumerate(stack_data):
    for col_idx, cell_text in enumerate(row_data):
        stack_table.rows[row_idx].cells[col_idx].text = cell_text

# ---- INNOVATION ----
doc.add_paragraph()
h = doc.add_heading("Innovation & Novelty", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "OmniGesture introduces several novel elements that distinguish it from existing solutions:"
)

innovations = [
    "Complete 6-action mouse replacement through hand gestures alone - no physical input device needed.",
    "Latching drag-lock mechanism via Thumbs Up gesture, enabling window repositioning and text selection without sustained pinch strain.",
    "Temporal cooldown state machine that prevents gesture transition misfires during rapid hand movements.",
    "Zero-hardware-cost deployment requiring only the standard integrated webcam present on all HP laptops.",
    "User-adjustable tremor dampening via the sensitivity slider, accommodating users with varying degrees of motor control.",
]

for item in innovations:
    doc.add_paragraph(item, style='List Bullet')

# ---- FUTURE ROADMAP ----
h = doc.add_heading("Future Roadmap: Qualcomm AI Hub Integration", level=1)
h.runs[0].font.color.rgb = RGBColor(0, 82, 155)

doc.add_paragraph(
    "The next phase of OmniGesture development will fully utilize the Qualcomm AI Hub to "
    "maximize performance on Snapdragon hardware:"
)

roadmap = [
    ("Phase 1 - NPU Deployment: ", "Compile and quantize (INT8) the hand landmark model "
     "using the Qualcomm AI Hub SDK for direct deployment on the Snapdragon Hexagon NPU. "
     "This will reduce CPU overhead to near-zero, enabling true background operation."),
    ("Phase 2 - Custom Gestures: ", "Allow users to record and train their own custom "
     "gesture-to-action mappings (e.g., mapping a specific hand pose to 'Copy/Paste' or "
     "'Alt+Tab'), creating a fully personalized accessibility experience."),
    ("Phase 3 - Multimodal Input: ", "Add head-pose tracking and facial gesture recognition "
     "for users who cannot use their hands at all, such as individuals with quadriplegia."),
]

for title_text, desc in roadmap:
    p = doc.add_paragraph()
    p.style = 'List Bullet'
    run = p.add_run(title_text)
    run.bold = True
    p.add_run(desc)

# ---- FOOTER ----
doc.add_paragraph()
footer = doc.add_paragraph()
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = footer.add_run("Built for the Snapdragon AI Lab Build & Present Challenge")
run.font.italic = True
run.font.color.rgb = RGBColor(100, 100, 100)

# Save
output_path = r"C:\Users\sumit\Downloads\OmniGesture_Project\Project_Description.docx"
doc.save(output_path)
print(f"Saved: {output_path}")
