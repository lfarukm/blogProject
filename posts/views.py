from django.shortcuts import render, redirect

from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

#! index sayfası :
def index(request):
    posts = Post.objects.filter(isPublish = True).order_by('-created_at')#? ("[:1]" şunu parentezin sonuna yazarsan bir sayfada kaçtane gözükeceğini belirler.) burdaki order_by('-created_at') sayfada hangi post daha önce geliri yapıyoruz.başına - koyduğmuz için en son kaydolan en başta gözükücek. yada direk hiçbişey yazmayıp sadece ? koyarsan rastgale bir post çıkarır.
    #? burda izin verdiğmiz postları yayınlamak için yaziyoruz.
    if request.method == 'POST':
        if request.user.is_authenticated:
            postId = request.POST['postId']
            post = Post.objects.get(id = postId)

            if 'like' in request.POST:
                if request.user.profile in post.like.all():
                    post.like.remove(request.user.profile)
                    post.save()
                    return redirect('index')

                else:
                    post.like.add(request.user.profile)
                    post.dislike.remove(request.user.profile)
                    post.save()
                    return redirect('index')
                    
            if 'dislike' in request.POST:
                if request.user.profile in post.dislike.all():
                    post.dislike.remove(request.user.profile)
                    post.save()
                    return redirect('index')
                else:
                    post.dislike.add(request.user.profile)
                    post.like.remove(request.user.profile)
                    post.save()
                    return redirect('index')

    context = {
        'posts':posts
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
#! create sayfası :
def create(request):
    #? formu sayfa ilk açıldığında normal haliyle göstermek için .
    form = PostForm()
    #? sayfada çalıştırılan bir post methodu varmı.
    if request.method == 'POST':
        #? post methodu ile gönderilen formun içerisindeki bilgileri ve resimleri çekmek için.
        form = PostForm(request.POST, request.FILES)
        #? formun doğruluğunu kontrol etme.
        if form.is_valid():
            #? kaydetmeden önce form üzerinde değişiklik yapmak için commit = Flase ile kaydetme özelliğini devre dışı bırakma.
            post = form.save(commit=False)
            #? postun owner bilgisini girişli kullanıcıya bağlama. 
            post.owner = request.user.profile
            #? post kaydetme.
            post.save()
            #? mesaj.
            messages.success(request, 'Postunuz Oluşturulmuştur. Denetlendikten Sonra Yayınlanıcaktır.')
            #? yönlendirme.
            return redirect('index')

    #? form değişkeni içerisinde tanımlanan formu html sayfada göstermek için önce contexte tanımlanır.
    #? sonra render fonkisyonun içine yazılır.
    context = {
        'form':form
    }        
    return render(request, 'create.html', context)


#! detail sayfası :
def detail(request, postId, slug):
    post = Post.objects.get(id = postId, slug= slug)
    context = {
        'post':post
    }
    return render(request, 'detail.html', context)

