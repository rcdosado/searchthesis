from django.test import TestCase
from search.models import Thesis

class ThesisModelTest(TestCase):

    def test_string_representaiton(self):
        post = Thesis(title="Some research title")
        self.assertEqual(str(post),post.title)

