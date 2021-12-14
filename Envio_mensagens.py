# -*- coding: utf-8 -*-

#Insira o IP na classe server thread
import PyQt5
from PyQt5 import QtGui, QtWidgets, QtCore
import pandas as pd
from threading import Thread 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions
import time
from urllib.parse import quote_plus
from ajeitaTelefones import ajeitaTels
from webdriver_manager.chrome import ChromeDriverManager
#from dependencias import dependencias_install
options = webdriver.ChromeOptions()


class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(CustomTableModel, self).__init__()
        self.load_data(data)

    def load_data(self, data):
        self.input_Pessoa = data[0].values
        self.input_Telefone = data[1].values
        self.input_Negocio = data[2].values
        self.input_verificacao = data[3].values
        self.input_status=data[4].values

        self.column_count = 5
        self.row_count = len(self.input_Pessoa)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            
            return ("Pessoa", "Telefone", 'Negocio', 'wpp verificado', 'Tentativa envio')[section]
        else:
            return "{}".format(section)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                raw_user = self.input_Pessoa[row]
                
                return raw_user
            elif column == 1:
                return self.input_Telefone[row]
            elif column==2:
                return self.input_Negocio[row]
            elif column==3:
                return self.input_verificacao[row]

            elif column==4:
                return self.input_status[row]

        elif role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor(QtCore.Qt.white)
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignRight

        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, df):
        data=self.read_data(df)

        self.cond=True
        self.df=df
        
        self.ativ=''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelNegocios=QtWidgets.QLabel(self.centralwidget)
        self.labelNegocios.setGeometry(QtCore.QRect(135, 0, 150, 22))
        self.labelNegocios.setText('Escolha o negócio:')

        self.Ring = QtWidgets.QComboBox(self.centralwidget)
        self.Ring.setGeometry(QtCore.QRect(135, 20, 150, 22))
        self.Ring.setObjectName("Ring")
        self.Ring.addItem('Todos os negócios')
        for item in list(self.df.Negocio.dropna().unique()):
            self.Ring.addItem(item)
        #self.Ring.activated.connect(self.selecionar)




        self.Tabela = QtWidgets.QTableView(self.centralwidget)
        self.Tabela.setGeometry(QtCore.QRect(20, 60, 650, 301))
        self.Tabela.setObjectName("Tabela")
        self.Tabela.modelo=CustomTableModel(data)
        self.Tabela.setModel(self.Tabela.modelo)
        self.horizontal_header = self.Tabela.horizontalHeader()
        self.vertical_header = self.Tabela.verticalHeader()
        self.horizontal_header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.horizontal_header.setStretchLastSection(False)



        self.labelanda=QtWidgets.QLabel(self.centralwidget)
        self.labelanda.setGeometry(QtCore.QRect(20, 0, 150, 22))
        self.labelanda.setText('Status da atividade:')
        self.Opcoes = QtWidgets.QComboBox(self.centralwidget)
        self.Opcoes.setGeometry(QtCore.QRect(20,20, 110,22))
        self.Opcoes.setObjectName("Andamento")
        self.Opcoes.addItem('Tudo')
        self.Opcoes.addItem('Já tentou enviar')
        self.Opcoes.addItem('Ainda não tentou')
        self.Opcoes.addItem('Falha')
        #self.Ring1.activated.connect(self.clickme)


        self.Button_search = QtWidgets.QPushButton(self.centralwidget)
        self.Button_search.setGeometry(QtCore.QRect(445, 20, 70, 23))
        self.Button_search.setObjectName("Pesquisa")
        self.Button_search.clicked.connect(self.pesquisa)

        self.Button_withoutimage=QtWidgets.QPushButton(self.centralwidget)
        self.Button_withoutimage.setGeometry(QtCore.QRect(20, 362, 120, 23))
        self.Button_withoutimage.setObjectName("Disparo sem imagem")
        self.Button_withoutimage.clicked.connect(self.pesquisa)



        self.labelhoras=QtWidgets.QLabel(self.centralwidget)
        self.labelhoras.setGeometry(QtCore.QRect(20, 362, 480, 23))
        #self.labelhoras.setText('Horas Trabalhadas: '+str(self.ativ))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Users activities"))
        self.Button_search.setText(_translate("MainWindow", "Filtrar"))
        self.Button_withoutimage.setText(_translate("MainWindow", "Disparo sem imagem"))


    def read_data(self, df):
        # Read the CSV content
        Pessoa = df["Pessoa"]
        Telefone=df['Telefone']
        Negocio=df.Negocio
        Verificacao=df['wpp verificado']
        status_envio=df['Status envio']

        return Pessoa, Telefone, Negocio, Verificacao, status_envio
    def mod(self):
        df=pd.read_csv('Base.csv')
        
        data = self.read_data(df)
        x = CustomTableModel(data)
        self.model=x
        self.Tabela.setModel(x)
        self.df=df
        return 1

    def pesquisa(self):
        df=pd.read_csv('Base.csv')
        negocio=str(self.Ring.currentText())
        andamento=str(self.Opcoes.currentText())

        if negocio=='Todos os negócios':
            if andamento=='Tudo':
                df=df
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            elif andamento=='Já tentou enviar':
                df=df.loc[df['Status envio']=='v']
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            elif andamento=='Falha':
                df=df.loc[df['Status envio']=='x']
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            else:
                df=df.loc[df['Status envio'].isna()]
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))




        else:
            if andamento=='Tudo':
                df=df.loc[df.Negocio==negocio]
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            elif andamento=='Já tentou enviar':
                df=df.loc[df['Status envio']=='v']
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            elif andamento=='Falha':
                df=df.loc[df['Status envio']=='x']
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            else:
                df=df.loc[df['Status envio'].isna()]
                new=self.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))

           
       
        self.df=df

        


