from django.conf.urls import url
from . import views
urlpatterns=[
url(r'^$',views.get,name="get"),
url(r'^uname',views.disp,name="disp")




]