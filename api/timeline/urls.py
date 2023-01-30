from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.authn.urls')),
    path('api/', include('apps.user.urls')),
    path('api/', include('apps.project.urls')),
    path('api/', include('apps.schedule.urls')),
]
