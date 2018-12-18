from django.shortcuts import render

from pprint import pprint

import numpy as np

# function based views
def home(request):
	# View what request offers
	#pprint(request.__dict__)
	template = 'home.html'
	context ={
		# "username": "Sunil",
		'title': 'Home Page',
		'data': {'santosh', 'ram', 'shyam'},
		'numpyData': np.zeros(5),
	}
	# render(request, template, context=should be dict)
	return render(request, template, context=context)

