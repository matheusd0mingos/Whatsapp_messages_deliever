class File:
    def __init__(self, filename='msg.txt'):
        self.filename=filename

    def get_msg(self):
        file=open(self.filename, 'r', encoding='utf-8')
        msg=file.read()
        return msg