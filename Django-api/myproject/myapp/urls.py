from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from . import views


urlpatterns = [
    path('api_json',csrf_exempt(views.api_json)),
    path('api_create_meetings',csrf_exempt(views.api_create_meetings)),
    path('show_meetings',views.show_meetings,name="meetings"),
    path('',views.index,name="index")
]

