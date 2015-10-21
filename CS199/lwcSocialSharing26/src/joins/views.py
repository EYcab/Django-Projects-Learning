
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect

from .forms import EmailForm, JoinForm
from .models import Join
#Server hierachy:
#User address goes first
#Remote default comes last
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip	

#str(user_id)[:11].replace('-', '').lower()
import uuid

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	#ref_id = 'dd40b8ab59'
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		#print "run getting the id"
		get_ref_id()
	except:
		return ref_id

def share(request, ref_id):	
	print ref_id
	context = {"ref_id": ref_id}
	template = "share.html"
	return  render(request, template,context)

def home(request):
	print request.META.get("REMOTE_ADDR")
	print request.META.get("HTTP_X_FORWARDED_FOR")

	#--------3rd approach---storing data by using model form
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		#we might do something here
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		#redirect here
		return HttpResponseRedirect("/%s"%new_join_old.ref_id)
	context = {"form": form}
	template = "home.html"
	return  render(request, template,context)
		
# def home(request):
# 	form = EmailForm()
	# context = {"for m": form}
	# template = "home2.html"
	# return  render(request, template,context)