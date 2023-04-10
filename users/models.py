from django.contrib.auth.models import AbstractUser
from django.db import models

from real_estate_card.models import RealEstate


class Role(models.Model):
    title = models.CharField(max_length=20, verbose_name='название')
    admin = models.BooleanField(default=False, verbose_name='админ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, verbose_name='роль')

    def __str__(self):
        return f'{self.username}: {self.role}'

    def get_real_estates(self) -> set[RealEstate]:
        groups = self.get_groups()
        real_estate_list = []
        for group in groups:
            real_estate_list.append(group.real_estates.values())

        return set(real_estate_list)

    def get_groups(self) -> list:
        groups = Group.objects.filter(users=self)
        return groups

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Group(models.Model):
    users = models.ManyToManyField(User, verbose_name='участиники')
    real_estates = models.ManyToManyField(RealEstate, verbose_name='объекты')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
