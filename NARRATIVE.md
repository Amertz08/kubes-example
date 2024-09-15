# Narrative document

This document outlines why I did certain things and just general thoughts.

## Database stuff

### Why use SQLAlchemy Core instead of the ORM?

SQLAlchemy ORM like many ORMs adds a lot of cruft to the models. By using Core + mappers + pydantic models I can write
unit tests and init Pydantic models without dealing with the DB at all, thus writing true unit tests. For integration
tests I just have to invoke `start_mappers` to interact with the database.

### How are migrations handled?

I went with Alembic as the migration tool. I have not used this professionally but I have poked around with it. This project
is probably the most concrete usage of it. In order to run the actual migrations in the cluster I used a Job. I felt this
was the appropriate Kubernetes object to use. I wrote a migrate up and migrate down job. I could probably just use a single
job config and change the `command:` for whatever action I needed to take.

## Productionalizing

### Post Deployment Tests

I like to try and write some basic smoke tests for APIs that can be ran after the application is deployed to an environment.
A lot of the time they're just `GET` requests to make sure the API is basically working. The actual logic should be tested
via the application test suite. I started writing smoke tests at Farmobile because we would see errors that could not be
caught in our application test suite (such as multi db routing in our Django based APIs) until the application was deployed.
I actually created a Jenkins job specific for post deployment tests and modified our ECS deployment job to allow the config
to define the test suite to be ran after the deployment job completed.

### Load testing

Locust is a framework I am decently familiar with. I have only ever used it via a local machine against a deployed API.
One of my core goals with this project is to learn how to deploy it into a K8 cluster and run it with a lot more volume.
This will also allow me to learn how to scale in K8s.
