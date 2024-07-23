from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

browser = webdriver.Chrome()

class RoboLinkedin:

    def __init__(self) -> None:
        pass

    def validation(validation):
        input_validation = browser.find_element(By.ID, 'input__email_verification_pin')
        input_validation.send_keys(validation)

        browser.find_element(By.ID, 'email-pin-submit-button').click()

        return input_validation

    def get_job(search: str):

        browser.find_element(By.CLASS_NAME, 'search-global-typeahead__collapsed-search-button').click()

        input_seach_job = browser.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
        input_seach_job.send_keys(search)
        input_seach_job.send_keys(Keys.RETURN)

        browser.find_element(By.CLASS_NAME, 'search-global-typeahead__collapsed-search-button').click()

        time.sleep(3)

        browser.find_element(By.CLASS_NAME, 'search-reusables__primary-filter').click()

        time.sleep(5)

        list_elements = browser.find_elements(By.CLASS_NAME, 'job-card-container__link')

        text_job = [job.text for job in list_elements]
        link_job = [job.get_attribute("href") for job in list_elements]

        dictDF = {
            'Vaga': text_job,
            'Links': link_job
        }

        pdDF = pd.DataFrame(dictDF)

        pdDF.to_excel('./jobs.xlsx', index=True)

        print(pdDF)

        browser.quit()

    def initialise_robo(self, username: str, passowrd: str, search: str, validation: int):
        browser.get("https://www.linkedin.com/login")

        input_email = browser.find_element(By.ID, 'username')
        input_email.send_keys(username)

        input_password = browser.find_element(By.ID, 'password')
        input_password.send_keys(passowrd)

        browser.find_element(By.CLASS_NAME, 'login__form_action_container').click()

        time.sleep(3)

        try:
            RoboLinkedin.validation(validation=validation)

            print('\nVerificação realizada!\n')

            RoboLinkedin.get_job(search=search)
        except:
            print('\nNão tem validação\n')
            RoboLinkedin.get_job(search=search)