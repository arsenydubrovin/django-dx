from rest_framework.routers import SimpleRouter
from django.urls import path, include
from books.api.views import BookViewSet

router = SimpleRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
