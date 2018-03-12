# Copyright (C) 2015 Twitter, Inc.

"""Container for all creative management logic used by the Ads API SDK."""

from requests.exceptions import HTTPError

from twitter_ads import API_VERSION
from twitter_ads.enum import TRANSFORM
from twitter_ads.http import Request
from twitter_ads.resource import resource_property, Resource, Persistence, Analytics


class PromotedAccount(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/promoted_accounts'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/promoted_accounts/{id}'


# promoted account properties
# read-only
resource_property(PromotedAccount, 'approval_status', readonly=True)
resource_property(PromotedAccount, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(PromotedAccount, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(PromotedAccount, 'entity_status', readonly=True)
resource_property(PromotedAccount, 'id', readonly=True)
resource_property(PromotedAccount, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(PromotedAccount, 'line_item_id')
resource_property(PromotedAccount, 'user_id')


class PromotedTweet(Resource, Persistence, Analytics):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/promoted_tweets'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/promoted_tweets/{id}'

    def save(self):
        """
        Saves or updates the current object instance depending on the
        presence of `object.id`.
        """
        params = self.to_params()
        if 'tweet_id' in params:
            params['tweet_ids'] = [params['tweet_id']]
            del params['tweet_id']

        if self.id:
            raise HTTPError("Method PUT not allowed.")

        resource = self.RESOURCE_COLLECTION.format(account_id=self.account.id)
        response = Request(self.account.client, 'post', resource, params=params).perform()
        return self.from_response(response.body['data'][0])


# promoted tweet properties
# read-only
resource_property(PromotedTweet, 'approval_status', readonly=True)
resource_property(PromotedTweet, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(PromotedTweet, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(PromotedTweet, 'entity_status', readonly=True)
resource_property(PromotedTweet, 'id', readonly=True)
resource_property(PromotedTweet, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(PromotedTweet, 'line_item_id')
resource_property(PromotedTweet, 'tweet_id')  # SDK limitation


class Video(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/videos'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/videos/{id}'


# video properties
# read-only
resource_property(Video, 'aspect_ratio', readonly=True)
resource_property(Video, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(Video, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(Video, 'duration', readonly=True, transform=TRANSFORM.INT)
resource_property(Video, 'id', readonly=True)
resource_property(Video, 'media_key', readonly=True)
resource_property(Video, 'poster_url', readonly=True)
resource_property(Video, 'preview_url', readonly=True)
resource_property(Video, 'ready_to_tweet', readonly=True, transform=TRANSFORM.BOOL)
resource_property(Video, 'reasons_not_servable', readonly=True, transform=TRANSFORM.LIST)
resource_property(Video, 'tweeted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(Video, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(Video, 'description')
resource_property(Video, 'poster_image_media_id')
resource_property(Video, 'title')
resource_property(Video, 'video_media_id')


class AccountMedia(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/account_media'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/account_media/{id}'


# Account Media properties
# read-only
resource_property(AccountMedia, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(AccountMedia, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(AccountMedia, 'id', readonly=True)
resource_property(AccountMedia, 'media_url', readonly=True)
resource_property(AccountMedia, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(AccountMedia, 'creative_type')
resource_property(AccountMedia, 'media_id')
resource_property(AccountMedia, 'video_id')


class MediaCreative(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/media_creatives'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/media_creatives/{id}'


# Media Creative properties
# read-only

resource_property(MediaCreative, 'approval_status', readonly=True)
resource_property(MediaCreative, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(MediaCreative, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(MediaCreative, 'id', readonly=True)
resource_property(MediaCreative, 'serving_status', readonly=True)
resource_property(MediaCreative, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(MediaCreative, 'account_media_id')
resource_property(MediaCreative, 'landing_url')
resource_property(MediaCreative, 'line_item_id')


class WebsiteCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/website'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/website/{id}'


# website card properties
# read-only
resource_property(WebsiteCard, 'card_type', readonly=True)
resource_property(WebsiteCard, 'card_uri', readonly=True)
resource_property(WebsiteCard, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(WebsiteCard, 'id', readonly=True)
resource_property(WebsiteCard, 'image', readonly=True)
resource_property(WebsiteCard, 'image_display_height', readonly=True)
resource_property(WebsiteCard, 'image_display_width', readonly=True)
resource_property(WebsiteCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(WebsiteCard, 'preview_url', readonly=True)
resource_property(WebsiteCard, 'website_dest_url', readonly=True)
resource_property(WebsiteCard, 'website_display_url', readonly=True)
resource_property(WebsiteCard, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(WebsiteCard, 'image_media_id')
resource_property(WebsiteCard, 'name')
resource_property(WebsiteCard, 'website_title')
resource_property(WebsiteCard, 'website_url')


class VideoWebsiteCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/video_website'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/video_website/{id}'


# video website card properties
# read-only
resource_property(VideoWebsiteCard, 'account_id', readonly=True)
resource_property(VideoWebsiteCard, 'card_type', readonly=True)
resource_property(VideoWebsiteCard, 'card_uri', readonly=True)
resource_property(VideoWebsiteCard, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(VideoWebsiteCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(VideoWebsiteCard, 'id', readonly=True)
resource_property(VideoWebsiteCard, 'preview_url', readonly=True)
resource_property(VideoWebsiteCard, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(VideoWebsiteCard, 'video_content_id', readonly=True)
resource_property(VideoWebsiteCard, 'video_height', readonly=True)
resource_property(VideoWebsiteCard, 'video_hls_url', readonly=True)
resource_property(VideoWebsiteCard, 'video_owner_id', readonly=True)
resource_property(VideoWebsiteCard, 'video_poster_height', readonly=True)
resource_property(VideoWebsiteCard, 'video_poster_url', readonly=True)
resource_property(VideoWebsiteCard, 'video_poster_width', readonly=True)
resource_property(VideoWebsiteCard, 'video_url', readonly=True)
resource_property(VideoWebsiteCard, 'video_width', readonly=True)
resource_property(VideoWebsiteCard, 'website_dest_url', readonly=True)
resource_property(VideoWebsiteCard, 'website_display_url', readonly=True)
# writable
resource_property(VideoWebsiteCard, 'name')
resource_property(VideoWebsiteCard, 'title')
resource_property(VideoWebsiteCard, 'video_id')
resource_property(VideoWebsiteCard, 'website_url')


class ImageAppDownloadCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/image_app_download'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/image_app_download/{id}'


# image app download card properties
# read-only
resource_property(ImageAppDownloadCard, 'id', readonly=True)
resource_property(ImageAppDownloadCard, 'image_display_height', readonly=True)
resource_property(ImageAppDownloadCard, 'image_display_width', readonly=True)
resource_property(ImageAppDownloadCard, 'wide_app_image', readonly=True)
resource_property(ImageAppDownloadCard, 'card_uri', readonly=True)
resource_property(ImageAppDownloadCard, 'card_type', readonly=True)
resource_property(ImageAppDownloadCard, 'preview_url', readonly=True)
resource_property(ImageAppDownloadCard, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(ImageAppDownloadCard, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(ImageAppDownloadCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
# writable
resource_property(ImageAppDownloadCard, 'app_country_code')
resource_property(ImageAppDownloadCard, 'app_cta')
resource_property(ImageAppDownloadCard, 'iphone_app_id')
resource_property(ImageAppDownloadCard, 'iphone_deep_link')
resource_property(ImageAppDownloadCard, 'ipad_app_id')
resource_property(ImageAppDownloadCard, 'ipad_deep_link')
resource_property(ImageAppDownloadCard, 'googleplay_app_id')
resource_property(ImageAppDownloadCard, 'googleplay_deep_link')
resource_property(ImageAppDownloadCard, 'name')
resource_property(ImageAppDownloadCard, 'wide_app_image_media_id')


class VideoAppDownloadCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/video_app_download'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/video_app_download/{id}'


# video app download card properties
# read-only
resource_property(VideoAppDownloadCard, 'card_uri', readonly=True)
resource_property(VideoAppDownloadCard, 'card_type', readonly=True)
resource_property(VideoAppDownloadCard, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(VideoAppDownloadCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(VideoAppDownloadCard, 'id', readonly=True)
resource_property(VideoAppDownloadCard, 'preview_url', readonly=True)
resource_property(VideoAppDownloadCard, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(VideoAppDownloadCard, 'video_content_id', readonly=True)
resource_property(VideoAppDownloadCard, 'video_hls_url', readonly=True)
resource_property(VideoAppDownloadCard, 'video_owner_id', readonly=True)
resource_property(VideoAppDownloadCard, 'video_poster_url', readonly=True)
resource_property(VideoAppDownloadCard, 'video_url', readonly=True)
# writable
resource_property(VideoAppDownloadCard, 'app_country_code')
resource_property(VideoAppDownloadCard, 'app_cta')
resource_property(VideoAppDownloadCard, 'image_media_id')
resource_property(VideoAppDownloadCard, 'ipad_app_id')
resource_property(VideoAppDownloadCard, 'ipad_deep_link')
resource_property(VideoAppDownloadCard, 'iphone_app_id')
resource_property(VideoAppDownloadCard, 'iphone_deep_link')
resource_property(VideoAppDownloadCard, 'googleplay_app_id')
resource_property(VideoAppDownloadCard, 'googleplay_deep_link')
resource_property(VideoAppDownloadCard, 'name')
resource_property(VideoAppDownloadCard, 'video_id')


class ImageConversationCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/image_conversation'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/image_conversation/{id}'


# image conversation card properties
# read-only
resource_property(ImageConversationCard, 'card_type', readonly=True)
resource_property(ImageConversationCard, 'card_uri', readonly=True)
resource_property(ImageConversationCard, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(ImageConversationCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(ImageConversationCard, 'id', readonly=True)
resource_property(ImageConversationCard, 'image', readonly=True)
resource_property(ImageConversationCard, 'preview_url', readonly=True)
resource_property(ImageConversationCard, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(ImageConversationCard, 'cover_image_id')
resource_property(ImageConversationCard, 'fouth_cta')
resource_property(ImageConversationCard, 'fouth_cta_tweet')
resource_property(ImageConversationCard, 'image_media_id')
resource_property(ImageConversationCard, 'first_cta')
resource_property(ImageConversationCard, 'first_cta_tweet')
resource_property(ImageConversationCard, 'name')
resource_property(ImageConversationCard, 'second_cta')
resource_property(ImageConversationCard, 'second_cta_tweet')
resource_property(ImageConversationCard, 'thank_you_text')
resource_property(ImageConversationCard, 'thank_you_url')
resource_property(ImageConversationCard, 'third_cta')
resource_property(ImageConversationCard, 'third_cta_tweet')
resource_property(ImageConversationCard, 'title')


class VideoConversationCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/video_conversation'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/video_conversation/{id}'


# video conversation card properties
# read-only

resource_property(VideoConversationCard, 'card_uri', readonly=True)
resource_property(VideoConversationCard, 'card_type', readonly=True)
resource_property(VideoConversationCard, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(VideoConversationCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(VideoConversationCard, 'id', readonly=True)
resource_property(VideoConversationCard, 'preview_url', readonly=True)
resource_property(VideoConversationCard, 'video_url', readonly=True)
resource_property(VideoConversationCard, 'video_poster_url', readonly=True)
resource_property(VideoConversationCard, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(ImageConversationCard, 'cover_image_id')
resource_property(ImageConversationCard, 'cover_video_id')
resource_property(ImageConversationCard, 'fouth_cta')
resource_property(ImageConversationCard, 'fouth_cta_tweet')
resource_property(ImageConversationCard, 'image_media_id')
resource_property(ImageConversationCard, 'first_cta')
resource_property(ImageConversationCard, 'first_cta_tweet')
resource_property(ImageConversationCard, 'name')
resource_property(ImageConversationCard, 'second_cta')
resource_property(ImageConversationCard, 'second_cta_tweet')
resource_property(ImageConversationCard, 'thank_you_text')
resource_property(ImageConversationCard, 'thank_you_url')
resource_property(ImageConversationCard, 'third_cta')
resource_property(ImageConversationCard, 'third_cta_tweet')
resource_property(ImageConversationCard, 'title')
resource_property(ImageConversationCard, 'video_id')


class ScheduledTweet(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/scheduled_tweets'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/scheduled_tweets/{id}'
    PREVIEW = '/' + API_VERSION + '/accounts/{account_id}/scheduled_tweets/preview/{id}'

    def preview(self):
        """
        Returns an HTML preview for a Scheduled Tweet.
        """
        if self.id:
            resource = self.PREVIEW
            resource = resource.format(account_id=self.account.id, id=self.id)
            response = Request(self.account.client, 'get', resource).perform()
            return response.body['data']


# scheduled tweet properties
# read-only
resource_property(ScheduledTweet, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(ScheduledTweet, 'completed_at', read_only=True, transform=TRANSFORM.TIME)
resource_property(ScheduledTweet, 'id', read_only=True)
resource_property(ScheduledTweet, 'id_str', read_only=True)
resource_property(ScheduledTweet, 'media_keys', readonly=True, transform=TRANSFORM.LIST)
resource_property(ScheduledTweet, 'scheduled_status', read_only=True)
resource_property(ScheduledTweet, 'tweet_id', readonly=True)
resource_property(ScheduledTweet, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(ScheduledTweet, 'user_id', read_only=True)
# writable
resource_property(ScheduledTweet, 'as_user_id')
resource_property(ScheduledTweet, 'card_uri')
resource_property(ScheduledTweet, 'media_ids', transform=TRANSFORM.LIST)
resource_property(ScheduledTweet, 'nullcast', transform=TRANSFORM.BOOL)
resource_property(ScheduledTweet, 'scheduled_at', transform=TRANSFORM.TIME)
resource_property(ScheduledTweet, 'text')


class MediaLibrary(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/media_library'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/media_library/{id}'

    def reload(self, **kwargs):
        if not self.media_key:
            return self

        resource = self.RESOURCE.format(account_id=self.account.id, id=self.media_key)
        response = Request(self.account.client, 'get', resource, params=kwargs).perform()

        return self.from_response(response.body['data'])

    def save(self):
        if self.media_key:
            method = 'put'
            resource = self.RESOURCE.format(account_id=self.account.id, id=self.media_key)
        else:
            method = 'post'
            resource = self.RESOURCE_COLLECTION.format(account_id=self.account.id)

        response = Request(
            self.account.client, method,
            resource, params=self.to_params()).perform()

        return self.from_response(response.body['data'])

    def delete(self):
        resource = self.RESOURCE.format(account_id=self.account.id, id=self.media_key)
        response = Request(self.account.client, 'delete', resource).perform()
        self.from_response(response.body['data'])


# media library properties
# read-only
resource_property(MediaLibrary, 'aspect_ratio', readonly=True)
resource_property(MediaLibrary, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(MediaLibrary, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(MediaLibrary, 'duration', readonly=True, transform=TRANSFORM.INT)
resource_property(MediaLibrary, 'media_status', readonly=True)
resource_property(MediaLibrary, 'media_type', readonly=True)
resource_property(MediaLibrary, 'media_url', readonly=True)
resource_property(MediaLibrary, 'tweeted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(MediaLibrary, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
# writable
resource_property(MediaLibrary, 'media_category')
resource_property(MediaLibrary, 'media_id')
resource_property(MediaLibrary, 'media_key')
resource_property(MediaLibrary, 'description')
resource_property(MediaLibrary, 'file_name')
resource_property(MediaLibrary, 'name')
resource_property(MediaLibrary, 'poster_image_media_id')
resource_property(MediaLibrary, 'poster_image_media_key')
resource_property(MediaLibrary, 'title')


class PollCard(Resource, Persistence):

    PROPERTIES = {}

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/poll'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/poll/{id}'


# poll card properties
# read-only
resource_property(PollCard, 'card_type', readonly=True)
resource_property(PollCard, 'card_uri', readonly=True)
resource_property(PollCard, 'content_duration_seconds', readonly=True)
resource_property(PollCard, 'created_at', readonly=True)
resource_property(PollCard, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(PollCard, 'end_time', readonly=True)
resource_property(PollCard, 'id', readonly=True)
resource_property(PollCard, 'image', readonly=True)
resource_property(PollCard, 'image_display_height', readonly=True)
resource_property(PollCard, 'image_display_width', readonly=True)
resource_property(PollCard, 'preview_url', readonly=True)
resource_property(PollCard, 'start_time', readonly=True)
resource_property(PollCard, 'updated_at', readonly=True)
resource_property(PollCard, 'video_height', readonly=True)
resource_property(PollCard, 'video_hls_url', readonly=True)
resource_property(PollCard, 'video_poster_height', readonly=True)
resource_property(PollCard, 'video_poster_url', readonly=True)
resource_property(PollCard, 'video_poster_width', readonly=True)
resource_property(PollCard, 'video_url', readonly=True)
resource_property(PollCard, 'video_width', readonly=True)
# writable
resource_property(PollCard, 'duration_in_minutes')
resource_property(PollCard, 'first_choice')
resource_property(PollCard, 'fourth_choice')
resource_property(PollCard, 'media_key')
resource_property(PollCard, 'name')
resource_property(PollCard, 'second_choice')
resource_property(PollCard, 'third_choice')


class CardsFetch(Resource):

    PROPERTIES = {}

    FETCH_URI = '/' + API_VERSION + '/accounts/{account_id}/cards'
    FETCH_ID = '/' + API_VERSION + '/accounts/{account_id}/cards/all/{id}'

    def all(klass):
        raise AttributeError("'CardsFetch' object has no attribute 'all'")

    def load(klass, account, card_uri=None, card_id=None, with_deleted=None):
        # check whether both are specified or neither are specified
        if all([card_uri, card_id]) or not any([card_uri, card_id]):
            raise ValueError('card_uri and card_id are exclusive parameters. ' +
                             'Please supply one or the other, but not both.')
        params = {}
        if card_uri:
            params['card_uri'] = card_uri
            resource = klass.FETCH_URI.format(account_id=account.id)
        else:
            resource = klass.FETCH_ID.format(account_id=account.id, id=card_id)
        if with_deleted:
            params['with_deleted'] = 'true'
        response = Request(account.client, 'get', resource, params=params).perform()
        return klass.from_response(response.body['data'])

    def reload(self):
        if self.id:
            self.load(self.account, card_id=self.id)


# card properties
# read-only
resource_property(CardsFetch, 'app_country_code', readonly=True)
resource_property(CardsFetch, 'app_cta', readonly=True)
resource_property(CardsFetch, 'card_type', readonly=True)
resource_property(CardsFetch, 'card_uri', readonly=True)
resource_property(CardsFetch, 'content_duration_seconds', readonly=True)
resource_property(CardsFetch, 'created_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(CardsFetch, 'deleted', readonly=True, transform=TRANSFORM.BOOL)
resource_property(CardsFetch, 'duration_in_minutes', readonly=True)
resource_property(CardsFetch, 'end_time', readonly=True, transform=TRANSFORM.TIME)
resource_property(CardsFetch, 'first_choice', readonly=True)
resource_property(CardsFetch, 'first_cta', readonly=True)
resource_property(CardsFetch, 'first_cta_tweet', readonly=True)
resource_property(CardsFetch, 'first_cta_welcome_message_id', readonly=True)
resource_property(CardsFetch, 'fouth_choice', readonly=True)
resource_property(CardsFetch, 'fouth_cta', readonly=True)
resource_property(CardsFetch, 'fouth_cta_tweet', readonly=True)
resource_property(CardsFetch, 'fourth_cta_welcome_message_id', readonly=True)
resource_property(CardsFetch, 'googleplay_app_id', readonly=True)
resource_property(CardsFetch, 'googleplay_deep_link', readonly=True)
resource_property(CardsFetch, 'id', readonly=True)
resource_property(CardsFetch, 'image', readonly=True)
resource_property(CardsFetch, 'image_display_height', readonly=True)
resource_property(CardsFetch, 'image_display_width', readonly=True)
resource_property(CardsFetch, 'ipad_app_id', readonly=True)
resource_property(CardsFetch, 'ipad_deep_link', readonly=True)
resource_property(CardsFetch, 'iphone_app_id', readonly=True)
resource_property(CardsFetch, 'iphone_deep_link', readonly=True)
resource_property(CardsFetch, 'name', readonly=True)
resource_property(CardsFetch, 'preview_url', readonly=True)
resource_property(CardsFetch, 'recipient_user_id', readonly=True)
resource_property(CardsFetch, 'second_choice', readonly=True)
resource_property(CardsFetch, 'second_cta', readonly=True)
resource_property(CardsFetch, 'second_cta_tweet', readonly=True)
resource_property(CardsFetch, 'second_cta_welcome_message_id', readonly=True)
resource_property(CardsFetch, 'start_time', readonly=True, transform=TRANSFORM.TIME)
resource_property(CardsFetch, 'thank_you_text', readonly=True)
resource_property(CardsFetch, 'thank_you_url', readonly=True)
resource_property(CardsFetch, 'third_choice', readonly=True)
resource_property(CardsFetch, 'third_cta', readonly=True)
resource_property(CardsFetch, 'third_cta_tweet', readonly=True)
resource_property(CardsFetch, 'third_cta_welcome_message_id', readonly=True)
resource_property(CardsFetch, 'title', readonly=True)
resource_property(CardsFetch, 'updated_at', readonly=True, transform=TRANSFORM.TIME)
resource_property(CardsFetch, 'video_content_id', readonly=True)
resource_property(CardsFetch, 'video_height', readonly=True)
resource_property(CardsFetch, 'video_hls_url', readonly=True)
resource_property(CardsFetch, 'video_owner_id', readonly=True)
resource_property(CardsFetch, 'video_poster_height', readonly=True)
resource_property(CardsFetch, 'video_poster_url', readonly=True)
resource_property(CardsFetch, 'video_poster_width', readonly=True)
resource_property(CardsFetch, 'video_width', readonly=True)
resource_property(CardsFetch, 'video_url', readonly=True)
resource_property(CardsFetch, 'website_dest_url', readonly=True)
resource_property(CardsFetch, 'website_display_url', readonly=True)
resource_property(CardsFetch, 'website_shortened_url', readonly=True)
resource_property(CardsFetch, 'website_title', readonly=True)
resource_property(CardsFetch, 'website_url', readonly=True)
resource_property(CardsFetch, 'wide_app_image', readonly=True)
