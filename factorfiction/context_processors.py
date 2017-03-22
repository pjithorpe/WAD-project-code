from factorfiction.models import Page

def add_variable_to_context(request):
	page_list = Page.objects.order_by('-totalVotes')[:3]
	return {'trendingPages': page_list}