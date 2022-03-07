from django.shortcuts import render

context = {
    'index' : {'judul' : 'Home'
        , 'kontributor' : 'Ridwan'
        ,'konten':'home'
        ,'banner':'img/banner_home.png'
        ,'nav':(("/blog","Blog"),("/about","About"),("/","Home"))}
    ,'recent' : {'judul' : 'Recent Blog'
        , 'kontributor' : 'Tita'
        ,'konten':'recent blog'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
    ,'news' : {'judul' : 'News'
        , 'kontributor' : 'Ridwan'
        ,'konten':'news'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
    ,'story' : {'judul' : 'Cerita'
        , 'kontributor' : 'Ridwan'
        ,'konten':'cerita'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
    , 'about': {'judul': 'About'
        , 'kontributor': 'Ridwan'
        , 'konten': 'about'
        , 'nav': (("/about", "Blog"), ("/", "Home"), ("/blog/story", "Story"), ("/blog/news", "News"),
                      ("/blog/recent", "Recent"))
            }}

# Create your views here.
def index(response):
    return render(response,'home.html',context['index'])