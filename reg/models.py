from datetime import datetime
from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from crum import get_current_user
from django.db.models.signals import post_save
from django.dispatch import receiver

#дополнение для модели юзеров в бд

class Uzer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile/', default=" ")
    BirthDay = models.DateField(auto_now=False, null=True, blank=True)
    Info = models.CharField(max_length=300, help_text="Введите информацию о себе",default=" ")
    Visits = models.IntegerField(default=0)
    Friends = models.IntegerField(default=0)
    Rating = models.IntegerField(default=0)
    School = models.CharField(max_length=30, default=" ")
    Uni = models.CharField(max_length=30, default=" ")
    UniEnd = models.CharField(max_length=30, default=" ")
    Place = models.CharField(max_length=30,default=" ")
    Skills = TaggableManager()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Uzer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.uzer.save()
 
class Post(models.Model):
    Text = RichTextField(help_text="Введите полностью условия",default="") #TODO remove this awful plugin
    pub_date = models.DateField(default=datetime.now, blank=True)
    added_by = models.ForeignKey('auth.User', blank=True, null=True,
                                   default=None, on_delete=models.CASCADE,)
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.added_by = user
        super(Post, self).save(*args, **kwargs)
    #функция, которая возвращает название в админке
    def __str__(self):
        return self.Text


class EventsModel(models.Model):
    Filters = (
        ('online', 'онлайн'),
        ('offline', 'оффлайн'),
    )
    Filters2 = (
        ('hackathon', 'хакатон'),
        ('meet', 'митап'),
        ('breakfast', 'завтрак'),
        ('conference', 'конференция'),
        ('course', 'курсы'),
    )
    title = models.CharField(max_length=200, help_text="Введите название")
    small_description = models.TextField(max_length=200, help_text="Введите краткое описание")
    Text = models.TextField(help_text="Введите полностью условия",default="")
    event_start = models.DateField(default=datetime.now, blank=True)
    event_end = models.DateField(default=datetime.now, blank=True)
    added_by = models.ForeignKey('auth.User', blank=True, null=True,
                                   default=None,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='', default=" ")
    filter = models.CharField(max_length=20, choices=Filters, default='online')
    filter2 = models.CharField(max_length=20, choices=Filters2, default='hackathon')
    visits = models.IntegerField(default=0)
    tags = TaggableManager()
 #функция которая автоматически инициализирует юзера
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.added_by = user
        super(EventsModel, self).save(*args, **kwargs)
    #функция, которая возвращает название в админке
    def __str__(self):
        return self.title
