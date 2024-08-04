import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading

class Alarma:
    def __init__(self, root):
        self.root = root
        self.root.title("Alerta")

        self.time_label = tk.Label(root, text="Hora (HH:MM:SS)", font=("Arial", 12))
        self.time_label.pack(pady=10)

        self.time_entry = tk.Entry(root, font=("Arial", 16))
        self.time_entry.pack(pady=10)

        self.button = tk.Button(root, text="Establecer alarma", command=self.set_alarm, font=("Arial", 12))
        self.button.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.alarm_time = None

    def set_alarm(self):
        alarm_time_str = self.time_entry.get()
        try:
            self.alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").time()
            self.status_label.config(text=f"Alarma establecida para {self.alarm_time.strftime('%H:%M:%S')}")
            threading.Thread(target=self.check_alarm).start()
        except ValueError:
            messagebox.showerror("Formato incorrecto", "Por favor introduce una hora correcta")

    def check_alarm(self):
        while True:
            if self.alarm_time:
                now = datetime.now().time()
                if now >= self.alarm_time:
                    messagebox.showinfo("Alarma", "Alerta!!!!")
                    self.alarm_time = None
                    self.status_label.config(text="")
                    break
            time.sleep(1)

root = tk.Tk()
root.geometry("300x200")

alarma = Alarma(root)
root.mainloop()