from chrome import *
import keyboard
#  é o valor do data_tab


class Whatsapp(chrome):
    def __init__(self, url='https://web.whatsapp.com/', admin="Matheus Domingos")->None:
        super().__init__(url, admin)

    def enter_site_with_msg(self, telefone, encoded_msg)->None:
        url = 'https://web.whatsapp.com/send?phone=55' + telefone + '&text=' +encoded_msg
        self.driver.get(url)
        print("Entrando na conversa...")
        self.driver.execute_script("window.onbeforeunload = function() {};")

    def element_finder_msg_sender(self, data_tab=10)->None:
        elemento = WebDriverWait(self.driver, 13).until(ec.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='"+str(data_tab)+"']")))
        time.sleep(2)
        elemento.send_keys(Keys.RETURN)
        time.sleep(2)
        elemento.send_keys(Keys.RETURN)
        time.sleep(3)
        print('Enviando...')

    def element_finder_file_sender(self, imgPath):
        #To send attachments
        #click to add
        self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
        #add file to send by file path
        self.driver.find_element_by_css_selector("input[type='file']").send_keys(imgPath)
        #click to send            
        keyboard.press_and_release('enter')
        time.sleep(2)
        #Por precaução
        msg1_box = self.driver.switch_to.active_element
        msg1_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def send_text_only(self, telefone, encoded_msg)->bool:
        self.enter_site_with_msg(telefone, encoded_msg)
        try:
            self.element_finder_msg_sender( )
            return True
        except selenium.common.exceptions.TimeoutException:
            try:
                print('O elemento não foi encontrado na primeira tentativa')
                self.element_finder_msg_sender(9)
                return True
            except selenium.common.exceptions.TimeoutException:
                try:
                    print('O elemento não foi encontrado na segunda tentativa')
                    self.element_finder_msg_sender(6)
                except selenium.common.exceptions.TimeoutException:
                    print('Ocorreu um erro no envio, provavelmente conexão lenta... Fale com '+self.admin)
                    return False
        except selenium.common.exceptions.InvalidElementStateException:
            try:
                self.element_finder_msg_sender( ) 
                time.sleep(2)
                msg1_box = self.driver.switch_to.active_element
                msg1_box.send_keys(Keys.RETURN)
                return True

            except selenium.common.exceptions.TimeoutException:
                print('Ocorreu um erro fale com '+self.admin)
                return False

    def send_text_and_image(self, telefone, encoded_msg, imgPath)->bool:
        self.enter_site_with_msg(telefone, encoded_msg)
        try:
            self.element_finder_msg_sender()
            self.element_finder_file_sender(imgPath)
            return True
                
        except selenium.common.exceptions.TimeoutException:
            try:
                self.element_finder_msg_sender(9)
                self.element_finder_file_sender(imgPath)
                return True
            except selenium.common.exceptions.TimeoutException:
                try:
                    self.element_finder_msg_sender(6)
                    self.element_finder_file_sender(imgPath)
                    return True
                except selenium.common.exceptions.TimeoutException:
                    print('Ocorreu um erro no envio, provavelmente conexão lenta... Fale com '+self.admin)
                    return False
            
        except selenium.common.exceptions.InvalidElementStateException:
            try:
                self.element_finder_msg_sender() 
                time.sleep(2)
                msg1_box = self.driver.switch_to.active_element
                msg1_box.send_keys(Keys.RETURN)
                self.element_finder_file_sender(imgPath)
                return True

            except selenium.common.exceptions.TimeoutException:
                print('Ocorreu um erro fale com '+self.admin)
                return False


    def close_window(self):
        self.driver.quit()