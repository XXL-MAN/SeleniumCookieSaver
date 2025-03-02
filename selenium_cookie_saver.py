# SeleniumCookieSaver - by Andrés Naranjo - 2025

"""
Este script de Python utiliza Selenium para automatizar la interacción con un sitio web y gestionar las cookies.

1. Importa las librerías necesarias:
   - selenium: Para automatizar el navegador web.
   - pickle: Para serializar y deserializar objetos Python (en este caso, las cookies).
   - os: Para interactuar con el sistema operativo, como comprobar si existe un archivo.
   - keyboard: Para detectar la pulsación de teclas.

2. Define las variables WEBSITE y COOKIES:
   - WEBSITE: La URL del sitio web que se va a automatizar.
   - COOKIES: El nombre del archivo donde se guardarán las cookies.

3. Configura el driver de Chrome:
   - Crea un objeto Service con la ruta al chromedriver.
   - Crea un objeto webdriver.Chrome utilizando el servicio configurado.

4. Comprueba si existen cookies guardadas:
   - Si el archivo COOKIES existe, carga las cookies utilizando pickle.load, las añade al driver con driver.add_cookie y recarga la página.
   - Si el archivo no existe, abre el sitio web, espera a que el usuario pulse Intro después de aceptar las cookies y guarda las cookies utilizando pickle.dump.

5. Espera a que se pulse la barra espaciadora:
   - Muestra un mensaje indicando que se pulse la barra espaciadora.
   - Utiliza keyboard.wait para pausar la ejecución hasta que se pulse la barra espaciadora.

6. Cierra el navegador:
   - Utiliza driver.quit para cerrar el navegador.

Este script permite automatizar el inicio de sesión en un sitio web utilizando cookies guardadas, evitando tener que introducir las credenciales cada vez.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os
import keyboard

# Configura el sitio web
WEBSITE = "https://www.ejemplo.com"  # Reemplaza con la URL deseada
COOKIES = "cookies.pkl"

# Configura el driver de Chrome
service = Service('./chromedriver')  # Reemplaza con la ruta a tu chromedriver
driver = webdriver.Chrome(service=service)

# Comprueba si existen cookies guardadas
if os.path.exists(COOKIES):
    print(f"Cargando COOKIES para {WEBSITE}")
    driver.get(WEBSITE)
    cookies = pickle.load(open(COOKIES, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(WEBSITE)  # Recarga la página con las cookies
else:
    print(f"Guardando COOKIES para {WEBSITE}")
    driver.get(WEBSITE)
    input("Pulsa Intro después de aceptar las cookies...")  # Espera a que el usuario acepte las cookies
    pickle.dump(driver.get_cookies(), open(COOKIES, "wb"))

# Espera a que se pulse la barra espaciadora
print("Pulsa la barra espaciadora para cerrar el navegador...")
keyboard.wait("space")

# Cierra el navegador
driver.quit()
