import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Set the correct path to Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pick_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )
    if file_path:
        image = Image.open(file_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)

        label_image.config(image=img)
        label_image.image = img  # Keep reference

        # Extract text from the resized image
        text = pytesseract.image_to_string(image)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("OCR Image to Text")
root.geometry("500x300")

# Left Frame (For Image)
left_frame = tk.Frame(root, width=200, height=300)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

pick_button = tk.Button(left_frame, text="Pick Image", command=pick_image)
pick_button.pack(pady=20)

label_image = tk.Label(left_frame)
label_image.pack()

# Right Frame (For Text Display)
right_frame = tk.Frame(root, width=300, height=300)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

text_area = tk.Text(right_frame, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
