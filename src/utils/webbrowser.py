from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebBrowser():
    def __init__(self, url: str) -> None:
        self.url = url
        self.browser = None

    # Inicializa um webdriver, acessa a url enviada na instância do objeto
    def initalise_web_browser(self):
        try:
            print("Iniciando web browser")
            browser = webdriver.Chrome()
            browser.get(self.url)

            self.browser = browser
        except Exception as e:
            print(f"Ocorreu um erro no initalise_web_browser(): {e}")

    # esportando a conexão
    def atribuites(self) -> webdriver:
        return self.browser
    
    # Método de espera por elemento
    def driver_wait(self, driver: webdriver, element: any, time: int = 10) -> WebDriverWait:
         return WebDriverWait(driver, time).until(EC.element_to_be_clickable(element))