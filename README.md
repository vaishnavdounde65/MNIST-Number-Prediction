# 🔢 MNIST Number Prediction

> Predict handwritten digits using a trained deep learning model and an interactive drawing canvas built with Tkinter.

---

## 📌 Project Overview

This project demonstrates a simple yet effective way to train a digit recognition model on the MNIST dataset and use it in a graphical interface for real-time predictions.

- 🎯 **Train your own model** with `model.py`  
- 🎨 **Draw digits and predict** them live with `drawingPredict.py`

---

## ✨ Features

- 🧠 Trains a deep learning model using TensorFlow/Keras
- 🖌️ Interactive canvas using Tkinter
- 💾 Saves and loads trained model automatically
- 🔍 Real-time digit recognition after drawing

---

## 🛠️ Tech Stack

| Tool           | Purpose                  |
|----------------|--------------------------|
| Python         | Programming Language     |
| TensorFlow/Keras | Model Training         |
| Tkinter        | GUI Drawing Canvas       |
| NumPy & PIL    | Image Processing         |
| MNIST Dataset  | Training Dataset         |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vaishnavdounde65/MNIST-Number-Prediction.git
cd mnist-number-predictor
```

### 2️⃣ Install Dependencies
pip install PIL numpy tensorflow tkinter

    Note: Make sure Python ≥ 3.6 is installed.
    
### 🧠 Train the Model

Run the script to train and save the model:

python model.py

    Trains on the MNIST dataset

    Saves the model as mnist_model.h5

### 🖼️ Predict with Drawing Interface

Use the drawing interface to draw digits and predict:

python drawingPredict.py

    A Tkinter window will open

    Draw a digit with your mouse

    Click Predict to see the model’s guess!

### 📁 File Structure
```📦 MNIST-Number-Prediction
├── model.py              # Train and save the model
├── drawingPredict.py     # GUI for drawing and predicting
├── mnist_model.h5        # Saved model (after training)
└── README.md             # Project overview
```

### 📸 Demo
[![Watch the video](https://img.youtube.com/vi/pG6k8O-8NP4/maxresdefault.jpg)](https://youtu.be/pG6k8O-8NP4)

### 🙌 Acknowledgements

    MNIST Dataset - Yann LeCun

    TensorFlow/Keras

    Tkinter GUI Library

### 📬 Contact

Vaishnav Dounde
🌐 [vaishnav.site](https://vaishnav.site/)
    
### ⭐ Star This Repository

If you found this project useful, feel free to ⭐ the repo and share it!
