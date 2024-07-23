from main import Main

main = Main()

class LinkedinService:
    def __init__(self, username: str, password: str, search: str, validation: int = 0) -> None:
       self.validation = validation
       self.passowrd = password
       self.username = username
       self.search = search

    def init_robo_linkedin(self):
        try:
            dict_jobs = main.start_robo_linkedin(self.username, self.passowrd, self.search, self.validation)
            print("Robô Linkedin finalizado")
            return dict_jobs
        except Exception as e:
            print(f"Ocorreu um erro no init_robo_linkedin(): {e}")