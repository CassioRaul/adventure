from django.db import models

class Plans(models.Model):
    titulo = models.CharField('TÍTULO', max_length=120)
    description = models.CharField('DESCRIÇÃO', max_length=300)
    type_plan = models.CharField('TIPO DE PLANO', max_length=50)
    road_map = models.CharField('ROTEIRO', max_length=300)
    duration = models.IntegerField('DURAÇÃO', default=0)
    value = models.FloatField('PREÇO', default=0)

    def __str__(self):
        return f'{self.titulo}'
    