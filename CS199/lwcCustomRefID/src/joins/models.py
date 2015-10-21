from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField(unique=True)
	ref_id = models.CharField(max_length=120, default='ABC',unique=True)
	#default ABC instead of "null = True, blank = True" TO avoid confusion
	ip_address = models.CharField(max_length=120,default="ABC")
	timestamp = models.DateTimeField(auto_now_add = True,auto_now =False)
	updated = models.DateTimeField(auto_now_add = False,auto_now = True)

	def __unicode__(self):
			return "%s"%(self.email)

	class Meta:
		unique_together = ("email","ref_id")