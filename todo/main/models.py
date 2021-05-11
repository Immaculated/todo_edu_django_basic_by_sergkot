from django.db import models


class ListModel(models.Model):
    """
    Модель списка дел
    """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'@id={self.id} @name={self.name} @user={self.user.username}'

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'
        unique_together = ('name', 'user')
