from django.db import models

# Create your models here.
class SendEmailForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
         get_latest_by = 'created_at'

    