from django.db import models

from django.utils.translation import gettext_lazy as _

class Blog(models.Model):
    author = models.CharField(
        _("Author"),
        max_length=55
    )
    title = models.CharField(
        _("Titulo"),
        max_length=55
    )
    description = models.TextField(
        _("Descripcion"),
    )

    image = models.ImageField(
        _("Imagen"),
        upload_to = "public/blog"
    )
    create_at = models.DateTimeField(
        _("Fecha de creacion"),
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        _("Fecha de modificacion"),
        auto_now=True
    )

    class Meta:
        verbose_name = _("Blog Personal")
        verbose_name_plural =_("Blog personales")

    def __str__(self):
        return self.author
