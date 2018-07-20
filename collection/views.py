from django.template.loader import get_template 
from django.core.mail import EmailMessage
from collection.forms import ContactForm
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect

from collection.forms import ThingForm
from collection.models import Thing
from django.contrib.auth.decorators import login_required
from django.http import Http404

# the rewritten view!
def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })


def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })

@login_required
def edit_thing(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    if thing.user != request.user:
        raise Http404

    # set the form we're using...
    form_class = ThingForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=thing)

        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })
    
def create_thing(request):
	form_class = ThingForm
	if request.method == 'POST':
	    form = form_class(request.POST)
	    if form.is_valid():
		    thing = form.save(commit=False)
		    thing.user = request.user
		    thing.slug = slugify(thing.name)
		    thing.save()
		    return redirect('thing_detail', slug=thing.slug)
	else:
		form = form_class()

	return render(request, 'things/create_thing.html', {
        'form': form,
    })
    
def browse_by_name( request, initial = None):
    if initial:
        things = Thing.objects.filter(name__istartswith=initial)
        things = things.order_by('name')
    else:
        things = Thing.objects.all(). order_by('name')
	
    return render( request, 'search/search.html', {
        'things': things, 
        'initial': initial,
})


 # add to your views 
def contact(request): 
    form_class = ContactForm
    
    # new logic!
    if request.method == 'POST':
	    form = form_class(data=request.POST)
	    if form.is_valid():
		    contact_name = form.cleaned_data['contact_name'] 
		    contact_email = form.cleaned_data['contact_email'] 
		    form_content = form.cleaned_data['content']
		
		    # email the profile with the contact info 
		    template = get_template('contact_template.txt')

		    context = {
			    'contact_name': contact_name, 'contact_email': contact_email,
			    'form_content': form_content,
		    }
		    content = template.render(context)

		    email = EmailMessage(
			    'New contact form submission', content,
			    'Your website <hi@example.com>', ['john.pilbeam@sbs.ox.ac.uk'],
			    headers = {'Reply-To': contact_email }
		    )
		    email.send()
		    return redirect('contact')
 
    return render(request, 'contact.html', { 
        'form': form_class, 
    })