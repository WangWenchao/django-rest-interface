I know three projects that overlap with the first part of my proposal:

  * **[djangocollection](http://code.google.com/p/djangocollection/)**

> The djcollection app provides a set of generic RESTful urls for all
> the models of a project and a GenericCollection class which uses
> Django's generic views (and therefore templates) to make models
> CRUD-accessible.

  * **[django-crudapi](http://code.google.com/p/django-crudapi/)**

> Provides a set of catch-all urls and CRUD functions that make the apps
> of all models of a project CRUD-accessible, uses Django's serializers
> to return json or xml.

  * **[django-restful-model-views](http://code.google.com/p/django-restful-model-views/)**

> Adam Smith follows an approach similar to the one I proposed (an
> abstract Resources class and a ModelResources class for model-bound
> resources). He uses a lot of introspection to automagically create url
> patterns for all models that should be available. Adam intends to use
> Django's generic views (not implemented yet).

These projects look like a good point to start, but they don't seem to
pay much attention to security questions like which data should be
accessible, which CRUD actions possible and which model fields
visible. To my mind, these should be available as settings similar to
the urls.py example shown in my proposal.