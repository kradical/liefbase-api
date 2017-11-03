from web import views

from rest_framework import routers
from dynamic_rest.routers import DynamicRouter

from django.conf.urls import url, include

router = DynamicRouter()
router.register('users', views.UserViewSet)
router.register('teams', views.TeamViewSet)
router.register('organizations', views.OrganizationViewSet)
router.register('memberships', views.MembershipViewSet)

router.register('reliefmaps', views.ReliefMapViewSet)

router.register(r'mapitemtemplates', views.MapItemTemplateViewSet)
router.register(r'filterpresets', views.FilterPresetViewSet)
router.register(r'templatepresets', views.TemplatePresetViewSet)
router.register(r'datalayers', views.DataLayerViewSet)

router.register(r'mapitems', views.MapItemViewSet)


urlpatterns = [
    url(r'users/me/$', views.UserViewSet.as_view({'get': 'retrieve'}), kwargs={'pk': 'me'}),
    url(r'^', include(router.urls))
]
