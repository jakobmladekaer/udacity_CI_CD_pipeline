from locust import HttpUser, task, between

# Setting the  test JSON data
test_data = {
   "CHAS": {
      "0": 0
   },
   "RM": {
      "0": 6.575
   },
   "TAX": {
      "0": 296.0
   },
   "PTRATIO": {
      "0": 15.3
   },
   "B": {
      "0": 396.9
   },
   "LSTAT": {
      "0": 4.98
   }
}


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    host = "https://udacity-ci-cd-project.azurewebsites.net/"

    @task(1)
    def hello_world(self):
        self.client.get("/")

    # Defining the post task using the JSON test data
    @task(2)
    def predict_endpoint(self):
        self.client.post('/predict', json=test_data)
