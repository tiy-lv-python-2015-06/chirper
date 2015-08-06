import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
from updates.models import Chirp


class ChirpMethodTests(TestCase):

    def test_was_recently_published_old_chirp(self):
        time = timezone.now() - datetime.timedelta(days=10)
        chirp = Chirp(message="Test", title="Title", posted_at=time)
        self.assertFalse(chirp.was_published_recently(), "Chirp not recent")

    def test_was_recently_published_new(self):
        time = timezone.now()
        chirp = Chirp(message="Test", title="Title", posted_at=time)
        self.assertTrue(chirp.was_published_recently(), "Chirp was published recently")

    def test_was_recently_published_future(self):
        time = timezone.now() + datetime.timedelta(days=10)
        chirp = Chirp(message="Test", title="Title", posted_at=time)
        self.assertFalse(chirp.was_published_recently(), "Chirp future not recent")

class ChirpViewTests(TestCase):

    def test_detail_chirp_404(self):
        url = reverse('detail_chirp', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, "Didn't return 404")

    def test_detail_chirp_return_new_chirp(self):
        test_user = User.objects.create_user("test", "test@test.com", "pass")
        test_user.save()

        time = timezone.now()
        chirp = Chirp(message="Testing", title="Title", posted_at=time, author=test_user)
        chirp.save()

        response = self.client.get(reverse('detail_chirp', args=[chirp.id]))
        self.assertContains(response,"Testing")
