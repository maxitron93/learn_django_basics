from django.db import models

# 1. Create the model (class) in models.py
# 2. Add the app to the settings
# 3. Create a migration
# 4. Migrate
# 5. Add the model to the admin


# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

