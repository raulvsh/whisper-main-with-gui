import subprocess
import threading
import os

def run_whisper_command(file_path, output_widget, on_completion):
    def execute():
        # Obtener el directorio del archivo de audio
        output_dir = os.path.dirname(file_path)

        command = [
            "whisper", 
            file_path, 
            "--model", "medium", 
            "--output_format", "txt", 
            "--output_dir", output_dir
        ]

        # Crear el objeto de proceso con CREATE_NO_WINDOW
        startup_info = subprocess.STARTUPINFO()
        startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startup_info.wShowWindow = subprocess.SW_HIDE

        try:
            # Ejecutar el comando
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, startupinfo=startup_info)

            # Obtener la salida y los errores del proceso
            stdout, stderr = process.communicate()

            # Insertar la salida estándar en el widget de salida
            if stdout:
                output_widget.insert("end", stdout)
                output_widget.see("end")  # Scroll al final
                output_widget.update()

            # Insertar la salida de error en el widget de salida si la hay
            if stderr:
                output_widget.insert("end", stderr)
                output_widget.see("end")
                output_widget.update()

        except Exception as e:
            # Manejo de excepciones si ocurre un error durante la ejecución
            output_widget.insert("end", f"Error al ejecutar el comando: {str(e)}\n")
            output_widget.see("end")
            output_widget.update()

        finally:
            # Asegúrate de que el proceso se cierre correctamente
            if process.poll() is None:  # Verifica si el proceso sigue en ejecución
                process.terminate()  # Termina el proceso si aún está en ejecución
                output_widget.insert("end", "llego a terminate\n")


            # Llama al callback de finalización
            if on_completion:
                output_widget.after(0, on_completion)



    # Ejecuta en un hilo separado para no bloquear la GUI
    threading.Thread(target=execute).start()
