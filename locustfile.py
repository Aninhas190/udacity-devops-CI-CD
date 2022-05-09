from locust import HttpUser, task, TaskSet

class MyTaskSet(TaskSet):
    @task
    def go_to_site(self):
        self.client.get("")

class MyLocust(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000

    host = https://udacity-project-2.azurewebsites.net
