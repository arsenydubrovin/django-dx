from django.urls import path, include

urlpatterns = [
    path("v1/books/", include("books.urls")),
]
