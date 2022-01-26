import pandas as pd

class Table:
    def __init__(self, df=pd.read_csv('Base.csv'), filename='Base.csv'):
        self.filename=filename
        self.df=df
    
    def read_data(self):
        # Read the CSV content
        Pessoa = self.df["Pessoa"]
        Telefone=self.df['Telefone']
        Negocio=self.df['Negocio']
        Verificacao=self.df['wpp verificado']
        status_envio=self.df['Status envio']

        return Pessoa, Telefone, Negocio, Verificacao, status_envio

    def modify_df(self, new_df):
        self.df=new_df
        return self.df

    def update_base(self):
        self.df.to_csv(self.filename, index=False)

    def read_base(self):
        self.df=pd.read_csv(self.filename)
