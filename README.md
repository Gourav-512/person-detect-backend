# 📸 Smart Students Attendance System – Person Detection Backend

**YOLOv8n + Flask API** | Auto person counting from classroom photo | Dockerized | Render Deployed | Perfect for Expo / React Native Mobile App

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-000000?logo=ultralytics&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?logo=render&logoColor=white)

### 🎯 Problem Solved
Manual attendance lene mein time waste + proxy issues.  
**Bas ek photo click karo** → AI automatically students count kar dega!

### ✨ Features
- Real-time person detection using **YOLOv8n** (class 0 = person)
- Annotated image with green bounding boxes
- Base64 image response (Expo/React Native mein directly display kar sakte ho)
- CORS enabled → Mobile + Web dono se call kar sakte ho
- Docker ready → Render pe 1-click deploy
- Lightweight & fast (yolov8n.pt model)

### 🛠 Tech Stack
- **Backend**: Flask + Flask-CORS
- **AI Model**: Ultralytics YOLOv8n (`yolov8n.pt`)
- **Computer Vision**: OpenCV
- **Deployment**: Docker + Render
- **Mobile**: Expo (React Native) – Camera → POST to `/detect`

### 🚀 Live API
**Render URL:** `https://person-detect-backend.onrender.com/detect`

### 📡 API Endpoint
**POST** `/detect`

**Request:**  
Form-data key = `image` (jpg/png file)

**Response:**
```json
{
  "person_count": 34,
  "image_base64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/..."
}
```
### 🧪 How to Test Locally
git clone https://github.com/Gourav-512/person-detect-backend.git
cd person-detect-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

###  🐳 Docker Build & Run
docker build -t person-detect .
docker run -p 5000:5000 person-detect

### 📁 Project Structure

├── app.py                 # Main Flask API
├── yolov8n.pt             # YOLOv8n model
├── requirements.txt
├── Dockerfile
├── attendance.csv         # Future attendance logging
├── uploads/               # Uploaded images
└── outputs/               # Processed images
