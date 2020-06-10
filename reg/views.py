from django.shortcuts import redirect
from django.http import Http404
from .models import EventsModel, Post
from .forms import EventForm, UserForm, ProfileForm, PostForm,EventFormEdit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.models import User
from friendship.models import Friend
from django.shortcuts import render


def Privacy(request):
    return render(request, 'privacy.html')
def AboutUs(request):
    return render(request, 'about_us.html')
def FriendsList(request):
    friend_requests = Friend.objects.requests(request.user)

    return render(request, 'friends.html',{"friend_requests": friend_requests})


def AddFriend(request, username):
    other_user = User.objects.get(username=username)
    Friend.objects.add_friend(
        request.user,  # The sender
        other_user)  # This message is optional
    return redirect('/')
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    user.uzer.Visits += 1
    user.save()
    events = EventsModel.objects.filter(added_by=user.id)
    count = len(events)

    return render(request, 'user_profile.html', {"user": user, "events": events, "count": count})

@login_required
def createEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            messages.success(request, "thanks for making new Event")
            form.save()

            return redirect("/events")
    else:
        form = EventForm()

    return render(request, 'createEvent.html', {'form': form})
@login_required
def createPost(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            messages.success(request, "thanks for making new Post")
            form.save()

            return redirect("/my_content")
    else:
        form = PostForm()

    return render(request, 'createPost.html', {'form': form})


#Страница профиля
@login_required #ну это английский все знают
def Profile(request):
    events = EventsModel.objects.filter(added_by=request.user.id)
    posts = Post.objects.filter(added_by=request.user.id)
    return render(request, 'profile.html', context={'events': events,'posts':posts,})

@login_required
@transaction.atomic
def EditProfile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.uzer)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.uzer)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def EditEvent(request, id):
    if request.method == 'POST':
        event_form = EventsModel.objects.get(pk=id)
        event_form = EventFormEdit(request.POST, request.FILES, instance=event_form)
        if event_form.is_valid():
            event_form.save()

            return redirect('/my_content')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        event_form = EventsModel.objects.get(pk=id)
        event_form = EventFormEdit(instance=event_form)

    return render(request, 'edit_event.html', {
        'event_form': event_form,
    })

def index(request):
    return render(
         request,
        'index.html',)
def myContent(request):
    events = EventsModel.objects.filter(added_by=request.user.id)
    posts = Post.objects.filter(added_by=request.user.id)
    return render(request, 'mycontent.html', context={'events': events, 'posts': posts})

def Events(request):
    events = EventsModel.objects.order_by('-event_start')
    posts = Post.objects.order_by('-pub_date')
    return render(
        request,
        'events.html',
        context={'events': events,'posts':posts },
    )



def detailEvent(request, event_id):
    try:
        event_full = EventsModel.objects.get(pk=event_id)
    except EventsModel.DoesNotExist:
        raise Http404("page doest not exist")
    event_full.visits += 1
    event_full.save()
    return render(request, 'detailEvents.html', {'event_full': event_full})



def SearchResult(request):
    query = request.GET.get('q')
    error = ""
    events = EventsModel.objects.filter(Q(title__icontains=query))
    if not EventsModel.objects.filter(Q(title__icontains=query)):
        error = "<h1 style='color:white '>Извините ваш хакатон не найден</h1><br> <div style='font-size: 100px;color:white ' >~( ´•︵•` )~</div>"
    return render(
            request,
            'search_result.html',
            context={'events': events, 'error': error},
        )




