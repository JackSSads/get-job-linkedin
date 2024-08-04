from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep

from src.utils import WebBrowser

class RoboLinkedin:

    def __init__(self) -> None:
        self.browser = WebBrowser(url="https://www.linkedin.com/login")

    def validation(self):
        control = True
        while control:
            try:
                self.browser.driver_wait(
                    driver=self.browser.atribuites(),
                    element=(By.ID, 'input__email_verification_pin'),
                    time=10
                )

                print("Aguardando validação")

                sleep(2)
            except Exception as e:
                control = False
                return print("Linkedin validado!")

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

            # buscando elemento footer para fazer o scroll
            scroll = self.browser.driver_wait(
                driver=self.browser.atribuites(),
                element=(By.CLASS_NAME, 'global-footer-compact'),
                time=15
            )
            if scroll:
                # Execute o script para rolar até o elemento
                self.browser.atribuites().execute_script("arguments[0].scrollIntoView(true);", scroll)
                print("Scrollado para o elemento Footer.")
                sleep(5)

            else:
                print("Elemento Footer não encontrado, scrolling falhou.")

            # Capturando texto e link da vaga
            list_elements = self.browser.atribuites().find_elements(By.CLASS_NAME, 'job-card-container__link')
            text_job = [job.text for job in list_elements]
            link_job = [job.get_attribute("href") for job in list_elements]
                       
            self.insert_data_in_excel_file(text_job, link_job)

            print("Terminado")
            return self.browser.atribuites().quit()
        except Exception as e:
            return print(f"Ocorreu um erro no get_job(): {e}")

    def insert_data_in_excel_file(self, jobs, links):
        print("Inserindo dados no arquivo jobs.xlsx")

        dictDF = {
            'Vaga': jobs,
            'Links': links
        }

        pdDF = pd.DataFrame(dictDF)
        pdDF.to_excel('./jobs.xlsx', index=True)
        print("Arquivo jobs.xlsx criado\n")
        
        print(pdDF)

    def initialise_robo(self, username: str, passowrd: str, search: str):
        
        print("Iniciando robô linkedin")
        self.browser.initalise_web_browser()
        
        input_email = self.browser.driver_wait(
            driver=self.browser.atribuites(),
            element=(By.ID, 'username'),
            time=10
        )
        input_email.send_keys(username)

        input_password = self.browser.driver_wait(
            driver=self.browser.atribuites(),
            element=(By.ID, 'password'),
            time=10
        )
        input_password.send_keys(passowrd)

        self.browser.driver_wait(
            driver=self.browser.atribuites(),
            element=(By.CLASS_NAME, 'login__form_action_container'),
            time=10
        ).click()

        self.validation()

        self.get_job(search=search)