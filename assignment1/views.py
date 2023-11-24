from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from users.models import User
from projects.models import Project
from .models import Assignment

@login_required
def assign_project(request):
   # ee = ['abhi@gmail.com','dsn@sfl.com']
   # User.objects.filter(email__in=ee).delete()
   if str(request.user) != 'admin@example.com':
        return HttpResponse("<h1>You are not authorized to access this page</h1>", status=403)
   all_projects = Project.objects.all()
   # return HttpResponse('hello')
   con = {}
   for project in all_projects:
      title = project.title
      try:
        email = Assignment.objects.get(project_id=project.id).assigned_to
      except:
         email = 'None'
      con[str(project.id)] = [title,email]
      # project.created_by = request.user
      # project.save()
   print(con)
   
   return render(request,"test.html",{'con': con})

@login_required
def show_user(request,pk):
    if str(request.user) != 'admin@example.com':
        return HttpResponse("<h1>You are not authorized to access this page</h1>", status=403)
    all_users = User.objects.all()
    if request.method == 'POST':
      # Assignment.objects.all().delete()
       assigned_to = request.POST['user']
       project_id = pk
       try:
            assignment = Assignment.objects.get(project_id=project_id)
            assignment.assigned_to = assigned_to
       except Assignment.DoesNotExist:
            assignment = Assignment(project_id=project_id, assigned_to=assigned_to)

       assignment.save()


       all_projects = Project.objects.all()
       con = {}
       for project in all_projects:
         title = project.title
         try:
           email = Assignment.objects.get(project_id=project.id).assigned_to
         except:
            email = 'None'
         con[str(project.id)] = [title,email]
   
       return render(request,"test.html",{'con': con})

    return render(request,"users.html",{"all_users":all_users,"pk":pk})

