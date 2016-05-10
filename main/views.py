from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Area, Developer, Language
from django.http import HttpResponseRedirect

def hello_world(request):
	#dev1 = Developer(name="Juan Ramos", years=5, area="Backend")
	#dev2 = Developer(name="Pepito", years=4, area="Frontend")
	#developers = [ dev1, dev2 ]
	#dev1.save()
	#dev2.save()
	developers = Developer.objects()
	template = loader.get_template('index.html')
	context = {
		'developers': developers
	}

	return HttpResponse(template.render(context, request))

def developer(request, name):
	name=name.replace("_", " ")
	developer = Developer.objects(name=name).first()

	if request.method == 'POST':
		new_language = Language(name=request.POST['name'])
		developer.languages.append(new_language)
		developer.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/')) 

	template = loader.get_template('developer.html')
	context = {
		'developer': developer
	}

	return HttpResponse(template.render(context, request))

def new_developer(request):
	if request.method == 'POST':
		new_developer = Developer(name=request.POST['name'], years=request.POST['years'], area=request.POST['area'])
		new_developer.save()
		return HttpResponseRedirect('/')

	areas = Area.objects()
	template = loader.get_template('register.html')
	context = {
		'areas': areas
	}

	return HttpResponse(template.render(context, request))	
