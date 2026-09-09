import uvicorn
import webbrowser
import threading
import time

def open_browser():
    time.sleep(1.2)
    webbrowser.open("http://localhost:8000")

if __name__ == "__main__":
    print("==================================================")
    print("  Iniciando PhysicsLab Uruguay...")
    print("  Abriendo navegador en: http://localhost:8000")
    print("==================================================")
    # Abre el navegador automaticamente en 1 segundo
    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
