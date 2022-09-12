import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from configdb.models import Artist, Channel, YouTubeDetail, InstagramDetail, TikTokDetail, TwitterDetail, TwitchDetail, HistoryEntry, Post, PostAnalytic, Brand, Coupon, Milestone

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

class ChannelType(DjangoObjectType):
    class Meta:
        model = Channel

class YouTubeDetailType(DjangoObjectType):
    class Meta:
        model = YouTubeDetail

class InstagramDetailType(DjangoObjectType):
    class Meta:
        model = InstagramDetail

class TikTokDetailType(DjangoObjectType):
    class Meta:
        model = TikTokDetail

class TwitterDetailType(DjangoObjectType):
    class Meta:
        model = TwitterDetail

class TwitchDetailType(DjangoObjectType):
    class Meta:
        model = TwitchDetail

class HistoryEntryType(DjangoObjectType):
    class Meta:
        model = HistoryEntry

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class PostAnalyticType(DjangoObjectType):
    class Meta:
        model = PostAnalytic

class BrandType(DjangoObjectType):
    class Meta:
        model = Brand

class CouponType(DjangoObjectType):
    class Meta:
        model = Coupon

class MilestoneType(DjangoObjectType):
    class Meta:
        model = Milestone

class Query(graphene.ObjectType):
    artists = graphene.List(ArtistType, search=graphene.String())
    channels = graphene.List(ChannelType, search=graphene.String())
    youtube_details = graphene.List(YouTubeDetailType, search=graphene.String())
    instagram_details = graphene.List(InstagramDetailType, search=graphene.String())
    tiktok_details = graphene.List(TikTokDetailType, search=graphene.String())
    twitter_details = graphene.List(TwitterDetailType, search=graphene.String())
    twitch_details = graphene.List(TwitchDetailType, search=graphene.String())
    history_entries = graphene.List(HistoryEntryType, search=graphene.String())
    posts = graphene.List(PostType, search=graphene.String())
    post_analytics = graphene.List(PostAnalyticType, search=graphene.String())
    brands = graphene.List(BrandType, search=graphene.String())
    coupons = graphene.List(CouponType, search=graphene.String())
    milestones = graphene.List(MilestoneType, search=graphene.String())

    def resolve_artists(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(name__icontains=search) |
                Q(avatar_url__icontains=search)
            )
            return Artist.objects.filter(filter)

        return Artist.objects.all()

    def resolve_channels(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(name__icontains=search) |
                Q(avatar_url__icontains=search) |
                Q(chanel_type__icontains=search)
            )
            return Channel.objects.filter(filter)

        return Channel.objects.all()

    def resolve_youtube_details(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(channel__name__icontains=search)
            )
            return YouTubeDetail.objects.filter(filter)

        return YouTubeDetail.objects.all()

    def resolve_instagram_details(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(channel__name__icontains=search)
            )
            return InstagramDetail.objects.filter(filter)

        return InstagramDetail.objects.all()

    def resolve_tiktok_details(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(channel__name__icontains=search)
            )
            return TikTokDetail.objects.filter(filter)

        return TikTokDetail.objects.all()

    def resolve_twitter_details(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(channel__name__icontains=search)
            )
            return TwitterDetail.objects.filter(filter)

        return TwitterDetail.objects.all()

    def resolve_twitch_details(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(channel__name__icontains=search)
            )
            return TwitchDetail.objects.filter(filter)

        return TwitchDetail.objects.all()

    def resolve_history_entries(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(followers__icontains=search) |
                Q(timestamp__icontains=search)
            )
            return HistoryEntry.objects.filter(filter)

        return HistoryEntry.objects.all()

    def resolve_posts(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(content__icontains=search) |
                Q(description__icontains=search) |
                Q(published__icontains=search)
            )
            return Post.objects.filter(filter)

        return Post.objects.all()

    def resolve_post_analytics(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(age__icontains=search) |
                Q(post_type__icontains=search) |
                Q(channel__name__icontains=search) |
                Q(post__description__icontains=search) |
                Q(value__icontains=search)
            )
            return PostAnalytic.objects.filter(filter)

        return PostAnalytic.objects.all()

    def resolve_brands(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(branch__icontains=search) |
                Q(color__icontains=search) |
                Q(name__icontains=search) |
                Q(url__icontains=search)
            )
            return Brand.objects.filter(filter)

        return Brand.objects.all()

    def resolve_coupons(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(code__icontains=search) |
                Q(discount__icontains=search) |
                Q(terms__icontains=search) |
                Q(timestamp__icontains=search) |
                Q(url__icontains=search) |
                Q(valid__icontains=search) |
                Q(valid_until__icontains=search) |
                Q(artist__name__icontains=search) |
                Q(brand__name__icontains=search)
            )
            return Coupon.objects.filter(filter)

        return Coupon.objects.all()

    def resolve_milestones(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(followers__icontains=search) |
                Q(expected_time__icontains=search) |
                Q(channel__name__icontains=search)
            )
            return Milestone.objects.filter(filter)

        return Milestone.objects.all()

schema = graphene.Schema(query=Query)