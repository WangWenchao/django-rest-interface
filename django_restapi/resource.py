"""
Generic resource class.
"""
from django.http import Http404, HttpResponseNotAllowed, HttpResponseBadRequest, QueryDict

def load_put_and_files(request):
    """
    Populates request.PUT and request.FILES from
    request.raw_post_data. PUT and POST requests differ 
    only in REQUEST_METHOD, not in the way data is encoded. 
    Therefore we can use Django's POST data retrieval method 
    for PUT.
    """
    if request.method == 'PUT':
        request.method = 'POST'
        request._load_post_and_files()
        request.PUT = request.POST
        request.method = 'PUT'

class Resource(object):
    """
    Generic resource class that can be used for
    resources that are not based on Django models.
    """
    def __init__(self, authentication=None, permitted_methods=None):
        """
        authentication:
            the authentication instance that checks whether a
            request is authenticated
        permitted_methods:
            the HTTP request methods that are allowed for this 
            resource e.g. ('GET', 'PUT')
        """
        # Access restrictions
        self.authentication = authentication
        if permitted_methods:
            self.permitted_methods = [op.upper() for op in permitted_methods]
        else:
            self.permitted_methods = ["GET"]
    
    def __call__(self, request, *args, **kwargs):
        """
        Redirects to one of the CRUD methods depending 
        on the HTTP method of the request. Checks whether
        the requested method is allowed for this resource.
        """
        # Check permission
        if self.authentication:
            if not self.authentication.is_authenticated(request):
                return self.authentication.challenge()
        request_method = request.method.upper()
        if request_method not in self.permitted_methods:
            return HttpResponseNotAllowed(self.permitted_methods)
        
        if request_method == 'GET':
            return self.read(request, *args, **kwargs)
        elif request_method == 'POST':
            return self.create(request, *args, **kwargs)
        elif request_method == 'PUT':
            load_put_and_files(request)
            return self.update(request, *args, **kwargs)
        elif request_method == 'DELETE':
            return self.delete(request, *args, **kwargs)
        else:
            raise Http404
    
    # The four CRUD methods that any class that 
    # inherits from Resource may implement:
    
    def create(self, request):
        raise Http404
    
    def read(self, request):
        raise Http404
    
    def update(self, request):
        raise Http404
    
    def delete(self, request):
        raise Http404
    