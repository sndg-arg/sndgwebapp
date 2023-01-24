from django.urls import path
from .views.MainPage import main_page
#from .views.TestCelery import test_celery

from sndgwebapp.views.UserViews import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from .admin import *


app_name = "sndgwebapp"
urlpatterns = [
    #path("~redirect/", view=user_redirect_view, name="redirect"),
    #path("~update/", view=user_update_view, name="update"),
    #path("<str:username>/", view=user_detail_view, name="detail"),
    #path("test_celery/", view=test_celery, name="test_celery"),
    path("",view=main_page)
]