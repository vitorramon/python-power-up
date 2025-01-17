# pip install pyautogui 
import pyautogui

# Permite manipular o intervalo de execução do código
import time

# pip install pandas openpyxl
import pandas

# pip freeze > requirements.txt // exporta as dependências em txt

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

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Pedir para o computador esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=824, y=405)
pyautogui.write("teste@teste.com")

pyautogui.press("tab")
pyautogui.write("teste-senha")

pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos

# Ler o arquivo .csv

tabela = pandas.read_csv("../data/produtos.csv")
print(tabela)
time.sleep(2)


# Passo 5: Repetir o passo 4 até acabar todos os produtos
for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto

    pyautogui.click(x=788, y=294)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preço unitário
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    # pressionar botão de enviar
    pyautogui.press("enter")

    # numero positivo = scroll pra cima
    # numero negativo = scroll pra baixo
    pyautogui.scroll(10000)
