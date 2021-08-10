from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from repo.models import Image
from django.urls import reverse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Django provides a default registration form (UserCreationForm) to create new users. This is being passed to
# the template register.html
# Django handles validation checks (ex. passwords match, valid email, correct types of information for fields
# are being inputted) through the UserCreationForm()
# @params request: takes in the request provided by the form in register.html
# @returns if the post request from the form on register.html sends user information, the form fields are
#          validated and the user is created if form is valid. If not the register template is rendered again with
#          the form and its validation error messages.
#          When the URL is first hit, since there is no post request, the blank form is rendered on the register template
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login with your new account.')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# Archives and unarchives an image (sets the 'archived' boolean in the image model to True or False)
# Images can only be archived by the user that uploaded the image.
# @params request: takes in the post request provided by pressing the archive/unarchive button
#         **kwargs: keyword arguments (a dictionary of values provided in the url when reaching
#                   this view) that contains the id of the image that is to be archived/unarchived
# @returns a redirect to the home page once the image has been archived (also redirects to home if
#          user that tried to archive was not the user that uploaded the image and redirects to the
#          login page if the current user is not logged in)
def archive(request, **kwargs):
    if request.method == 'POST':
        if request.POST.get('imageArchive'):
            if request.user.is_authenticated:
                image = Image.objects.filter(id=kwargs['pk']).first()
                if request.user == image.uploader:
                    if image.archived == False:
                        image.archived = True
                        image.save()
                    else:
                        image.archived = False
                        image.save()
                else:
                    messages.warning(
                        request, f'You cannot archive images you did not upload.')
            else:
                messages.warning(
                    request, f'You cannot archive images you did not upload.')
                return redirect('login')

            return redirect('home')

# Renders the archive template with the archived images for a specific user
# Uses the login_required decorater provided by Django to make sure the user is logged in;
# if they are not logged in, they will redirected to the login page.
# @params request: takes the request information by the path to render the view
# @returns the rendered template and sends a dictionary to the template containing the
#          archived images for the current logged in user
@login_required
def viewArchive(request):
    archived_images = Image.objects.filter(
        uploader=request.user).filter(archived=True)

    return render(request, 'users/archive.html', {'archived_images': archived_images})