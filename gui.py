import tkinter as tk
from tkinter import filedialog, scrolledtext
from whisper_runner import run_whisper_command

class WhisperApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Whisper")
        self.setup_ui()

    def setup_ui(self):
        # Configuración de la ventana principal
        self.root.geometry("1300x800")  # Un poco más grande para incluir márgenes y otros elementos
        
        # Título
        title_label = tk.Label(self.root, text="Whisper", font=("Arial", 16))
        title_label.pack(pady=10)

        # Botón "Seleccionar archivo"
        select_button = tk.Button(self.root, text="Seleccionar archivo", command=self.select_file)
        select_button.pack(pady=10)

        # Cuadro de texto para la salida con tamaño 1280x720 px
        self.output_text = tk.Text(self.root, width=150, height=45)  # Ajuste de tamaño basado en aproximación de píxeles
        self.output_text.pack(pady=10)

        # Fijar el tamaño del cuadro de texto
        self.output_text.config(width=128, height=45)  # Ajuste aproximado para llegar a 1280x720
        
        # Etiqueta para el mensaje de finalización
        self.completion_label = tk.Label(self.root, text="", fg="green", font=("Arial", 12))
        self.completion_label.pack(pady=10)

    def select_file(self):
        # Abrir explorador de archivos para seleccionar archivo de audio
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg")]
        )
        if file_path:
            self.run_whisper(file_path)

    def run_whisper(self, file_path):
        # Ejecuta el comando Whisper y muestra la salida
        self.output_text.insert(tk.END, f"Ejecutando Whisper en: {file_path}\n")
        self.root.update()

        # Define la función de callback para mostrar el mensaje de finalización
        def on_completion():
            self.completion_label.config(text="Proceso completado")
        
        run_whisper_command(file_path, self.output_text, on_completion)

    def run(self):
        self.root.mainloop()
