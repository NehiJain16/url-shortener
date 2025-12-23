import pytest

class FakeRedis:
    def __init__(self):
        self.store = {}

    def get(self, key):
        return self.store.get(key)

    def incr(self, key):
        self.store[key] = int(self.store.get(key, 0)) + 1

    def expire(self, key, ttl):
        pass

@pytest.fixture
def mock_redis(mocker):
    fake = FakeRedis()
    mocker.patch("app.main.redis_client", fake)
    return fake
