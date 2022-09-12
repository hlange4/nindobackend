from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255, null=True)
    avatar_url = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Channel(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    avatar_url = models.CharField(max_length=255)
    chanel_type = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    chart_placed = models.BooleanField(default=False)
    rank = models.IntegerField(null=True)
    subscribers = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class YouTubeDetail(models.Model):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.channel.name

class InstagramDetail(models.Model):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    average_comments = models.IntegerField(null=True)
    average_engagement = models.IntegerField(null=True)
    average_likes = models.IntegerField(null=True)
    last_post = models.DateTimeField(null=True)
    comments_rank = models.IntegerField(null=True)
    likes_rank = models.IntegerField(null=True)
    followers_rank = models.IntegerField(null=True)
    recent_shitstorm = models.BooleanField(default=False)
    regular_clickbait = models.BooleanField(default=False)
    regular_fsk18 = models.BooleanField(default=False)
    followers_last_month = models.IntegerField(null=True)
    posts_last_month = models.IntegerField(null=True)
    stories_last_month = models.IntegerField(null=True)
    total_igtv = models.IntegerField(null=True)
    total_posts = models.IntegerField(null=True)
    verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.channel.name

class TikTokDetail(models.Model):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.channel.name

class TwitterDetail(models.Model):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.channel.name

class TwitchDetail(models.Model):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.channel.name

class HistoryEntry(models.Model):
    followers = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.timestamp



class Post(models.Model):
    content = models.TextField(null=True)
    description = models.TextField(null=True)
    published = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.description

class PostAnalytic(models.Model):
    age = models.DurationField(null=True)
    post_type = models.CharField(max_length=255, null=True)
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    value = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.post


class Brand(models.Model):
    branch = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    terms = models.TextField()
    timestamp = models.DateTimeField()
    url = models.CharField(max_length=255)
    valid = models.BooleanField()
    valid_until = models.DateTimeField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __str__(self):
        return self.code


class Milestone(models.Model):
    followers = models.CharField(max_length=255)
    expected_time = models.DateTimeField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    def __str__(self):
        return f"Milestone: {self.followers} Subs for {self.channel} expected at: {self.expected_time}"