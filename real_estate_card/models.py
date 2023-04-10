from django.db import models


class RealEstate(models.Model):
    STATES = (
        ('new', 'новый'),
        ('process', 'в работе'),
        ('finish', 'завершен'),
    )

    county = models.CharField(max_length=255, verbose_name='округ')
    district = models.CharField(max_length=255, verbose_name='район')
    address = models.CharField(max_length=255, verbose_name='адрес')

    #тип объекта
    type = models.CharField(max_length=255, verbose_name='тип')

    description = models.CharField(max_length=255, verbose_name='описание', blank=True, null=True)

    #состояние объекта
    state = models.CharField(max_length=255, choices=STATES, default=STATES[0][0], verbose_name='состояние')

    #площадь объекта в кв.м.
    square = models.FloatField(verbose_name='площадь (кв.м.)')

    #Кадастр
    cadastral_number = models.CharField(verbose_name='кадастровый номер', blank=True, null=True)
    cadastral_price = models.FloatField(verbose_name='кадастровая стоимость', blank=True, null=True)

    #владелец и фактический пользователь
    owner = models.CharField(max_length=255, verbose_name='владелец')
    actual_user = models.CharField(max_length=255, verbose_name='пользователь')

    def __str__(self):
        return f'{self.id}: {self.address}'

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


def media_dir_path(instance, filename):
    file_extension = filename.split('.')[-1]
    a = instance.real_estate.id
    print(type(instance.real_estate))
    b = instance.title
    print(b)
    return f'real_estate/{a}/{b}.{file_extension}'


class RealEstatePhoto(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='название')
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, verbose_name='объект')
    image = models.ImageField(upload_to=media_dir_path, verbose_name='фотография')

    class Meta:
        verbose_name = "Фото объектов"
        verbose_name_plural = "Фото объектов"
