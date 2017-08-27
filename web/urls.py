from web import views

from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'reliefmaps', views.ReliefMapViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'mapitemtemplates', views.MapItemTemplateViewSet)
router.register(r'mapitems', views.MapItemViewSet)

# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]