from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Choice

def hello_world(request):
	choice1 = Choice(choice_text="I'm a f*cking choice !", votes=20)
	choice2 = Choice(choice_text="So so, we are dummy data", votes=25)
	choices = [ choice1, choice2 ]
	template = loader.get_template('index.html')
	context = {
		'choices': choices
	}

	return HttpResponse(template.render(context, request))
