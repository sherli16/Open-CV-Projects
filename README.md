# OpenCV Vision Projects
A collection of beginner-friendly Computer Vision projects built with Python and OpenCV.

## Projects

# Project-Description
1 Real-Time Blue Object Detection and Tracking - Detects and tracks blue objects from a live webcam feed using HSV color masking
2 Pencil Sketch Converter - Converts a normal image into a pencil sketch

---

## 1. Real-Time Blue Object Detection and Tracking
Detects blue-colored objects in real time using the webcam and draws a bounding box around them.

### How it works
1. Capture frames from the webcam
2. Convert each frame from BGR to HSV color space
3. Create a mask for the blue color range using `cv2.inRange`
4. Find contours on the mask
5. Draw a green bounding box around contours with area greater than 1000 pixels

### Run
python blue_object_tracking.py
Press **q** to quit.

---

## 2. Pencil Sketch Converter
Converts an image into a pencil sketch effect.

### How it works
1. Convert the image to grayscale
2. Invert the grayscale image
3. Apply Gaussian Blur
4. Invert the blurred image
5. Blend using `cv2.divide` to get the sketch effect

### Run
python pencil_sketch.py
Keep `image.jpg` in the same folder. The output is saved as `pencil_sketch.jpg`.

## Technologies Used
- Python
- OpenCV (cv2)
- NumPy

## Author
*
