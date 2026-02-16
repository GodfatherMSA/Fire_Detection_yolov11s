# 🔥 AI-Based Fire & Smoke Detection System (YOLOv11)

This project is a real-time **Fire and Smoke Detection System** developed for industrial safety and surveillance (CCTV) applications. 

Powered by the high-performance **YOLOv11** architecture, the model is optimized to detect fire and smoke at long distances while minimizing **false positives** (such as human faces, reflections, or hot objects like thermoses).

## 🚀 Key Features

- **Real-Time Detection:** High FPS processing on video streams or recorded footage.
- **High Accuracy:** Trained on a comprehensive dataset of **36,000+ images** (D-Fire + Custom Industrial Dataset).
- **Smart Classification:** Distinguishes between 'Fire' and 'Smoke' with high precision.
- **False Alarm Reduction:** Specifically tuned to ignore common false positives in factory environments.
- **Dynamic Class Mapping:** Includes a programmatic fix for model label ID swapping issues.

## 🛠️ Installation

Make sure you have Python installed. Install the required dependencies:

```bash
pip install ultralytics opencv-python
```
💻 Usage
Load the Model: Ensure yolo11s.pt is in the project directory.

Set the Source: Update the SOURCE variable in the code with your video path or RTSP stream link.

Run the System: python main.py

📂 Project Structure
Fire_test.py: Main application script for video analysis.

11sson.pt: Custom trained YOLOv11 weight file.

README.md: Project documentation.

🔍 Technical Details
Model: YOLOv11s (Custom Trained)

Dataset: 36k+ Labelled Images (Fire & Smoke)

Framework: PyTorch & Ultralytics

Image Processing: OpenCV