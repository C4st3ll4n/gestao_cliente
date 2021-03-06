from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, my_logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
