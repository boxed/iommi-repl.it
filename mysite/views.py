from iommi import *


def index(request):
    class MyPage(Page):
        foo = html.h1('title')
        body = 'body text'
    return MyPage()