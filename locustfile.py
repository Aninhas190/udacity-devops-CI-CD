from locust import HttpUser, task

class UdacityProject2(HttpUser):
    @task
    def enter_udacity_project(self):
        self.client.get("/")
        self.client.get("/predict")
