from selenium.webdriver.common.by import By
import openpyxl
from urllib.parse import quote
from time import sleep

from src.utils import WebBrowser

class RoboWhatsapp:
    def __init__(self) -> None:
        self.browser = WebBrowser(url="https://web.whatsapp.com/")

    def initialise_robo_whatsapp(self, phone: int):
        self.browser.initalise_web_browser()
        print("iniciando robô whatsapp")
        sleep(5)

        path_file = "./jobs.xlsx"
        workbook = openpyxl.load_workbook(path_file)
        page_jobs = workbook['Sheet1']

        sleep(20)
              
        for line in page_jobs.iter_rows(min_row=2):
            job = line[1].value
            link = line[2].value

            #https://web.whatsapp.com/send?phone=<go_to>&text=<message>
            message = f'Vaga: {quote(job)}. Link: {link}'
            link_message = f'https://web.whatsapp.com/send?phone={phone}&text={message}'
            
            sleep(5)
            
            self.browser.atribuites().get(link_message)

            sleep(5)

            self.browser.atribuites().find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()

            sleep(2)

        self.browser.atribuites().quit()
