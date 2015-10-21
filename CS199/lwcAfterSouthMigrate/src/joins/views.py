from django.shortcuts import render

# Create your views here.
from .forms import EmailForm, JoinForm
from .models import Join
def home(request):
	#---------1st approach ---Using raw html form 

	#print request.POST["email"], request.POST["email_2"] 

	#------2nd approach---store data by using a general django form

	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print new_join, created
	# 	print new_join.timestamp
	# 	if created:
	# 		print "this obj was created" 


	#--------3rd approach---storing data by using model form
	form = JoinForm(request.POST or None)

	context = {"form": form}
	template = "home.html"
	return  render(request, template,context)
	if form.is_valid():
		new_join = form.save(commit=False)
		#we might do something here
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		new_join.save()

		
# def home(request):
# 	form = EmailForm()
# 	context = {"form": form}
# 	template = "home2.html"
# 	return  render(request, template,context)