from django.db import models


class Notes(models.Model):
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

    def __str__(self):
        return self.vk

    class Meta:
        verbose_name_plural = 'contact'