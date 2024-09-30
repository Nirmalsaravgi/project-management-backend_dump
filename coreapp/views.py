# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
# from .models import appUsers, projects, tickets
# from .serializers import AppUsersSerializer, ProjectsSerializer, TicketsSerializer

# import logging
# logger = logging.getLogger(__name__)

# class AppUsersViewSet(viewsets.ViewSet):
#     # Retrieve all appUsers
#     def list_app_users(self, request):
#         queryset = appUsers.objects.all().order_by('id')
#         serializer = AppUsersSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # Create a new appUser
#     def create_app_user(self, request):
#         serializer = AppUsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Update an appUser
#     def update_app_user(self, request, pk=None):
#         try:
#             user_obj = appUsers.objects.get(pk=pk)
#         except appUsers.DoesNotExist:
#             raise NotFound("User not found")

#         serializer = AppUsersSerializer(user_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete an appUser
#     def destroy_app_user(self, request, pk=None):
#         try:
#             user_obj = appUsers.objects.get(pk=pk)
#         except appUsers.DoesNotExist:
#             raise NotFound("User not found")

#         user_obj.delete()
#         return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

# class ProjectsViewSet(viewsets.ViewSet):
#     # Retrieve all projects
#     def list_projects(self, request):
#         queryset = projects.objects.all().order_by('id')
#         serializer = ProjectsSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # Create a new project
#     def create_project(self, request):
#         serializer = ProjectsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Project created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Update a project
#     def update_project(self, request, pk=None):
#         try:
#             project_obj = projects.objects.get(pk=pk)
#         except projects.DoesNotExist:
#             raise NotFound("Project not found")

#         serializer = ProjectsSerializer(project_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Project updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete a project
#     def destroy_project(self, request, pk=None):
#         try:
#             project_obj = projects.objects.get(pk=pk)
#         except projects.DoesNotExist:
#             raise NotFound("Project not found")

#         project_obj.delete()
#         return Response({"message": "Project deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

# class TicketsViewSet(viewsets.ViewSet):
#     # Retrieve all tickets
#     def list_tickets(self, request):
#         queryset = tickets.objects.all().order_by('id')
#         serializer = TicketsSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def get_tickets_by_project_name(self, request, projectName=None):
#         try:
#             # Get the project object by projectName
#             project = projects.objects.filter(projectName=projectName).first()
            
#             if project:
#                 # Filter tickets by the related project
#                 filtered_tickets = tickets.objects.filter(projectShortName=project)
                
#                 # Serialize the filtered tickets
#                 serializer = TicketsSerializer(filtered_tickets, many=True)
                
#                 return Response({"message": "Tickets retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         except Exception as e:
#             # Return an error response if something goes wrong
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     # Create a new ticket
#     # def create_ticket(self, request):
#     #     serializer = TicketsSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({"message": "Ticket created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
#     #     print("Validation Errors:", serializer.errors)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def create_ticket(self, request):
#         serializer = TicketsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Ticket created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
#         # Log the errors using Django's logging system
#         logger.error("Validation Errors: %s", serializer.errors)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Update a ticket
#     def update_ticket(self, request, pk=None):
#         try:
#             ticket_obj = tickets.objects.get(pk=pk)
#         except tickets.DoesNotExist:
#             raise NotFound("Ticket not found")

#         serializer = TicketsSerializer(ticket_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Ticket updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete a ticket
#     def destroy_ticket(self, request, pk=None):
#         try:
#             ticket_obj = tickets.objects.get(pk=pk)
#         except tickets.DoesNotExist:
#             raise NotFound("Ticket not found")

#         ticket_obj.delete()
#         return Response({"message": "Ticket deleted successfully"}, status=status.HTTP_204_NO_CONTENT)