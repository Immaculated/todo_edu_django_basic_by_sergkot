from django.db import models


class ListItem(models.Model):
    """
    Модель элемента списка
    """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    list_model = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'@id={self.id}@name={self.name}@list={self.list_model.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        items = ListItem.objects.filter(list_model=self.list_model)

        if all([item.is_done for item in items]):
            self.list_model.is_done = True
            self.list_model.save()
        else:
            self.list_model.is_done = False
            self.list_model.save()

    class Meta:
        verbose_name = 'Элемент списка'
        verbose_name_plural = 'Элементы списка'
        unique_together = ('name', 'list_model')
