# 🐶 Dog Breed Identification using Deep Learning

## 📌 Overview
This project is a Flask web application that predicts the breed of a dog from an uploaded image using Deep Learning (VGG19 Transfer Learning).

Workflow:  
User uploads image → Model predicts breed → Result displayed instantly.

---

## 🚀 Features
- Upload dog image via web interface  
- Predicts 20 dog breeds  
- Transfer Learning using VGG19  
- Image augmentation for better accuracy  
- Simple Flask deployment  

---

## 🧠 Model Summary

| Item | Details |
|------|---------|
| Model | VGG19 Transfer Learning |
| Input Size | 224 × 224 |
| Classes | 20 Dog Breeds |
| Framework | TensorFlow / Keras |
| Saved Model | dogbreed.h5 |

---

## 🐕 Supported Breeds
Affenpinscher, Beagle, Appenzeller, Basset, Bluetick, Boxer, Cairn, Doberman,  
German Shepherd, Golden Retriever, Kelpie, Komondor, Leonberg, Mexican Hairless,  
Pug, Redbone, Shih-Tzu, Toy Poodle, Vizsla, Whippet.

---

## 📥 Download Trained Model
The trained model file (223MB) is not stored in this repository due to size limitations.

Download it from Google Drive:  
https://drive.google.com/file/d/1RQlBXRI01BkJi0Q317zgXwbDxdI_Gw6w/view?usp=sharing

After downloading, place the file in the project root directory:

```

project/
│
├── app.py
└── dogbreed.h5

```

---

## 📂 Project Structure
```

project/
│
├── static/          # CSS files
├── templates/       # HTML pages
├── uploads/         # Uploaded images
├── app.py           # Flask backend
└── dogbreed.h5      # Trained model (download separately)

```

---

## 📊 Dataset & Training
Dataset used: **Kaggle Dog Breed Identification**

Training steps:
1. Download dataset using Kaggle API (Google Colab)  
2. Selected 20 dog breeds from dataset  
3. Applied image augmentation & normalization  
4. Created 80/20 train–validation split  
5. Used VGG19 pretrained model (transfer learning)  
6. Added custom classifier layers  
7. Trained for 6 epochs  
8. Saved model as **dogbreed.h5**

---

## 🌐 Run the Web App

### Step 1 — Install dependencies
```

pip install flask tensorflow numpy pillow

```

### Step 2 — Run the application
```

python app.py

```

### Step 3 — Open in browser
```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

---

## 🔮 Future Improvements
- Add more dog breeds  
- Improve accuracy with fine-tuning  
- Deploy on cloud platforms (Render / AWS / Heroku)