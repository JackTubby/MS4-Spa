from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treatments, name='treatments'),
    path('<int:treatment_id>/', views.treatment_detail, name='treatment_detail'),
    path('add/', views.add_treatment, name='add_treatment'),
    path('edit/<int:treatment_id>/', views.edit_treatment, name='edit_treatment'),
    path('delete/<int:treatment_id>/', views.delete_treatment, name='delete_treatment'),
    path('add_rating/<int:treatment_id>/', views.add_rating, name='add_rating'),
    path('refund_policy/', views.refund_policy, name='refund_policy'),
]
