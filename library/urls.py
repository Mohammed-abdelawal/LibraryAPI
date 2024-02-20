from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library import views

router = DefaultRouter()
router.register('borrowers', views.BorrowerViewSet)
router.register('borrow-records', views.BorrowRecordViewSet)

urlpatterns = [
    path('', include(router.urls))
]