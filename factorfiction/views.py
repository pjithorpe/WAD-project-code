from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from factorfiction.forms import PageForm, UserForm, UserProfileForm, CommentForm, UpdateProfile
from factorfiction.models import UserProfile, Page, UserVotes, Comment
from django.template import RequestContext
from goose import Goose
import urllib
import os

def can_user_vote(thisUser, thisPage):
	# Check to see if the user has already voted on the page.
	# If yes, return false; if not, return true.
	if thisUser.is_authenticated:
			
		if UserVotes.objects.filter(user=thisUser, page=thisPage).exists():
			# If user has already voted on this article
			return False
			
		return True
		
	else:
	
		return False

def show_page(request, page_name_slug):
	# Create a context dictionary which we can pass
	# to the template rendering engine.

	context_dict = {}
	context_dict['can_vote'] = False
	try:
		# Can we find a page name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		currentPage = Page.objects.get(slug=page_name_slug)
		context_dict['page'] = currentPage
		
		currentUser = request.user
		context_dict['can_vote'] = can_user_vote(currentUser, currentPage)
		
		
	except Page.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't	 do anything -
		# the template will display the "no category" message for us.

		context_dict['page'] = None

	return render(request, 'factorfiction/page.html', context_dict)
	
def vote_fact(request):
	context = RequestContext(request)
	page_id = None
	currentUser = request.user
	
	if request.method == 'GET':
		page_id = request.GET['page_id']
		
	facts = 0
	if page_id:
		page = Page.objects.get(id=int(page_id))
		if page:
			facts = page.facts + 1
			page.facts = facts
			page.save()
			
			userVote = UserVotes.objects.create(user=currentUser, page=page)
			userVote.save()
	
	return HttpResponse(facts)
	
def vote_fiction(request):
	context = RequestContext(request)
	page_id = None
	currentUser = request.user
	
	if request.method == 'GET':
		page_id = request.GET['page_id']
		
	fictions = 0
	if page_id:
		page = Page.objects.get(id=int(page_id))
		if page:
			fictions = page.fictions + 1
			page.fictions = fictions
			page.save()
			
			userVote = UserVotes.objects.create(user=currentUser, page=page)
			userVote.save()
	
	return HttpResponse(fictions)

def index(request):
	page_list = Page.objects.order_by('-created_date')[:10]
	context_dict = {'pages': page_list}
	return render(request, 'factorfiction/index.html', context_dict)

def fofgame(request):
	return render(request, 'factorfiction/fofgame.html')
	
def about(request):
	return render(request, 'factorfiction/about.html')

def my_profile(request):	
	currentUser = request.user
	username = currentUser.username
	
	if currentUser.is_authenticated:
		try:
			articles_list = Page.objects.filter(postedBy=username)
			
			userprofile = UserProfile.objects.get_or_create(user=currentUser)[0]
			context_dict = {'articles': articles_list, 'userprofile': userprofile}

			return render(request, 'factorfiction/my_profile.html', context_dict)
		except Page.DoesNotExist:
			return HttpResponse("No articles found.")
	
	return render(request, 'factorfiction/my_profile.html')
	
def update_profile(request):
	if request.method == 'POST':
		form = UpdateProfile(request.POST, instance=request.userprofile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('my_profile'))
	else:
		form = UpdateProfile()

	return render(request, 'factorfiction/update_profile.html', {'update_profile_form': form})

def search(request):
	if request.method == 'POST':
	
		terms = request.POST.get('terms', None)
		postedByTerm = request.POST.get('postedBy', None)
		
		try:
			term_list = terms.split(' ')
	
			articles_list = Page.objects.all()
	
			q = (Q(title__icontains=term_list[0]) | Q(postedBy=postedByTerm))
	
			for term in term_list[1:]:
				q.add(Q(title__icontains=term), q.connector)
	
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
			page = form.save(commit=False)

			g = Goose()
			article = g.extract(url=page.url)
			try:
				urllib.urlretrieve(article.top_image.src, os.path.join("static/images/article_pics", article.title.replace(" ", "")) + ".jpg")
				page.articleImage = "images/article_pics/" +article.title.replace(" ", "") + ".jpg"
			except:
				pass
			page.postedBy = request.user
			page.title = article.title
			page.content = article.cleaned_text[:3000]
			page.save()

			#Now that the page is saved, return to homepage
			return index(request)
		else:
			print(form.errors)
	
	return render(request, 'factorfiction/submit_page.html', {'form': form})
	
@login_required
def add_comment(request, pk):
	page = get_object_or_404(Page, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.postedBy = request.user
			comment.page = page
			comment.save()
			
			return redirect('/factorfiction/page/' + page.slug + '/')
		else:
			form = CommentForm()
			print(form.errors)
	return redirect('/factorfiction/page/' + page.slug + '/')


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
			return HttpResponse("Invalid login details supplied." + " <br /> <a href='/factorfiction/' %}'>Try again?</a>")
	
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




	