from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='başlıq')
    content = models.TextField()
    publish_date = models.DateField()
    is_show = models.BooleanField(default=True)
    cover_image = models.ImageField(verbose_name='Foto blog', upload_to="blogs/", null=True, blank=True)
    view_count = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'bloq'
        verbose_name_plural = 'bloqlar'


class BlogImage(models.Model):
    image = models.ImageField(upload_to='blogs/images/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title
