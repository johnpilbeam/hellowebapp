from django.shortcuts import render

# Create your views here.
def index(request): 
    # this is your new view
    # return render(request, 'index.html')
    # defining the variable 
    number = 6 
    thing = "Thing name"
    # passing the variable to the view 
    return render(request, 'index.html', { 
        'number': number, 
        'thing': thing,
    })