from .views import TestView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/user/', include('userAPI.urls'))
]
urlpatterns = [
    path('test', TestView.as_view()),
]

# localhost:8000/api/v1.0/user/test
