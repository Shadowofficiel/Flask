import pytest
from server import loadClubs

def test_load_clubs():
    clubs = loadClubs()
    assert len(clubs) > 0  # Vérifie que la liste des clubs n'est pas vide
    assert isinstance(clubs, list)  # Vérifie que le résultat est une liste
    assert "name" in clubs[0]  # Vérifie que les clubs contiennent une clé "name"
