# from django.urls import path
# from .views import AppUsersViewSet, ProjectsViewSet, TicketsViewSet

# urlpatterns = [
#     path('get-app-users/', AppUsersViewSet.as_view({'get': 'list_app_users'}), name='get_app_users'),
#     path('create-app-user/', AppUsersViewSet.as_view({'post': 'create_app_user'}), name='create_app_user'),
#     path('update-app-user/<int:pk>/', AppUsersViewSet.as_view({'put': 'update_app_user'}), name='update_app_user'),
#     path('destroy-app-user/<int:pk>/', AppUsersViewSet.as_view({'delete': 'destroy_app_user'}), name='destroy_app_user'),


#     path('get-projects/', ProjectsViewSet.as_view({'get': 'list_projects'}), name='get_projects'),
#     path('create-project/', ProjectsViewSet.as_view({'post': 'create_project'}), name='create_project'),
#     path('update-project/<int:pk>/', ProjectsViewSet.as_view({'put': 'update_project'}), name='update_project'),
#     path('destroy-project/<int:pk>/', ProjectsViewSet.as_view({'delete': 'destroy_project'}), name='destroy_project'),


#     path('get-tickets/', TicketsViewSet.as_view({'get': 'list_tickets'}), name='get_tickets'),
#     path('create-ticket/', TicketsViewSet.as_view({'post': 'create_ticket'}), name='create_ticket'),
#     path('update-ticket/<int:pk>/', TicketsViewSet.as_view({'put': 'update_ticket'}), name='update_ticket'),
#     path('destroy-ticket/<int:pk>/', TicketsViewSet.as_view({'delete': 'destroy_ticket'}), name='destroy_ticket'),
#     path('get-tickets-by-projectname/<str:projectName>/', TicketsViewSet.as_view({'get': 'get_tickets_by_project_name'})),

# ]
