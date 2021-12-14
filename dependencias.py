import selenium
from getpip import installer

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def dependencias_install():
    install('pandas')
    install('PyQt5')
    install('selenium')
    install('webdriver-manager')

