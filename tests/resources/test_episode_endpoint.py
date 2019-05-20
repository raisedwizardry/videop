# Import the resource/controllers we're testing
from resources.episode import *

# client is a fixture, injected by the `pytest-flask` plugin

def test_get_episode(client):
    # Make a tes call to /books/1
    response = client.get("/api/episodes/1")

    # Validate the response
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "episodesign": "S01E12", 
        "title": "Robin in the Hood",
        "show": "Bob's Burgers"
    }
