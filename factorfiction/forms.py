from django import forms
from django.contrib.auth.models import User
from factorfiction.models import Page, UserProfile, Comment

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

class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=2000, widget=forms.Textarea, help_text="Add Comment: ")
	
	class Meta:
		model = Comment
		fields = ('text',)
		
class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','email','password')
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('name','age','location','website','bio','picture')
		
class UpdateProfile(forms.ModelForm):
	username = forms.CharField(required=False)
	email = forms.CharField(required=False)
	name = forms.CharField(required=False)
	age = forms.IntegerField(required=False)
	location = forms.CharField(required=False)
	website = forms.CharField(required=False)
	bio = forms.CharField(required=False)
	picture = forms.ImageField(required=False)

	class Meta:
	
		model = User
		fields = ('username', 'email')
		
		modelProfile = UserProfile
		fieldsProfile = ('name','age','location','website','bio','picture')

	def save(self, commit=True):
		user = super(UserProfileForm, self).save(commit=False)

		if commit:
			user.save()

		return user