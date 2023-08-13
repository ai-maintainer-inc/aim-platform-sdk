from fastapi.testclient import TestClient

from fastapi.testclient import TestClient
from reference_agent.agent import (
    app,
    Ticket,
    Bid,
    Artifact,
)

client = TestClient(app)

# Test data
test_ticket = Ticket(
    ticketId="1",
    userId="user1",
    title="Test Ticket",
    description="This is a test ticket",
    code={
        "userId": "user1",
        "repoId": "repo1",
        "branch": "master",
        "commit": "commit1",
    },
    public=True,
    status="open",
    createdAt="2022-01-01T00:00:00Z",
    updatedAt="2022-01-02T00:00:00Z",
)

test_bid = Bid(
    bidId="1",
    ticketId="1",
    agentId="agent1",
    rate=3.0,
    status="accepted",
    createdAt="2022-01-01T00:00:00Z",
    updatedAt="2022-01-02T00:00:00Z",
)

test_artifact = Artifact(
    artifactId="1",
    ticketId="1",
    bidId="1",
    agentId="agent1",
    code={
        "userId": "user1",
        "repoId": "repo1",
        "branch": "master",
        "commit": "commit1",
    },
    status="accepted",
    createdAt="2022-01-01T00:00:00Z",
    updatedAt="2022-01-02T00:00:00Z",
)


# Test functions
def test_ticket_event(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    response = client.post("/ticket_event", json=test_ticket.model_dump())
    assert response.status_code == 200


def test_bid_event(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    response = client.post("/bid_event", json=test_bid.model_dump())
    assert response.status_code == 200


def test_artifact_event():
    response = client.post("/artifact_event", json=test_artifact.model_dump())
    assert response.status_code == 200


# Mock classes
class MockResponse:
    def __init__(self):
        self.status_code = 200
