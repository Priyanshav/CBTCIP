import tkinter as tk
from tkinter import messagebox
import numpy as np
import sounddevice as sd
import wavio


class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")
        self.root.geometry("400x300")
        self.root.config(bg="grey")

        self.is_recording = False
        self.audio = None

        self.record_btn = tk.Button(root, text="Record", command=self.start_rec, fg="green")
        self.record_btn.pack(padx=50, pady=20)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_rec, state=tk.DISABLED, fg="red")
        self.stop_btn.pack(padx=50, pady=20)

        self.play_btn = tk.Button(root, text="Play", command=self.play_rec, state=tk.DISABLED, fg="cyan")
        self.play_btn.pack(padx=50, pady=20)

        self.save_btn = tk.Button(root, text="Save", command=self.save_rec, state=tk.DISABLED, fg="magenta")
        self.save_btn.pack(padx=50, pady=20)

    def start_rec(self):
        self.is_recording = True
        self.record_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.audio = []

        def callback(indata, frames, time, status):
            if status:
                print(status, flush=True)
            if self.is_recording:
                self.audio.append(indata.copy())

        self.stream = sd.InputStream(samplerate=44100, channels=1, callback=callback)
        self.stream.start()

    def stop_rec(self):
        self.is_recording = False
        self.stream.stop()
        self.stream.close()

        self.record_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.play_btn.config(state=tk.NORMAL)
        self.save_btn.config(state=tk.NORMAL)

        self.audio = np.concatenate(self.audio)

    def play_rec(self):
        if self.audio is not None:
            sd.play(self.audio, samplerate=44100)
            sd.wait()

    def save_rec(self):
        if self.audio is not None:
            wavio.write("recording.wav", self.audio, 44100, sampwidth=2)
            messagebox.showinfo("Info", 'Audio saved as "recording.wav"')


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
