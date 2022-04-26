from django.urls import path
from .views import DocumentList, DocumentDetails


urlpatterns = [
    path('document/', DocumentList.as_view(), name='document-list'),
    path('document/<int:pk>/', DocumentDetails.as_view(), name='document-details'),
]