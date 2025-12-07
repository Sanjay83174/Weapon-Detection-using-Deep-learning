import tkinter as tk
from tkinter import filedialog
import sys
import cv2
import numpy as np
import pyttsx3
import sendmail
from pygame import mixer
import threading
engine = pyttsx3.init()
engine.setProperty("rate", 120)
mixer.init()

def buzzer():
    sound = mixer.Sound('alarm.wav')
    sound.play()



def voicebuzzer():
    engine.say('crime detected')
    engine.runAndWait()

def detect_live_camera():
    # Add your code for live camera detection here
    net = cv2.dnn.readNet("savedmodel/yolo_training_2000.weights", "savedmodel/yolo.cfg")
    classes = ["Weapon"]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    count=0
    engine.say("Weapon detection activated")
    engine.runAndWait()
    cap=cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        height, width, channels = img.shape
        # width = 512
        # height = 512

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.9:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        #print(indexes)
        if indexes == 0: print("weapon detected in frame")
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
                cv2.imwrite("weapon.jpg", img)
                threading.Thread(target=buzzer).start()
                threading.Thread(target=voicebuzzer).start()
                count+=1
                print(count)
                if count==1:
                    threading.Thread(target=sendmail.sendalert).start()
                    #cv2.waitKey(0)
                    #cv2.destroyAllWindows()
        #counter=0

        # frame = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def detect_from_video():
    # Open file dialog to select video file
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
    # Update label to display selected file path
    if file_path:
        selected_video_label.config(text=file_path)
    net = cv2.dnn.readNet("savedmodel/yolo_training_2000.weights", "savedmodel/yolo.cfg")
    classes = ["Weapon"]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    count = 0
    # filename = selected_video_label
    print(file_path)
    path = file_path
    cap = cv2.VideoCapture(path)
    # print(path)
    while True:
        _, img = cap.read()
        height, width, channels = img.shape
        # width = 512
        # height = 512

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        # print(indexes)
        if indexes == 0:
            print("weapon detected in frame")
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
                cv2.imwrite("weapon.jpg", img)
                threading.Thread(target=buzzer).start()
                threading.Thread(target=voicebuzzer).start()
                count += 1
                if count == 1:
                    threading.Thread(target=sendmail.sendalert).start()
                    
        # counter=0
        # frame = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# Create the main window
root = tk.Tk()
root.title("WEAPON DETECTION AND ALERT SYSTEM")

# Set window size and center it on screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load background image
background_image = tk.PhotoImage(file="background.png")

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create header label
header_label = tk.Label(root, text="WEAPON DETECTION AND ALERT SYSTEM", font=("Arial", 16, "bold"))
header_label.place(relx=0.5, rely=0.1, anchor="center")

# Create buttons
detect_live_button = tk.Button(root, text="DETECT FROM LIVE CAMERA", command=detect_live_camera)
detect_live_button.place(relx=0.5, rely=0.4, anchor="center")

detect_video_button = tk.Button(root, text="DETECT FROM VIDEO", command=detect_from_video)
detect_video_button.place(relx=0.5, rely=0.6, anchor="center")

# Create label to display selected video file path
selected_video_label = tk.Label(root, text="", bg="white", wraplength=400)
selected_video_label.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
