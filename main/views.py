from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
import csv
from django.http import HttpResponse

# Create your views here.
def all_users(request):
    users = User.objects.all()
    print(users)
    return render(request, 'list_users.html', {'users': users})

def new_user(request):
    form = UserForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_users)
    return render(request,'user_form.html', {'form' : form})

def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect(all_users)
    return render(request,'user_form.html', {'form' : form})

def delete_user(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        user.delete()
        return redirect(all_users)

    return render(request, 'confirm.html', {'user': user})


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    users = User.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Username','Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    for user in users:
        writer.writerow([user.username, user.birth_date, user.calculateAge(), user.random_number, user.BizzFuzz()])
    return response