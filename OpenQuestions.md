### Open ###

  * If we want to allow different levels of access for authenticated and unauthenticated users, how should this be configured?
  * Can we make creating resources that don't correspond 1:1 to models easier instead of just changing the type of work that is required to implement them?

### Solved ###

  * Should URLs be generated automatically? Yes. To what extent automation is used is up to the API user.
  * Do we make use of the existing generic views, use serializers or make both an option? Both, via Responder classes.