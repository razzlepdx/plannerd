from django.urls import resolve
from django.test import TestCase
from tracker.views import home_page


class HomePageTest(TestCase):

    def test_root_url_returns_home_page_template(self):

        found = resolve('/')
        self.assertEqual(found.func, home_page)