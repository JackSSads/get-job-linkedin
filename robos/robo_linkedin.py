from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
from time import sleep

from src.utils import Driver

driver = Driver()

class RoboLinkedin:

    def __init__(self) -> None:
        pass

    def validation(self):
        # Caso haja um pop-up de validação de email, aguarda até dois minutos
        control = 0
        while control < 120:
            try:
                inputVerification = driver.waiting("//input[@id='input__email_verification_pin']")

                if inputVerification:
                    print("Aguardando validação")

                    sleep(2)
                    control += 2
                else: 
                    raise Exception("Não encontrou validação")
            except Exception:
                control = 120
                print("Não encontrou validação")
                return

    def get_job(self, search: str):
        try:
            
            # input search
            print("Buscando botão de busca...")
            input_search_job = driver.waiting("//div[@id='global-nav-typeahead']/input")
            input_search_job.click()
            driver.write(input_search_job, search)
            driver.keys(input_search_job, Keys.RETURN)
            
            print("Buscando vagas...")

            # Clicar no filtro "Vagas"
            driver.waiting("//div[@id='search-reusables__filters-bar']//button[text()='Vagas']").click()

            sleep(5)

            # buscando elemento footer para fazer o scroll
            scroll = driver.waiting("//footer")

            # TODO Corrigir esse scroll
            if scroll:
                # Execute o script para rolar até o elemento
                driver.scroll(scroll)
                sleep(3)
            else:
                print("Elemento Footer não encontrado, scrolling falhou.")

            # TODO verificar se os dados que estão sendo capturados estão corretos
            # Capturando texto e link da vaga
            list_elements = driver.waiting(
                ec=EC.visibility_of_all_elements_located,
                search="//ul[@class='scaffold-layout__list-container']/li//div/div/div/div/div[2]/div/a"
            )

            text_job = [job.text for job in list_elements]
            link_job = [job.get_attribute("href") for job in list_elements]
                       
            self.insert_data_in_excel_file(text_job, link_job)

            print("Terminado")
            return driver.close_web_driver()
        except Exception as e:
            driver.close_web_driver()
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
        driver.initialize_webdriver()

        driver.navigate_to("https://www.linkedin.com/login")
        
        input_email = driver.waiting("//input[@id='username']")
        driver.write(input_email, username)

        input_password = driver.waiting("//input[@id='password']")
        driver.write(input_password, passowrd)

        driver.waiting("//button[@class='btn__primary--large from__button--floating']").click()

        self.validation()

        self.get_job(search=search)