from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    content1 = models.TextField()
    content2 = models.TextField()

    image1 = models.ImageField(upload_to='about_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='about_images/', null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"   


# class TeamMember(models.Model):
#     full_name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='team_images/')
#     twitter_link = models.URLField(blank=True)
#     instagram_link = models.URLField(blank=True)
#     linkedin_link = models.URLField(blank=True)

#     def __str__(self):
#         return self.full_name

#     class Meta:
#         verbose_name_plural = "Team Members"


class Service(models.Model):
    title=models.CharField(max_length=200)  
    description=models.TextField()    
    image=models.ImageField(upload_to='service_images') 

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Our Services"



class Project(models.Model):
    text1 = models.CharField(max_length=200)  
    text2 = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='project_images') 

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name_plural = "Our Projects"



class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)  
    profession = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='testimonial_images') 
    stars = models.IntegerField(default=0)  # For example, you can adjust the field type as needed
    #comment = models.TextField()  # Adjust field options as needed
    comment = models.TextField(default='')  # Manually define a default value for the comment field

    

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = "Our Testimonials"


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Our Team"  


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='author_images/', default='default_author_image.jpg')
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Our Blog"  


class Contact(models.Model):  # Changed "models.model" to "models.Model"
    name = models.CharField(max_length=250)  # Fixed typo in "max_length"
    email = models.EmailField()
    number = models.CharField(max_length=12)  # Specify max length for number field
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = "Registration Table"



# class UserLogin(models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username
    
#     class Meta:
#         verbose_name_plural = "Login Table"