
from .models import EventsModel, Uzer, Post
from django.contrib.auth.models import User

from django.forms import ModelForm, Textarea

#Форма создания хактонов
class EventForm(ModelForm):
    class Meta:
        model = EventsModel
        fields = ['title', 'small_description', 'Text', 'event_start', 'event_end', 'image', 'filter', 'filter2', 'tags']
        widgets = {
            'small_description': Textarea(attrs={'cols': 40, 'rows': 3}),
            'Text': Textarea(attrs={'cols': 40, 'rows': 7}),
        }
class EventFormEdit(ModelForm):
    class Meta:
        model = EventsModel
        fields = ['title', 'small_description', 'Text', 'event_start', 'event_end', 'image', 'filter', 'filter2', 'tags']
        widgets = {
            'small_description': Textarea(attrs={'cols': 40, 'rows': 3}),
        }
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['Text']
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
#Форма доп. информации о пользователе
class ProfileForm(ModelForm):
       class Meta:
        model = Uzer
        fields = ('avatar', 'BirthDay', 'Info', 'School', 'Uni', 'UniEnd', 'Place', 'Skills')
