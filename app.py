"""
Automatizar as mensagens de cobrança para os clientes em determinados dias com os clientes
com vencimentos diferentes (datas).
"""
# Descrever os passos manuais e depois transformar isso em código
# Ler planilha e guardar informações sobre nome, telefone e data de vencimento

import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(5)

workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    #nome, telefone e vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
   
   
# Criar links personalizados do whatsapp e enviar mensagens para cada cliente
   
mensagem = f'Olá {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.chipiratanga.com.br'

link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
webbrowser.open(link_mensagem_whatsapp)
sleep(10)
try:
    seta = pyautogui.locateCenterOnScreen('botao.png')
    sleep(5)
    pyautogui.click(seta[0],seta[1])
    sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    sleep(5)
except:
    print(f'Não foi possível enviar mensagem para {nome}')
    with open('erros.csv', 'a', newline='',encoding='utf-8') as arquivo:
        arquivo.write(f'{nome},{telefone}')






