from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.conf import settings
from factorfiction import test_utils
from factorfiction.models import User, UserProfile
import os

class GeneralTests(TestCase):
	def test_serving_static_image_files(self):
		result = finders.find('images/logo.jpg')
		self.assertIsNotNone(result)
		
	def test_serving_css_files(self):
		result = finders.find('css/factorfiction.css')
		self.assertIsNotNone(result)
		
	def test_serving_javascript_files(self):
		result = finders.find('js/game.js')
		self.assertIsNotNone(result)
		
	def test_does_slug_field_work(self):
		from factorfiction.models import Page
		article = Page(title='newly created slug text')
		article.save()
		self.assertEqual(article.slug, 'newly-created-slug-text')
		
	def test_base_template_exists(self):
		path_to_base = settings.TEMPLATE_DIR + '/factorfiction/base.html'
		print (path_to_base)
		self.assertTrue(os.path.isfile(path_to_base))

class IndexTestCases(TestCase):
	def test_index_success(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		
	def test_index_using_template(self):
		response = self.client.get(reverse('index'))
		self.assertTemplateUsed(response, 'factorfiction/index.html')
		
	def test_see_new_post(self):
		article = Page(title="New Article", postedBy="Mystery User",
                        url="http://www.articlepage.com", views=10, facts=10, fictions=10)
		article.save()
		
		response = self.client.get(reverse('index'))
		self.assertIn('New Article', response.content)
		self.assertIn('Mystery User', response.content)

class FoFGameTestCases(TestCase):		
	def test_FoFGame_success(self):
		response = self.client.get(reverse('fofgame'))
		self.assertEqual(response.status_code, 200)
		
	def test_FoFGame_using_template(self):
		response = self.client.get(reverse('fofgame'))
		self.assertTemplateUsed(response, 'factorfiction/fofgame.html')

class SearchTestCases(TestCase):		
	def test_search_success(self):
		response = self.client.get(reverse('search'))
		self.assertEqual(response.status_code, 200)
		
	def test_search_using_template(self):
		response = self.client.get(reverse('search'))
		self.assertTemplateUsed(response, 'factorfiction/search.html')

class AboutTestCases(TestCase):		
	def test_about_success(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)
	
	def test_about_using_template(self):
		response = self.client.get(reverse('about'))
		self.assertTemplateUsed(response, 'factorfiction/about.html')
		
	def test_about_contains_text(self):
		response = self.client.get(reverse('about'))
		self.assertIn(b'Created by', response.content)
		
	def test_about_contains_logo(self):
		response = self.client.get(reverse('about'))
		self.assertIn(b'src="/static/images/logo.jpg', response.content)

class RegisterTestCases(TestCase):		
	def test_register_success(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)
		
	def test_register_using_template(self):
		response = self.client.get(reverse('register'))
		self.assertTemplateUsed(response, 'factorfiction/register.html')
	
	def test_registration_form_is_displayed_correctly(self):
		try:
			response = self.client.get(reverse('register'))
		except:
			try:
				response = self.client.get(reverse('factorfiction:register'))
			except:
				return False

		self.assertIn('Register a user account with factorfiction', response.content)

		self.assertTrue(isinstance(response.context['user_form'], UserForm))

		self.assertTrue(isinstance(response.context['profile_form'], UserProfileForm))

		user_form = UserForm()
		profile_form = UserProfileForm()

		self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())
		self.assertEquals(response.context['profile_form'].as_p(), profile_form.as_p())

		self.assertIn('type="submit" name="submit" value="Register"', response.content)
		
class SubmitTestCases(TestCase):

	def test_submit_success(self):
		test_utils.create_user()
		self.client.login(username='testuser123', password='test1234')
		response = self.client.get(reverse('submit_page'))
		self.assertEqual(response.status_code, 200)
		
	def test_submit_using_template(self):
		test_utils.create_user()
		self.client.login(username='testuser123', password='test1234')
		response = self.client.get(reverse('submit_page'))
		self.assertTemplateUsed(response, 'factorfiction/submit_page.html')

class MyProfileTestCases(TestCase):

	def test_myprofile_success(self):
		test_utils.create_user()
		self.client.login(username='testuser123', password='test1234')
		response = self.client.get(reverse('myprofile'))
		self.assertEqual(response.status_code, 200)
		
	def test_myprofile_using_template(self):
		test_utils.create_user()
		self.client.login(username='testuser123', password='test1234')
		response = self.client.get(reverse('myprofile'))
		self.assertTemplateUsed(response, 'factorfiction/myprofile.html')
		
	def test_myprofile_correct_info(self):
		test_utils.create_user()
		self.client.login(username='testuser123', password='test1234')
		
		response = self.client.get(reverse('myprofile'))
		self.assertIn("testuser123", response.content)
		self.assertIn("21", response.content)
		self.assertIn("http://www.testuser.com", response.content)
		
