from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Badge
from course.models import userprogress,Answers
from django.conf import settings  
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import re,os,glob
@login_required
def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if user_profile is None:
        return redirect('home')
    else:
        context = {'user_profile': user_profile}
        return render(request, 'profile/userprofile.html', context)
    
@login_required
def editprofile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if user_profile is None:
        return redirect('home')
    else:
        context = {'user_profile': user_profile}
        return render(request, 'profile/editprofile.html', context)
    
@login_required
def profileedithandle(request):
    if request.method == 'POST':
        # Get the updated form data from the POST request
        changed_name = request.POST.get('changedName')
        changed_email = request.POST.get('changedEmail')
        changed_hack_id = request.POST.get('changedHackId')
        profile_image = request.FILES.get('changedProfileimg')
        changed_nickname = request.POST.get('changedNickName')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Get the current user's profile
        user_profile = Profile.objects.get(user=request.user)
        if profile_image:
            # Check if user has remaining image upload limit
            if user_profile.imguploadlimit > 0:
                # Check file size
                if profile_image.size > (5 * 1024 * 1024):  # 5MB limit
                    messages.error(request, "Profile picture size exceeds 5MB limit.")
                    return redirect('editprofile')

                # Check file type
                valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
                _, extension = os.path.splitext(profile_image.name.lower())
                if extension not in valid_extensions:
                    messages.error(request, "Uploaded file is not a valid image.")
                    return redirect('editprofile')

                # Change image file name following username pattern
                username = request.user.username
                new_filename = f"{username}_profile_image{extension}"
                profile_image.name = new_filename

                # Save the image to user profile
                user_profile.image = profile_image
                user_profile.imguploadlimit -= 1  # Decrement the upload limit
                user_profile.save()
            else:
                messages.error(request, "Sorry! You have exceeded the profile image update limit")
                return redirect("editprofile")



        if not changed_name.isalpha():
            messages.error(request, "The Name should not contain any numbers or special characters")
            return redirect("editprofile")
        
        if len(changed_name) > 50:
            messages.error(request, "The Name is too long")
            return redirect("editprofile") 
        
        if len(changed_nickname) > 50:
            messages.error(request, "The Nickname is too long")
            return redirect("editprofile") 
        
        if len(changed_hack_id) > 17:
            messages.error(request, "Invalid HackerRank Username")
            return redirect("editprofile") 

        if not (re.match(email_regex, changed_email) and changed_email.endswith('@gmail.com')):
            messages.error(request, "Enter valid Email")
            return redirect("editprofile") 

       
        
        # Update the profile data
        user_profile.name = changed_name
        user_profile.nickname = changed_nickname
        
        # Update the email in the User model
        request.user.email = changed_email
        
        
        user_profile.hackerrank_id = changed_hack_id
            

        # Save all changes to the database
        user_profile.save()
        request.user.save()
        
        # Show success message
        messages.success(request, 'Profile details updated successfully.')
        return redirect('profile')

    return redirect('editprofile')  # Redirect if request method is not POST

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        username = request.user.username

        # Check if new passwords match
        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return redirect('editprofile')

        # Check if old password is correct
        if not request.user.check_password(old_password):
            messages.error(request, 'Incorrect current password.')
            return redirect('editprofile')

        # Check if new password meets requirements
        if len(new_password1) < 8 or len(new_password1) > 20:
            messages.error(request, 'New password must be between 8 and 20 characters long.')
            return redirect('editprofile')

        if username.lower() in new_password1.lower():
            messages.error(request, 'New password cannot contain your username.')
            return redirect('editprofile')

        if new_password1.isdigit() or new_password1.isalpha():
            messages.error(request, 'New password must contain a mix of letters, digits, and special characters.')
            return redirect('editprofile')

        if not any(char.isupper() for char in new_password1):
            messages.error(request, 'New password must contain at least one uppercase letter.')
            return redirect('editprofile')

        if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_+{}\[\]:;.,?\'"\\/|<>~-]+$', new_password1):
            messages.error(request, 'New password must contain only alphanumeric characters and special characters.')
            return redirect('editprofile')

        # Change the user's password
        request.user.set_password(new_password1)
        request.user.save()

        # Update session authentication hash
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Your password was successfully updated!')
        return redirect('profile')
   



def badges(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'badge/badge.html', {'user_profile': user_profile})


 
def recent_badge(request):
    # Fetch the user's profile. Adjust this based on your actual implementation.
    user_profile = Profile.objects.get(user=request.user)

    # Filter badges based on the user's profile and get the most recent one
    recent_badge = Badge.objects.filter(user_profile=user_profile).order_by('-created_at').first()

    return render(request, 'profile/userprofile.html', {'recent_badge': recent_badge})

    

