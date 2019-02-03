from .. import portfolio_apis as api
from . import controller

# End point declarations
api.add_resource(controller.insertEducation, '/insertEducation/v1.0')
api.add_resource(controller.insertExperience, '/insertExperience/v1.0')
