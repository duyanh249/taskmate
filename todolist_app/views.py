from django.core import paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context={'welcome_message':'Welcome to Home Page'}
    return render(request,'index.html',context)
@login_required
def todolist(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request,('New Task Added'))
        return redirect('todolist')
    else:
        task_list=TaskList.objects.filter(manage=request.user)
        
        paginator=Paginator(task_list,5)
        page=request.GET.get('pg')
        task_list=paginator.get_page(page)
        context={'welcome_message':'Welcome to ToDo List',
                'task_list':task_list
                }
        return render(request,'todolist.html',context)
@login_required
def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.delete()
    else:
        messages.error(request,('You are restricted'))
        return redirect('todolist')
@login_required
def edit_task(request,task_id):
    if request.method=="POST":
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('Task Editted'))
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)
        context={
                    'task_obj':task_obj
                }
        return render(request,'edit.html',context)
@login_required
def mark_completed(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,('You are restricted'))
    
    
    return redirect('todolist')
@login_required
def mark_pending(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,('You are restricted'))
    return redirect('todolist')        
def about(request):
    context={'welcome_message':'Welcome to About Us'}
    return render(request,'about.html',context)
def contact(request):
    context={'welcome_message':'Welcome to Contact Us'}
    return render(request,'contact.html',context)