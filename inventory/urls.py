from django.urls import path
from . import views



urlpatterns = [
    path("",views.home,name="home-page"),
    path("contact/",views.contact , name="contact-page"),
    path("order/",views.order,name="order-page"),
    path("about/",views.about,name="about-page"),
    path("order_success/",views.order_success,name="order-success")
]
