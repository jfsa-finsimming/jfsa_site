from django.db import models
from mdeditor.fields import MDTextField
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField
from datetime import date


class Team(models.Model):
    short_name = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=30)
    college_or_club = models.CharField(max_length=10)
    training_place = models.CharField(max_length=50, null=True, blank=True)
    training_term = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='teamimages/')
    web_url=models.URLField(blank=True)
    instagram_url=models.URLField(blank=True)
    twitter_url=models.URLField(blank=True)
    facebook_url=models.URLField(blank=True)
    email=models.EmailField(blank=True)
    number_of_url_and_email = models.IntegerField(default=0)

    class Meta:
        ordering = ['-number_of_url_and_email']

    def __str__(self):
       return self.short_name + ' (' + self.owner + ')'


class NationalMember(models.Model):
    name_romaji = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.PROTECT,null=True, blank=True)
    race = models.CharField(max_length=200)
    selected_year = models.DateField(blank=True, null=True)
    rank = models.IntegerField(default=1)
    image = models.ImageField(upload_to='nationalimages/')

    class Meta:
        ordering = ['-selected_year','rank','name']

    def save(self, *args, **kwargs):
        if not self.selected_year.month==1 or not self.selected_year.day==1:
            self.selected_year = date(self.selected_year.year,1,1)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.rank==1 :
            return str(self.selected_year.year) + '：' + self.name + '(正代表)'
        elif self.rank==2 :
            return str(self.selected_year.year) + '：' +self.name + '(正代表/学生代表)'
        elif self.rank==3 :
            return str(self.selected_year.year) + '：' +self.name + '(学生代表)'


class Position(models.Model):
    name = models.CharField(max_length=100)
    position_number = models.IntegerField(default=0)

    class Meta:
        ordering = ['-position_number']

    def __str__(self):
       return str(self.position_number) + '：' + self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    name_romaji = models.CharField(max_length=100)
    college = models.ForeignKey(Team, on_delete=models.PROTECT,null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='memberimages/')

    class Meta:
        ordering = ['position','name']

    def __str__(self):
        return self.position.name + '：' + self.name




class PostManager(models.QuerySet):
    def published(self):
        return self.filter(published_at__lte=timezone.now())

    def is_public(self):
        return self.filter(is_public=True)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    thumnail = models.ImageField(upload_to='newsimages/', null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    event_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)
    contents = MDTextField(blank=True)

    objects = PostManager.as_manager()


    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

    def formatted_markdown(self):
        return markdownify(self.contents)

    def __str__(self):
        if self.is_public :
            return self.title
        else:
            return 'Not Checked: ' + self.title




class Event(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100,blank=True, null=True)
    thumnail = models.ImageField(upload_to='eventimages/', null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    place = models.CharField(max_length=100,blank=True, null=True)
    entry_fee = models.CharField(max_length=100,blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    event_url = models.URLField(blank=True)

    objects = PostManager.as_manager()

    class Meta:
        ordering = ['-event_date']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_public :
            return self.title
        else:
            return 'Not Checked: ' + self.title

class Race(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=10)
    image = models.ImageField(upload_to='raceimages/')
    race_info_url=models.URLField(blank=True)
    entry_info_url=models.URLField(blank=True)
    is_public = models.BooleanField(default=False)

    objects = PostManager.as_manager()

    class Meta:
        ordering = ['month']

    def __str__(self):
        if self.is_public :
            return self.month + '月:' + self.name
        else:
            return 'Not Checked: ' + self.month + '月:' + self.name



class JFSACupResult(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    event_date = models.DateTimeField(blank=True, null=True)
    thumnail = models.ImageField(upload_to='jfsacupresultimages/',null=True)
    upload = models.FileField(upload_to='file/%Y/%m/%d')
    is_public = models.BooleanField(default=False)

    objects = PostManager.as_manager()

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        if self.is_public :
            return self.name
        else:
            return 'Not Checked: ' + self.name



class JFSACupRecord(models.Model):
    upload = models.FileField(upload_to='file/%Y/%m/%d')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.updated_at)

class JFSACupMedia(models.Model):
    images = models.ImageField(upload_to='jfsacupimages/')
