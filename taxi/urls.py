from django.urls import path

from .views import index, manufacturer_list

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        manufacturer_list.as_view(),
        name="manufacturer-list",
    ),
]
