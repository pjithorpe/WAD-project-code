from django import template
from factorfiction.models import Page, GameArticle
	
register = template.Library()

@register.inclusion_tag('factorfiction/fofgame.html')
def getGameArticles(article=None):
	return {'gameArticles': GameArticle.objects.all(),
			'currentArticle': article}

def get_pages(page=None):
	return {'pages': Page.objects.all(),
			}