class whatsapp(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.df=pd.read_csv('Base.csv')
        self.window=window
    



    def run(self):
        ajeitaTels()
        self.df=pd.read_csv('Base.csv')

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get('https://web.whatsapp.com/')
        time.sleep(10)

        file=open('msg.txt', 'r', encoding='utf-8')
        msg=file.read()
        for i in range(self.df.shape[0]):
            n=self.window.mod()
            self.window.pesquisa()
            self.df.to_csv('Base.csv', index=False)
   
            if self.df['Status envio'][i]=='v':
                print('Já enviamos para esse número')
                continue 
            
            else:
                name=self.df['Pessoa'][i]
                msg_aux=msg.replace("NOME", name)
                encoded_msg = quote_plus(msg_aux, safe='?!,@')
                telefone = str(self.df.Telefone[i])
                url = 'https://web.whatsapp.com/send?phone=55' + telefone + '&text=' +encoded_msg


                driver.get(url)
                print("Entrando na conversa...")
                driver.execute_script("window.onbeforeunload = function() {};")





                try:


                    elemento = WebDriverWait(driver, 13).until(ec.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='9']")))
                    time.sleep(2)
                    elemento.send_keys(Keys.RETURN)
                    self.df['Status envio'][i]='v'
                    elemento.send_keys(Keys.RETURN)
                    time.sleep(3)
                    print("Enviando...")
                    self.df.to_csv('Base.csv', index=False)
                    continue
                except selenium.common.exceptions.TimeoutException:
                    try:
                        print("Não encontrou o elemento na 1a tentativa, tentando novamente...")
                        elemento = WebDriverWait(driver, 13).until(ec.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='3']")))
                        time.sleep(2)
                        msg1_box = driver.switch_to.active_element
                        msg1_box.send_keys(Keys.RETURN)
                        self.df['Status envio'][i]='v'

                        msg1_box.send_keys(Keys.RETURN)
                        time.sleep(3)
                        print(2)
                        self.df.to_csv('Base.csv', index=False)
                        continue
                    except selenium.common.exceptions.TimeoutException:
                        try:
                            print("Não encontrou o elemento na 2a tentativa, tentando novamente...")
                            elemento = WebDriverWait(driver, 13).until(ec.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='3']")))
                            time.sleep(2)
                            msg1_box = driver.switch_to.active_element
                            msg1_box.send_keys(Keys.RETURN)
                            self.df['Status envio'][i]='v'

                            msg1_box.send_keys(Keys.RETURN)
                            time.sleep(5)
                            print("Enviando...")
                            self.df.to_csv('Base.csv', index=False)
                            continue
                        except selenium.common.exceptions.TimeoutException:
                            self.df['Status envio'][i]='x'
                            self.df.to_csv('Base.csv', index=False)


                            print("Conexão provavelmente lenta ou desconectada, mandar msg pro Matheus Domingos")
                            continue
                except selenium.common.exceptions.InvalidElementStateException:
                    try:
                        print(7)
                        elemento = WebDriverWait(driver, 13).until(ec.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='3']")))
                        time.sleep(2)
                        msg1_box = driver.switch_to.active_element
                        msg1_box.send_keys(Keys.RETURN)
                        self.df['Status envio'][i]='v'

                        msg1_box.send_keys(Keys.RETURN)
                        time.sleep(5)
                        print("Enviando...")
                        self.df.to_csv('Base.csv', index=False)
                        continue
                    except selenium.common.exceptions.TimeoutException:
                        self.df['Status envio'][i]='x'
                        self.df.to_csv('Base.csv', index=False)


                        print("Conexão provavelmente lenta ou desconectada, mandar msg para o Matheus Domingos")
                        continue
        print("wppapi finalizado!")
        self.df.to_csv('Base.csv', index=False)
        n=self.window.mod()
        self.window.pesquisa()





if __name__ == "__main__":
    import sys
    #dependencias_install()
    data=pd.read_csv('Base.csv')

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, data)

    whatsappThread=whatsapp(ui)
    whatsappThread.start()


    MainWindow.show()
    sys.exit(app.exec_())
    
