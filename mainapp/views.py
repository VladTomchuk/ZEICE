from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.template.loader import get_template
from .models import IceType, Clients, Distributor, IceTypeImages, ZeBarTools, ZeBarToolsImages
from .forms import MyForm
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate


def home(request):
    ice_type = IceType.objects.all()
    clients = Clients.objects.all()
    return render(request, 'mainapp/home/home.html', {
        'clients': clients,
        'ice_type': ice_type,
        'title': _('Home'),
    })


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)
    return


def about(request):
    clients = Clients.objects.all()
    return render(request, 'mainapp/about/about.html', {
        'title': _('About us'),
        'clients': clients,
    })


def ice(request):
    ice_type = IceType.objects.all()

    return render(request, 'mainapp/ice/ice.html', {
        'ice_type': ice_type,
        'title': _('Ice Types'),
    })


def view_ice_type(request, ice_id):
    icetype_item = IceType.objects.get(pk=ice_id)
    photos = IceTypeImages.objects.filter(icetype_item=icetype_item)
    return render(request, 'mainapp/view_ice_type/view_ice_type.html', {
        "icetype_item": icetype_item,
        "photos": photos,
        "title": icetype_item.title
    })


def delivery(request):
    distributor = Distributor.objects.all()

    return render(request, 'mainapp/delivery/delivery.html', {
        'distributor': distributor,
        'title': _('Delivery'),
    })


def rent(request):
    return render(request, 'mainapp/rent/rent.html', )


def zebartools(request):
    zebartools = ZeBarTools.objects.all()

    return render(request, 'mainapp/zebartools/zebartools.html', {
        'zebartools': zebartools,
        'title': 'ZeBarTools',
    })


def view_zebartools_product(request, product_id):
    zebartools_item = ZeBarTools.objects.get(pk=product_id)
    photos = ZeBarToolsImages.objects.filter(zebartools_item=zebartools_item)
    return render(request, 'mainapp/view_zebartools_product/view_zebartools_product.html', {
        'zebartools_item': zebartools_item,
        'photos': photos,
        'title': zebartools_item.title,
    })


def clients(request):
    clients = Clients.objects.all()

    return render(request, 'mainapp/clients/clients.html', {
        'clients': clients,
        'title': 'Clients',
    })


def contacts(request):
    if request.method == 'GET':
        form = MyForm()
    else:
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                ctx = {
                    'message_name': name,
                    'message_email': email,
                    'message_phone': phone,
                    'message_comment': message,
                }
                text_content = get_template('mainapp/mail/mail.txt').render(ctx)
                html_content = get_template('mainapp/mail/contact-us/email-contact-us.html').render(ctx)
                subject = 'Запрос на обратную связь'
                from_email = 'info@zeice.es'
                to = 'info@zeice.es'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'mainapp/mail/contact-us/web-page-contact-us.html',{
                'message_name': name,
                'message_email': email,
                'message_phone': phone,
                'message_comment': message,
            })
    return render(request, 'mainapp/contacts/contacts.html', {
        'form': form,
        'title': _('Сontacts'),
    })

# if request.method == 'POST':
#     message_name = request.POST['message-name']
#     message_email = request.POST['message-email']
#     message_phone = request.POST['message-phone']
#     message_comment = request.POST['message-comment']
#     ctx = {
#         'message_name': message_name,
#         'message_email': message_email,
#         'message_phone': message_phone,
#         'message_comment': message_comment,
#     }
#     text_content = get_template('mainapp/mail/mail.txt').render(ctx)
#     html_content = get_template('mainapp/mail/contact-us/email-contact-us.html').render(ctx)
#     subject = 'Запрос на обратную связь'
#     from_email = 'info@zeice.es'
#     to = 'info@zeice.es'
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#     return render(request, 'mainapp/mail/contact-us/web-page-contact-us.html', {
#         'message_name': message_name,
#         'message_email': message_email,
#         'message_phone': message_phone,
#         'message_comment': message_comment,
#         'title': 'Thank you for request!'
#     })
# else:
#     return render(request, 'mainapp/contacts/contacts.html', {
#         'title': _('Сontacts'),
#     })
