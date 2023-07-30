from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

'''
def contact_view(reuqest):
    return HttpResponse("Contact Works")
'''
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'contact/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact copy.html', context)

from .models import NewsletterSubscriber

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                # You can add some success message here if you want
                print("user created")
                pass
            else:
                # Email already exists, you can show an error message
                print("user already created")
                pass
    return redirect('index')  # Redirect the user back to the home page or any other page
