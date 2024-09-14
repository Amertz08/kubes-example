import locust


class APIUser(locust.HttpUser):
    host = "http://localhost:8000"

    @locust.task
    def health(self):
        self.client.get("/healthcheck")
