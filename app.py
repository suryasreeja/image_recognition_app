# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np
from PIL import Image

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# load model once
model = MobileNetV2(weights="imagenet")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path, top=5):
    img = Image.open(img_path).convert("RGB").resize((224, 224))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=top)[0]
    return [(name.replace("_", " "), float(score)) for (_, name, score) in decoded]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)
            preds = predict_image(save_path, top=5)
            return render_template("index.html", filename=filename, predictions=preds)
    return render_template("index.html", filename=None)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return redirect(url_for('static', filename=f"uploads/{filename}"), code=301)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
