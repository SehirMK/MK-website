from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    #if request.user.is_authenticated():
     #   title = "My title %s" %(request.user)

    #if request.method == "POST":
     #   print request.POST
    context = {
        "template_title": title,
        "form": form
}

    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
       # if not instance.full_name:
        #    instance.full_name = "osman"
        instance.save()
      #  print instance.email
       # print instance.timestamp
        context = {
            "template_title": "thank you"
}

    return render(request, "home.html",context)


def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value
        #email = form.cleaned_data.get("email")
        #message = form.cleaned_data.get("message")
        #full_name = form.cleaned_data.get("full_name")
        #print email, message, full_name
    context = {
        "form": form,
        "title": title,
}
    return render(request, "forms.html", context)