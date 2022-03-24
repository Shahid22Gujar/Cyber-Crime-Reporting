

from django.views.generic import TemplateView,View
from django.shortcuts import get_object_or_404, render,redirect
from .forms import ReportingForm,NewUserForm,ReportingFormAnonmously
from django.contrib.auth import login, authenticate,logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import *
from ipware import get_client_ip

# if ip is None:
#     # Unable to get the client's IP address
# else:
#     # We got the client's IP address
#     if is_routable:
#         # The client's IP address is publicly routable on the Internet
#     else:
#         # The client's IP address is private

# Order of precedence is (Public, Private, Loopback, None
# Create your views here.
class Home(TemplateView):
    template_name='home.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        ip, is_routable = get_client_ip(self.request)
        if ip is None:
            # Unable to get the client's IP address
            print("Unable to get ip")
        else:
            # We got the client's IP address
           
            if is_routable:
                print(ip)
                # The client's IP address is publicly routable on the Internet
                print("Public IP")
            else:
                # The client's IP address is private
                print(ip)
                print("Private IP")

        return self.render_to_response(context)
# Report Anonymously
def report_anonmously(request):
    form=ReportingFormAnonmously(request.POST or None,request.FILES or None)
    files=request.FILES.getlist("screenshots")
    ip, is_routable = get_client_ip(request)
    if request.method=="POST":
        # print(form)
        
        # print(screenshots)
        if form.is_valid():
            form=form.save(commit=False)
            if ip is None:
                form.ip=''
            form.ip=ip
           
            # form.screenshots_obj=form
            form.save()
            for f in files:
                # form.screenshot=f
                screenshots=Screenshots.objects.create(
                    screenshots=f,victimuser=form
                )
            
                
            
            messages.success(request,'Your complaint have been registered')
            return redirect('home')
    else:
        form=ReportingFormAnonmously()
    context={'form':form}
    return render(request,'report_anonmously.html',context)

@login_required(login_url='login/')
def report(request):
    form=ReportingForm(request.POST or None,request.FILES or None)
    files=request.FILES.getlist("screenshots")
    user=request.user
    if request.method=="POST":
        # print(form)
        
        # print(screenshots)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=user
           
            # form.screenshots_obj=form
            form.save()
            for f in files:
                # form.screenshot=f
                screenshots=Screenshots.objects.create(
                    screenshots=f,victimuser=form
                )
            
                
            
            messages.success(request,'Your complaint have been registered')
            return redirect('home')
    else:
        form=ReportingForm()
    context={'form':form}
    return render(request,'report.html',context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

@login_required(login_url='login/')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("home")
@login_required(login_url='login/')
def user_profile(request):
    profile=Report.objects.all()
    print(profile)
    context={'profile':profile}
    return render(request,'profile.html',context)

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# import json.decoder
# def some_view(request,id):
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     victim=VictimUser.objects.filter(id=id)
#     for data in victim:

#         p.drawString(100, 100, f'date_crime:{data.date_crime}\nCategory:{data.category_crime[1]}')


#     # p.drawString(100, 100, "Hello world.")
#     # p.drawString(100, 100, f'{data}')

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
@login_required(login_url='login/')
def show_reports(request):
    user=request.user
    reports=Report.objects.filter(user=user)
    context={'reports':reports}
    return render(request,'download_reported_detail.html',context)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
def victim_render_pdf_view(request,*args,**kwargs):
    pk=kwargs.get('pk')
    victim=get_object_or_404(Report,pk=pk)
    screenshots=Screenshots.objects.filter(victimuser=victim)
    template_path = 'pdf2.html'
    # context = {'myvar': 'this is your template context'}
    context = {'victim': victim,'screenshots':screenshots}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download -> keep attachement
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
     # if show only -> remove attachement
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# def render_pdf_view(request,id):
#     template_path = 'pdf1.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # if download -> keep attachement
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#      # if show only -> remove attachement
#     response['Content-Disposition'] = ' filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

class AcceptTerm(TemplateView):
    template_name='accept_terms.html'

class MethodToReport(TemplateView):
    template_name='methd_report.html'