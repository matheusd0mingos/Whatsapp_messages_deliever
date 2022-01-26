from customtable import *
from whatsapp import *
from tabela_utilitarios import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.tabela=TabelaMelhorada()


        #Vamos já ajeitar os telefones:
        self.tabela.ajeita_verify_telefones()

        data=self.tabela.read_data()
        

        self.cond=True

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
        for item in list(self.tabela.df.Negocio.dropna().unique()):
            self.Ring.addItem(item)
        #self.Ring.activated.connect(self.selecionar)




        self.Tabela = QtWidgets.QTableView(self.centralwidget)
        self.Tabela.setGeometry(QtCore.QRect(20, 60, 650, 301))
        self.Tabela.setObjectName("Tabela")
        self.Tabela.setModel(CustomTableModel(data))
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

        self.labeltipoenvio=QtWidgets.QLabel(self.centralwidget)
        self.labeltipoenvio.setGeometry(QtCore.QRect(80*3+60, 0, 150, 22))
        self.labeltipoenvio.setText('Modo de operação:')
        self.Opcoesenvio = QtWidgets.QComboBox(self.centralwidget)
        self.Opcoesenvio.setGeometry(QtCore.QRect(80*3+60,20, 140,22))
        self.Opcoesenvio.setObjectName("Tipo de disparo")
        self.Opcoesenvio.addItem('Disparo sem imagem')
        self.Opcoesenvio.addItem('Disparo com imagem')


        self.Button_search = QtWidgets.QPushButton(self.centralwidget)
        self.Button_search.setGeometry(QtCore.QRect(445, 20, 70, 23))
        self.Button_search.setObjectName("Pesquisa")
        self.Button_search.clicked.connect(self.pesquisa)

        self.Button_disparo=QtWidgets.QPushButton(self.centralwidget)
        self.Button_disparo.setGeometry(QtCore.QRect(520, 20, 120, 23))
        self.Button_disparo.setObjectName("Botão de disparo")
        self.Button_disparo.clicked.connect(self.mododisparo)



        self.labelstatus=QtWidgets.QLabel(self.centralwidget)
        self.labelstatus.setGeometry(QtCore.QRect(20, 362, 480, 23))
        self.labelstatus.setText('Selecione um modo de operação para iniciarmos o programa')

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Bot whatsapp"))
        self.Button_search.setText(_translate("MainWindow", "Filtrar"))
        self.Button_disparo.setText(_translate("MainWindow", "Fazer disparo"))

    def update_status(self, logica):
        if logica==False:
            self.labelstatus.setText('Imagem não encontrada')
        else:
            self.labelstatus.setText('Começando o programa')

    def mododisparo(self):
        modo=self.Opcoesenvio.currentText()
        if modo=='Disparo sem imagem':
            self.update_view()
            self.tabela.send_messages_text_only()
            self.update_view()

            
        else:
            image=Image()
            if image.exist():
                self.update_status(True)
                self.update_view()
                self.tabela.send_messages_text_image()
                self.update_view()
            else:
                self.update_status(False)


    def update_view(self):
        x = CustomTableModel(self.tabela.read_data())
        self.model=x
        self.Tabela.setModel(x)
        return 1

    def pesquisa(self):
        df=self.tabela.df
        negocio=str(self.Ring.currentText())
        andamento=str(self.Opcoes.currentText())

        if negocio=='Todos os negócios':
            if andamento=='Tudo':
                df=df
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            elif andamento=='Já tentou enviar':
                df=df.loc[df['Status envio']=='v']
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            elif andamento=='Falha':
                df=df.loc[df['Status envio']=='x']
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            else:
                df=df.loc[df['Status envio'].isna()]
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))




        else:
            if andamento=='Tudo':
                df=df.loc[df.Negocio==negocio]
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            elif andamento=='Já tentou enviar':
                df=df.loc[df['Status envio']=='v']
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            elif andamento=='Falha':
                df=df.loc[df['Status envio']=='x']
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))
            
            else:
                df=df.loc[df['Status envio'].isna()]
                new=self.tabela.read_data(df)
                self.Tabela.setModel(CustomTableModel(new))

       
        self.tabela.modify_df(df)