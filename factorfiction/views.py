from django.shortcuts import render
from django.http import HttpResponse
from factorfiction.forms import PageForm

def index(request):
	return render(request, 'factorfiction/index.html',)
	
def fofgame(request):
	return render(request, 'factorfiction/fofgame.html')
	
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
	