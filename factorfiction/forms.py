from django import forms
from django.contrib.auth.models import User
from factorfiction.models import Page, UserProfile, Comment, UpdateProfile

#Form for displaying all information of a page
class PageForm(forms.ModelForm):
	content = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
	title = forms.CharField(max_length=128,widget=forms.HiddenInput(), required=False)
	postedBy = forms.CharField(max_length=128,widget=forms.HiddenInput(), required=False)
	url = forms.URLField(max_length=200, help_text="Please enter the URL:  ")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	facts = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	fictions = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required = False)

	class Meta:
		model = Page
		fields = ('url',)
		
		def clean(self):
			cleaned_data = self.cleaned_data
			url = cleaned_data.get('url')
			
			if url and not url.startswith('http://'):
				url = 'http://' + url
				cleaned_data['url'] = url
				return cleaned_data

#Form for commenting up to a max of 2000 characters
class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=2000, widget=forms.Textarea, help_text="Add Comment: ")
	
	class Meta:
		model = Comment
		fields = ('text',)
		
#Used to get the standard Django user information on registration
class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','email','password')
		
#Used when a new user is registering their profile details
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('name','age','location','website','bio','picture')
		
#Form to allow users to update their existing profile details
class UpdateProfile(forms.ModelForm):
	class Meta:
		model = UpdateProfile
		fields = ('name','age','location','website','bio','picture')
		