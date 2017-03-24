from factorfiction.models import Page, User
from django.db.models import Q

#Passes the top 3 pages with the most votes to the base template
def add_trending_to_context(request):
	page_list = Page.objects.order_by('-totalVotes')[:3]
	return {'trendingPages': page_list}

#Passes up to 5 users with the most posts to the base template
def add_top_users_to_context(request):
	user_list = User.objects.all()
	
	top_users = ['','','','','']
	top_counts = [0,0,0,0,0]
	
	#Generates a nested list of usernames and the number of posts they have made
	for u in user_list:
		u_name = u.username
		
		try:
			u_pages = Page.objects.all()
			q = Q(postedBy=u_name)
			u_pages = u_pages.filter(q)
			
			u_count = u_pages.count()
		except:
			u_count = 0
		
		i = 4
		
		#Ensures only returns at most 5 users
		while (u_count > top_counts[i]) and (i >= 0):
			if i < 4:
				top_counts[i+1] = top_counts[i]
				top_users[i+1] = top_users[i]
				
			top_counts[i] = u_count
			top_users[i] = u_name
			
			i = i - 1
	
	top_list = []
	i = 0
	
	while (i < 5):
		top_list.append([top_users[i],top_counts[i]])
		i = i + 1
	
	context_dict = {'topUsers': top_list}
	return {'topUsers': top_list}