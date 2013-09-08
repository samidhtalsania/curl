# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from curl_app.forms import MainForm
from curl_app import main_logic
from curl_app.models import urls
from curl_app import reverse_logic


def hello(request):
	form = MainForm()
	return render(request,
		         'generate.html',
		         {'form':form})



def generate(request):
	form = MainForm(request.POST)
	if form.has_changed():
		if request.method == 'POST': # if form is submitted
			# form = MainForm(request.POST) # a form object bound to the POST data
			if form.is_valid():
				#success
				cdURL = form.cleaned_data['urlField']
				try:
					count = urls.objects.latest('id')
					count = count.id + 1
				except urls.DoesNotExist:
					count = 1
				
				cdURL_proc = main_logic.cropurl(count)
				print cdURL_proc
				print cdURL
				query_proc = urls(url=cdURL)
				query_proc.save()

				return render_to_response('success.html',
											{'result':cdURL_proc})
				# return render(request,
				# 		  'success.html',
				# 		  {'result':cdURL_proc})
			else:
				return render(request,
							'generate.html',
							{'form':form})
	else:
		form = MainForm()
		error = "Empty URL not allowed"
		return render(request,
					  'generate.html',
					  {'form':form,
					  'error':error})

		

def cropurl_redirect(request,offset):
	pid = reverse_logic.cropurl(offset)
	redirect_url = get_object_or_404(urls,id=pid)
	return HttpResponsePermanentRedirect(redirect_url.url)

