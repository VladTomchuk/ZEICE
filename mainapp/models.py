from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class ZeBarTools(models.Model):
    main_image = models.ImageField('Main foto', upload_to='zebartools_image/%Y/%m/')
    title = models.CharField(max_length=100, verbose_name='Title')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True, verbose_name='Description')

    def get_absolute_url(self):
        return reverse('view_zebartools_product', kwargs={"product_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ZeBarTools'
        verbose_name_plural = 'ZeBarTools'


class ZeBarToolsImages(models.Model):
    zebartools_item = models.ForeignKey(ZeBarTools, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='photos/zebartools_photo/%Y/%m/', blank=True)

    def __str__(self):
        return self.zebartools_item.title


class IceType(models.Model):
    image = models.ImageField('Main foto', upload_to='ice_type_image/%Y/%m/', default='')
    title = models.CharField(max_length=100, verbose_name='Название льда')
    size = models.CharField(max_length=100, verbose_name='Размер льда', default='')
    slug = models.SlugField()
    box_weight = models.DecimalField(max_digits=9, decimal_places=2)
    cubes_quantity = models.IntegerField(default=1, verbose_name="Количество льда в пачке")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True, verbose_name='Description')

    def get_absolute_url(self):
        return reverse('view_ice_type', kwargs={"ice_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ice type'
        verbose_name_plural = 'Ice types'


class IceTypeImages(models.Model):
    icetype_item = models.ForeignKey(IceType, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='photos/icetype_photo/%Y/%m/', blank=True)

    def __str__(self):
        return self.icetype_item.title


class Distributor(models.Model):
    logo = models.ImageField('Logo', upload_to='distributor/%Y/%m/')
    title = models.CharField(max_length=100, verbose_name='Distributor name')
    location = models.CharField(max_length=100, verbose_name='Location')
    website = models.CharField(blank=True, max_length=100, verbose_name='Website')
    phone_number = PhoneNumberField()
    email = models.CharField(max_length=100, verbose_name='Email')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Distributor'
        verbose_name_plural = 'Distributors'


class Clients(models.Model):
    logo = models.ImageField('Logo', upload_to='clients/%Y/%m/')
    title = models.CharField(max_length=100, verbose_name='Client name')
    country = models.CharField(blank=True,max_length=100, verbose_name='Country')
    city = models.CharField(blank=True,max_length=100, verbose_name='City')
    website = models.CharField(blank=True,max_length=100, verbose_name='Website')
    CHOICES = (
        ('50', 'Top-50'),
        ('100', 'Top-100'),
        ('500', 'Top-500'),
        ('none', 'None'),
    )
    awards = models.CharField('Awords', max_length=14, choices=CHOICES, default='none', blank=True)

    def __str__(self):
        return self.title


class ClientImages(models.Model):
    client_item = models.ForeignKey(Clients, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='photos/client_photo/%Y/%m/', blank=True)

    def __str__(self):
        return self.client_item.title
