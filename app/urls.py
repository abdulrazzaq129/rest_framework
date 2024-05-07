from django.urls import path
from . import views

urlpatterns = [
    path("cars/",views.car_list_view, name="car-list-view"),
    path("cars/<int:pk>/",views.car_detail_view, name="car-detail-view"),
    path('showroom/',views.ShowroomList.as_view(), name="showroom-list-view"),
    path('showroom/<int:pk>/',views.ShowroomDetail.as_view(), name='showroom-detail-view'),
]
