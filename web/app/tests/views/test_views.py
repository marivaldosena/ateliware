from flask import url_for, request


class TestView:
    def test_get_home(self, client):
        response = client.get('/')

        assert response.status_code == 200
