from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def get_post_image_path(instance,filename):
	return 'posts/{0}/{1}'.format(instance.post.user.username,filename)

def get_material_file_path(instance, filename):
    return 'material/{0}/{1}'.format(instance.course, filename)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    ACADEMIC = 'AC'
    CLUBSANDASSOCIATIONS = 'CA'
    CLASSREPRESENTATIVE = 'CR'
    GENERAL = 'GN'
    SPORTS = 'SP'
    CATEGORY_CHOICES = (
        (ACADEMIC, 'Academics'),
        (CLUBSANDASSOCIATIONS, 'Clubs and Associations'),
        (GENERAL,'General'),
        (CLASSREPRESENTATIVE, 'Class Representative'),
        (SPORTS, 'Sports'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=ACADEMIC,
    )

    def __str__(self):
        return self.text

class Photo(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='photo')
    file = models.FileField(upload_to=get_post_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100, default=None)

class Course(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField()
    DEPARTMENT_CHOICES = (
        ('---', '---'),
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('MME', 'Metallurgy Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('BIO', 'Biotechnology'),
    )
    YEAR_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    )
    
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class CourseMaterial(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=200, default=None)
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='material')
    ASSIGNMENT = 'AS'
    NOTES = 'NO'
    PREVIOUS_PAPERS = 'PP'
    CATEGORY_CHOICES = (
        (ASSIGNMENT, 'Assignment'),
        (NOTES, 'Notes'),
        (PREVIOUS_PAPERS,'Previous Papers'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
    )
    file = models.FileField(upload_to=get_material_file_path)

class Timetable(models.Model):
    date = models.DateField()
        
    years = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
      )
      
    year = models.CharField(max_length=20, choices=years, blank=True, null=True)
    section = models.CharField(max_length=2, blank=True, null=True)
    course8_9= models.CharField(max_length= 10, blank=True, null=True)
    course9_10= models.CharField(max_length= 10, blank=True, null=True)
    course10_11= models.CharField(max_length= 10, blank=True, null=True)
    course11_12= models.CharField(max_length= 10, blank=True, null=True)
    course12_1= models.CharField(max_length= 10, blank=True, null=True)
    course2_3= models.CharField(max_length= 10, blank=True, null=True)
    course3_4= models.CharField(max_length= 10, blank=True, null=True)
    course4_5= models.CharField(max_length= 10, blank=True, null=True)
    semester = models.IntegerField(null=True)
      
    def __str__(self):
     return self.year + ' '+self.section


