from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from .models import Boardgame


def index(request: HttpRequest):
    context = {
        "boardgames": Boardgame.objects.order_by("pk").all()
    }
    return render(request=request, template_name="boardgames/index.html", context=context)


def details(request: HttpRequest, pk: int, slug):
    context = {
        "boardgame": get_object_or_404(Boardgame, pk=pk)
    }
    cart_product_form = CartAddProductForm()
    return render(request=request, template_name="boardgames/details.html", context=context)

# slug= {'product': product, 'cart_product_form': cart_product_form}


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

