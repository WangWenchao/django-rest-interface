General procedure (from "RESTful Web Services" by Leonard Richardson and Sam Ruby):

  1. Figure out the data set
  1. Split the data set into resources; for each kind of resource:
  1. Name the resources with URIs
  1. Expose a subset of the uniform interface (GET, PUT, DELETE, POST, HEAD)
  1. Design the representation(s) accepted from the client (see below)
  1. Design the representation(s) served to the client (see below)
  1. Integrate this resource into existing resources, using hypermedia links and forms
  1. Consider the typical course of events: what’s supposed to happen?
  1. Consider error conditions: what might go wrong?

RESTful web services with Django (cf. Jacob Kaplan-Moss, "RESTful Web Services"):

  1. Create the data model (models.py) -- usually: What's stored in the DB
  1. Define resources and give them URIs (urls.py) -- not every Django model is a resource; you might for example not want to expose user accounts as a resource
  1. Implement resources as Django views (views.py) -- function or `Class.__call__` that takes URL parameters and returns a HttpResponse
