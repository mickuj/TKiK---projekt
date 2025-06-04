import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from antlr4 import *
from PythonMelodyLexer import PythonMelodyLexer
from PythonMelodyParser import PythonMelodyParser
from MelodyInterpreter import MelodyInterpreter
from player import play_melody
from error_handler import CustomErrorListener
from midi_writer import save_melody_to_midi
import threading
import os


class MelodyGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Melody Composer")
        self.root.geometry("400x700")  # smukły wygląd pionowy
        self.root.configure(bg="#121212")

        self.current_notes = []
        self.progress_var = tk.DoubleVar(value=0)
        self.status_var = tk.StringVar(value="Ready")

        self.setup_ui()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background="#1c1c2e")
        style.configure("TLabel", background="#1c1c2e", foreground="#e0e0ff", font=("Helvetica", 10))
        style.configure("Tool.TButton", font=("Helvetica", 14), background="#1db954", foreground="#ffffff")
        style.map("Tool.TButton",
                  background=[('active', '#1ed760')],
                  foreground=[('active', '#ffffff')])

        style.configure("Horizontal.TProgressbar",
                        troughcolor="#2f2f3f",
                        background="#66ccff",
                        thickness=10)

        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pole kodu
        code_frame = ttk.LabelFrame(main_frame, text="Python Code", padding=10)
        code_frame.pack(fill=tk.BOTH, expand=True)

        self.code_input = scrolledtext.ScrolledText(
            code_frame,
            height=22,
            wrap=tk.WORD,
            font=('Consolas', 11),
            bg="#2e2e42",
            fg="#e0e0ff",
            insertbackground="#e0e0ff"
        )
        self.code_input.pack(fill=tk.BOTH, expand=True)

        self.code_input.insert(tk.END, '''def example():
    print("Hello!")
    for i in range(3):
        if i % 2 == 0:
            print(i)
    return 42''')

        # Status
        status_label = ttk.Label(main_frame, textvariable=self.status_var, anchor=tk.CENTER)
        status_label.pack(pady=(10, 5))

        # Przyciski
        style.configure("Emoji.TButton",
                        font=("Segoe UI Emoji", 14),
                        padding=8,
                        background="#8a2be2",
                        foreground="white")
        style.map("Emoji.TButton",
                  background=[('active', '#b75ec5'), ('!disabled', '#8c4697')],
                  foreground=[('active', 'white'), ('!disabled', 'white')])

        # Ramka na przyciski
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=5)

        # Przyciski z emoji i stylami
        btn_play = ttk.Button(buttons_frame, text="▶", command=self.generate_and_play, width=3, style="Emoji.TButton")
        btn_save = ttk.Button(buttons_frame, text="💾", command=self.save_midi, width=3, style="Emoji.TButton")
        btn_open = ttk.Button(buttons_frame, text="📂", command=self.open_file, width=3, style="Emoji.TButton")
        btn_clear = ttk.Button(buttons_frame, text="🗑️", command=self.clear_code, width=3, style="Emoji.TButton")

        # Rozmieszczenie przycisków
        btn_play.grid(row=0, column=0, padx=6)
        btn_save.grid(row=0, column=1, padx=6)
        btn_open.grid(row=0, column=2, padx=6)
        btn_clear.grid(row=0, column=3, padx=6)

        for i, btn in enumerate([btn_play, btn_save, btn_open, btn_clear]):
            btn.grid(row=0, column=i, padx=6)

        # Pasek postępu
        self.progress_bar = ttk.Progressbar(
            main_frame,
            variable=self.progress_var,
            orient=tk.HORIZONTAL,
            length=300,
            mode='determinate',
            style="Horizontal.TProgressbar"
        )
        self.progress_bar.pack(pady=(5, 5))

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def generate_and_play(self):
        code = self.code_input.get("1.0", tk.END).strip()
        if not code:
            messagebox.showwarning("Warning", "Please enter Python code first!")
            return

        try:
            self.status_var.set("Generating melody...")
            self.root.update()
            input_stream = InputStream(code)

            lexer = PythonMelodyLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = PythonMelodyParser(token_stream)

            listener = MelodyInterpreter()

            parser.removeErrorListeners()
            parser.addErrorListener(CustomErrorListener(listener))

            tree = parser.program()

            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            listener.finish()
            self.background_notes = listener.background_notes

            self.current_notes = listener.notes
            self.status_var.set("Generated melody. Playing...")
            threading.Thread(target=self.play_notes, daemon=True).start()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate melody:\n{str(e)}")
            self.status_var.set("Error occurred")

    def play_notes(self):
        try:
            total = len(self.current_notes)
            for idx, (note, duration) in enumerate(self.current_notes):
                self.progress_var.set((idx + 1) / total * 100)
                self.root.update_idletasks()
                play_melody([(note, duration)])
            self.status_var.set("Playback finished")
        except Exception as e:
            messagebox.showerror("Playback Error", f"Cannot play melody:\n{str(e)}")
            self.status_var.set("Playback failed")

    def save_midi(self):
        if not self.current_notes:
            messagebox.showwarning("Warning", "No melody to save. Generate one first!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".mid",
                                                 filetypes=[("MIDI files", "*.mid")])
        if file_path:
            save_melody_to_midi(self.current_notes, self.background_notes, file_path)
            self.status_var.set(f"MIDI saved to {os.path.basename(file_path)}")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as f:
                content = f.read()
            self.code_input.delete("1.0", tk.END)
            self.code_input.insert(tk.END, content)
            self.status_var.set(f"Loaded: {os.path.basename(file_path)}")

    def clear_code(self):
        self.code_input.delete("1.0", tk.END)
        self.status_var.set("Editor cleared")