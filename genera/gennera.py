from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

load_dotenv()

USUARIO = ""
SENHA = ""

firefox_driver = webdriver.Firefox()
firefox_driver.get("https://apps.gennera.com.br/public/#/login")

#wait for page to load
firefox_driver.implicitly_wait(10)

wait = WebDriverWait(firefox_driver, 10)

#set value to input
inputlogin = wait.until(EC.visibility_of_element_located(("xpath", "/html/body/div[2]/div[2]/div[2]/div[3]/form/div/input")))
inputlogin.clear()
inputlogin.send_keys(USUARIO)

bottom_pass = wait.until(EC.visibility_of_element_located(("xpath", "/html/body/div[2]/div[2]/div[2]/div[3]/button/div[2]/span")))
bottom_pass.click()

firefox_driver.implicitly_wait(10)

inputpassword = wait.until(EC.visibility_of_element_located(("xpath", "/html/body/div[2]/div[2]/div[2]/div[5]/div[1]/input")))
inputpassword.clear()
inputpassword.send_keys(SENHA)

bottom_login = wait.until(EC.visibility_of_element_located(("xpath", "/html/body/div[2]/div[2]/div[2]/div[5]/button")))
bottom_login.click()

link_turmas = "https://classroom2.gennera.com.br/admin/#!/institutions/64/diaries"
firefox_driver.get(link_turmas)


button_relogin = wait.until(EC.visibility_of_element_located(("xpath", "/html/body/div[2]/div[2]/div[1]/button[1]")))
button_relogin.click()
    #acessando as frequencias

firefox_driver.get("https://classroom2.gennera.com.br/admin/#!/institutions/64/diaries/379518/users/13605933/attendances")

import requests 

resposta = requests.get("https://classroom2.gennera.com.br/admin/#!/institutions/64/diaries/379518/users/13605933/attendances")
print(resposta)

soup = BeautifulSoup(resposta.text, 'html.parser')
faltas = soup.find_all('xpath', '/html/body/div[2]/div[3]/div/div[4]/div[1]/div[2]/div/div[1]/div[2]')
allA = soup.find_all('a')

for falta in faltas:
  numero_falta = "Falta: " + falta.text

print(numero_falta)