# nginx_auth

## Description

An absolutely bare-bones boilerplate for exploring NGINX's `ngx_http_auth_request_module`.

Run `./run.sh` to get up and running. This creates a Docker Compose stack so you'll need to have everything installed to do that.

This will stand up the following containers:

1. `app` — a basic Flask app server serving some (protected) page routes and (unprotected) static assets.
2. `auth` — a basic Flask auth server and login page (wip).
3. `server` — an NGINX server that orchestrates requests to the aforementioned services, including auth sub-requests.

Logs for each container are visible in `logs`. These are purged every time the compose stack is started.

Once up and running, go to [http://localhost:9999](http://localhost:9999) — you should be redirected to a login form at `/auth/login`.

Then, just click "Login", there's no real concept of validation of user input at the moment because that's not the point of this exercise (but I'll probably add it soon anyway for completeness :wink:)
