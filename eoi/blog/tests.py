from django.test import TestCase

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='aldres', password='enplano')

    def test_is_published_return_false(self):
        post = Post.objects.create(
            author=self.user, title='mi titulo'
        )

        is_published = post.is_published()

        self.assertFalse(is_published)

    
    