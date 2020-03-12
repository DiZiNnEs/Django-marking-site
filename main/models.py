from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'notes'


class Contact(models.Model):
    vk = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    habr = models.CharField(max_length=100)
    name = 'contact for layout'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'contact'


class About(models.Model):
    full_name = models.CharField(max_length=40)
    about_me = models.CharField(max_length=200)
    telephone_number = models.IntegerField()
    address = models.CharField(max_length=20)
    name = 'about me'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'about'
