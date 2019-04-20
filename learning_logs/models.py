from django.db import models

# Create your models here.
class Topic(models.Model):
    """a class to hold our topic data"""

    # set the text field as a charfield of 200 characters max
    text = models.CharField(max_length=200)
    # set the date_added to store the date as the time of posting
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retruns a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        txt = self.text
        if len(txt) < 50:
            return txt
        else:
            return txt[:50] + '...'
