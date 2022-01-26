import pandas as pd

class Table:
    def __init__(self, df=pd.read_csv('Base.csv'), filename='Base.csv'):
        self.filename=filename
        self.df=df
    
    def read_data(self):
        # Read the CSV content
        Pessoa = self.df["Pessoa"]
        Telefone=self.df['Telefone']
        Telefone=Telefone.apply(lambda x:str(x))
        Negocio=self.df['Negocio']
        Negocio=Negocio.apply(lambda x:str(x))
        Verificacao=self.df['wpp verificado']
        Verificacao=Verificacao.apply(lambda x:str(x))

        status_envio=self.df['Status envio']
        status_envio=status_envio.apply(lambda x:str(x))


        return Pessoa, Telefone, Negocio, Verificacao, status_envio

    def modify_df(self, new_df):
        self.df=new_df
        return self.df

    def update_base(self):
        self.df.to_csv(self.filename, index=False)

    def read_base(self):
        self.df=pd.read_csv(self.filename)
