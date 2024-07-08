from django.db import models
from stdimage import StdImageField
import uuid

class Base(models.Model):
    criado = models.DateField('Criado em', auto_now_add=True)
    modicado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta():
        abstract = True


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Project(Base):
    name_project = models.CharField('Name Project', max_length=100)
    description = models.TextField('Description', blank=False)
    coordinate = models.DecimalField('Coordinates', max_digits=5, decimal_places=5)
    latitude = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    longitude = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    point_x = models.FloatField()
    point_y = models.FloatField()
    point_z = models.FloatField()
    altitudes_elavation = models.DecimalField('Altitudes and elevation', max_digits=9, decimal_places=2)
    accountable = models.CharField('Accountable', max_length=100)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    status = models.CharField(max_length=20, choices=[
        ('In progress', 'In progress'),
        ('Finished', 'Finished'),
        ('Canceled', 'Canceled'),
    ])
    slug = models.SlugField('Slug', max_length=100, unique=True, default='')
    local = models.CharField('Local', max_length=100, default='')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        
        def __str__(self) -> str:
            return self.name_project