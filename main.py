import warnings

# Ignorar el FutureWarning específico de PyTorch
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")

from gui import WhisperApp

if __name__ == "__main__":
    app = WhisperApp()
    app.run()