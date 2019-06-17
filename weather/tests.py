from django.test import SimpleTestCase

HTTP_OK = 200


class IndexPageTests(SimpleTestCase):

    def test_index_page_status_code(self):
        self.assertEqual(self.client.get('/').status_code, HTTP_OK)
