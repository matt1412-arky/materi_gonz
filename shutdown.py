import os
import platform

def shutdown():
    sistem = platform.system()
    if sistem == "Windows":
        os.system("shutdown /s /t 1")   # shutdown langsung
    elif sistem == "Linux" or sistem == "Darwin":  # Darwin = MacOS
        os.system("sudo shutdown now")
    else:
        print("Sistem operasi tidak dikenali.")

shutdown()
