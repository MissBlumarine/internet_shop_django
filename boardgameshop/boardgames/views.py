from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView

from .models import Boardgame, BoardgameAge, Addition


def index(request: HttpRequest):
    context = {
        "boardgames": Boardgame.objects.order_by("pk").all()
    }
    return render(request=request, template_name="boardgames/index.html", context=context)


def details(request: HttpRequest, pk: int):
    context = {
        "boardgame": get_object_or_404(Boardgame, pk=pk)
    }
    return render(request=request, template_name="boardgames/details.html", context=context)


def addition(request: HttpRequest):
    context = {
        "additions": Addition.objects.order_by("pk").all()
    }
    return render(request=request, template_name="boardgames/addition.html", context=context)


class BoardgameListView(ListView):
    context_object_name = "boardgames"
    queryset = (Boardgame
                .objects
                .select_related("min_age_of_player")
                .order_by("pk")
                .all()
                )


class BoardgameDetailView(DetailView):
    model = Boardgame


class AdditionListView(ListView):
    model = Addition
    context_object_name = "addition"
    queryset = (Addition
                .objects
                .order_by("pk")
                .all()
                )


class AdditionDetailView(DetailView):
    model = Addition


class BoardgameByAgeListView(ListView):
    queryset = Boardgame.objects.select_related("min_age_of_player")
