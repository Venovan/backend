from django import forms
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def image_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["photos", '{}.{}'.format(instance.rollNumber, ext)])

def council_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["council", '{}.{}'.format(instance.por, ext)])


def post_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["posts", '{}.{}'.format(instance.title, ext)])

def menu_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["pdf", '{}.{}'.format("menu", ext)])

def constitution_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["pdf", '{}.{}'.format("constitution", ext)])


def cult_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["inventory/cult", '{}.{}'.format(instance.name, ext)])


def sport_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["inventory/sport", '{}.{}'.format(instance.name, ext)])


def tech_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["inventory/tech", '{}.{}'.format(instance.name, ext)])


def complaint_handler(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["complaints", '{}.{}'.format(instance.title, ext)])


def otherimages(instance, filename):
    ext = filename.split('.')[-1]
    return "/".join(["images", '{}.{}'.format(instance.title, ext)])


TECH_INVENTORY = [("E", "Electrical"), ("M", "Mechanical")]


MEAL_CHOICES = [('B', 'Breakfast'),
                ('L', 'Lunch'),
                ('S', 'Snacks'),
                ('D', 'Dinner')]


STATUS = [('A', "Allowed"),
          ('NA', "Not Allowed")]

COMPLAINT_CATEGORY = [("mess", "Mess"), ("maint", "Maintanence")]


def image_name_validation(filename):
    print(len(filename.split(" ")))
    if len(filename.split(" "))> 1:
        print("entry")
        raise ValidationError(
            ("%(filename)s must not contain spaces!"),
            params={"filename": filename},
        )


class User(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit: True):
        user = super(Student, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    rollNumber = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=20)
    roomNumber = models.CharField(max_length=3)
    photo = models.ImageField(upload_to=image_handler, default='default.jpg')
    RFID = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['roomNumber']

    def __str__(self):
        return self.name



class Council(models.Model):
    por = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mobile =  models.CharField(max_length=15)
    image = models.ImageField(upload_to=council_handler, default='default.jpg')

    def __str__(self):
        return self.por


class Event(models.Model):
    title = models.CharField(max_length=20, blank=False)
    post = models.ImageField(upload_to=post_handler)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=500)
    likes = models.IntegerField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-date']


class MessMenu(models.Model):
    file = models.FileField(upload_to=menu_handler)
    start = models.DateField(auto_now=False, default=now)

    def __str__(self):
        return str(self.start.day) + str(self.start.strftime('%b'))

    class Meta:
        ordering = ["start"]


class HostelConstitution(models.Model):
    file = models.FileField(upload_to=constitution_handler)
    amended = models.DateField(auto_now=False, default=now)
    def __str__(self):
        return "Constitution"


class CultInventory(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField()
    image = models.ImageField(upload_to=cult_handler)


class SportInventory(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField()
    image = models.ImageField(upload_to=sport_handler)
    

class TechInventory(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField()
    image = models.ImageField(upload_to=tech_handler)
    type = models.CharField(max_length=20, choices=TECH_INVENTORY, default='E')


class Meal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=MEAL_CHOICES)
    weight = models.CharField(max_length=6, blank=True, null=True)
    date = models.DateField()

    class Meta:
        ordering = ["-date", "student__rollNumber"]

    def __str__(self):
        if self.weight != None:
            return self.student.rollNumber + "/" + str(self.date) + "/" + self.type + "/" + self.weight
        else:
            return self.student.rollNumber + "/" + str(self.date) + "/" + self.type + "/"


class Complaint(models.Model):
    title = models.CharField(max_length=20)
    type = models.CharField(max_length = 20, choices=COMPLAINT_CATEGORY, default="maint")
    date = models.DateField(auto_now_add=now)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=complaint_handler)
    details = models.TextField(blank=False, default="default.jpg")


class OtherImages(models.Model):
    title = models.CharField(max_length=20, validators=[image_name_validation])
    image = models.ImageField(upload_to=otherimages)
    
    def __str__(self):
        return self.title



