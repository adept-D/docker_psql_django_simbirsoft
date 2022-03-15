import email
from django.shortcuts import redirect, render

from .models import Note
from .forms import NoteForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

def index(request):
    return render(request, 'index.html')


def home(request):
    # print(request.user == 'AnonymousUser')
    if request.user.is_authenticated:
        notes_count = Note.objects.filter(user=request.user).count()
        return render(request, 'home.html', {"notes_count":notes_count})
    else:
        return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()

    return render(request, 'user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        
        print(request.POST)
        if form.is_valid():
            # form.save()
            Note.objects.create(content=request.POST['content'], user=request.user)
            # return render(request, 'add_note.html')
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form':form})

def get_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'notes':notes})

from django.views import generic

class NoteListView(generic.ListView):
    model = Note
    paginate_by = 10