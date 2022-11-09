from django.urls import path
from .views import index, details, BoardgameListView, BoardgameDetailView, addition, AdditionListView, \
    AdditionDetailView, BoardgameByAgeListView

app_name = "boardgames"

urlpatterns = [
    # path("", index, name="index"),
    path("", BoardgameListView.as_view(), name="index"),
    path("addition/", AdditionListView.as_view(), name="addition"),
    path("<int:pk>/", AdditionDetailView.as_view(), name="details_addition"),
    # path("addition/", addition, name="additional"),
    path("<int:pk>/", BoardgameDetailView.as_view(), name="details"),
    # path("<int:pk>/", details, name="details"),
    # path("ages/", BoardgameAgeListView.as_view(), name="min_age"),
    # path("<boardgame_min_age_of_player>", BoardgameByAgeListView.as_view(), name="by-age"),

]