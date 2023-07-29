from django.urls import path
# from app1 import views
from .views import employeeListView, userListView,employeeDetailView
from app1 import views_decorator
# from .views_decorator import employeeListView, userListView,employeeDetailView

urlpatterns = [
    path('',views_decorator.home_page,name='index'),
    path('employee/',employeeListView),
    path('employee/<int:pk>',employeeDetailView),
    path('users/',userListView),
]