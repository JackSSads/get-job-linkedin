from main import Main

main = Main()

class WhatsappService():
    def __init__(self, contact) -> None:
        self.contact = contact

    def init_robo_whatsapp(self):
        try:
            res = main.start_robo_whatsapp(self.contact)
            print("Robô Whatsapp finalizado")
            return res
        except Exception as e:
             return print(f"Ocorreu um erro no init_robo_whatsapp(): {e}")