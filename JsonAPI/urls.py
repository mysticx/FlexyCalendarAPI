from django.conf.urls import patterns, include, url
from django.contrib import admin
from JsonAPI import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/event_period_type', views.EventPeriodType)

urlpatterns = patterns('',    
    url(r'^', include(router.urls)),
    url(r'^api/login', views.login),
    url(r'^api/is_logged', views.is_logged),     
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),    
)
