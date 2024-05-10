from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('showroom',views.ShowRoom_ViewSet, basename='showroom')

urlpatterns = [
    path("cars/",views.car_list_view, name="car-list-view"),
    path("cars/<int:pk>/",views.car_detail_view, name="car-detail-view"),
    path('', include(router.urls)),
    # path('showroom/',views.ShowroomList.as_view(), name="showroom-list-view"),
    # path('showroom/<int:pk>/',views.ShowroomDetail.as_view(), name='showroom-detail-view'),
    # path('review/', views.ListCreateView.as_view(), name='review-list'),
    # path('review/<int:pk>/', views.RetrieveUpdateDestroyView.as_view(), name='review-retrieve')
    path('showroom/<int:pk>/review_create/',views.ReviewCreate.as_view(), name='review_create'),
    path('showroom/<int:pk>/review/',views.ReviewList.as_view(), name='review_list'),
    path('showroom/review/<int:pk>/',views.RetrieveUpdateDestroyView.as_view(), name='review_detail'),
]
