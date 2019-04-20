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
