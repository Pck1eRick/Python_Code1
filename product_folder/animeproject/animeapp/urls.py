from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name='animeapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('anime/<int:anime_id>/',views.detail,name='detail'),
    path('add/',views.add_anime,name='add_anime'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    ]

if settings.DEBUG:
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)