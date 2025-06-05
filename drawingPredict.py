import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('mnist_model.h5')

class DigitRecognizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Handwritten Digit Recognizer")

        self.canvas_width = 280
        self.canvas_height = 280
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.image = Image.new("L", (self.canvas_width, self.canvas_height), color=255)  # white background
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.predict_button = tk.Button(master, text="Predict", command=self.predict_digit)
        self.predict_button.pack()

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        self.result_label = tk.Label(master, text="Draw a digit and click Predict", font=("Helvetica", 16))
        self.result_label.pack()

    def paint(self, event):
        x1, y1 = (event.x - 8), (event.y - 8)
        x2, y2 = (event.x + 8), (event.y + 8)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
        self.draw.ellipse([x1, y1, x2, y2], fill=0)  # draw black on PIL image

    def preprocess_image(self):
        # Resize to 28x28 and invert colors (MNIST digits are white on black)
        img = self.image.resize((28, 28))
        img = ImageOps.invert(img)
        img = img.convert('L')

        # Normalize pixels
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)  # Model input shape

        return img_array

    def predict_digit(self):
        img_array = self.preprocess_image()
        prediction = model.predict(img_array)
        digit = np.argmax(prediction)
        confidence = np.max(prediction)
        self.result_label.config(text=f"Predicted Digit: {digit} (Confidence: {confidence:.2f})")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.canvas_width, self.canvas_height], fill=255)
        self.result_label.config(text="Draw a digit and click Predict")        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drawing Prediction")

    app = DigitRecognizerApp(root)
    root.mainloop()
