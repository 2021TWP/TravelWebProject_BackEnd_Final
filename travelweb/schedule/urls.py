from django.urls import path

# from travel import views
# from  import views
from schedule import views
urlpatterns = [
    path('', views.schedule_list, name="schedule_list"),
    path('<int:pk>/', views.schedule_detail, name="schedule_detail"),
    path('create/', views.schedule_create, name="schedule_create"),
    path('update/<int:pk>/', views.schedule_update, name="schedule_update"),
    path('delete/<int:pk>/', views.schedule_delete, name="schedule_delete"),

    path('content/', views.schedule_content_list, name="schedule_content_list"),
    path('content/create/', views.schedule_content_create, name="schedule_content_create"),
    path('content/update/<int:pk>/', views.schedule_content_update, name="schedule_content_update"),
    path('content/<int:pk>/', views.schedule_content_detail, name="schedule_content_detail"),
    path('content/delete/<int:pk>/', views.schedule_content_delete, name="schedule_content_delete"),
]

