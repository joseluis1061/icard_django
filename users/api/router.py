from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()
router_user.register(
  prefix = 'user',
  basename = 'users',
  viewset= UserApiViewSet
)

urlpatterns = [
  path('auth/me/', UserView.as_view())
]