from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)# create onto one relationship between User field
    # CASCADE means when we delete the user it should delete the profile

    image = models.ImageField(default = 'default.jpg',upload_to=' profile_pics')# it is image field and it accept the .jpg by defalut and uploadt_to directory that images uploded to tath
    def __str__(self):
        return f'{self.user.username} Profile'#dender str describ the out put of our out put of this models
    