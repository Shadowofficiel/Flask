import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_reservation_success(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': 5
    })
    assert response.status_code == 200
    # Encodage du message attendu pour supporter les accents
    assert "Réservation réussie !".encode('utf-8') in response.data
