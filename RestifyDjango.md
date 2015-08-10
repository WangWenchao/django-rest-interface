**1. Design the interface**

Decide, which resources you want to make available and in what way.

> Resources are sources of specific information, each of which
> can be referred to using a global identifier (a URI). In
> order to manipulate these resources, components of the network
> (clients and servers) communicate via a standardized interface
> (e.g. HTTP) and exchange representations of these resources
> (the actual documents conveying the information). [Wikipedia: REST](http://en.wikipedia.org/wiki/Representational_State_Transfer)

Usually, this involves [four steps](http://bitworking.org/news/How_to_create_a_REST_Protocol):

  1. What are the URIs? (Resources)
  1. What's the format? (Representation)
  1. What methods are supported at each URI? (Access restriction)
  1. (What status codes could be returned?)

Some resources may directly correspond to Django models, others may not involve model data at all (e.g. an index page for service discovery) or may correspond to more than one model (e.g. a "marriage" resource that corresponds to a "married\_to" one-to-one relationship between two user models). For a good example of how to identify the resources of a complex application, see [Restify DayTrader](http://bitworking.org/news/201/RESTify-DayTrader).

**2. Create model-based resources**

For every model you want to be part of the API, create a `Collection` instance and add it to `urlpatterns` in urls.py:

```
from django_restapi.model_resource import Collection
from django_restapi.responder import XMLResponder
from django_restapi_tests.polls.models import Poll, Choice

xml_poll_resource = Collection(
    queryset = Poll.objects.all(),
    permitted_methods = ('GET', 'POST', 'PUT', 'DELETE'),
    responder = XMLResponder(paginate_by = 10)
)

urlpatterns = patterns('',
   # ...
   url(r'^xml/polls/(.*?)/?$', xml_poll_resource),
)
```

See [more elaborate examples](http://django-rest-interface.googlecode.com/svn/trunk/django_restapi_tests/examples/).


**3. Create non-model-based resources**

Subclass Resource, overwrite some or all of the `create`/`read`/`update`/`delete` methods and, in some cases, `get_url`, and add it to urlpatterns in urls.py:

```
from django_restapi.resource import Resource

class MyResource(Resource):
    def read(self, request):
        # ...
    def update(self, request):
        # ...

urlpatterns = patterns('',
   # ...
   url(r'^my_resource/$', MyResource()),
)
```

See [an example](http://django-rest-interface.googlecode.com/svn/trunk/django_restapi_tests/examples/generic_resource.py).