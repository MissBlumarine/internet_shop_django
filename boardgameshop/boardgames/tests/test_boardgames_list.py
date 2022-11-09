from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse, reverse_lazy

from boardgames.models import Boardgame, Addition


class BoardgamesListTestCase(TestCase):
    fixtures = [
        "addition.fixture.json",
        "boardgameages.fixture.json",
        "boardgames.fixture.json",
    ]

    url = reverse_lazy("boardgames:index")

    def test_list_boardgames(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        boardgames = (Boardgame
                      .objects
                      .select_related("min_age_of_player")
                      .order_by("pk")
                      .all()
                      )
        print(boardgames)
        boardgames_in_context = response.context["boardgames"]
        print(boardgames_in_context)
        self.assertEqual(len(boardgames), len(boardgames_in_context))
        for b1, b2 in zip(boardgames, boardgames_in_context):
            self.assertEqual(b1.pk, b2.pk)

    def test_anon_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context["user"].is_anonymous)

class AdditionListTestCase(TestCase):
    fixtures = [
        "addition.fixture.json",
        "boardgameages.fixture.json",
        "boardgames.fixture.json",
    ]

    def test_list_addition(self):
        url = reverse("boardgames:addition")
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        additions = (Addition
                     .objects
                     .order_by("pk")
                     .all()
                     )
        print(additions)
        additions_in_context = response.context["addition"]
        print(additions_in_context)
        self.assertEqual(len(additions), len(additions_in_context))
        for a1, a2 in zip(additions, additions_in_context):
            self.assertEqual(a1.pk, a2.pk)
