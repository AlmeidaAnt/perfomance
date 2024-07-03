import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


navegador = webdriver.Chrome()
navegador.maximize_window()

# Abrir Página do Sistema
navegador.get('https://gps.performance-al.com.br/login/login.xhtml;JSESSIONID=8234d2cf-bf9f-45c6-8f05-3378b158a217')

# Inserir Credenciais e logar
usuario = navegador.find_element(By.XPATH,'//*[@id="j_username"]')
usuario.send_keys('aalmeida')
senha = navegador.find_element(By.XPATH,'//*[@id="j_password"]')
senha.send_keys('Endicon2023.', Keys.TAB, Keys.ENTER)
time.sleep(1)


# 1. Acessar a aba de motoristas
navegador.get('https://gps.performance-al.com.br/secure/manager/contact/#/')
time.sleep(1)

# 2. Acessar Planilha de Cadastro
workbook = openpyxl.load_workbook('C:\\temp\\usuario_performance.xlsx')
planilha = workbook.active


for coluna in planilha.iter_rows(min_row=2, values_only=True):
    nome = coluna[0]
    usuario = coluna[1]
    senha = coluna[2]

#Pesquisa
    pesquisa = navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/input')
    pesquisa.send_keys(nome)
    time.sleep(3)
#ação
    acao = navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/table/tbody/tr/td[10]/div/button')
    acao.click()
    time.sleep(3)
#Tornar em usuario
    tornar_user = navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/table/tbody/tr/td[10]/div/ul/li[4]/a')
    tornar_user.click()
    time.sleep(2)
#cadastro Usuario
    user = navegador.find_element(By.XPATH,'//*[@id="username"]')
    user.send_keys(usuario)
    time.sleep(2)
    senha1 = navegador.find_element(By.XPATH,'//*[@id="password"]')
    senha1.send_keys(senha)
    senha2 = navegador.find_element(By.XPATH,'//*[@id="confirmPassword"]')
    senha2.send_keys(senha)
    papel = navegador.find_element(By.XPATH,'//*[@id="roles"]')
    papel.click()
    papel.send_keys('MOTORISTA')
    papel.send_keys(Keys.ENTER)
    time.sleep(2)
    confirmar = navegador.find_element(By.XPATH,'//*[@id="ngdialog1"]/div[2]/div[5]/button[2]')
    confirmar.click()
    time.sleep(2)
    print('Colaborador ',nome,' Cadastrado com Sucesso')
    navegador.refresh()
    time.sleep(3)