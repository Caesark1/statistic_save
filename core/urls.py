from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as docs


v1_api = ([
    path('statistic/', include('apps.main.urls'))
], 'v1')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_api, namespace='v1'))
]

urlpatterns += docs
