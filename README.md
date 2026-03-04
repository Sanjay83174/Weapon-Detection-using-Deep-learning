# 🔫 Weapon Detection Using Deep Learning

An intelligent **Weapon Detection System** built using Deep Learning and OpenCV.

This project detects:

- 🔫 Guns  
- 🔪 Knives  

It works with:

- 🎥 Live Webcam  
- 🎬 Video Files  

The system provides real-time monitoring, alert generation, and evidence capture, making it suitable for surveillance and security applications.

---

# 📌 Project Overview

This project focuses on building a real-time weapon detection system using a **YOLO-based Deep Learning model**.

The system:

- Detects weapons in video frames  
- Draws bounding boxes with confidence scores  
- Plays alert sounds  
- Sends email notifications with captured evidence  
- Provides a simple Tkinter GUI for user interaction  

The goal is to enhance surveillance and support early threat detection.

---

# ✨ Features

- 🔫 Detects guns  
- 🔪 Detects knives  
- 🎥 Works with webcam or video file  
- 🟥 Draws bounding boxes around detected weapons  
- 🖥️ Tkinter GUI for easy usage  
- 🔊 Sound alerts when weapon is detected  
- 📧 Sends email alerts with captured frame  
- 💾 Saves detection frame as evidence  

---

# 🧠 How Detection Works

- Uses **YOLO-based Deep Learning model**
- Processes video frame-by-frame
- Detects:
  - Gun
  - Knife
- Draws colored bounding boxes
- Displays confidence score
- Triggers alert system when detection confidence crosses threshold

This ensures fast and accurate real-time detection.

---

# 📂 Project Structure

```
Weapon-Detection-using-Deep-learning/
│
├── weapon detection with tkinter/
│   └── weapondetectiontkinter.py     # Tkinter GUI application
│
├── detect.py                        # Detection via webcam/video
│
├── model/ or weights/               # YOLO model files (weights/config)
│
├── Images/                          # Sample images
├── Videos/                          # Sample videos
│
└── README.md
```

---

# 🖥️ How to Run the Project

## 1️⃣ Install Required Libraries

```bash
pip install opencv-python numpy pygame
```

Tkinter comes pre-installed with Python.

SMTP for email alerts uses built-in Python libraries.

If pygame is missing:

```bash
pip install pygame
```

---

# ▶ Run Detection (Without GUI)

## 🔹 Using Webcam

```bash
python detect.py
```

## 🔹 Using Video File

```bash
python detect.py --video yourvideo.mp4
```

---

# 🖥️ Run the Tkinter GUI Application

```bash
python "weapon detection with tkinter/weapondetectiontkinter.py"
```

The GUI allows you to:

- ▶ Start webcam  
- 📂 Upload video  
- 👀 View live detection  
- 🔊 Get sound alerts  
- 📧 Receive email alerts  

---

# 🔊 Alert System (Sound + Email)

## ✔ Sound Alert

- Plays loud alert sound when weapon detected  
- Helps in immediate real-time warning  

## ✔ Email Alert

When a weapon is detected:

- 📤 Automatic email is sent  
- 🖼️ Captured frame attached  
- 📝 Warning message included  

Useful for:

- 🏫 Schools  
- 🏢 Offices  
- 🎓 Colleges  
- 🛡️ Security Rooms  
- 🌍 Remote Monitoring  

---

# 📸 Example Output

When a weapon is detected:

- 🟥 Red bounding box drawn  
- 🏷️ Label displayed (Gun / Knife)  
- 📊 Confidence percentage shown  
- 📧 Email alert sent  
- 💾 Frame saved for evidence  

---

# 🛠️ Requirements

- Python 3  
- OpenCV  
- NumPy  
- Tkinter  
- Pygame  
- smtplib (built-in)  

---

# 🎯 Why This Project Is Useful

- ✔ Real-time surveillance system  
- ✔ Enhances security monitoring  
- ✔ Automatic remote alerts  
- ✔ Academic demonstration project  
- ✔ Beginner-friendly and extendable  
- ✔ Can be integrated into CCTV systems  

---

# 🚀 Future Improvements

- Deploy on edge devices (Raspberry Pi)  
- Cloud-based alert system  
- SMS integration  
- Multiple camera support  
- Improve model accuracy with custom dataset  
- Web-based dashboard  

---

# 👨‍💻 Author

Sanjay HL  
Deep Learning & Computer Vision Enthusiast  

If you found this project useful, please ⭐ star the repository!

---

# 📜 License

This project is open for learning, development, and improvements.

Licensed under the MIT License.
