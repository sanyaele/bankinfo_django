

# from django.conf.urls import re_path, include
from django.urls import include, path, re_path
from rest_framework import routers
from . import views
# from banksinfo.api import views

router = routers.DefaultRouter()
router.register(r'banks', views.BankViewSet)
# router.register(r'banks/<str:bank>/', views.SearchBankViewSet)
router.register(r'bankbranches', views.BankBranchViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('bank/<bank_name>/', views.SearchBankView, name='bank_name'),
    path('hi', views.sayHi ),
    # # ex: /banks/5/website/
    # path('banks/<int:bank_id>/website/', views.website, name='website'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]