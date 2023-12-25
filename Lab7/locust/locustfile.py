from locust import HttpUser, task, between

class StrategiumUser(HttpUser):
    wait_time = between(3, 5)

    @task
    def test_main_page(self):
        self.client.get("/forum/")

    @task
    def test_forum_search(self):
        self.client.post("/forum/search/", json={"query": "your_search_query"})


    @task
    def test_register_page(self):
        self.client.get("/forum/register/")


    @task
    def test_login_page(self):
        self.client.get("/forum/login/")


    @task
    def test_start_topic_page(self):
        self.client.get("/forum/startTopic/")