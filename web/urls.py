from web import views

from rest_framework_nested import routers

from django.conf.urls import url, include


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()

router.register(r'reliefmaps', views.ReliefMapViewSet)
maps_router = routers.NestedSimpleRouter(router, r'reliefmaps', lookup='memberable')
maps_router.register(r'admins', views.AdminViewSet, base_name='reliefmap-admins')
maps_router.register(r'members', views.MemberViewSet, base_name='reliefmap-members')


router.register(r'organizations', views.OrganizationViewSet)
organization_router = routers.NestedSimpleRouter(router, r'organizations', lookup='memberable')
organization_router.register(r'admins', views.AdminViewSet, base_name='organization-admins')
organization_router.register(r'members', views.MemberViewSet, base_name='organization-members')

router.register(r'teams', views.TeamViewSet)
team_router = routers.NestedSimpleRouter(router, r'teams', lookup='memberable')
team_router.register(r'admins', views.AdminViewSet, base_name='team-admins')
team_router.register(r'members', views.MemberViewSet, base_name='team-members')

router.register(r'users', views.UserViewSet)

router.register(r'mapitemtemplates', views.MapItemTemplateViewSet)
router.register(r'mapitems', views.MapItemViewSet)



router.register(r'filterpresets', views.FilterPresetViewSet)
router.register(r'templatepresets', views.TemplatePresetViewSet)

router.register(r'memberships', views.MembershipViewSet)

# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(maps_router.urls)),
    url(r'^', include(organization_router.urls)),
    url(r'^', include(team_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
