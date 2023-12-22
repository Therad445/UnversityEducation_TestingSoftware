from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_is_prime(self):
        self.client.get("/is_prime?n=1000")

    @task
    def test_prime_factors(self):
        self.client.get("/prime_factors?n=1000")