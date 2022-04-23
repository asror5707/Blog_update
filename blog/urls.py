from django.contrib import admin
from django.urls import path
from blog_app.views import AboutView,Blog,home,MaqolaView,maqola,LoginView,RegisterView,Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('blog/', Blog.as_view(),name='blog'),
    path('about/', AboutView.as_view()),
    path('maqola/',maqola ,name='maqola'),
    path('maqola/<int:son>', MaqolaView.as_view(),name="maqola"),
    path('login/', LoginView.as_view(),name='login'),
    path('reg', RegisterView.as_view(),name='reg'),
    path('logout/', Logout, name='logout')

]
