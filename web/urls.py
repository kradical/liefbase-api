from web import views

from rest_framework import routers

from django.conf.urls import url, include

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()

router.register(r'reliefmaps', views.ReliefMapViewSet, base_name='reliefmaps')
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'memberships', views.MembershipViewSet)

router.register(r'mapitemtemplates', views.MapItemTemplateViewSet)
router.register(r'mapitems', views.MapItemViewSet)
router.register(r'filterpresets', views.FilterPresetViewSet)
router.register(r'templatepresets', views.TemplatePresetViewSet)

# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
