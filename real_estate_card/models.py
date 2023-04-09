from django.db import models


class RealEstateOwner(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='имя')
    last_name = models.CharField(max_length=255, verbose_name='фамилия')
    surname = models.CharField(max_length=255, verbose_name='отчество')

    passport = models.CharField(max_length=10, unique=True, verbose_name='паспорт')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    def __str__(self):
        return f'{self.passport}: {self.get_full_name()}'

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"


class RealEstateActualUser(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='имя')
    last_name = models.CharField(max_length=255, verbose_name='фамилия')
    surname = models.CharField(max_length=255, verbose_name='отчество')

    #passport = models.CharField(max_length=10, unique=True)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.surname

    def __str__(self):
        #return f'{self.passport}: {self.get_full_name()}'
        return self.get_full_name()

    class Meta:
        verbose_name = "Фактиечский пользовтаель"
        verbose_name_plural = "Фактические пользователи"


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

    #владелец и фактический пользователь
    owner = models.ForeignKey(RealEstateOwner, on_delete=models.PROTECT, verbose_name='владелец')
    actual_user = models.ForeignKey(RealEstateActualUser, on_delete=models.PROTECT, verbose_name='фактический пользователь')

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
