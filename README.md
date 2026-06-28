# WakeGuard

WakeGuard is a real-time AI-powered drowsiness detection system that monitors eye movement using a webcam and alerts users when signs of drowsiness are detected.

## Features

- Real-time webcam monitoring
- Eye closure detection
- Live facial landmark tracking
- Audio alarm on drowsiness
- Visual alerts
- Lightweight and easy to run

## Tech Stack

- Python
- OpenCV
- cvzone
- MediaPipe
- Pygame

## Project Structure
WakeGuard/
│── main.py
│── alarm.wav
│── requirements.txt
│── README.md

## Installation

### Clone the repository

git clone https://github.com/yourusername/WakeGuard.git

### Install dependencies

pip install opencv-python
pip install cvzone
pip install mediapipe
pip install pygame

### Run
python main.py

##  How It Works

1. Opens the webcam.
2. Detects facial landmarks.
3. Tracks eye openness.
4. If the eyes remain closed for a specified duration:
   - Displays a warning.
   - Plays an alarm sound.

##  Applications

- Students
- Office workers
- Long study sessions
- Fatigue awareness

## 📸 Future Improvements

- Android application
- Website integration
- Driver drowsiness detection
- AI-based fatigue prediction


## 👩‍💻 Developed By

Reshita Bendi
