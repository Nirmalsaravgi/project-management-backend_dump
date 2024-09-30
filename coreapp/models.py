from django.db import models

# Create your models here.

# class base(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class appUsers(base):
#     emailId = models.EmailField(max_length=500, null=True, blank=True)
#     fullName = models.CharField(max_length=500, null=True, blank=True)
#     password = models.CharField(max_length=500, null=True, blank=True)

#     def __str__(self):
#         return self.fullName or "UnNamed"


# class projects(base):
#     projectName = models.CharField(max_length=500, null=True, blank=True)
#     shortName = models.CharField(max_length=256, null=True, blank=True)

#     def __str__(self):
#         return self.shortName or "UnNamed"
    

# class tickets(base):
#     summary = models.TextField(null=True, blank=True)
#     storyPoint = models.IntegerField(default=0)
#     mission_status = (
#         ('Td', 'To Do'),
#         ('Ip', 'In Progress'),
#         ('C', 'Completed'),
#     )
#     status = models.CharField(max_length=256, choices=mission_status)
#     assignedTo = models.ForeignKey(appUsers, null=True, blank=True, on_delete=models.CASCADE)
#     projectShortName = models.ForeignKey(projects, null=True, blank=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.status or "UnNamed"