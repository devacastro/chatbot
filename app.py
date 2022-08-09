import os

#importa os para para quebra de linha - linesep
def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} voce pode encontrar oportunidades no Linkedin, Cathoo e Infojobs{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} o front-end pode ser definido como a profissão que cuida da apresentação de um site. Ou seja, cuida das partes visuais e da interação entre usuários e tela. Gerencia a usabilidade, o design e a experiência do usuário. Já a parte do back-end é a que cuida dos bastidores, do funcionamento estrutural de uma página{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} um Front-End precisa saber logo de início HTML, CSS, JavaScript, deixar as telas funcionando em todos os tamanhos de dispositivos, etc, enquanto o Back-End precisará de uma linguagem de programação e um banco de dados, podendo o Back-End ser um pouco mais amigável para alguns iniciantes{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} nao se considera obrigatorio, contudo cada vez mais os recrutadores estao utilizando do GitHub para medir sua capacidade.{os.linesep}')
    else:
        print("Digite apenas as opcoes 1, 2, 3, 4")

def start ():
    
    #Apresentar o chatbot:
    
    print("Ola! Bem vindo")
    
    #Pedir o nome:
    
    nome = input("Digite o seu nome: ")
    
    #Pedir o email:
    
    email = input("Digite seu e-mail: ")
    while True:
    #Oferecer o menu de opcoes:
    
            resposta = input(
                f'Oque gostaria de saber hoje?{os.linesep}[1] - Em quais plataformas posso conseguir meu primeiro emprego?{os.linesep}[2] - Qual a diferenca entre Front-End e Back-End?{os.linesep}[3] - Qual e mais facil de comecar ?{os.linesep}[4] - Devo ter um portifolio ?{os.linesep}'
            )
    
    
    #Processar a resposta enviada:
    
            processar_resposta(resposta, nome)
    
if __name__ == '__main__':
    start()