from django.test import TestCase
from django.urls import reverse


#Index page
class IndexTestView(TestCase):

    # test that the page index on route '/' returns 200
    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
