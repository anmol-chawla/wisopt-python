from .. import portfolio_apis as api
from . import controller

# End point declarations
api.add_resource(controller.Education, '/education/v1.0')
api.add_resource(controller.Experience, '/experience/v1.0')
api.add_resource(controller.ExtraCurricular, '/extraCurricular/v1.0')
api.add_resource(controller.Social, '/social/v1.0')
