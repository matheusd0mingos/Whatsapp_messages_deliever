from urllib.parse import quote_plus
from read_file import *

class Message:
    def __init__(self) -> None:
        file=File()
        self.msg=file.get_msg()

    def message_modifier(self, pessoa, negocio) -> str:
        msg=self.msg.replace('NOME', str(pessoa))
        self.msg=msg.replace('NEGOCIO', str(negocio))
        encoded_msg = quote_plus(msg, safe='?!,@')
        return encoded_msg

    