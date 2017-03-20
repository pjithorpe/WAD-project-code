from django import forms
from django.contrib.auth.models import User
from factorfiction.models import Page, UserProfile

class PageForm(forms.ModelForm):
	content = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
	title = forms.CharField(max_length=128,widget=forms.HiddenInput(), required=False)
	postedBy = forms.CharField(max_length=128,widget=forms.HiddenInput(), required=False)
	url = forms.URLField(max_length=200, help_text="Please enter the URL")
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
				
class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','email','password')
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('age','website','picture')