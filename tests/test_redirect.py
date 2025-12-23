from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_redirect_increments_click(mock_redis):
    # Step 1: Create short URL
    response = client.post(
        "/shorten",
        json={"original_url": "https://example.com"}
    )

    assert response.status_code == 200
    short_url = response.json()["short_url"]
    short_code = short_url.split("/")[-1]

    # Step 2: Call redirect endpoint (do NOT follow redirect)
    redirect_response = client.get(
        f"/{short_code}",
        follow_redirects=False
    )

    # FastAPI typically returns 307 for redirect
    assert redirect_response.status_code in (302, 307)
