from django.contrib.auth import get_user_model, login, logout, authenticate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from .forms import UserRegisterForm
from django.contrib import messages
from .utils import generate_token
from django.conf import settings
from django.db.models import Q
from .models import Product
import os

User = get_user_model()

def send_activation_email(request, user):
    link = get_current_site(request)
    subject = 'Activate Your Account On The Social Network'
    body = render_to_string('email_activation.html', {
        'user': user,
        'link': link,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': generate_token.make_token(user)
    })
    mail = EmailMessage(subject, body, settings.EMAIL_FROM, [user.email])
    mail.send()

def activate_user(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(force_str(uidb64))
        user = User.objects.get(id=uid)
    except:
        user = None

    if user and generate_token.check_token(user, token):
        user.verified_email = True
        user.save()
        messages.success(request, f'{user.username} is activated successfully')
        return redirect('signin')

    messages.error(request, 'Activation failed, Please retry to resend an email')
    return redirect('signin')

def test(request):
    queryset = Product.objects.order_by('-id').all()
    return render(request, 'index.html', {'posts': list(queryset)})

def post(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    if request.method == 'POST':
        title = request.POST['title']
        label = request.POST['label']
        category = request.POST['category']
        image = None
        if len(request.FILES) > 0:
            image = request.FILES.get('image')
        price = request.POST['price']

        if title and image and label and category and price:
            if len(title) > 50:
                return render(request, 'post.html', {'error': 'Title field must contain less than 50 characters'})
            if len(label) >= 750:
                return render(request, 'post.html', {'error': 'Label field must contain less than 500 characters'})
            if len(label) < 50:
                return render(request, 'post.html', {'error': 'Label field must contain more than 50 characters'})
            try:
                raw_price = float(price)
            except:
                return render(request, 'post.html', {'error': 'Price field must be a number'})
            product = Product()
            product.title = title
            product.image = image
            product.label = label
            product.category = category
            product.price = raw_price
            product.user = request.user
            product.save()
            return render(request, 'post.html', {'success': 'Product posted successfully'})
        else:
            return render(request, 'post.html', {'error': 'All fields must be filled out'})
    
    return render(request, 'post.html')

def edit(request, postID): 
    if not request.user.is_authenticated:
        return redirect('signin')
    try:
        product = Product.objects.get(pk=postID)
    except Product.DoesNotExist:
        return redirect('home')
    if not request.user.id == product.user.id:
        return redirect('home')
    if request.method == 'POST':
        title = request.POST['title']
        label = request.POST['label']
        category = request.POST['category']
        image = None
        if len(request.FILES) > 0:
            image = request.FILES.get('image')
        price = request.POST['price']
        if title and label and category and image and price:
            if len(title) > 50:
                return render(request, 'post.html', {'product': product, 'error': 'Title field must contain less than 50 characters'})
            if len(label) >= 750:
                return render(request, 'post.html', {'product': product, 'error': 'Label field must contain less than 500 characters'})
            if len(label) < 50:
                return render(request, 'post.html', {'product': product, 'error': 'Label field must contain more than 50 characters'})
            try:
                raw_price = float(price)
            except:
                return render(request, 'post.html', {'product': product, 'error': 'Price field must be a number'})
            try:
                product.title = title
                product.label = label
                product.category = category
                product.price = raw_price
                os.remove(product.image.path)
                product.image = image
                product.save()
                return redirect('profile', userID=product.user.id)
            except Exception as e:
                return render(request, 'post.html', {'product': product, 'error': e}) 
        else:
            return render(request, 'post.html', {'error': 'All fields must be filled out', 'product': product})

    return render(request, 'edit.html', {'product': product})

def delete(request, postID):
    if not request.user.is_authenticated:
        return redirect('signin')
    try:
        product = Product.objects.get(pk=postID)
    except Product.DoesNotExist:
        return redirect('home')
    if not request.user.id == product.user.id:
        return redirect('home')
    try:
        os.remove(product.image.path)
    except:
        pass
    product.delete();
    return redirect('profile', userID=product.user.id)

def register(request):  
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            form.save()
            try:
                user = User.objects.get(username=username)
            except:
                return render(request, 'signup.html', {'form': form, 'error': 'Error'})
            send_activation_email(request, user)
            messages.success(request, 'User created successfully, please verify your account by the email we sent you')
            return redirect('signin')

    form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                if not user.verified_email:
                    send_activation_email(request, user)
                    messages.error(request, 'User is not verified, We resent you a verification link please check your inbox')
                    return render(request, 'signin.html')
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'User is not found')
                return render(request, 'signin.html')
        else:
            messages.error(request, 'All Fields Must Be Filled Out')
            return render(request, 'signin.html')

    return render(request, 'signin.html')

def signout(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    return redirect('home')

def profile(request, userID): 
    if not User.objects.filter(pk=userID).exists():
        return redirect('home')
    user = User.objects.filter(pk=userID).first()
    products = Product.objects.filter(user__id=user.id).all()
    return render(request, 'profile.html', {'user': user, 'products': list(products)})

def search(request):
    query = request.GET['q'];
    if not query:
        return redirect('home')
    pqs = Product.objects.filter(Q(title__contains=query) | Q(category__icontains=query[0])).all()
    return render(request, 'search.html', {'products': list(pqs)})

def product(request, postID):
    try:
        product = Product.objects.get(pk=postID)
    except Product.DoesNotExist:
        return redirect('home')
    return render(request, 'product.html', {'product': product});

def store(request):
    pqs = Product.objects.order_by('?').all()
    return render(request, 'search.html', {'products': list(pqs)})