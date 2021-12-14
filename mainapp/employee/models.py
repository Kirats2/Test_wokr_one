from django.db import models
from .assistant import experience
from django.shortcuts import reverse


class Department(models.Model):
    name = models.CharField("Подразделение", max_length=200)


    def get_absolute_url(self):
        return reverse('department_detail_url', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField("Должность", max_length=200)

    def get_absolute_url(self):
        return reverse('position_detail_url', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия ')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество')
    employment_position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, verbose_name='Должность',
        related_name='position', default=' ', null=True, blank=True)
    employment_department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, verbose_name='Подразделение',
        related_name='department', default=' ', null=True, blank=True)
    employment_start_date = models.DateField(verbose_name='Дата', auto_now_add=False)

    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'pk': self.id})

    def get_experience(self):
        return experience(self.employment_start_date)

    def __str__(self):
        return f'{self.name} {self.last_name} '
