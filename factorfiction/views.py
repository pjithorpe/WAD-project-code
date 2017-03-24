from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from factorfiction.forms import PageForm, UserForm, UserProfileForm, CommentForm, UpdateProfile
from factorfiction.models import UserProfile, Page, UserVotes, Comment, User
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

#Allows users to look at other user's profiles
#Users can only edit their own profile
def show_user_page(request, username):
	context_dict = {}
	try:
		user = User.objects.get(username=username)
		
		#Go to your own profile if you have click on your own name
		if request.user.username == user.username:
			return redirect("my_profile")

		context_dict['user'] = user
		articles_list = Page.objects.filter(postedBy=username)
		userprofile = UserProfile.objects.get_or_create(user=user)[0]
		context_dict = {'articles': articles_list, 'userprofile': userprofile, 'user' : user}

	except Page.DoesNotExist:
		context_dict['page'] = None

	return render(request, 'factorfiction/my_profile.html', context_dict)


#View to show the individual page for each article
#Displays title with link to url of story, description, voting buttons, comments
def show_page(request, page_name_slug):
	context_dict = {}
	
	#Keeps a track of whether the user has already voted on this article
	context_dict['can_vote'] = False
	try:
		currentPage = Page.objects.filter(slug=page_name_slug)
		if currentPage.count() > 1:
			currentPage = currentPage[0]
		else:
			currentPage = Page.objects.get(slug=page_name_slug)
		context_dict['page'] = currentPage
		currentUser = request.user
		context_dict['can_vote'] = can_user_vote(currentUser, currentPage)
		currentPage.views += 1
		currentPage.save()
		
	except Page.DoesNotExist:
		context_dict['page'] = None

	return render(request, 'factorfiction/page.html', context_dict)
	
#Allows users to vote fact on articles and increases the vote count in the database
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
	
#Allows users to vote fiction on articles and increases the vote count in the database
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

#View for index which passes up to 10 articles to be displayed on the main page
def index(request):
	page_list = Page.objects.order_by('-created_date')[:10]
	context_dict = {'pages': page_list}
	return render(request, 'factorfiction/index.html', context_dict)

def fofgame(request):
	return render(request, 'factorfiction/fofgame.html')
	
def about(request):
	return render(request, 'factorfiction/about.html')

#Stanard view for my profile view
#Includes all profile information along with the posts the user has added
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

#Users can search for articles by username of the person who posted or by terms in the title
#Results including either of these will be displayed to user
def search(request):
	if request.method == 'POST':
	
		terms = request.POST.get('terms', None)
		postedByTerm = request.POST.get('postedBy', None)
		
		try:
			term_list = terms.split(' ')
	
			articles_list = Page.objects.all()
	
			q = Q(title__icontains=term_list[0])
	
			for term in term_list[1:]:
				q.add(Q(title__icontains=term), q.connector)
			
			q.add(Q(postedBy__icontains=postedByTerm), q.connector)
			
			articles_list = articles_list.filter(q)
			
			context_dict = {'articles': articles_list}
	
			return render(request, 'factorfiction/search.html', context_dict)
		except Page.DoesNotExist:
			return HttpResponse("No articles found.")
	else:
		return render(request, 'factorfiction/search.html')

#Users can submit a url which will create a new Page Form and use Goose to extract data
#New articles will be displayed on main page
@login_required
def submit_page(request):
	form = PageForm()
	
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
		
			#Save new page to the database
			page = form.save(commit=False)

			#Use Goose to get all details from webpage
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
			return index(request)
		else:
			print(form.errors)
	
	return render(request, 'factorfiction/submit_page.html', {'form': form})
	
#Allow users to add comments to posts and display their username and profile picture
@login_required
def add_comment(request, pk):
	page = get_object_or_404(Page, pk=pk)
	
	#Creates new comment form for each comment along with who it was posted by
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

#Allow user to register new profile on factorfiction
def register(request):
	registered = False
	
	#Create seperate form instances for generic user form and profile form
	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:

		user_form = UserForm()
		profile_form = UserProfileForm()

	#Return user and user profile form
	return render(request,
				'factorfiction/register.html',
				{'user_form': user_form,
				'profile_form': profile_form,
				'registered': registered})
				
				
#Allows user to update existing profile details
def update_profile(request):
	if request.method == 'POST':
		form = UpdateProfile(request.POST, instance=request.user.userprofile, initial ={"name": request.user.userprofile.name, 'age':request.user.userprofile.age, 'location':request.user.userprofile.location, 'website':request.user.userprofile.website, 'bio':request.user.userprofile.bio, 'picture':request.user.userprofile.picture})
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('my_profile'))
	else:
		form = UpdateProfile(initial ={"name": request.user.userprofile.name, 'age':request.user.userprofile.age, 'location':request.user.userprofile.location, 'website':request.user.userprofile.website, 'bio':request.user.userprofile.bio, 'picture':request.user.userprofile.picture})

	return render(request, 'factorfiction/update_profile.html', {'update_profile_form': form})


# Log user in if details correct
def user_login(request):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
			
			
		#Return error if account is disabled or details are incorrect
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied." + " <br /> <a href='/factorfiction/' %}'>Try again?</a>")
	
	else:
		return render(request, 'rango/index.html', {})

# Log user out and return to homepage
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))




	