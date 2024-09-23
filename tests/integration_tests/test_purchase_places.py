import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_purchase_places_success(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': 5
    })
    assert response.status_code == 200
    # Vérifier une partie du message de succès encodé en UTF-8
    assert "Réservation réussie".encode('utf-8') in response.data

