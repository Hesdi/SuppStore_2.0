from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.
class Product(models.Model):
    prod_name = models.CharField('Product Name', max_length=200)
    prod_date = models.DateTimeField('Product Date', default=timezone.now())
    prod_description = models.TextField('Product Description', max_length=2000)
    prod_price = models.IntegerField('Product Price')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prod_image = models.ImageField(default='default_prod.jpg', upload_to='product_pics')
    class Category(models.TextChoices):
        BSU = "Building Supplies"
        TLS = "Tools"
        ELC = "Electrics"
        ENS = "Engineering Systems"

    category = models.CharField(
        max_length=19,
        choices=Category.choices,
        default=Category.BSU
    )


    def __str__(self):
        return self.prod_name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.prod_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.prod_image.path)
