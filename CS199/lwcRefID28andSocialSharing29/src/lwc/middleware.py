from joins.models import Join
class ReferMiddleware():
	def process_request(self, request):
		#print request
		# try:
		# 	ref_id = request.GET.get("ref", "")
		# except:
		# 	ref_id = False
		ref_id = request.GET.get("ref")
		try:
			obj = Join.objects.get(ref_id=ref_id)
		except:
			obj = None
		if obj:
			request.session['rf']=obj.id