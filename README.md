# Função de Restart em Servidor Python

Este programa em Python recebe alterações no código que faz a interação de cliente e servidor, inserindo uma variável que permite que o servidor seja desligado e ligado novamente em seguida ao digitar um comando no terminal.

# Configuração e Dependências:
- Python: O código requer a versão mais recente do Python, que pode ser instalada pelo site oficial (https://www.python.org/).

#	Execução:
- Clone o repositório: `git clone https://github.com/Dollynski/Trabalho-Final-Automacao`
- Rode o programa através de dois terminais, um para o servidor e outro para o cliente: `python servidor.py`; `python cliente.py`
- No mesmo terminal que está rodando a parte do cliente, insira o seguinte comando: `reiniciar`
- Aguarde alguns segundos e veja o feedback do servidor; Ele será encerrado e logo em seguida se iniciará novamente.

# Conclusão:
Adicionar a funcionalidade de reiniciar o servidor pelo cliente tornou o programa mais prático e fácil de usar. Enfrentamos alguns desafios, como corrigir o endereço do cliente para se reconectar ao servidor, mas resolvemos isso com uma função que garante a reconexão automática. Essa melhoria não só simplifica o gerenciamento do servidor, mas também torna o sistema mais robusto e flexível, mostrando como o trabalho em equipe e a automação podem ser eficazes.
