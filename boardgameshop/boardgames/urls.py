from django.urls import path
from .views import index, details, BoardgameListView, BoardgameDetailView

app_name = "boardgames"

urlpatterns = [
    path("", BoardgameListView.as_view(), name="index"),
    path("<int:pk>/", BoardgameDetailView.as_view(), name="details"),
]