from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import os
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = YOLO("yolov8n.pt")

@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image"}), 400

    file = request.files["image"]
    img_bytes = file.read()

    np_img = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    results = model(img)[0]

    count = 0
    for box in results.boxes:
        if int(box.cls[0]) == 0:  # person
            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)

    _, buffer = cv2.imencode(".jpg", img)
    img_base64 = base64.b64encode(buffer).decode("utf-8")

    return jsonify({
        "person_count": count,
        "image_base64": img_base64
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
