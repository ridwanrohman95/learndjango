from django.shortcuts import render

context = {
    'index' : {'judul' : 'Blog'
        , 'kontributor' : 'Ridwan'
        ,'konten':'blog'
        ,'banner':'blog/img/banner_blog.png'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
    ,'recent' : {'judul' : 'Recent Blog'
        , 'kontributor' : 'Tita'
        ,'konten':'recent blog'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
    ,'news' : {'judul' : 'News'
        , 'kontributor' : 'Ridwan'
        ,'konten':'news'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
    ,'story' : {'judul' : 'Story'
        , 'kontributor' : 'Ridwan'
        ,'konten':'story'
        ,'banner':'blog/img/banner_stories.jpg'
        ,'nav':(("/blog","Blog"),("/","Home"),("/blog/story","Story"),("/blog/news","News"),("/blog/recent","Recent"))}
}

def index(response):
    return render(response,'blog/index.html',context['index'])

def recent(response):
    return render(response,'blog/recent.html',context['recent'])

def news(response):
    return render(response,'blog/news.html',context['news'])

def story(response):
    return render(response,'blog/story.html',context['story'])