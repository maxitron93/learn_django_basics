from django.db import models

# 1. Create the model (class) in models.py
# 2. Add the app to the settings
# 3. Create a migration
# 4. Migrate
# 5. Add the model to the admin

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    # This function returns the title as the main description or the admin site :D
    def __str__(self):
        return self.title

    # Create a function to return only the first 100 characters of the body
    def summary(self):
        return self.body[:15]

    # Function to return a nicely formatted time
    def formattedTime(self):
        return self.pub_date.strftime('%b %e %Y')

    