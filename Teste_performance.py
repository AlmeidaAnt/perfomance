import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.ui import Select
import openpyxl
from selenium.webdriver import ActionChains
import os
import shutil
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Formatação de datas
hoje = datetime.date.today()
hoje_formatado = hoje.strftime('%d/%m/%Y')
hoje_extenso = hoje.strftime('%d de %B de %Y')
ontem = hoje - datetime.timedelta(days=1)
ontem_formatado = ontem.strftime('%d/%m/%Y')
ontem_extenso = ontem.strftime('%d de %B de %Y')
ultima_semana = hoje - datetime.timedelta(days=7)
semana_formatada = ultima_semana.strftime('%d/%m/%Y')
ontem_dia = ontem.strftime('%d')
ontem_mes = ontem.strftime('%m')
ontem_ano = ontem.strftime('%Y')

navegador = webdriver.Chrome()
navegador.maximize_window()

# Abrir Página do Sistema
navegador.get('https://app.zuq.com.br/secure/report/poi/')

# Inserir Credenciais e logar
usuario = navegador.find_element(By.XPATH, '//*[@id="j_username"]')
usuario.send_keys('aalmeida')
senha = navegador.find_element(By.XPATH, '//*[@id="j_password"]')
senha.send_keys('Endicon2023.', Keys.TAB, Keys.ENTER)
time.sleep(1)


#periodo
data = navegador.find_element(By.XPATH, '//*[@id="dropdownMenu1"]')
data.click()

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

inicio = navegador.find_element(By.XPATH, '//*[@id="ngdialog2"]/div[2]/div[1]/div/div[1]/input')
inicio.send_keys('01/07/2023')
termino = navegador.find_element(By.XPATH, '//*[@id="ngdialog2"]/div[2]/div[1]/div/div[2]/input')
termino.send_keys('27/07/2023')

ok = navegador.find_element(By.XPATH, '//*[@id="ngdialog1"]/div[2]/div[1]/div/div[3]/button[2]')
time.sleep(10)
