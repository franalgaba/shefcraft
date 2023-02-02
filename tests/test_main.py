from shefcraft.main import app


def test_app():
    assert callable(app)
