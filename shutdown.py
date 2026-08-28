import os
import platform
opesys = platform.system()
is opesys == 'Linux':
    os.system("sudo shutdown -h now")
elif opesys == "win32":
  os.system("shutdown /s /t 0")
