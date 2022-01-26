from urllib.parse import quote_plus
from read_file import *

class Message:
    def __init__(self) -> None:
        file=File()
        self.msg=file.get_msg()

    def message_modifier(self, pessoa, negocio) -> str:
        msg=self.msg.replace('NOME', str(pessoa))
        msg=msg.replace('NEGOCIO', negocio)

        encoded_msg = quote_plus(msg, safe='?!,@')
        return str(encoded_msg)

    