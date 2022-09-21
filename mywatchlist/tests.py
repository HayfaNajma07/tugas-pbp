from django.test import TestCase, Client

# Create your tests here.
class WatchListTestCase(TestCase):
    client = Client()
    def test_html(self):
        response = self.client.get('/mywatchlist/html/')
        return self.assertEqual(response.status_code, 200)


    def test_xml(self):
        response = self.client.get('/mywatchlist/xml/')
        return self.assertEqual(response.status_code, 200)


    def test_json(self):
        response = self.client.get('/mywatchlist/json/')
        return self.assertEqual(response.status_code, 200)

# Source: https://stackoverflow.com/questions/35741090/how-to-test-url-in-django