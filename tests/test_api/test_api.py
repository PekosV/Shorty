
class TestApi:

    def test_api_with_valid_url_bitly(self, post):
        # when we ask to shorten a valid url
        response = post(
            '/shortlinks',
            data={'url': 'https://www.withnottplum.com', 'provider': 'bitly'}
        )

        # then
        assert response.status_code == 200
        assert response.get_json()['data']['url'] == 'https://www.withnottplum.com'
        assert response.get_json()['data']['short_link'].startswith('https://bit.ly')

    def test_api_with_valid_url_tinyurl(self, post):
        # when we ask to shorten a valid url
        response = post(
            '/shortlinks',
            data={'url': 'https://www.pekosestate.com', 'provider': 'tinyurl'}
        )

        # then
        assert response.status_code == 200
        assert response.get_json()['data']['url'] == 'https://www.pekosestate.com'
        assert response.get_json()['data']['short_link'].startswith('https://tinyurl.com')

    def test_api_with_invalid_url_bitly(self, post):
        # when we ask to shorten a valid url
        response = post(
            '/shortlinks',
            data={'url': 'https://www.pekos  estate'}
        )

        assert response.status_code == 422
        assert response.get_json()['error']['message'] == 'Malformed URL'

    def test_api_default_provider(self, post):
        # when we ask to shorten a valid url
        response = post(
            '/shortlinks',
            data={'url': 'https://www.withplum.com'}
        )
        assert response.status_code == 200
        assert response.get_json()['data']['short_link'].startswith('https://bit.ly')
