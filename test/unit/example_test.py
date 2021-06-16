from unittest import TestCase
from post import Post

p = Post("Test", "Test Content")


class PostTest(TestCase):

    def test_create_post(self):

        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content)

    def test_json(self):

        expected = {"title": "Test", "content": "Test Content"}

        self.assertEqual(p.json(), expected)