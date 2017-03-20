from goose import Goose
import urllib
import os


url = 'http://edition.cnn.com/2017/03/19/politics/trump-golf-weekends/'
g = Goose()
article = g.extract(url=url)
print article.title
print article.cleaned_text
urllib.urlretrieve(article.top_image.src, os.path.join("static/images/article_pics" , article.title) + ".jpg")
urllib.urlretrieve(article.top_image.src, "000001.jpg")

urllib.urlretrieve(article.top_image.src, os.path.join("static/images/article_pics", article.title) + ".jpg")