from flask import Blueprint
from .linkedin_jobs import robo_resource

resources = Blueprint("getJobsLinkedin", __name__)

resources.register_blueprint(robo_resource)
