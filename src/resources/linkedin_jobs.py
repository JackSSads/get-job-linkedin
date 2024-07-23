from selenium import webdriver
from flask import Blueprint, request, jsonify
from src.service.linkedin_service import LinkedinService
from src.service.whatsapp_service import WhatsappService

robo_resource = Blueprint("robo", __name__, url_prefix="/robo")

@robo_resource.route("/", methods=["GET"])
def get_jobs():
    try:
        browser = webdriver.Chrome()

        req = request.json
        robo_linkedin = LinkedinService(username=req['username'], password=req["password"], search=req["search"])
        robo_linkedin.init_robo_linkedin()

        robo_whatsapp = WhatsappService(phone=req['phone'])
        robo_whatsapp.init_robo_whatsapp()

        response = {"status": "success", "data": "Vagas enviadas com sucesso!"}
        return jsonify(response), 200
    except Exception as e:
        print(f"Ocorreu um erro no get_jobs(): {e}")

        response = {"status": "error", "message": str(e)}
        return jsonify(response), 500
