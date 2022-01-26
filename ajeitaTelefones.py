import pandas as pd

def ajeitaTels():
    df = pd.read_csv('Base.csv')
    for i in range(df.shape[0]):
        contato = str(df['Telefone'][i])
        contato = contato.replace("+55", "")
        print(contato)
        contato = contato.replace("-", "")
        contato = contato.replace("(", "")
        contato = contato.replace(")", "")
        contato = contato.replace(" ", "")

        print(contato)
        df.loc[i, 'Telefone'] = str(contato)

        if (len(contato)>15 or len(contato)<7) or contato.isdecimal()==False:
            df.loc[i, 'wpp verificado']='Não é número válido'

        else:
            df.loc[i,'wpp verificado']='É número válido'




    df.to_csv('Base.csv', index=False)
    return df
if __name__ == '__main__':
    print("ei! não rode esse programa! rode apenas o wppapi_link!")