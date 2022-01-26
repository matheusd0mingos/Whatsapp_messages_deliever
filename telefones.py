class Telefone:
    
    def ajeitaTel(self, telefone)->str:
        telefone=str(telefone)
        updated=telefone.replace('+55','')
        updated=updated.replace('-', '')
        updated=updated.replace('(','')
        updated=updated.replace(')','')
        updated=updated.replace(' ', '')

        return str(updated)

    def verifyTel(self, telefone)->bool:
        if (len(telefone)>15 or len(telefone)<7 or telefone.isdecimal()==False):
            return False

        else:
            return True
