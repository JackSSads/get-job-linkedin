from robos import RoboLinkedin
from robos import RoboWhatsapp

class Main:
    def __init__(self) -> None:
        self.robo_linkedin = RoboLinkedin()
        self.robo_whatsapp = RoboWhatsapp()

    def start_robo_linkedin(self, username: str, passowrd: str, search: str, validation: int):
        return self.robo_linkedin.initialise_robo(username, passowrd, search, validation)
    
    def start_robo_whatsapp(self, phone: int):
        return self.robo_whatsapp.initialise_robo_whatsapp(phone)