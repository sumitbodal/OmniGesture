"""
Simple camera test - no MediaPipe, just OpenCV.
This will tell us if the camera itself works.
"""
import cv2
import sys

print("=" * 50)
print("CAMERA DIAGNOSTIC TEST")
print("=" * 50)

# Test 1: Try opening camera without any flags
print("\n[Test 1] Trying cv2.VideoCapture(0) ...")
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(f"  SUCCESS! Camera 0 works. Frame size: {frame.shape}")
        # Try showing a window
        cv2.imshow("Camera Test - Press Q to close", frame)
        print("  Window should be visible now. Press 'q' to close.")
        cv2.waitKey(3000)  # Wait 3 seconds
        cv2.destroyAllWindows()
    else:
        print("  Camera opened but could not read a frame.")
    cap.release()
else:
    print("  FAILED to open camera 0.")

# Test 2: Try with DirectShow
print("\n[Test 2] Trying cv2.VideoCapture(0, cv2.CAP_DSHOW) ...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(f"  SUCCESS! Camera 0 (DSHOW) works. Frame size: {frame.shape}")
    else:
        print("  Camera opened but could not read a frame.")
    cap.release()
else:
    print("  FAILED to open camera 0 with DSHOW.")

# Test 3: Try with MSMF (Microsoft Media Foundation)
print("\n[Test 3] Trying cv2.VideoCapture(0, cv2.CAP_MSMF) ...")
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(f"  SUCCESS! Camera 0 (MSMF) works. Frame size: {frame.shape}")
    else:
        print("  Camera opened but could not read a frame.")
    cap.release()
else:
    print("  FAILED to open camera 0 with MSMF.")

# Test 4: Try all camera indices 0-4
print("\n[Test 4] Scanning all camera indices 0-4 ...")
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"  Camera index {i}: WORKS! Frame size: {frame.shape}")
        else:
            print(f"  Camera index {i}: Opens but cannot read frames.")
        cap.release()
    else:
        print(f"  Camera index {i}: Not available.")

print("\n" + "=" * 50)
print("DIAGNOSTIC COMPLETE")
print("=" * 50)
print("\nPlease copy the output above and share it.")
