from .. import portfolio_apis as api
from . import controller

# End point declarations
api.add_resource(controller.Education, '/Education/v1.0')
api.add_resource(controller.Experience, '/Experience/v1.0')
api.add_resource(controller.ExtraCurricular, '/ExtraCurricular/v1.0')
api.add_resource(controller.Social, '/Social/v1.0')
