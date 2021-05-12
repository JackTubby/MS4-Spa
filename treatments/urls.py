from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treatments, name='treatments'),
    path('<treatment_id>', views.treatment_detail, name='treatment_detail'),
]