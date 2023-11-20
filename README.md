# Drowsiness_Project

Objective:
The main goal of the project seems to be detecting drowsiness in a person, likely from a video feed captured by a camera.

Components:

*Object Detection with YOLOv5:
     The project uses the YOLOv5 model for object detection. YOLO (You Only Look Once) is a real-time object detection system that can detect multiple objects in an image or video frame.
*Serial Communication with Arduino:
     The script establishes a serial communication connection (serial.Serial) with an Arduino board connected to the computer through a specific COM port (COM7). The Arduino likely controls external hardware based on the drowsiness detection.
*Alarm System:
    Pygame is used to play an alarm sound when drowsiness is detected. The play_alarm() function is called when the script detects a drowsy state for four consecutive frames.
*Drowsiness Detection Logic:
    The script maintains a score variable, which increments when drowsiness is detected and resets when no drowsiness is found. When the score reaches a threshold (4 frames in a row with drowsiness), the alarm is triggered.
*User Interface:
    The script uses OpenCV to display the video feed with YOLOv5 detections in real-time. This provides a visual representation of the object detection process.

Workflow:

*Capture Video:
    The script captures video frames from a camera (likely the default camera) using OpenCV.
*Object Detection:
   YOLOv5 is applied to each frame to detect objects, particularly focusing on detecting signs of drowsiness.
*Communication with Arduino:
   Information about the detected state ('drowsy', 'null', or other) is sent to the Arduino through serial communication.
*Drowsiness Evaluation:
   The script evaluates the drowsiness state based on the YOLOv5 detections and increments a score accordingly.
*Alarm Trigger:
   If the drowsiness score exceeds a certain threshold, the alarm is triggered.
*Visual Feedback:
    The video frames with YOLOv5 detections are displayed in real-time using OpenCV.
*User Interaction:
   The script exits the loop when the user presses the 'q' key.
