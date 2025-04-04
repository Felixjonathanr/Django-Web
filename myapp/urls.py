from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path ('', views.index, name ='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('users',views.users,name="users")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)