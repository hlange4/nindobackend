from django.contrib import admin

from .models import *

class HistoryEntryInline(admin.TabularInline):
    model = HistoryEntry
    extra = 0

class HistoryEntryAdmin(admin.ModelAdmin):
    pass

class PostAnalyticInline(admin.TabularInline):
    model = PostAnalytic
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [PostAnalyticInline]

class PostAnalyticAdmin(admin.ModelAdmin):
    pass

class CouponAdmin(admin.ModelAdmin):
    pass

class MilestoneAdmin(admin.ModelAdmin):
    pass

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar_url', 'deleted', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['name']
    ordering = ['name']


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('artist', 'name', 'avatar_url', 'chanel_type', 'deleted', 'chart_placed', 'rank', 'subscribers', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['name']
    ordering = ['name']
    list_select_related = ['artist','youtubedetail','instagramdetail','tiktokdetail','twitterdetail','twitchdetail','postanalytic']
    autocomplete_fields = ['artist']

class YouTubeDetailAdmin(admin.ModelAdmin):
    list_display = ('channel', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['channel']
    ordering = ['channel']
    list_select_related = ['channel']
    autocomplete_fields = ['channel']

class InstagramDetailAdmin(admin.ModelAdmin):
    list_display = ('channel', 'average_comments', 'average_engagement', 'average_likes', 'last_post', 'comments_rank', 'likes_rank', 'followers_rank', 'recent_shitstorm', 'regular_clickbait', 'regular_fsk18', 'followers_last_month', 'posts_last_month', 'stories_last_month', 'total_igtv', 'total_posts', 'verified', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['channel']
    ordering = ['channel']
    list_select_related = ['channel']
    autocomplete_fields = ['channel']

class TikTokDetailAdmin(admin.ModelAdmin):
    list_display = ('channel', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['channel']
    ordering = ['channel']
    list_select_related = ['channel']
    autocomplete_fields = ['channel']

class TwitterDetailAdmin(admin.ModelAdmin):
    list_display = ('channel', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['channel']
    ordering = ['channel']
    list_select_related = ['channel']
    autocomplete_fields = ['channel']

class TwitchDetailAdmin(admin.ModelAdmin):
    list_display = ('channel', 'created', 'updated_at')
    list_filter = ['created', 'updated_at']
    search_fields = ['channel']
    ordering = ['channel']
    list_select_related = ['channel']
    autocomplete_fields = ['channel']

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'color', 'url')
    search_fields = ('name', 'branch', 'color', 'url')
    list_filter = ('name', 'branch', 'color', 'url')
    list_select_related = True

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(YouTubeDetail, YouTubeDetailAdmin)
admin.site.register(InstagramDetail, InstagramDetailAdmin)
admin.site.register(TikTokDetail, TikTokDetailAdmin)
admin.site.register(TwitterDetail, TwitterDetailAdmin)
admin.site.register(TwitchDetail, TwitchDetailAdmin)
admin.site.register(HistoryEntry, HistoryEntryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostAnalytic, PostAnalyticAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Milestone, MilestoneAdmin)