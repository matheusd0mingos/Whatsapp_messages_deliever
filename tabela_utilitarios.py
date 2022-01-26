from operator import ne
from tabela import *
from whatsapp import *
from telefones import *
from message import *
from image import *



class TabelaMelhorada(Table):
    def __init__(self, df=pd.read_csv('Base.csv'), filename='Base.csv'):
        super().__init__(df, filename)
        self.message=Message()
        self.tel=Telefone()
        self.read_base()

    def ajeita_verify_telefones(self):

        self.df['Telefone']=self.df.Telefone.apply(self.tel.ajeitaTel)
        self.df['wpp verificado']=self.df.Telefone.apply(self.tel.verifyTel)
        self.update_base()
        self.read_base()


    def send_messages_text_only(self):
        self.whatsapp=Whatsapp()

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'wpp verificado']==True and self.df.loc[i, 'Status envio']!=True:
                pessoa=self.df.loc[i, 'Pessoa']
                telefone=self.df.loc[i, 'Telefone']
                negocio=self.df.loc[i, 'Negocio']
                encoded_message=self.message.message_modifier(pessoa,negocio)
                self.df.loc[i, "Status envio"]=self.whatsapp.send_text_only(str(telefone), encoded_message)
        self.update_base()
        self.read_base()
        self.whatsapp.close_window()
        

    def send_messages_text_image(self)->bool:

        if Image().exist():
            self.whatsapp=Whatsapp()

            for i in range(self.df.shape[0]):
                if self.df.loc[i, 'wpp verificado']==True and self.df.loc[i, 'Status envio']!=True:
                    pessoa=str(self.df.loc[i, 'Pessoa'])
                    telefone=str(self.df.loc[i, 'Telefone'])
                    if str(self.df.Negocio)!='nan':
                        negocio=str(self.df.loc[i, 'Negocio'])
                    else:
                        negocio=''
                    encoded_message=self.message.message_modifier(pessoa,negocio)
                    self.df['Status envio'][i]=self.whatsapp.send_text_and_image(str(telefone), encoded_message, Image().imgPath)
            self.update_base()
            self.read_base()
            self.whatsapp.close_window()
            return True

        else:
            return False
    
