from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep

from src.utils import WebBrowser

class RoboLinkedin:

    def __init__(self) -> None:
        self.browser = WebBrowser(url="https://www.linkedin.com/login")

    def validation(self, validation):
        input_validation = self.browser.atribuites().find_element(By.ID, 'input__email_verification_pin')
        input_validation.send_keys(validation)

        self.browser.atribuites().find_element(By.ID, 'email-pin-submit-button').click()

    def get_job(self, search: str):
        try:
            # button search
            self.browser.driver_wait(
                driver=self.browser.atribuites(), 
                element=(By.CLASS_NAME, 'search-global-typeahead__collapsed-search-button'), 
                time=10
            ).click()
            
            # input search
            input_search_job = self.browser.driver_wait(
                driver=self.browser.atribuites(), 
                element=(By.CLASS_NAME, 'search-global-typeahead__input'), 
                time=10
            )
            input_search_job.click()
            input_search_job.send_keys(search)
            input_search_job.send_keys(Keys.RETURN)
            
            print("Buscando vagas...")

            # Clicar no filtro "Vagas"
            self.browser.driver_wait(
                driver=self.browser.atribuites(),
                element=(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]'),
                time=15
            ).click()

            sleep(5)

            # Capturando texto e link da vaga
            list_elements = self.browser.atribuites().find_elements(By.CLASS_NAME, 'job-card-container__link')
            text_job = [job.text for job in list_elements]
            link_job = [job.get_attribute("href") for job in list_elements]
            
            dictDF = {
                'Vaga': text_job,
                'Links': link_job
            }
            
            print("Vagas agrupadas")
            pdDF = pd.DataFrame(dictDF)
            pdDF.to_excel('./jobs.xlsx', index=True)
            print("Arquivo jobs.xlsx criado\n")
            
            print(pdDF)
            
            self.browser.atribuites().quit()
            print("Terminado")
        except Exception as e:
            print(f"Ocorreu um erro no get_job(): {e}")

    def initialise_robo(self, username: str, passowrd: str, search: str, validation: int):
        
        self.browser.initalise_web_browser()
        
        print("Iniciando robô linkedin")

        input_email = self.browser.atribuites().find_element(By.ID, 'username')
        input_email.send_keys(username)

        input_password = self.browser.atribuites().find_element(By.ID, 'password')
        input_password.send_keys(passowrd)

        self.browser.atribuites().find_element(By.CLASS_NAME, 'login__form_action_container').click()

        sleep(3)

        try:
            self.validation(validation=validation)

            print('\nVerificação realizada!\n')

            self.get_job(search=search)
        except:
            print('\nNão tem validação\n')
            self.get_job(search=search)