from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('demo1/',views.demo1,name='demo1'),
    # path('demo2/',views.demo2,name='demo2'),
    # path('operation/',views.operation,name='operation')
]