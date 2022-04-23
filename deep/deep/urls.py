from django.contrib import admin
from django.urls import path,include

# MEDIA
from django.conf import settings
from django.conf.urls.static import static
statics = static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# //MEDIA

# VIEW 
from deep_app.views import *
# //VIEW 

# Rest Framework
from rest_framework import routers
router = routers.DefaultRouter()
router.register("",ProductMaster,basename='productmaster')
# //Rest Framework


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]+statics
