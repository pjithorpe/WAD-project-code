import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'fact_or_fiction.settings')

import django
django.setup()
from factorfiction.models import Page

def populate():
    articles = [
        {"title": "Sole candidate loses U of G student president election in narrow vote",
         "postedBy": "todo",
        "url":"http://guelph.ctvnews.ca/sole-candidate-loses-u-of-g-student-president-election-in-narrow-vote-1.3318301",
         "views" : 43,
         "facts" : 13,
         "fictions": 14},
        {"title":"Harambe: Stop making memes of our dead gorilla, Cincinnati Zoo pleads",
         "postedBy": "todo",
        "url":"http://www.independent.co.uk/life-style/gadgets-and-tech/news/harambe-memes-cincinnati-zoo-gorilla-shot-dead-rip-a7203356.html",
         "views" : 17,
         "facts" : 3,
         "fictions": 14},
         {"title":"Donald Trump says hes too smart for daily intelligence briefings",
          "postedBy": "todo",
         "url":"http://www.independent.co.uk/news/world/americas/us-elections/donald-trump-says-hes-too-smart-for-daily-intelligence-briefings-a7468456.html",
         "views" : 17,
         "facts" : 13,
         "fictions": 14},
         {"title":"Anti-Defamation League Declares Pepe the Frog a Hate Symbol",
          "postedBy": "todo",
         "url":"http://time.com/4510849/pepe-the-frog-adl-hate-symbol/",
         "views" : 17,
         "facts" : 13,
         "fictions": 14},
         {"title":"US airline wins right to weigh passengers to prevent crash landings",
          "postedBy": "todo",
         "url":"http://www.independent.co.uk/news/world/americas/hawaiian-airlines-american-samoa-honolulu-obese-discrimination-weigh-passengers-new-policy-crash-a7375426.html",
         "views" : 17,
         "facts" : 13,
         "fictions": 14} ]

    for p in articles:
         add_page(p["title"], p["postedBy"], p["url"], p["views"], p["facts"], p["fictions"])


def add_page(title,postedBy, url, views=0, facts=0, fictions=0 ):
     p = Page.objects.get_or_create(title=title)[0]
     p.postedBy=postedBy
     p.url=url
     p.views=views
     p.facts=facts
     p.fictions=fictions
     p.save()
     return p

#

 # Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
