from django.db import models

from real_estate_card.models import RealEstate
from users.models import Group


class Solutions(models.Model):
    wording = models.CharField(max_length=255, verbose_name='формулировка')
    date = models.DateField(verbose_name='дата')
    group = models.ForeignKey(Group, verbose_name='группа', on_delete=models.PROTECT, default=None, null=True)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.PROTECT, verbose_name='объекты')

    def __str__(self):
        return f'{self.wording}: {self.date}'

    class Meta:
        verbose_name = "Решение"
        verbose_name_plural = "Решения"


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='вопрос')
    real_estate = models.ManyToManyField(RealEstate, verbose_name='объекты')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
