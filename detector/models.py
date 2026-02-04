from django.db import models

class FailedLoginEvent(models.Model):
    time = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    ip_address = models.CharField(max_length=50)
    logon_type = models.CharField(max_length=50)
    username = models.CharField(max_length=100, blank=True) 

    def __str__(self):
        return f"{self.ip_address} - {self.time}"


class BruteForceAlert(models.Model):
    ip_address = models.CharField(max_length=50)
    attempts = models.IntegerField()
    severity = models.CharField(max_length=20)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ALERT {self.ip_address} ({self.attempts})"
