import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions

username = input('Introduzca el usuario: ')
password = input('Introduzca contraseña: ')

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 5)

time.sleep(1)

botonCookies = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
botonCookies.click()
time.sleep(3)
usernameField = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usernameField.send_keys(username)
passwordField = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordField.send_keys(password)
loginButton = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()
time.sleep(7)

archivo = open('listado.txt')
cabrones = archivo.readlines()
indice = 0
for linea in cabrones:
    linea = linea.strip()
    cabrones[indice] = linea
    indice += 1
print(cabrones)

for cuenta in cabrones:
    driver.get('https://www.instagram.com/' + cuenta + '/')
    time.sleep(3)
    boton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button")
    boton.click()
    time.sleep(3)
    divUnfollow = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]')
    divUnfollow.click()
    time.sleep(1)


