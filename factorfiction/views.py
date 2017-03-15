from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from factorfiction.forms import PageForm, UserForm, UserProfileForm
from factorfiction.models import UserProfile, Page

def index(request):
	return render(request, 'factorfiction/index.html',)
	
def fofgame(request):
	return render(request, 'factorfiction/fofgame.html')

def about(request):
	return render(request, 'factorfiction/about.html')

def search(request):
	if request.method == 'POST':
	
		terms = request.POST.get('terms', None)
		postedBy = request.POST.get('postedBy', None)
		
		try:
			term_list = terms.split(' ')
			term_list.extend(postedBy)
	
			articles_list = Page.objects.all()
	
			q = Q(title__icontains=term_list[0]) | Q(postedBy__icontains=term_list[0])
	
			for term in term_list[1:]:
				q.add((Q(title__icontains=term) | Q(postedBy__icontains=term)), q.connector)
	
			articles_list = articles_list.filter(q)
			
			context_dict = {'articles': articles_list}
	
			return render(request, 'factorfiction/search.html', context_dict)
		except Page.DoesNotExist:
			return HttpResponse("No articles found.")
	else:
		return render(request, 'factorfiction/search.html')

@login_required
def submit_page(request):
	form = PageForm()
	
	if request.method == 'POST':
		form = PageForm(request.POST)
		#Is form valid?
		if form.is_valid():
			#Save new page to the database
			form.save(commit=True)
			#Now that the page is saved, return to homepage
			return index(request)
		else:
			print(form.errors)
	
	return render(request, 'factorfiction/submit_page.html', {'form': form})
	
def register(request):
	# True when registration succeeds.
	registered = False
	
	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()
			
			# Now we hash the password with the set_password method.

			user.set_password(user.password)
			user.save()
			
			# Since we need to set the user attribute ourselves,
			# we set commit=False. This delays saving the model
			# until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# get profile picture from the input form and
			#put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			
			# Now we save the UserProfile model instance.
			profile.save()

			# Update our variable to indicate that the template
			# registration was successful.
			registered = True
		else:
			# Invalid form or forms - mistakes or something else?
			# Print problems to the terminal.
			print(user_form.errors, profile_form.errors)
	else:
		# Not a HTTP POST, so we render our form using two ModelForm instances.
		# These forms will be blank, ready for user input.
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render(request,
				'factorfiction/register.html',
				{'user_form': user_form,
				'profile_form': profile_form,
				'registered': registered})

def user_login(request):
	# If the request is a HTTP POST, try to pull out the relevant information.

	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST.get('username')
		password = request.POST.get('password')
			
		# See if user/pass combo is valid
		user = authenticate(username=username, password=password)
			
		# If we have a User object, the details are correct.
		# If None no user with matching credentials was found.
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Rango account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	
	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render(request, 'rango/index.html', {})

def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)
	# Take the user back to the homepage.
	return HttpResponseRedirect(reverse('index'))




	