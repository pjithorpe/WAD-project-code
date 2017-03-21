from factorfiction.models import Page

def add_variable_to_context(request):
	page_list = Page.objects.order_by('-views')[:3]
	return {'pages': page_list}