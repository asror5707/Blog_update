from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import Maqola, Rasm, Comment, About


def home(request):
    return render(request,'home.html')


class Blog(View):
    def get(self,request):
        maqola = Maqola.objects.all().order_by("-time")
        return render(request, 'blog.html', {'maqola': maqola})





class MaqolaView(View):
    def get(self,request, son):
        maqola = Maqola.objects.get(id=son)
        rasm = Rasm.objects.filter(maqola=maqola)
        comments = Comment.objects.filter(maqola=maqola)
        return render(request, 'maqola.html', {'m': maqola, 'r': rasm,'comments':comments})

    def post(self,request,son):
        if request.user.is_authenticated:
            m = Maqola.objects.get(id=son)
            user = request.user
            Comment.objects.create(
                comments= request.POST["comment"],
                maqola=m,
                user = user
            )
            return redirect('maqola', son)
        else:
            return redirect('login')




def maqola(request):
    return render(request,'maqola.html')
class AboutView(View):
    def get(self,request):
        about = About.objects.all()
        print(about)
        return render(request , 'about.html', {'about':about})


class LoginView(View):
    def get(self, request):
        return render(request, 'googlelogin.html')

    def post(self, request):
        l = request.POST['login']
        parol = request.POST['parol']
        user = authenticate(request, username=l, password=parol)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')


class RegisterView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'myregister.html')
    def post(self,request):
        parol = request.POST.get('parol1')
        parol2 = request.POST.get('parol2')
        if parol == parol2:
            a = User.objects.create_user(
                username=request.POST['login'],
                password=request.POST['parol1'],
                email=request.POST['email']
            )
        login(request, a)
        return redirect('login')

def Logout(request):
    logout(request)
    return redirect('login')

# Create your views here.
