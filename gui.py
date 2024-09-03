import tkinter as tk
from tkinter import filedialog
from whisper_runner import run_whisper_command

class WhisperApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Whisper")
        self.setup_ui()

    def setup_ui(self):
        # Configuración de la ventana principal
        self.root.geometry("1300x800")  # Tamaño de la ventana principal

        # Configuración del diseño principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Añade márgenes a los lados y arriba/abajo

        # Título
        title_label = tk.Label(main_frame, text="Whisper", font=("Arial", 16))
        title_label.pack(pady=10)

        # Botón "Seleccionar archivo"
        select_button = tk.Button(main_frame, text="Seleccionar archivo", command=self.select_file)
        select_button.pack(pady=10)

        # Frame para el cuadro de texto con márgenes laterales
        text_frame = tk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Cuadro de texto para la salida
        self.output_text = tk.Text(text_frame, width=150, height=45)  # Aproximación de tamaño
        self.output_text.pack(pady=10, fill=tk.BOTH, expand=True)

        # Configurar la etiqueta de estilo para el mensaje de finalización
        self.output_text.tag_configure("completion", foreground="green", font=("Arial", 20, "bold"))

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
            self.output_text.insert(tk.END, "\n PROCESO COMPLETADO", "completion")
            self.output_text.see(tk.END)
            self.output_text.update()
        
        run_whisper_command(file_path, self.output_text, on_completion)

    def run(self):
        self.root.mainloop()
