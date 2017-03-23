# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fact_or_fiction.settings')

import django
django.setup()
from factorfiction.models import Page, GameArticle
from goose import Goose
import urllib
from django.utils import timezone
from django.contrib.auth.models import User

def populate():

	User.objects.create_superuser('fofadmin', 'myemail@example.com', 'fofpassword')

	articles = [
		{"url":"http://guelph.ctvnews.ca/sole-candidate-loses-u-of-g-student-president-election-in-narrow-vote-1.3318301",
		"views" : 43,
		"facts" : 13,
		"fictions": 14,
		 "postedBy": "DonaldT"},
		{"url":"http://www.independent.co.uk/life-style/gadgets-and-tech/news/harambe-memes-cincinnati-zoo-gorilla-shot-dead-rip-a7203356.html",
		"views" : 17,
		"facts" : 3,
		"fictions": 14,
		 "postedBy": "DonaldT"},
		{"url":"http://www.independent.co.uk/news/world/americas/us-elections/donald-trump-says-hes-too-smart-for-daily-intelligence-briefings-a7468456.html",
		"views" : 17,
		"facts" : 13,
		"fictions": 14,
		 "postedBy":"DavidC"},
		{"url":"http://time.com/4510849/pepe-the-frog-adl-hate-symbol/",
		"views" : 17,
		"facts" : 13,
		"fictions": 14,
		 "postedBy": "DavidC"},
		{"url":"http://www.independent.co.uk/news/world/americas/hawaiian-airlines-american-samoa-honolulu-obese-discrimination-weigh-passengers-new-policy-crash-a7375426.html",
		"views" : 17,
		"facts" : 13,
		"fictions": 14,
		 "postedBy": "thomasthetank"} ]

	for p in articles:
		add_page(p["url"], p["postedBy"],  p["views"], p["facts"], p["fictions"])
		 
	game_articles = [
		{"title":"Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement",
		"description":"News outlets around the world are reporting on the news that Pope Francis has made the unprecedented decision to endorse a US presidential candidate. His statement in support of Donald Trump was released from the Vatican this evening: 'I have been hesitant to offer any kind of support for either candidate in the US presidential election but I now feel that to not voice my concern would be a dereliction of my duty as the Holy See...",
		"answer":"fake",
		"fact": 7,
		"fiction": 15,
		"picture": "../../static/images/popetrump.jpg"},
		{"title":"Trump Offering Free One-Way Tickets to Africa & Mexico for Those Who Wanna Leave America",
		"description":"President elect Donald Trump has sensationally offered free one-way tickets to Mexico or Africa for anyone who wants to leave America in the aftermath of his election victory. The extraordinary, and highly controversial, offer was revealed by an aid at a press conference in New York this morning...",
		"answer":"fake",
		"fact": 13,
		"fiction": 17,
		"picture": "../../static/images/TrumpTickets.jpg"},
		{"title":"Feral pig drinks 18 cans of beer, fights cow and then passes out drunk under tree",
		"description":"The swine drank 18 beers on its bender in Port Hedland, Western Australia, according to ABC News. The alcohol also made the pig hungry and was seen looking through rubbish bags for something to eat...",
		"answer":"true",
		"fact": 8,
		"fiction": 19,
		"picture": "../../static/images/pig.jpg"},
		{"title":"Cinnamon Roll Can Explodes Inside Man's Butt During Shoplifting Incident",
		"description":"Las Vegas – Martin Klein, 41 of Las Vegas, was arrested after a shopping lifting incident turned horribly wrong. According to reports, Mr. Klein and his partner, Jerry Weis, had stolen several grocery items from the Las Vegas Walmart...",
		"answer":"fake",
		"fact": 19,
		"fiction": 7,
		"picture": "../../static/images/CinnamonRollMan.jpg"},
		{"title":"Poll: 38% of Florida voters believe Ted Cruz could be the Zodiac Killer",
		"description":"While a 62 percent majority of voters answered 'No' when asked if they believed Cruz was responsible for the string of murders in the early 70s, 10 percent answered 'Yes' and an additional 28 percent said they were unsure...",
		"answer":"true",
		"fact": 11,
		"fiction": 6,
		"picture": "../../static/images/FloridaPoll.jpg"},
		{"title":"Hamster resurrection: Pet rises from the grave at Easter after being buried in garden",
		"description":"Tink the hamster was found ‘cold and lifeless’ in the bottom of her cage and laid to rest by a couple who were looking after her for a friend. But the next day the rodent – who was not dead but hibernating – reappeared as perplexed Les Kilbourne-Smith crushed a pile of old boxes for recycling...",
		"answer":"true",
		"fact": 15,
		"fiction": 9,
		"picture": "../../static/images/hamster.jpg"},
		{"title":"WikiLeaks CONFIRMS Hillary Sold Weapons to ISIS… Then Drops Another BOMBSHELL!",
		"description":"Now, WikiLeaks is announcing that Hillary Clinton and her State Department were actively arming Islamic jihadists, which includes the Islamic State (ISIS) in Syria. Clinton has repeatedly denied these claims, including during multiple statements while under oath in front of the United States Senate...",
		"answer":"fake",
		"fact": 17,
		"fiction": 12,
		"picture": "../../static/images/hillary.jpg"},
		{"title":"Winner Of French Scrabble Championship Does Not Speak French",
		"description":"Nigel Richards of New Zealand entered the French-language Scrabble tournament in Louvain, Belgium, in July, and took first place. But he doesn’t speak a word of French. Richards knows his Scrabble, though, and how to win. He’s held several English-language U.S. and world championships...",
		"answer":"true",
		"fact": 19,
		"fiction": 8,
		"picture": "../../static/images/scrabble.jpg"},
		{"title":"Man Shoots Armadillo, Bullet Hits Mother-In-Law",
		"description":"Sheriff’s deputies in Lee County, Georgia, said McElroy, 54, accidentally shot his mother-in-law with a 9mm pistol when he was trying to shoot an armadillo, WALB.com reports. The armadillo died from the shot, but the bullet ricocheted off the animal, hit a fence and went into the back door of his mother-in-law’s mobile home — a distance of about 100 yards...",
		"answer":"true",
		"fact": 7,
		"fiction": 16,
		"picture": "../../static/images/armadillo.jpg"},
		{"title":"Woman arrested for defecating on boss’ desk after winning the lottery",
		"description":"NEW YORK – A 41-year-old woman had the winning lottery ticket worth over 3 million dollars on Friday night, but showed up to work anyway on Monday to deliver one last package...",
		"answer":"fake",
		"fact": 12,
		"fiction": 14,
		"picture": "../../static/images/lotterywinner.png"}]
		
	for eachArticle in game_articles:
		add_game_article(eachArticle["title"], eachArticle["description"], eachArticle["picture"], eachArticle["answer"], eachArticle["fact"], eachArticle["fiction"])

	users = ["DonaldT", "DavidC" , "thomasthetank"]

	for username in users:
		add_user(username)

def add_user(username):
	newuser = User.objects.create_user(username, password='password')
	newuser.save()

def add_page( url , postedBy, views=0, facts=0, fictions=0 ):
	p = Page.objects.get_or_create(url=url)[0]
	p.postedBy=postedBy
	p.url=url
	p.views=views
	p.facts=facts
	p.fictions=fictions
	g = Goose()
	article = g.extract(url=url)
	urllib.urlretrieve(article.top_image.src, os.path.join("static/images/article_pics", article.title.replace(" ", "")) + ".jpg")
	p.articleImage = "images/article_pics/" + article.title.replace(" ", "") + ".jpg"
	p.title = article.title
	p.content = article.cleaned_text[:3000]
	p.save()
	return p
	 
def add_game_article(title,description,picture, answer, fact=0, fiction=0):
	games = GameArticle.objects.get_or_create(title=title)[0]
	games.description=description
	games.answer=answer
	games.fact=fact
	games.fiction=fiction
	games.picture=picture
	games.save()
	return games

#

 # Start execution here!
if __name__ == '__main__':
	print("Starting FactOrFiction population script...")
	populate()