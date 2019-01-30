from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.bank_list, name='bank_list'),
    re_path(r'^bank/(?P<pk>\d+)/$', views.bank_detail, name='bank_detail'),
]