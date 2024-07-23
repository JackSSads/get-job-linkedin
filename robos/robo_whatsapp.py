from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from urllib.parse import quote
from time import sleep

browser = webdriver.Chrome()

class RoboWhatsapp:
    def __init__(self) -> None:
        pass

    def initialise_robo_whatsapp(self, phone: int):
        print("iniciando robô whatsapp")
        sleep(5)

        path_file = "jobs.xlsx"
        workbook = openpyxl.load_workbook(path_file)
        page_jobs = workbook['Sheet1']

        browser.get("https://web.whatsapp.com")

        sleep(20)
              
        for line in page_jobs.iter_rows(min_row=2):
            job = line[1].value
            link = line[2].value

            #https://web.whatsapp.com/send?phone=<go_to>&text=<message>
            message = f'Vaga: {quote(job)}. Link: {link}'
            link_message = f'https://web.whatsapp.com/send?phone={phone}&text={message}'
            
            sleep(5)
            
            browser.get(link_message)

            sleep(5)

            browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()

            sleep(2)

        browser.quit()

