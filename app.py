'''
    Bot de curtidas e comentários no Instagram com Pyautogui

    Objetivo - Vamos criar um bot que define qual página quer seguir, verificar se a postagem mais atual ainda não foi curtida pelo bot. Caso uma nova postagem tenha sido feita, ele deve entrar nessa postagem, curtir e comentar algo nela.
'''
# Bibliotecas utilizadas
import pyautogui
import webbrowser
import pyperclip
from time import sleep

# Função principal
def iniciar_automacao():
    # Loop para rodar a automação toda vez que tiver completado 24 horas
    while True:
        # Passo 1 - Entrar página do instagram 
        webbrowser.open(url)
        sleep(3)
        usuario = pyautogui.locateCenterOnScreen('./assets/campo_usuario.png')
        pyautogui.click(x=usuario[0], y=usuario[1], duration=1)
        pyautogui.write('nome do usuário', interval=0.1)
        sleep(0.9)
        pyautogui.press('tab')
        pyautogui.write('senha do usuário', interval=0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(1)
        pyautogui.press('enter')
        sleep(4.5)
        confirmacao = pyautogui.locateCenterOnScreen('./assets/confirmar.png')
        pyautogui.click(x=confirmacao[0], y=confirmacao[1], duration=1)

        # Passo 2 - Ir no campo de buscar da página
        pesquisa = pyautogui.locateCenterOnScreen('./assets/pesquisa.png')
        pyautogui.click(x=pesquisa[0], y=pesquisa[1], duration=2)
        sleep(2)

        # Passo 3 - Digitar o nome da página e entrar nela
        pyautogui.write('nome da página')
        pyautogui.move(120, -20, duration=1)
        sleep(2)
        pyautogui.click()
        sleep(3)

        # Passo 4 - Entrar na última postagem e verificar se foi curtida
        postagem = pyautogui.locateCenterOnScreen('./assets/postagem.png')
        pyautogui.click(x=postagem[0], y=postagem[1], duration=1)
        sleep(3)
        # Passo 5 - Caso não tenha sido curtida, curti e comentar
        curtida_vazia = salvar_local_central_da_imagem('./assets/curtida_vazia.png')
        curtida = salvar_local_central_da_imagem('./assets/curtida.png')
        if curtida_vazia is not None:
            pyautogui.click(x=curtida_vazia[0], y=curtida_vazia[1], duration=1)
            sleep(1)
            comentario = pyautogui.locateCenterOnScreen('./assets/comentario.png')
            pyautogui.click(x=comentario[0], y=comentario[1], duration=1)
            sleep(1)
            escrever_comentario(comentario='Comentário automação', tempo=1)
            sleep(1)
            pyautogui.press('enter')
            logout()
            sleep(86400)
        elif curtida is not None:    
            logout()
            sleep(86400)


if __name__ == '__main__':
    # Funções e variáveis
    url = 'instagram.com'

    def escrever_comentario(comentario, tempo):
        pyperclip.copy(comentario)
        pyautogui.hotkey('ctrl', 'v')
        sleep(tempo)

    def logout():
        pyautogui.press('esc')
        mais_opcoes = pyautogui.locateCenterOnScreen('./assets/mais.png')
        pyautogui.click(x=mais_opcoes[0], y=mais_opcoes[1], duration=1.5)
        pyautogui.move(0, -50, duration=1)
        pyautogui.click()

    def salvar_local_central_da_imagem(imagem):
        try:
            return pyautogui.locateCenterOnScreen(imagem)
        except pyautogui.ImageNotFoundException:
            return None
    
    iniciar_automacao()