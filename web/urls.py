from web import views

from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'reliefmaps', views.ReliefMapViewSet, base_name='reliefmaps')
router.register(r'users', views.UserViewSet)
router.register(r'mapitemtemplates', views.MapItemTemplateViewSet)
router.register(r'mapitems', views.MapItemViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'filterpresets', views.FilterPresetViewSet)
router.register(r'templatepresets', views.TemplatePresetViewSet)
router.register(r'memberships', views.MembershipViewSet)

# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
