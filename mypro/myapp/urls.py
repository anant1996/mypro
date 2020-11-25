from rest_framework import routers
from django.urls import path, include
from .views import  Product_Vw, Category_Vw
from django.conf.urls import url
 

router = routers.DefaultRouter()
router.register('product', Product_Vw)
router.register('category', Category_Vw)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    # url(r'^api/test/', Test),
]