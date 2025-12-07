# Weapon-Detection-using-Deep-learning
🔫 Weapon Detection Using Deep Learning

A simple and effective project that detects weapons (Gun / Knife) using Deep Learning and OpenCV.
This system can be used for CCTV monitoring, safety systems, and real-time alert generation.

📌 What This Project Does

Detects guns and knives

Works with webcam or video file

Draws bounding boxes around detected weapons

Includes a Tkinter GUI for easy use

Supports sound alert + email alert

Saves the detected frame for evidence

📂 Project Structure
Weapon-Detection-using-Deep-learning
│
├── weapon detection with tkinter/
│   └── weapondetectiontkinter.py       → Tkinter GUI application
│
├── detect.py                            → Weapon detection through webcam/video
├── model/ or weights/                   → YOLO model files (weights/config)
│
├── Images/                              → Sample images
├── Videos/                              → Sample videos
│
└── README.md                            → Documentation

🖥️ How to Run the Project
1️⃣ Install Required Libraries
pip install opencv-python numpy pygame smtplib


(If using PyTorch/TensorFlow, install that too.)

2️⃣ Run Detection (Without GUI)

Webcam:

python detect.py


Video file:

python detect.py --video yourvideo.mp4

3️⃣ Run the Tkinter GUI
python "weapon detection with tkinter/weapondetectiontkinter.py"


This GUI allows you to:

Start webcam

Select video

View detection results

Get sound alerts

Get email alerts with captured image

🧠 How the Detection Works

Uses a YOLO-based deep learning model

Processes every video frame

Detects:

Gun

Knife

Draws colored bounding boxes

Shows confidence percentage

🔊 Alert System (Sound + Email)

When a weapon is detected, the system can:

✔ Play a sound alert

Useful for immediate onsite warning.

✔ Send an email alert automatically

The email contains:

A short warning message

A captured image of the frame where the weapon is detected

This feature is helpful for:

Security rooms

Colleges

Offices

Real-time monitoring systems

You can configure:

Sender email

Receiver email

Email subject and message

📸 Example Output

Gun detected → red box

Knife detected → red box

Label + confidence score displayed

Alert immediately triggered

🛠️ Requirements

Python 3

OpenCV

NumPy

Tkinter (comes with Python)

Pygame (for sound)

smtplib / email library (Python’s built-in email sending library)

Install pygame if needed:

pip install pygame

🎯 Why This Project Is Useful

Real-time safety monitoring

Helps in surveillance

Includes Email Alert System for immediate remote notification

Easy for students and developers to understand

Can be expanded into a full security product

📄 License

This project is open for learning, development, and improvements.

