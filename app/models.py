from django.db import models

class Links(models.Model):
    short_link = models.CharField(
        max_length=50,
        verbose_name='короткая ссылка',
    )
    full_link = models.TextField(
        verbose_name='длинная ссылка',
    )
    clicks_count = models.IntegerField(
        verbose_name='количество кликов',
        blank=True,
        null=True,
        default=0
    )
    class Meta:
        db_table = 'links'
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'

    def __str__(self):
        return self.short_link
