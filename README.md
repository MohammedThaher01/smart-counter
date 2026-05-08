# Smart Counter 🚀

A high-performance Computer Vision application designed to detect and count objects in images and real-time video streams using **YOLOv8**.

## 🌟 Features
- **Web Dashboard**: Interactive UI built with **Gradio** for processing image uploads.
- **Real-time Detection**: Local **OpenCV** script for live object counting via webcam.
- **State-of-the-Art Accuracy**: Powered by the **YOLOv8** (You Only Look Once) model.
- **Instant Reporting**: Provides annotated visual output and a textual summary of detected object counts.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Computer Vision**: Ultralytics YOLOv8, OpenCV
- **Interface**: Gradio
- **Data Handling**: NumPy, Pillow

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/MohammedThaher01/smart-counter.git
cd smart-counter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
- **For Web UI**:
  ```bash
  python app.py
  ```
- **For Real-time Webcam Counter**:
  ```bash
  python counter.py
  ```

## 📸 Usage
1. **app.py**: Open the local URL provided by Gradio in your browser. Upload any image to see detected objects and their counts.
2. **counter.py**: Opens your webcam. Press **'q'** to exit the live stream.

## 📄 License
This project is open-source and available under the MIT License.
