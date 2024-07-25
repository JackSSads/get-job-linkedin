from selenium.webdriver.common.by import By
import openpyxl
from urllib.parse import quote
from time import sleep

from src.utils import WebBrowser

class RoboWhatsapp:
    def __init__(self) -> None:
        self.browser = WebBrowser(url="https://web.whatsapp.com/")

    def initialise_robo_whatsapp(self, phone: int):
        print("\nIniciando robô whatsapp\n")
        self.browser.initalise_web_browser()

        print("Faça login no Whatsapp")

        # Aguardando login no Whatsapp
        control = True
        while control:
            try:
                self.browser.driver_wait(
                    driver=self.browser.atribuites(),
                    element=(By.CLASS_NAME, "_akau"),
                    time=10
                )

                print("Aguardando o login no Whatsapp")
                sleep(5)
            except:
                print("Login realizado")
                control = False

        print("Buscando arquivo jobs.xlsx")
        path_file = "./jobs.xlsx"
        workbook = openpyxl.load_workbook(path_file)
        page_jobs = workbook['Sheet1']

        # criando link personalizado para envio da mensagem
        for line in page_jobs.iter_rows(min_row=2):
            print(f"Vaga: {line[1].value}")
            job = line[1].value
            link = line[2].value

            #https://web.whatsapp.com/send?phone=<go_to>&text=<message>
            message = f'Vaga: {quote(job)}. Link: {link}'
            link_message = f'https://web.whatsapp.com/send?phone={phone}&text={message}'
                        
            self.browser.atribuites().get(link_message)

            self.browser.driver_wait(
                driver=self.browser.atribuites(),
                element=(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'),
                time=10
            ).click()
            
            print("Mensagem enviada")

            sleep(2)

        self.browser.atribuites().quit()
