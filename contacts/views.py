from django.shortcuts import render

def index(request):
    context = {'message': 'this is the index page'}
    return render(request, 'contacts/index.html', context=context)
