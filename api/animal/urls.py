from django.urls import path
from .views import AnimalList, AnimalDetail

urlpatterns = [
    path("animals/", AnimalList.as_view(), name="animal-list"),
    path("animals/<int:pk>/", AnimalDetail.as_view(), name="animal-detail"),
]
