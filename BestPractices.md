According to "RESTful Web Services" by Leonard Richardson and Sam Ruby.

  * **Addressability**

> Every resource has its own unique URI.
> Suggestion: Every _representation_ of a resource has its own URI.
> Headers shouldn't be the only tool a client has to specify which resource or representation is selected.

  * **Statelessness**

> The server never stores any application state. Each client request is considered in isolation.

  * **Safety**

> A client that makes a GET or HEAD request is not requesting any changes to server state.

  * **Idempotence**

> Making more than one PUT or DELETE request to a given URL should have the same effect as making only one.

  * **New Resources: PUT vs POST**

> A client can only use PUT to create resources when it can calculate the final URI. If the URI is not known, the client can POST to a "factory" resource.

  * **Connectedness**

> Instead of assuming that rules how to construct URIs are known, use links. A service ought to be self-describing, and not relying on auxiliary English text that tells programmers how to write clients.

  * **Relationships Between Resources**

> Instead of modifying the state of two resources, treat the relationship as a third kind of resource. The same goes for transactions. "When in doubt, make it a resource."

  * **URI Design**

> URIs should be meaningful and well-structured. Use query variables only to suggest arguments being plugged into an algorithm. It is almost never appropriate to put the names of operations in URIs.

  * **Outgoing Representations**

> Should be human-readable, but computer-oriented.

  * **Incoming Representations**

> Usually key-value pairs, form-encoding is the most popular representation. If a resource state is too complex for key-value pairs, the input format should be the same as the output format.

  * **Service Versioning**

> Simplest way: Incorporate versioning information into the resources' URIs.

  * **Permanent URIs Versus Readable URIs**

> Whether URIs as UIs (meaningful, may break when resource state changes) or opaque URIs (e.g. using only database id, permanent) are more appropriate depends on the clients.
