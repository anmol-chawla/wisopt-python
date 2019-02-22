from .. import discover_apis as api
from . import controller

# End point declarations
api.add_resource(controller.Articles, '/articles/v1.0')
