import webview # Importa la librería para crear la ventana web

def abrir_asistencia():
    # 1. Creamos la ventana con la URL de tu sistema
    # 'on_top=True' hace que la ventana sea flotante (siempre arriba)
    window = webview.create_window(
        'Sistema de Asistencia', 
        'https://www.google.com',
        width=400, 
        height=600,
        on_top=True 
    )
    
    # 2. Iniciamos el motor
    webview.start()

if __name__ == '__main__':
    abrir_asistencia()
