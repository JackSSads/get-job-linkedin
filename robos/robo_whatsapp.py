from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import pyautogui
import pyperclip

import openpyxl
from time import sleep

from src.utils import Driver

driver = Driver()

class RoboWhatsapp:
    def __init__(self) -> None:
        pass

    def initialise_robo_whatsapp(self, contact: str):
        print("\nIniciando robô whatsapp\n")
        driver.initialize_webdriver()
        driver.navigate_to("https://web.whatsapp.com/")

        print("Faça login no Whatsapp")

        # Aguardando login no Whatsapp
        control = True
        while control:
            qrcode = driver.waiting("//canvas")

            if qrcode:
                print("Aguardando o login no Whatsapp")
                sleep(5)
            else:
                control = False
                print("\nLogin realizado\n")
                self.enviar_mensagem(contact=contact)

    def enviar_mensagem(self, contact: int):
        def escrever(frase):
            pyperclip.copy(frase)
            pyautogui.hotkey("ctrl", "v")

        # Clicando no elemento de busca
        print("Clicando no elemento de busca")
        driver.waiting(
            ec=EC.presence_of_element_located,
            search="//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']"
        ).click()

        sleep(3)


        escrever(contact)
        
        sleep(1)

        pyautogui.hotkey("enter")

        driver.waiting("//div[@class='_ak1r']/div/div/div/p").click()

        print("Buscando arquivo jobs.xlsx\n")
        path_file = "./jobs.xlsx"
        workbook = openpyxl.load_workbook(path_file)
        page_jobs = workbook['Sheet1']

        # Escrevendo mensagem
        for collumn in page_jobs.iter_rows(min_row=2):
            print(f"Vaga: {collumn[1].value}")
            job = collumn[1].value
            link = collumn[2].value

            escrever(
                f"""
                Vaga: {job}
                Link: {link}
                """
            )
            
            pyautogui.hotkey("enter")
            
        print("\nMensages enviada\n")

        sleep(2)

        driver.close_web_driver()