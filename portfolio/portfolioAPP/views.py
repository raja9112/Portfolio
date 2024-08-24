from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import SendEmailForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        try:
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\n\nMessage: {message}',
                'rajarajan20bcs135@gmail.com',  # Replace with your email
                ['rrn.rajarajan@gmail.com'],  # Replace with your desired recipient
            )
            
            EmailDatabase = SendEmailForm(
                name = name,
                email = email,
                subject = subject,
                message = message
            )
            EmailDatabase.save()
            messages.success(request, "Email has been sent successfully.")
            return redirect('success')  # Redirect after successful email sending
        except Exception as e:
            messages.error(request, f'Error sending email: {e}')
            return redirect('/') 
        
    return render(request, "/")

    