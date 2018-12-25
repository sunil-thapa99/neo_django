from django.shortcuts import render

from pprint import pprint
import numpy as np

from .models import Category

# function based views
def home(request):
	# View what request offers
	#pprint(request.__dict__)
	template = 'home.html'
	context ={
		# "username": "Sunil",
		'title': 'Home Page',
		'data': Category.objects.all(),
		# 'numpyData': np.zeros(5),
	}
	# render(request, template, context=should be dict)
	return render(request, template, context=context)

