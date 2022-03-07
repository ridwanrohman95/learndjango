from django.shortcuts import render

context = {
    'index' : {'judul' : 'About'
        , 'kontributor' : 'Ridwan'
        ,'konten':'about'
        ,'banner':'about/img/banner_about.png'
        ,'nav':(("/about","About"),("/","Home"))}
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
}

def index(response):
    return render(response,'about/index.html',context['index'])
