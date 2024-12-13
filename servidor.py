import socket
import threading
import os
import sys

def handle_client(conn, addr):
    print(f'Conexão estabelecida com {addr}')
    try:
        conn.sendall('Servidor pronto.'.encode('utf-8'))  # Mensagem enviada imediatamente
        while True:
            data = conn.recv(1024)
            if not data:
                print(f'Conexão encerrada pelo cliente {addr}')
                break
            mensagem_cliente = data.decode()
            print(f'Cliente {addr}: {mensagem_cliente}')
            
            if mensagem_cliente.lower() == 'reiniciar':
                print('Comando de reiniciar recebido. Reiniciando o servidor...')
                conn.sendall('Servidor será reiniciado.'.encode('utf-8'))
                conn.close()
                os.execl(sys.executable, f'"{sys.executable}"', *sys.argv)
            
            mensagem_servidor = input('Você (servidor): ')
            conn.sendall(mensagem_servidor.encode('utf-8'))
    except ConnectionResetError:
        print(f'Conexão com {addr} foi encerrada abruptamente.')
    finally:
        conn.close()
        print(f'Conexão fechada com {addr}')


HOST = ''  # Escuta em todas as interfaces de rede disponíveis
PORT = 5000  # Porta para escutar as conexões

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f'Servidor escutando na porta {PORT}...')

while True:
    conn, addr = servidor.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f'Clientes ativos: {threading.active_count() - 1}')
