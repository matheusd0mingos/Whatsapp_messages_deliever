from operator import ne
from tabela import *
from whatsapp import *
from telefones import *
from message import *
from image import *

class TabelaMelhorada(Table):
    def __init__(self, df=pd.read_csv('Base.csv'), filename='Base.csv'):
        super().__init__(df, filename)
        self.whatsapp=Whatsapp()
        self.message=Message()
        self.image=Image()

    def ajeita_verify_telefones(self):
        for i in range(self.df.shape[0]):
            telefone=self.df.loc[i, 'Telefone']
            print('Olá:: '+str(telefone))
            self.df.loc[[i],['Telefone']]=Telefone().ajeitaTel(telefone)
            telefone=self.df.loc[i, 'Telefone']
            self.df.loc[[i],['wpp verificado']]=Telefone().verifyTel(telefone)
            if Telefone().verifyTel(telefone)==False:
                self.df.loc[[i], 'Status envio']=False

        self.update_base()


    def send_messages_text_only(self):
        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'wpp verificado']==True and self.df.loc[i, 'Status envio']!=True:
                pessoa=self.df.loc[i, 'Pessoa']
                telefone=self.df.loc[i, 'Telefone']
                negocio=self.df.loc[i, 'Negocio']
                encoded_message=self.message.message_modifier(pessoa,negocio)
                self.df.loc[[i],['Status envio']]=self.whatsapp.send_text_only(telefone, encoded_message)
        self.update_base()
        

    def send_messages_text_image(self)->bool:
        if self.image.exist():
            for i in range(self.df.shape[0]):
                if self.df.loc[i, 'wpp verificado']==True and self.df.loc[i, 'Status envio']!=True:
                    pessoa=self.df.loc[i, 'Pessoa']
                    telefone=self.df.loc[i, 'Telefone']
                    negocio=self.df.loc[i, 'Negocio']
                    encoded_message=self.message.message_modifier(pessoa,negocio)
                    self.df[[i], ['Status envio']]=self.whatsapp.send_text_and_image(telefone, encoded_message, self.image.imgPath)
            self.update_base()
            return True

        else:
            return False
    
