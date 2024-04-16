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

time.sleep(3)
botonCookies = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
botonCookies.click()
time.sleep(3)
usernameField = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usernameField.send_keys(username)
passwordField = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordField.send_keys(password)
loginButton = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()
time.sleep(8)



#Aqui conseguiremos el array de following
seccion_perfil = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[2]/div/div/span/span')
wait.until(expected_conditions.element_to_be_clickable(seccion_perfil))
seccion_perfil.click()
time.sleep(3)

driver.get('https://www.instagram.com/' + username + '/following/')
time.sleep(3)
# Obtener la altura de la página antes del scroll
div_element = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]")


# Obtener la posición inicial del scroll
last_scroll_position = driver.execute_script("return arguments[0].scrollTop;", div_element)

while True:
    # Hacer scroll hacia abajo
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_element)
    time.sleep(3)  # Esperar a que la página cargue más contenido (puedes ajustar este tiempo según sea necesario)

    # Obtener la nueva posición del scroll
    new_scroll_position = driver.execute_script("return arguments[0].scrollTop;", div_element)

    # Si la posición del scroll no ha cambiado, sal del bucle
    if new_scroll_position == last_scroll_position:
        break

    # Actualizar la posición del scroll
    last_scroll_position = new_scroll_position
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_element)
time.sleep(3)
arrayFollowing = []
padre = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div")
listado = len(padre.find_elements(By.XPATH, "*"))
print(f"Actualemente sigues a {listado-1} cuentas.")

hijos = padre.find_elements(By.XPATH, "*")
indice = 1
for hijo in hijos:
    if indice > listado:
        break
    span = driver.find_element(By.XPATH,f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{indice}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")
    spanText = span.get_attribute("innerText")

    indice += 1
    arrayFollowing.append(spanText)



#Aqui conseguiremos el array de followers
driver.get('https://www.instagram.com/' + username + '/followers/')

time.sleep(3)

arrayFollowers = []
padre2 = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")

# Obtener la altura de la página antes del scroll
div_element = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")


# Obtener la posición inicial del scroll
last_scroll_position = driver.execute_script("return arguments[0].scrollTop;", div_element)

while True:
    # Hacer scroll hacia abajo
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_element)
    time.sleep(3)  # Esperar a que la página cargue más contenido (puedes ajustar este tiempo según sea necesario)

    # Obtener la nueva posición del scroll
    new_scroll_position = driver.execute_script("return arguments[0].scrollTop;", div_element)

    # Si la posición del scroll no ha cambiado, sal del bucle
    if new_scroll_position == last_scroll_position:
        break

    # Actualizar la posición del scroll
    last_scroll_position = new_scroll_position
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_element)

listado2 = len(padre2.find_elements(By.XPATH, "*"))
print(f"Actualemente tienes {listado2-1} seguidores.")

hijos = padre2.find_elements(By.XPATH, "*")
indice = 1
for hijo in hijos:
    if indice > listado2:
        break
    span = driver.find_element(By.XPATH,f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{indice}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")
    spanText = span.get_attribute("innerText")

    indice += 1
    arrayFollowers.append(spanText)





arrayFinal=[]

for elemento in arrayFollowing:
    esta = False
    for seguidor in arrayFollowers:
        if seguidor == elemento:
            esta = True
            break
    if esta == False:
        arrayFinal.append(elemento)

file = open("listado.txt","w")
for cosa in arrayFinal:
    file.write(cosa)
    if cosa != arrayFinal[len(arrayFinal)-1]:
        file.write('\n')
file.close()
time.sleep(60)
driver.quit()
print(f'Hay {listado-listado2} cabrones que no te han devuelto el follow...')
input()


