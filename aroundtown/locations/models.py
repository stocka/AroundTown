from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=250)
  formatted_address = models.CharField('Address', max_length=1000, null=True, blank=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6)
  longitude = models.DecimalField(max_digits=10, decimal_places=6)
  last_visited_date = models.DateTimeField('Date Last Visited', editable=False, null=True, blank=True)
  
  def __unicode__(self):
      return self.name

class Visit(models.Model):
  RATINGS = (
    (1, 'Bad'),
    (2, 'OK'),
    (3, 'Good'),
    (4, 'Great'),
    (5, 'Fantastic')
  )
  location = models.ForeignKey(Location)
  visit_date = models.DateField()
  rating = models.IntegerField(choices=RATINGS)
  writeup = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.location.name + ': ' + self.visit_date.strftime('%x') + ' - ' + str(self.rating) + '/5 rating'
