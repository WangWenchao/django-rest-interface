## Summary ##

The Django REST interface makes it easy to offer private and public APIs for existing Django models. New generic views simplify data retrieval and modification in a resource-centric architecture and provide model data in formats such as XML, JSON and YAML with very little custom code.

[RESTify your Django apps!](http://code.google.com/p/django-rest-interface/wiki/RestifyDjango)

[Join the mailing list!](http://groups.google.com/group/django-rest-interface)

## Installation & Setup ##

**Step 1:** Checkout from Subversion:

```
svn checkout http://django-rest-interface.googlecode.com/svn/trunk/ django-rest-interface 
```

**Step 2:** Add the django-rest-interface directory to your PYTHONPATH.

**Step 3:** Add these lines to your urls.py:

```
from django_restapi.model_resource import Collection
from django_restapi.responder import XMLResponder
```

**Step 4:** For every model you want to be part of the API, create a Collection instance in urls.py (see [more elaborate examples](http://django-rest-interface.googlecode.com/svn/trunk/django_restapi_tests/examples/)):

```
mymodel_resource = Collection(
    queryset = MyModel.objects.all(),
    responder = XMLResponder()
)
```

**Step 5:** Add the resource to your URL patterns:

```
urlpatterns = patterns('',
   # ...
   url(r'^xml/mymodel/(.*?)/?$', mymodel_resource)
)
```

Voilà! Your XML API is ready at `http://yourhost/xml/mymodel/`.

## Contact ##

[Andreas Stuhlmüller](mailto:django@stuhlmueller.info)