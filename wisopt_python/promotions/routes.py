from .. import promotions_apis as api
from . import controller


# End point declarations
api.add_resource(controller.Promotions, '/events/v1.0')

