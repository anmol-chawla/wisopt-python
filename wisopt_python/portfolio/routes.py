from .. import api
from . import controller

# End point declarations
api.add_resource(controller.insertEducation, '/insertEducation/api/v1.0')
