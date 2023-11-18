import tkinter as tk
from PIL import Image, ImageTk


def center_frame(window, width, height):
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    x = (window_width - width) // 2
    y = (window_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

