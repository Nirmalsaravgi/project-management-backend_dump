# from rest_framework import serializers
# from .models import appUsers, projects, tickets

# # Serializer for appUsers model
# class AppUsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = appUsers
#         fields = ['id', 'emailId', 'fullName', 'password', 'created_at', 'updated_at']

# # Serializer for projects model
# class ProjectsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = projects
#         fields = ['id', 'projectName', 'shortName', 'created_at', 'updated_at']

# # Serializer for tickets model
# class TicketsSerializer(serializers.ModelSerializer):
#     assignedTo = serializers.CharField(source= 'assignedTo.fullName', required = False)  
#     projectShortName = serializers.CharField(source= 'projectShortName.shortName', required = False)  

#     class Meta:
#         model = tickets
#         fields = ['id', 'summary', 'storyPoint', 'status', 'assignedTo', 'projectShortName', 'created_at', 'updated_at']

#     def create(self, validated_data):
#         # Extract nested data (fullName and shortName)
#         assigned_to_name = validated_data.pop('assignedTo', {}).get('fullName', None)
#         project_short_name = validated_data.pop('projectShortName', {}).get('shortName', None)

#         # Fetch related appUsers instance based on fullName
#         assigned_to_user = None
#         if assigned_to_name:
#             assigned_to_user = appUsers.objects.filter(fullName=assigned_to_name).first()
#             if not assigned_to_user:
#                 raise serializers.ValidationError(f"User with full name '{assigned_to_name}' does not exist.")

#         # Fetch related projects instance based on shortName
#         project_instance = None
#         if project_short_name:
#             project_instance = projects.objects.filter(shortName=project_short_name).first()
#             if not project_instance:
#                 raise serializers.ValidationError(f"Project with short name '{project_short_name}' does not exist.")

#         # Create the ticket with the associated user and project
#         ticket = tickets.objects.create(
#             summary=validated_data.get('summary', ''),
#             storyPoint=validated_data.get('storyPoint', 0),
#             status=validated_data.get('status', ''),
#             assignedTo=assigned_to_user,
#             projectShortName=project_instance
#         )

#         return ticket