import socket

class Conexao:

    def __init__(self,porta=22205):
        self.porta=porta

    #funcao que craia a conexao TCP
    def conection(self):

        #especifico qual tecnologia vou usar,no caso a tcp
        self.servico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # definindo a porta que vai ser ultilizada
        self.servico.bind(('',self.porta))
        # deixa o servidor no modo escuta 
        self.servico.listen(1)
        #realiza a conexão
        self.conexao, self.endereco = self.servico.accept()

    def commands(self,command):

        if (command == '0'):
            print('Fim da conexão') 
            self.conexao.close()
            return -1
        elif(command == '1'):
            self.conexao.sendall(str.encode("Somos uma empresa que busca deixar sua casa mais simles e responsiva,"+
                                            "isso sempre buscando ser de maneira mais acessivel"))
        elif(command == '2'):
           self.conexao.sendall(str.encode("Cidades:\n1-Aracaju(SE)\n2-Maceio(AL)\n3-salvador(BA)\n4-Recife(PE)"))
        elif(command == '3'):
           self.formulario()
        elif(command == '4'):
           self.conexao.sendall(str.encode("Planos:\n99,99-plano premiun:atendimentos 24h ,limite de 10 aparelhos para conexão remota,e mais novidades em breve\n"+
                                                     "49.99-plano base:atendimentos 24h ,limite de 5 aparelhos para conexão remota,e mais novidades em breve"))
        elif(command == 'menu'):
           self.conexao.sendall(str.encode('Bem vindo a empresa Click house\nlista de comandos:\n'+
           '1-Quem somos\n2-localidades que atendemos\n3-Agendar consulta\n4-Valores de planos\n0-sair e fechar conexao\n'))
        else:
            self.conexao.sendall(str.encode('comando nao reconhecido,digite menu e veja as opcoes\n'))
        print(command=='1')
        return 1

    #fomulario que o usuario preenche 
    def formulario(self):

        Cidades=["Maceio","Alagoas","Aracaju","Salvador","Recife"]

        self.conexao.sendall(str.encode("informe a cidade"))
        cidade=str(self.conexao.recv(1024).decode())

        if not cidade in Cidades:
            self.conexao.sendall(str.encode("Cidade nao cadrastada\n"))
            return

        self.conexao.sendall(str.encode("Informe a Rua"))
        rua=str(self.conexao.recv(1024).decode())

        self.conexao.sendall(str.encode("informe o seu nome"))
        nome=str(self.conexao.recv(1024).decode())
        dados=[]
        dados.extend([cidade,rua,nome])
        self.conexao.sendall(str.encode(dados.__str__()))
        
    #recebe os comandos 
    def execution(self):
        #informar o menu quando acontece a conexão
        self.commands("menu")

        while True:
             data=self.conexao.recv(1024)
             if(self.commands(data.decode())==-1):
                self.conexao.close()
                break
        
        self.servico.close()


if __name__=='__main__':
    
    server=Conexao()

    server.conection()
    server.execution()


    