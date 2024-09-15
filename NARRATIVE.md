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
