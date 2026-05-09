import tkinter as tk
from tkinter import scrolledtext, messagebox
import speech_recognition as sr


# ==========================================
# SPEECH RECOGNITION FUNCTION
# ==========================================
def recognize_speech():

    recognizer = sr.Recognizer()

    try:

        # Use microphone as input source
        with sr.Microphone() as source:

            status_label.config(
                text="Listening...",
                fg="green"
            )

            root.update()

            # Reduce background noise
            recognizer.adjust_for_ambient_noise(source)

            # Listen from microphone
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            status_label.config(
                text="Recognizing Speech...",
                fg="blue"
            )

            root.update()

            # Convert speech to text
            text = recognizer.recognize_google(audio)

            # Clear previous text
            output_text.delete("1.0", tk.END)

            # Display recognized text
            output_text.insert(tk.END, text)

            status_label.config(
                text="Speech Recognized Successfully",
                fg="darkgreen"
            )

    except sr.WaitTimeoutError:

        messagebox.showwarning(
            "Warning",
            "No speech detected."
        )

        status_label.config(
            text="Timeout",
            fg="red"
        )

    except sr.UnknownValueError:

        messagebox.showerror(
            "Error",
            "Could not understand audio."
        )

        status_label.config(
            text="Recognition Failed",
            fg="red"
        )

    except sr.RequestError:

        messagebox.showerror(
            "Error",
            "Internet connection required."
        )

        status_label.config(
            text="Connection Error",
            fg="red"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status_label.config(
            text="Error Occurred",
            fg="red"
        )


# ==========================================
# CLEAR FUNCTION
# ==========================================
def clear_text():

    output_text.delete("1.0", tk.END)

    status_label.config(
        text="Text Cleared",
        fg="gray"
    )


# ==========================================
# MAIN WINDOW
# ==========================================
root = tk.Tk()

root.title("AI Speech Recognition System")

root.geometry("900x600")

root.config(bg="#f2f2f2")


# ==========================================
# TITLE
# ==========================================
title = tk.Label(
    root,
    text="Speech-to-Text Recognition System",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2",
    fg="#222222"
)

title.pack(pady=20)


# ==========================================
# INSTRUCTION
# ==========================================
instruction = tk.Label(
    root,
    text="Click 'Start Listening' and speak through your microphone",
    font=("Arial", 13),
    bg="#f2f2f2"
)

instruction.pack()


# ==========================================
# BUTTON FRAME
# ==========================================
button_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)

button_frame.pack(pady=20)


# ==========================================
# START BUTTON
# ==========================================
start_button = tk.Button(
    button_frame,
    text="Start Listening",
    font=("Arial", 14, "bold"),
    bg="#0078D7",
    fg="white",
    padx=15,
    pady=8,
    cursor="hand2",
    command=recognize_speech
)

start_button.grid(row=0, column=0, padx=10)


# ==========================================
# CLEAR BUTTON
# ==========================================
clear_button = tk.Button(
    button_frame,
    text="Clear Text",
    font=("Arial", 14, "bold"),
    bg="#444444",
    fg="white",
    padx=15,
    pady=8,
    cursor="hand2",
    command=clear_text
)

clear_button.grid(row=0, column=1, padx=10)


# ==========================================
# STATUS LABEL
# ==========================================
status_label = tk.Label(
    root,
    text="Waiting for Speech Input",
    font=("Arial", 12, "bold"),
    bg="#f2f2f2",
    fg="gray"
)

status_label.pack()


# ==========================================
# OUTPUT LABEL
# ==========================================
output_label = tk.Label(
    root,
    text="Recognized Text:",
    font=("Arial", 14),
    bg="#f2f2f2"
)

output_label.pack(pady=10)


# ==========================================
# OUTPUT TEXT AREA
# ==========================================
output_text = scrolledtext.ScrolledText(
    root,
    width=95,
    height=15,
    font=("Arial", 12),
    wrap=tk.WORD
)

output_text.pack(pady=10)


# ==========================================
# FOOTER
# ==========================================
footer = tk.Label(
    root,
    text="Developed using Python, SpeechRecognition, and Tkinter",
    font=("Arial", 10),
    bg="#f2f2f2",
    fg="gray"
)

footer.pack(pady=5)


# ==========================================
# RUN APPLICATION
# ==========================================
root.mainloop()
