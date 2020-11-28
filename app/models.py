from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse



class Team(models.Model):
    short_name = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=30)
    college_or_club = models.CharField(max_length=10)
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
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    race = models.CharField(max_length=200)
    selected_year = models.DateField(null=True)
    rank = models.IntegerField(default=1)
    image = models.ImageField(upload_to='nationalimages/')

    class Meta:
        ordering = ['-selected_year','rank','name']

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
    college = models.ForeignKey(Team, on_delete=models.PROTECT)
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
    contents = MarkdownxField(help_text='To Write with Markdown format')

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
