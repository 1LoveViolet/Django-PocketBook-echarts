# accounting_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('entry_list/', views.entry_list, name='entry_list'),
    path('create/', views.create_list, name='create_entry'),
    path('echarts/', views.chart_view, name='chart_view'),
    path('update/<int:entry_id>/', views.update_list, name='update_entry'),
    path('delete/<int:entry_id>/', views.delete_list, name='delete_entry'),
]
