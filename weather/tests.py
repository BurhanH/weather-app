from django.test import TestCase

HTTP_OK = 200


class IndexPageTests(TestCase):

    def test_index_page_status_code(self):
        self.assertEqual(self.client.get('/').status_code, HTTP_OK)
