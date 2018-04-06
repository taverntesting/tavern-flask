# Example flask server

To run the docker based tests, do:

1. `docker-compose up --build .`
2. `py.test`

To run the tests using tavern-flask, do:

1. `py.test --tavern-http-backend=flask`.
