from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.forms import UserRegistrationForm, UserLoginForm


# Create your views here.
from cart.cart import Cart


def register_view(request):
    cart = Cart(request)

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user, 'cart': cart})
        return render(request, 'register.html', {'register_form': user_form, 'cart': cart})
    else:
         user_form = UserRegistrationForm()
         return render(request, "register.html", {'register_form': user_form, 'cart': cart})


def login_view(request):
    cart = Cart(request)

    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username.strip(),
                            password=password.strip())
        login(request, user)
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or '/'
        return redirect(redirect_path)
    return render(request, 'login.html', {'login_form': form, 'cart': cart})


def logout_view(request):
    logout(request)
    return redirect('/')
