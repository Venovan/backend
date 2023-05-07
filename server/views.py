from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import backend.settings as settings
from .models import Student, Meal, MessMenu, Event, Council
from .serializer import StudentSerializer, EventSerializer, CouncilSerializer

@api_view(['GET'])
def fetch_profile(request, roll):
      student = Student.objects.get(rollNumber = roll)
      profile = StudentSerializer(student)
      return Response(profile.data)

@api_view(['GET'])
def fetch_events(request):
      events = EventSerializer(Event.objects.all(), many =True)
      return Response(events.data)


@api_view(['GET'])
def fetch_council(request):
      council = CouncilSerializer(Council.objects.all(), many=True)
      return Response(council.data)























from django.contrib.auth import authenticate, login, logout


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        pass
    else:
        pass



def logout_view(request):
    logout(request)
    pass



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Admin(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(Admin, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

