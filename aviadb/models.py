from django.db import models

class Compartments(models.Model):

    ###Таблица с отсеками###

    partName = models.CharField(max_length=200, help_text="Название детали")
    model = models.ForeignKey('Aircraft', on_delete=models.CASCADE)

    def __str__(self):
        return self.partName

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Aircraft(models.Model):

    ###Таблица с самолетами###

    productName = models.CharField(max_length=200, default='Models', help_text="Название модели")
    description = models.CharField(max_length=400, default='Description', help_text="Описание модели самолета")

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Drawing(models.Model):

    ###Таблица с чертежами###

    plan = models.CharField(max_length=200, help_text="Чертеж")
    equipment = models.CharField(max_length=200, help_text="Оснастка")
    material = models.CharField(max_length=200, help_text="Материал")
    square = models.CharField(max_length=200, help_text="Общая площадь")
    weight = models.CharField(max_length=200, help_text="Масса")
    diamino = models.CharField(max_length=200, help_text="Diamino")
    laser3d = models.CharField(max_length=200, help_text="Laser3D")
    revision = models.CharField(max_length=200, help_text="Ревизия")
    samplesAreWitnesses = models.CharField(max_length=200, help_text="Образцы свидетели")
    executor = models.CharField(max_length=200, help_text="Испольнитель")
    quantityA4 = models.CharField(max_length=200, help_text="Количество A4")
    name = models.CharField(max_length=200, help_text="Название")
    detail = models.ForeignKey('Compartments', on_delete=models.CASCADE)

    def __str__(self):
        return self.plan

    class Meta:
        verbose_name = 'Чертеж'
        verbose_name_plural = 'Чертежи'