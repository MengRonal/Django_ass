from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('kiyo/',views.kiyo,name='kiyo'),
    # path('',views.index,name='index'),
    path(route='home/', view=views.home, name='home'),
    path(route='about/',view=views.about,name='about'),
    path(route='contact/',view=views.contact,name='contact'),
    path(route='bookList/',view=views.bookList,name='bookList'),
    path(route='buy/<int:id>/',view=views.buy,name='buy'),
    path(route="detail/<int:id>", view=views.detail, name="detail"),
    path(route='search-result/',view=views.searchresult,name='search-result'),

]