import sys
from ..models import secureRequest
from ..settings import request_dict

''' this is a simple test '''

test = secureRequest.SecureRequest(request_dict['test'])
res = test.response()
print res.text

