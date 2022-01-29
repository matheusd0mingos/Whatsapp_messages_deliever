# Whatsapp_project
  O envio de imagens só funciona efetivamente em Windows.
  
## Sobre a UI
![image](https://user-images.githubusercontent.com/48094120/151669131-e82f6a86-c181-4668-afd1-c0a144b1d0a3.png)

Botão fazer disparo faz o disparo com o método selecionado em Modo de operação(as opções são disparo sem imagem e disparo com imagem)

Já filtrar é um utilitário para filtrar os que já foram enviados e entre os negócios

## Observação 
  Um ponto importante é que se pode fazer uma versão bash only utilizando o arquivo tabela_utilitarios.py

## Para gerar um executável
  É necessário ter na sua máquina os pacotes pyinstaller
  Exemplo:

  ```
  pyinstaller --noconfirm --onedir --windowed --add-data "C:/Users/MATHE/Whatsapp_project/Base.csv;." --add-data    "C:/Users/MATHE/Whatsapp_project/msg.txt;." --add-data "C:/Users/MATHE/Whatsapp_project/image.jpg;."  "C:/Users/MATHE/Whatsapp_project/Envio_mensagens.py"
  
  ```
## Sobre os arquivos
  base.csv: A base com colunas [Pessoa, Telefone, Negócio, wppverificado, Status envio]
  
  msg.txt: Tem a mensagem a ser enviada. Ao se escrever NEGOCIO, este será trocado pelo item correspondente em Base.csv, o mesmo acontecerá com NOME.
  
  image.jpg ou image.png: A imagem que será enviada
  
## Arquivos Python
  read_file.py: Possui classes necessárias para ler o arquivo msg.txt
  ```
    self.filename=filename #default: msg.txt
    get_msg(): return msg_lida
  ```
  
  message.py: Possui classes necessárias para a modificação da mensagem
  ```
    message_modifier(Nome, Negocio): return (msg_modificada_decodificada)
  ```
  
  
  image.py: Possui classes para verificar qual o arquivo de imagem existente e também mostrar o endereço.  
  ```
    self.imgPath: Endereço mensagem
    exist(): return True(se existe) or False
  ```
  
  tabela.py: Classe que possui os métodos adaptados para a formatação de base.csv  
  ```
    self.df: atributo data frame
    read_data(): return as colunas
    modify_df(new_df): modifica o dataframe para new_df
    update_base(): salva o df atual para Base.csv
    read_base(): Le o arquivo Base.csv
  ```
  
  telefones.py: Para verificar e ajeitar telefones  
  ```
    ajeitaTel(tel): Ajeita o telefone
    verifyTel(tel): True se tel válido, False contrário
  ```
  
  chrome.py: Iniciar uma sessão, por default no whatsapp  
  ```
    #Inicia thread
  ```
  
  whatsapp.py: Child(chrome) com métodos adaptados para o disparro de  mensagens  
  ```
    enter_site_with_msg(telefone, encoded_msg): Entra no link para enviar mensagem ao telefone com a mensagem já
    element_finder_msg_sender(): Encontra o campo para envio de mensagem
    element_finder_file_sender(): Encontra a div para enviar imagem
    send_text_only(telefone, encoded_msg): envia a mensagem com apenas texto
    send_text_and_image(telefone, encoded_msg, imgpath): envia texto e imagem
    close_window: fecha janela
  ```
  
  tabela_utilitarios.py: Combina métodos de tabela.py, whatsapp.py, tabela.py e telefones.py para fazer ajustes e envios na base
  ```
    ajeita_verify_telefones(): Ajeita todos os telefones da base
    send_messages_text_only(): Envia apenas texto para todos os elementos da base
    send_messages_text_image(): Envia texto e imagem para todos os elementos da base
  ```
  
  custom_table.py: Para formatar a tabela na UI
  
    Definições necessária para formatar ui
  
  ui.py: Configuração ui
  
  Enviar_mensagens.py: o main
  
