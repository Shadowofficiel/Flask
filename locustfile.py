from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 3)  # Temps d'attente entre deux requêtes
    host = "http://localhost:5000"  # Spécifier l'hôte de votre application

    @task
    def load_homepage(self):
        # Charger la page d'accueil
        self.client.get("/")

    @task
    def load_competitions(self):
        # Charger la page des compétitions avec un email de test
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def book_places(self):
        # Réserver des places pour une compétition spécifique
        self.client.post("/purchasePlaces", data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": 5
        })
