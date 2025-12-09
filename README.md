# 🖼️ Image Recognition Web App (Flask + TensorFlow)

A simple and powerful **Image Recognition Web Application** built using **Python, Flask, and TensorFlow (MobileNetV2)**.  
This app allows users to upload an image and get the **top 5 predicted objects** along with confidence scores.

🚀 **Live Demo:** https://image-recognition-app-b5sl.onrender.com

---

## ✨ Features

- Upload any image (JPG, PNG, JPEG, GIF)
- Identifies objects using a pretrained MobileNetV2 model
- Shows top-5 predictions with accuracy percentages
- Clean and simple web interface
- Fully deployable on Render, Railway, or Docker

---

## 🧠 Technologies Used

| Technology     | Purpose |
|----------------|---------|
| **Python**     | Backend logic |
| **Flask**      | Web framework |
| **TensorFlow** | Image classification |
| **Pillow**     | Image processing |
| **HTML/CSS**   | Frontend template |
| **Gunicorn**   | Production server (Render deployment) |

---

## 📂 Project Structure
image_recognition_app/
│── app.py
│── requirements.txt
│── Procfile
│── README.md
│── .gitignore
│── static/
│ └── uploads/
│── templates/
└── index.html




---

## ▶️ How It Works

1. User uploads an image  
2. Flask saves the image  
3. Image is preprocessed (224×224, RGB, normalization)  
4. TensorFlow model predicts labels  
5. App displays predictions + uploaded image

---

## 🛠️ Run Locally

### 1️⃣ Clone the repo
```bash
git clone https://github.com/suryasreeja/image_recognition_app.git
cd image_recognition_app



