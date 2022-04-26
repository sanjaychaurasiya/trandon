from django.db import models


# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='intern/MEDIA_ROOT/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
