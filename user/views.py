from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from posts.models import *
# Create your views here.


def like(request):
    postId = request.POST['postId']
    post = Post.objects.get(id = postId)

    if 'like' in request.POST:
        if request.user.profile in post.like.all():
            post.like.remove(request.user.profile)
            post.save()

        else:
            post.like.add(request.user.profile)
            post.dislike.remove(request.user.profile)
            post.save()

    if 'dislike' in request.POST:
        if request.user.profile in post.dislike.all():
            post.dislike.remove(request.user.profile)
            post.save()
        else:
            post.dislike.add(request.user.profile)
            post.like.remove(request.user.profile)
            post.save()




#! register sayfası :
def userRegister(request):
    #* burda register sayfasında inputları doldurduğmuzda ve refleş ettiğmizde o inputtaki şeyler silinmemesi için yapıyoruz.
    username = ''
    email = ''
    name = ''
    surname = ''
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Bu Kullanıcı Adı Zaten Alınmış.')
            elif User.objects.filter(email= email).exists()  :
                messages.error(request, 'Bu E-mail Zaten Alınmış.')
            elif len(password1) < 6:
                messages.error(request, 'Şifreniz En az 6 Karakterden Oluşmaldır.')
            elif username.lower() in password1:
                messages.error(request, 'Şifrenizle Kullanıcı Adınız Benzer Olmamalıdır.')
            else:
                user = User.objects.create_user(username= username, email= email, password= password1)
                user.save()

                Profile.objects.create(
                    user = user,
                    name = name,
                    surname = surname
                )
                messages.success(request, 'Kaydınız Oluşturuldu.')
                return redirect('index')
        
        else:
            messages.error(request, 'Şifreler Uyuşmuyor.')

    context = {
        'username':username,
        'email':email,
        'name':name,
        'surname':surname
    }

    return render(request, 'user/register.html',context)


#! login sayfası :
def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password= password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı.')
            return redirect('index')

        else:
            messages.error(request, 'Kullanıcı Adı veya Şifre Yanlış!')
            return redirect('login')

    return render(request, 'user/login.html')        

#! logout sayfası :
def userlogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı.')
    return redirect('index')


#! profil sayfası :
def profil(request, slug):
    profil = Profile.objects.get(slug=slug)
    paylasim = Post.objects.filter(owner = profil)
    begen = Post.objects.filter(like__in = [profil])
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            if  'takip' in request.POST:
                hesabim = Profile.objects.get(user = request.user)
                if Profile.objects.filter(slug = slug, followers__in = [hesabim]).exists():
                    profil.followers.remove(hesabim)
                    hesabim.follow.remove(profil)
                    messages.success(request, f'{profil.user.username} Kullanıcısını Takipten Bıraktınız.')
                    return redirect('profil', slug = profil.slug)

                else:
                    profil.followers.add(hesabim)
                    hesabim.follow.add(profil)
                    messages.success(request, f'{profil.user.username} Kullanıcısını Takip Etmeye Başladınız.')
                    return redirect('profil', slug = profil.slug)
            
            elif 'sil' in request.POST:
                postId = request.POST["postId"]
                post = Post.objects.get(id = postId)
                post.delete()
                messages.success(request, 'Paylaşım Silindi.')
                return redirect('profil', slug= slug)

            else:
                like(request)
                return redirect('profil', slug= slug)

        else:
            messages.error(request, 'Lütfen Giriş Yapınız.')
            return redirect('login')    
    
    context = {
        'profil':profil,
        'paylasim':paylasim,
        'begen':begen
    }
    return render(request, 'user/profil.html', context)


@login_required(login_url='login')
#! update sayfası :
def update(request):
    myUser = request.user
    myProfile = request.user.profile
    form = UserForm(instance= myUser) #* bilgilerini göstermek istediğimiz kullanıncınıyı instance olarak belirtiryoruz.
    profilForm = ProfilForm(instance= myProfile)

    if request.method == 'POST':
        form = UserForm(request.POST, instance= myUser)
        profilForm = ProfilForm(request.POST, request.FILES, instance= myProfile)
        if form.is_valid() and profilForm.is_valid():
            form.save()
            profilForm.save()
            messages.success(request, 'Profiliniz Güncellendi.')
            return redirect('profil', slug = myProfile.slug)

    context = {
        'form':form,
        'profilForm':profilForm
    }

    return render(request, 'user/update.html', context)


#! Şifre Değiştir (password.html)
@login_required(login_url='login')
def reset(request):
    myUser = request.user
    if request.method == 'POST':
        eski = request.POST['eski']
        yeni = request.POST['yeni']
        confirm = request.POST['confirm']

        user = authenticate(request, username = request.user, password= eski)

        if user is not None:
            if yeni == confirm:
                myUser.set_password(yeni)
                myUser.save()
                messages.success(request, 'Şifreniz Değiştirildi.')
                return redirect('login')

        else:
            messages.error(request, 'Mevcut Şifre Hatalı!')

    return render(request, 'user/password.html')






