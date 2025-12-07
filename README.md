# Weapon-Detection-using-Deep-learning
🔫 Weapon Detection Using Deep Learning

A simple and effective project that detects weapons (Gun / Knife) using Deep Learning and OpenCV.
This system can be used for CCTV monitoring, safety systems, and real-time alert generation.

📌 What This Project Does

✔ Detects guns

✔ Detects knives

✔ Works with webcam or video file

✔ Draws bounding boxes around detected weapons

✔ Includes a Tkinter GUI for easy usage

✔ Plays sound alerts when weapon is detected

✔ Sends email alerts with the captured frame

✔ Saves the detection frame for evidence

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
pip install opencv-python numpy pygame


If email alert uses SMTP, it is built-in with Python.

2️⃣ Run Detection (Without GUI)

Run using webcam:

python detect.py


Run using a video file:

python detect.py --video yourvideo.mp4

3️⃣ Run the Tkinter GUI Application
python "weapon detection with tkinter/weapondetectiontkinter.py"


The GUI allows you to:

▶ Start webcam

▶ Upload a video

▶ View live weapon detection

▶ Get sound alerts

▶ Receive email alerts with the detected frame

🧠 How the Detection Works

🔸 Uses YOLO-based Deep Learning model

🔸 Processes the video frame-by-frame

🔸 Detects:

🔫 Gun

🔪 Knife

🔸 Draws colored bounding boxes

🔸 Displays confidence score

This makes the system accurate and fast for real-time usage.

🔊 Alert System (Sound + Email)
✔ Sound Alert

A loud alert sound plays when a weapon is detected

Helps in real-time warning for nearby staff

✔ Email Alert

When a weapon is detected:

📤 An automatic email is sent

🖼️ The email contains the captured frame of the weapon

📝 Includes a warning message

This is useful for:

Schools

Colleges

Offices

Security rooms

Remote monitoring

📸 Example Output

✔ Weapon detected → highlighted with red box

✔ Label + confidence percentage displayed

✔ Email alert sent

✔ Frame saved for evidence

🛠️ Requirements

Python 3

OpenCV

NumPy

Tkinter (comes with Python)

Pygame (for alert sound)

smtplib / email library for sending alerts

Install pygame if missing:

pip install pygame

🎯 Why This Project Is Useful

✔ Real-time monitoring & surveillance

✔ Helps prevent dangerous situations

✔ Sends remote alerts via email

✔ Beginner-friendly and easy to extend

✔ Perfect for academic projects and demonstrations

📄 License

This project is open for learning, development, and improvements.