class ModelTests(TestCase):
	def setUp(self):
		try:
			from FoF_populate import populate
			populate()
		except ImportError:
			print("The module FoF_Populate does not exist")
		except NameError:
			print("The function populate() does not exist or is not correct")
		except:
			print("Something went wrong in the populate() function.")
			
	def get_article(self, title):
		from factorfiction.models import Page
		try:
			article = Page.objects.get(title=title)
		except Page.DoesNotExist:
			article = None
		return article
		
	def get_game_article(self, title):
		from factorfiction.models import GameArticle
		try:
			gameArticle = GameArticle.objects.get(title=title)
		except GameArticle.DoesNotExist:
			gameArticle = None
		return gameArticle
		
	def test_article_added(self):
		article = self.get_article('Sole candidate loses U of G student president election in narrow vote')
		self.assertIsNotNone(article)
		
	def test_article_with_url(self):
		article = self.get_article('Sole candidate loses U of G student president election in narrow vote')
		self.assertEquals(article.url, 'http://guelph.ctvnews.ca/sole-candidate-loses-u-of-g-student-president-election-in-narrow-vote-1.3318301')
		
	def test_article_with_views(self):
		article = self.get_article('Sole candidate loses U of G student president election in narrow vote')
		self.assertEquals(article.views, 43)
		
	def test_article_with_fact_votes(self):
		article = self.get_article('Sole candidate loses U of G student president election in narrow vote')
		self.assertEquals(article.facts, 13)
		
	def test_article_with_fiction_votes(self):
		article = self.get_article('Sole candidate loses U of G student president election in narrow vote')
		self.assertEquals(article.fictions, 14)
		
	def test_game_article_added(self):
		gameArticle = self.get_game_article('Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement')
		self.assertIsNotNone(gameArticle)
		
	def test_game_article_with_desciption(self):
		gameArticle = self.get_game_article('Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement')
		self.assertEquals(gameArticle.description, "News outlets around the world are reporting on the news that Pope Francis has made the unprecedented decision to endorse a US presidential candidate. His statement in support of Donald Trump was released from the Vatican this evening: 'I have been hesitant to offer any kind of support for either candidate in the US presidential election but I now feel that to not voice my concern would be a dereliction of my duty as the Holy See...")
		
	def test_game_article_with_answer(self):
		gameArticle = self.get_game_article('Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement')
		self.assertEquals(gameArticle.answer, "fake")
		
	def test_game_article_with_fact_votes(self):
		gameArticle = self.get_game_article('Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement')
		self.assertEquals(gameArticle.fact, 7)
		
	def test_game_article_with_fiction_votes(self):
		gameArticle = self.get_game_article('Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement')
		self.assertEquals(gameArticle.fiction, 15)
		
	def test_game_article_with_picture(self):
		gameArticle = self.get_game_article('Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement')
		self.assertEquals(gameArticle.picture, "../../static/images/popetrump.jpg")
		
	def test_admin_interface_page_view(self):
		from factorfiction.admin import PageAdmin
		self.assertIn('title', PageAdmin.list_display)
		self.assertIn('url', PageAdmin.list_display)
		
	def test_user_profile_model(self):
		
		user, user_profile = test_utils.create_user()
		
		all_users = User.objects.all()
		self.assertEquals(len(all_users), 1)
		
		all_profiles = UserProfile.objects.all()
		self.assertEquals(len(all_profiles), 1)
		
		all_profiles[0].user = user
		all_profiles[0].website = user_profile.website
		all_profiles[0].age = user_profile.age
		
class LoggedInUserTests(TestCase):

	def test_url_reference_in_index_page_when_logged(self):
		test_utils.create_user()
		self.client.login(username="testuser123", password="test1234")
		
		response = self.client.get(reverse('index'))
		
		self.assertIn(reverse('fofgame'), response.content)
		self.assertIn(reverse('submit'), response.content)
		self.assertIn(reverse('search_page'), response.content)
		self.assertIn(reverse('about'), response.content)
		self.assertIn(reverse('myprofile'), response.content)
	
	def test_url_reference_in_index_page_when_not_logged(self):

		response = self.client.get(reverse('index'))

		self.assertIn(reverse('fofgame'), response.content)
		self.assertIn(reverse('submit'), response.content)
		self.assertIn(reverse('search_page'), response.content)
		self.assertIn(reverse('about'), response.content)
		self.assertIn(reverse('register'), response.content)
		
	def test_login_provides_error_message(self):
		try:
			response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
		except:
			try:
				response = self.client.post(reverse('factorfiction:login'), {'username': 'wronguser', 'password': 'wrongpass'})
			except:
				return False

		print (response.content)
		try:
			self.assertIn('wronguser', response.content)
		except:
			self.assertIn('Invalid login details supplied.', response.content)
		