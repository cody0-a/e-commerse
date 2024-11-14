from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import UserRegistrationForm


app_name = 'account'

def index_views(request):
    return render(request, 'account/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  # Redirect to the product list or desired page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'account/login.html')
def register_views(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))  # Hash the password
            user.save()  
            
            
            
            login(request, user)
            
            # Redirect to a success page or home page
            return redirect('account:home')  # Change 'home' to your desired redirect URL
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})


def reset_passwd(request):
    return  render(request, 'account/reset_password.html')