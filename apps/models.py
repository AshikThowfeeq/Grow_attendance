from django.db import models

class AttendanceTest(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_test'

    def __str__(self):
        return self.name