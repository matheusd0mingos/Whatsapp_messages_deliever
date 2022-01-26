from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions
from threading import Thread 

#from dependencias import dependencias_install
options = webdriver.ChromeOptions()
import time

class chrome(Thread):
    def __init__(self, url='https://web.whatsapp.com/', admin="Matheus Domingos"):
        Thread.__init__(self)
        self.url=url
        self.admin=admin
        self.driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get(self.url)
        time.sleep(10)

       

