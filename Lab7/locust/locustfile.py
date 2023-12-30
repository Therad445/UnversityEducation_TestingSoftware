from locust import HttpUser, task, between
import random as rnd

class StrategiumUser(HttpUser):
    wait_time = between(3, 15)

    @task(1)
    def test_login_page(self):
        self.client.get("/forum/login/")

    @task(2)
    def test_main_page(self):
        self.client.get("/forum/")

    @task(3)
    def test_forum_search(self):
        search_send = "?q="+ "Europe" +"&quick=1"
        self.client.get("/forum/search/"+ search_send)

    @task(4)
    def check_treds(self):
        page_id = rnd.randint(1, 3)
        with self.client.get(f'/forum/f/56-crusader-kings-2-крестоносцы-2/page={page_id}', catch_response=True, name='/forum/f/56-crusader-kings-2-крестоносцы-2/page=[id]') as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'status code is {response.status_code}')


    @task(5)
    def test_register_page(self):
        self.client.get("/forum/register/")

    @task(6)
    def test_start_topic_page(self):
        self.client.get("/forum/startTopic/")

    @task(7)
    def test_activities(self):
        self.client.get("/forum/discover/")

    @task(8)
    def check_topics(self):
        page_id = rnd.randint(2, 1047)
        with self.client.get(f'/forum/topic/46806-игра-за-москву/page/{page_id}', catch_response=True, name='/forum/topic/46806-игра-за-москву/page/[id]') as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'status code is {response.status_code}')


    #
    # @task(6)
    # def search_for_product(self):
    #     self.client.get("/forum/search", {"q": "Europe"})
    #     # self.client.wait(1)  # Wait for some time to allow the server to respond
    #     result = self.client.get_response().content
    #     # Check if the product was found
    #     if "product-name" in result:
    #         self.client.log("Europe found")
    #     else:
    #         self.client.log("Europe not found")
