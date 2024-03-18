from django.db import models


class ProcessedFile(models.Model):
    file_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    processed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.file_name
