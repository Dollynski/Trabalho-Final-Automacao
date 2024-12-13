import socket
import time

def conectar_ao_servidor():
    while True:
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect((HOST, PORT))
            print('Conectado ao servidor.')
            data = cliente.recv(1024)  # Aguarda a mensagem de "pronto" do servidor
            if data.decode() == 'Servidor pronto.':
                print('Servidor está pronto para receber comandos.')
                return cliente
        except (ConnectionRefusedError, ConnectionResetError):
            print('Erro ao conectar. Tentando novamente em 2 segundos...')
            time.sleep(2)


HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000         # Porta que o servidor está escutando

cliente = conectar_ao_servidor()

try:
    while True:
        mensagem = input('Você (cliente): ')
        if mensagem.lower() == 'sair':
            print('Encerrando conexão.')
            break
        cliente.sendall(mensagem.encode())
        data = cliente.recv(1024)
        if not data:
            print('Conexão encerrada pelo servidor.')
            break
        resposta_servidor = data.decode()
        print(f'Servidor: {resposta_servidor}')
        
        if mensagem.lower() == 'reiniciar':
            print('Aguardando servidor reiniciar...')
            cliente.close()
            cliente = conectar_ao_servidor()
            print('Reconectado ao servidor.')
except KeyboardInterrupt:
    print('\nConexão interrompida pelo usuário.')
finally:
    if cliente:
        cliente.close()
    print('Conexão fechada.')
