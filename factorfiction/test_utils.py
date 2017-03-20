from factorfiction.models import Page, GameArticle
from django.contrib.auth.models import User

def create_articles():
	articles = []

	for i in range(1, 11):
		article = Page(title="Article " + str(i), postedBy="User " + str(i),
                        url="http://www.page" + str(i) + ".com", views=i, facts=i, fictions=i)
		article.save()
		articles.append(article)

	return articles


def create_user():
	from factorfiction.models import User, UserProfile
	user = User.objects.get_or_create(username="testuser123", password="test1234",
										first_name="Test", last_name="User", email="testuser@testuser.com")[0]
	user.set_password(user.password)
	user.save()

	user_profile = UserProfile.objects.get_or_create(user=user, age=21, website="http://www.testuser.com")[0]
	user_profile.save()

	return user, user_profile