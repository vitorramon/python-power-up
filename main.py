# pip install pyautogui 

import pyautogui

# Delay da execução dos comandos
pyautogui.PAUSE = 1.5

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho do teclado

# Cadastrar uma base de dados com centenas de produtos através de automação

# Passo 1: Abrir o sistema da empresa
    # Sistema de Referência: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Entrar no Google Chrome

# Apertar a tecla win
pyautogui.press("win")

# Digitar o navegador
pyautogui.write("chrome")

# Apertar enter
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

# Passo 2: Fazer login
# Passo 3: Importar a base de dados dos produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar todos os produtos