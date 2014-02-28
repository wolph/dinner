# vim: set fileencoding=utf-8 :
import models
from django.contrib import admin


class AdSkuAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'purchase_template',
        'manage_template',
        'ad_space',
        'priority',
        'price_per_click',
        'price_per_impression',
        'click_discounts',
        'impression_discounts',
        'karma',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'link_title',
        'link_url',
        'asset_id',
        'template_id',
        'revision_date',
        'cache_timeout',
        'storage_id',
    )


class CalendarAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'default_date',
        'default_view',
        'visitor_cache_timeout',
        'template_id_month',
        'template_id_week',
        'template_id_day',
        'template_id_event',
        'template_id_event_edit',
        'template_id_search',
        'template_id_print_month',
        'template_id_print_week',
        'template_id_print_day',
        'template_id_print_event',
        'group_id_event_edit',
        'group_id_subscribed',
        'subscriber_notify_offset',
        'sort_events_by',
        'list_view_page_interval',
        'template_id_list',
        'template_id_print_list',
        'ical_interval',
        'workflow_id_commit',
        'ical_feeds',
    )


class CarouselAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'items',
        'template_id',
        'slide_width',
    )


class DataFormAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'acknowledgement',
        'mail_data',
        'email_template_id',
        'acknowlegement_template_id',
        'list_template_id',
        'asset_id',
        'template_id',
        'default_view',
        'revision_date',
        'group_to_view_entries',
        'mail_attachments',
        'use_captcha',
        'store_data',
        'field_configuration',
        'tab_configuration',
        'workflow_id_add_entry',
        'html_area_rich_editor',
    )


class DataFormEntryAdmin(admin.ModelAdmin):

    list_display = (
        'data_form_entry_id',
        'user',
        'username',
        'ip_address',
        'asset_id',
        'entry_data',
        'submission_date',
    )
    list_filter = ('user', 'submission_date')


class DataTableAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'data',
        'template_id',
    )


class EMSBadgeAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'price',
        'seats_available',
        'related_badge_groups',
        'template_id',
        'early_bird_price',
        'early_bird_price_end_date',
        'pre_registration_price',
        'pre_registration_price_end_date',
    )


class EMSBadgeGroupAdmin(admin.ModelAdmin):

    list_display = (u'id', 'badge_group', 'ems_asset_id', 'name')
    list_filter = ('badge_group',)
    search_fields = ('name',)


class EMSEventMetaFieldAdmin(admin.ModelAdmin):

    list_display = (
        'field_id',
        'asset_id',
        'label',
        'data_type',
        'visible',
        'required',
        'possible_values',
        'default_values',
        'sequence_number',
    )


class EMSRegistrantAdmin(admin.ModelAdmin):

    list_display = (
        'badge_id',
        'user',
        'badge_number',
        'badge_asset_id',
        'ems_asset_id',
        'name',
        'address1',
        'address2',
        'address3',
        'city',
        'state',
        'zipcode',
        'country',
        'phone_number',
        'organization',
        'email',
        'notes',
        'purchase_complete',
        'has_checked_in',
        'transaction_item_id',
    )
    list_filter = ('user',)
    search_fields = ('name',)


class EMSRegistrantRibbonAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'badge_id',
        'ribbon_asset_id',
        'transaction_item_id',
    )


class EMSRegistrantTicketAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'badge_id',
        'ticket_asset_id',
        'purchase_complete',
        'transaction_item_id',
    )


class EMSRegistrantTokenAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'badge_id',
        'token_asset_id',
        'quantity',
        'transaction_item_ids',
    )


class EMSRibbonAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'percentage_discount',
        'price',
    )


class EMSTicketAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'price',
        'seats_available',
        'start_date',
        'duration',
        'event_number',
        'location',
        'related_badge_groups',
        'related_ribbons',
        'event_meta_data',
    )
    list_filter = ('start_date',)


class EMSTokenAdmin(admin.ModelAdmin):

    list_display = (u'id', 'asset_id', 'revision_date', 'price')


class EventAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'feed_id',
        'feed_uid',
        'start_date',
        'end_date',
        'user_defined1',
        'user_defined2',
        'user_defined3',
        'user_defined4',
        'user_defined5',
        'recur_id',
        'description',
        'start_time',
        'end_time',
        'related_links',
        'location',
        'storage_id',
        'time_zone',
        'i_cal_sequence_number',
        'sequence_number',
    )
    list_filter = ('start_date', 'end_date')


class EventManagementSystemAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'group_to_approve_events',
        'timezone',
        'template_id',
        'badge_builder_template_id',
        'lookup_registrant_template_id',
        'print_badge_template_id',
        'print_ticket_template_id',
        'badge_instructions',
        'ribbon_instructions',
        'ticket_instructions',
        'token_instructions',
        'registration_staff_group',
        'schedule_template_id',
        'schedule_columns_per_page',
    )
    list_filter = ('registration_staff_group',)


class EventRecurAdmin(admin.ModelAdmin):

    list_display = (
        'recur_id',
        'recur_type',
        'pattern',
        'start_date',
        'end_date',
    )
    list_filter = ('start_date',)


class EventRelatedlinkAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'eventlink_id',
        'asset_id',
        'link_url',
        'linktext',
        'group_id_view',
        'sequence_number',
    )


class FileAssetAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'storage_id',
        'filename',
        'template_id',
        'revision_date',
        'cache_timeout',
    )


class FlatDiscountAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'template_id',
        'must_spend',
        'percentage_discount',
        'price_discount',
        'thank_you_message',
    )


class FolderAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'template_id',
        'revision_date',
        'visitor_cache_timeout',
        'sort_alphabetically',
        'sort_order',
    )


class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'group_id_add_comment',
        'group_id_add_file',
        'image_resolutions',
        'image_view_size',
        'image_thumbnail_size',
        'max_space_per_user',
        'rich_edit_id_comment',
        'template_id_add_archive',
        'template_id_delete_album',
        'template_id_delete_file',
        'template_id_edit_album',
        'template_id_edit_file',
        'template_id_list_albums',
        'template_id_list_albums_rss',
        'template_id_list_files_for_user',
        'template_id_list_files_for_user_rss',
        'template_id_make_shortcut',
        'template_id_search',
        'template_id_view_slideshow',
        'template_id_view_thumbnails',
        'template_id_view_album',
        'template_id_view_album_rss',
        'template_id_view_file',
        'view_album_asset_id',
        'view_default',
        'view_list_order_by',
        'view_list_order_direction',
        'workflow_id_commit',
        'template_id_edit_comment',
        'rich_edit_id_album',
        'rich_edit_id_file',
        'default_files_per_page',
        'image_density',
    )


class GalleryAlbumAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'allow_comments',
        'asset_id_thumbnail',
        'user_defined1',
        'user_defined2',
        'user_defined3',
        'user_defined4',
        'user_defined5',
        'others_can_add',
    )


class GalleryFileAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'user_defined1',
        'user_defined2',
        'user_defined3',
        'user_defined4',
        'user_defined5',
        'views',
        'friends_only',
        'rating',
    )


class GalleryFileCommentAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'comment_id',
        'user',
        'visitor_ip',
        'creation_date',
        'body_text',
    )
    list_filter = ('user', 'creation_date')


class HttpProxyAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'proxied_url',
        'timeout',
        'remove_style',
        'filter_html',
        'follow_external',
        'follow_redirect',
        'cache_http',
        'use_cache',
        'debug',
        'rewrite_urls',
        'search_for',
        'stop_at',
        'cookie_jar_storage_id',
        'asset_id',
        'template_id',
        'revision_date',
        'cache_timeout',
        'use_ampersand',
        'url_pattern_filter',
    )


class ImageAssetAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'thumbnail_size',
        'parameters',
        'revision_date',
        'annotations',
    )


class KBAuthAdmin(admin.ModelAdmin):

    list_display = (u'id', 'username', 'password')


class LayoutAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'template_id',
        'content_positions',
        'assets_to_hide',
        'revision_date',
        'asset_order',
        'mobile_template_id',
    )


class MacroAttendEventAdmin(admin.ModelAdmin):

    list_display = (u'id', 'guid', 'user')
    list_filter = ('user',)


class MailingAdmin(admin.ModelAdmin):

    list_display = (
        'mailing_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'issue_id',
        'asset_id',
        'send_date',
        'configuration',
        'state',
    )
    list_filter = ('date_created', 'last_updated')


class MailingEmailAdmin(admin.ModelAdmin):

    list_display = (
        'mail_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'bounce_reason',
        'status',
        'user',
        'mailing_id',
        'error_message',
        'sent_to',
        'is_test',
        'send_date',
        'recipient_email',
    )
    list_filter = ('date_created', 'last_updated', 'user')


class MailmanManagerAdmin(admin.ModelAdmin):

    list_display = (u'id', 'asset_id', 'revision_date')


class MailmanManagerGroupsInListAdmin(admin.ModelAdmin):

    list_display = (u'id', 'list_id', 'group')
    list_filter = ('group',)


class MailmanManagerListAdmin(admin.ModelAdmin):

    list_display = (
        'list_id',
        'is_alias',
        'list_name',
        'list_title',
        'list_address',
        'extra_addresses',
        'config_overrides',
        'exclude_group',
    )


class MailmanManagerSubscribeConfirmationAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'list_id',
        'confirmation_code',
        'email',
        'date_added',
    )
    list_filter = ('date_added',)


class MapAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'group_id_add_point',
        'map_api_key',
        'map_height',
        'map_width',
        'start_latitude',
        'start_longitude',
        'start_zoom',
        'template_id_edit_point',
        'template_id_view',
        'template_id_view_point',
        'workflow_id_point',
    )


class MapPointAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'latitude',
        'longitude',
        'website',
        'address1',
        'address2',
        'city',
        'state',
        'zip_code',
        'country',
        'phone',
        'fax',
        'email',
        'storage_id_photo',
        'user_defined1',
        'user_defined2',
        'user_defined3',
        'user_defined4',
        'user_defined5',
    )


class MatrixAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'detail_template_id',
        'compare_template_id',
        'search_template_id',
        'categories',
        'asset_id',
        'template_id',
        'revision_date',
        'max_comparisons',
        'max_comparisons_privileged',
        'group_to_add',
        'default_sort',
        'compare_color_no',
        'compare_color_limited',
        'compare_color_costs_extra',
        'compare_color_free_add_on',
        'compare_color_yes',
        'submission_approval_workflow_id',
        'ratings_duration',
        'edit_listing_template_id',
        'screenshots_config_template_id',
        'screenshots_template_id',
        'statistics_cache_timeout',
        'max_comparisons_group',
        'max_comparisons_group_int',
        'max_screenshot_width',
        'max_screenshot_height',
        'listings_cache_timeout',
    )


class MatrixListingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'screenshots',
        'description',
        'version',
        'views',
        'compares',
        'clicks',
        'views_last_ip',
        'compares_last_ip',
        'clicks_last_ip',
        'last_updated',
        'maintainer',
        'manufacturer_name',
        'manufacturer_url',
        'product_url',
        'score',
    )


class MatrixListingAttributeAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'matrix_id',
        'matrix_listing_id',
        'attribute_id',
        'value',
    )


class MatrixListingRatingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'time_stamp',
        'category',
        'rating',
        'listing_id',
        'ip_address',
        'asset_id',
        'user',
    )
    list_filter = ('user',)


class MatrixListingRatingSummaryAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'listing_id',
        'category',
        'mean_value',
        'median_value',
        'count_value',
        'asset_id',
    )


class MatrixAttributeAdmin(admin.ModelAdmin):

    list_display = (
        'attribute_id',
        'category',
        'name',
        'description',
        'field_type',
        'default_value',
        'asset_id',
        'options',
    )
    search_fields = ('name',)


class MessageBoardAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'template_id',
        'revision_date',
        'visitor_cache_timeout',
    )


class MultiSearchAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'template_id',
        'predefined_searches',
        'cache_timeout',
    )


class NavigationAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'assets_to_include',
        'start_type',
        'start_point',
        'descendant_end_point',
        'show_system_pages',
        'show_hidden_pages',
        'show_unprivileged_pages',
        'template_id',
        'ancestor_end_point',
        'revision_date',
        'mime_type',
        'reverse_page_loop',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'newsletter_template_id',
        'my_subscriptions_template_id',
        'newsletter_header',
        'newsletter_footer',
        'newsletter_categories',
    )


class NewsletterCollectionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'view_template_id',
        'recent_issue_count',
    )


class NewsletterSubscriptionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'user',
        'subscriptions',
        'last_time_sent',
    )
    list_filter = ('user',)


class PMProjectAdmin(admin.ModelAdmin):

    list_display = (
        'project_id',
        'asset_id',
        'name',
        'description',
        'start_date',
        'end_date',
        'project_manager',
        'duration_units',
        'hours_per_day',
        'target_budget',
        'percent_complete',
        'parent_id',
        'creation_date',
        'created_by',
        'last_updated_by',
        'last_update_date',
        'project_observer',
    )
    search_fields = ('name',)


class PMTaskAdmin(admin.ModelAdmin):

    list_display = (
        'task_id',
        'project_id',
        'task_name',
        'duration',
        'start_date',
        'end_date',
        'dependants',
        'parent_id',
        'percent_complete',
        'sequence_number',
        'creation_date',
        'created_by',
        'last_updated_by',
        'last_update_date',
        'lag_time',
        'task_type',
    )


class PMTaskResourceAdmin(admin.ModelAdmin):

    list_display = (
        'task_resource_id',
        'task_id',
        'sequence_number',
        'resource_kind',
        'resource_id',
    )


class PMWobjectAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'project_dashboard_template_id',
        'project_display_template_id',
        'gantt_chart_template_id',
        'edit_task_template_id',
        'group_to_add',
        'revision_date',
        'resource_popup_template_id',
        'resource_list_template_id',
    )


class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'exif_data',
        'location',
    )


class PhotoRatingAdmin(admin.ModelAdmin):

    list_display = (u'id', 'asset_id', 'user', 'visitor_ip', 'rating')
    list_filter = ('user',)


class PollAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'active',
        'graph_width',
        'vote_group',
        'question',
        'a1',
        'a2',
        'a3',
        'a4',
        'a5',
        'a6',
        'a7',
        'a8',
        'a9',
        'a10',
        'a11',
        'a12',
        'a13',
        'a14',
        'a15',
        'a16',
        'a17',
        'a18',
        'a19',
        'a20',
        'karma_per_vote',
        'randomize_answers',
        'asset_id',
        'template_id',
        'revision_date',
        'graph_configuration',
        'generate_graph',
    )


class PollAnswerAdmin(admin.ModelAdmin):

    list_display = (u'id', 'answer', 'user', 'ip_address', 'asset_id')
    list_filter = ('user',)


class PostAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'thread_id',
        'username',
        'content',
        'views',
        'content_type',
        'user_defined1',
        'user_defined2',
        'user_defined3',
        'user_defined4',
        'user_defined5',
        'storage_id',
        'rating',
        'revision_date',
        'original_email',
    )


class PostRatingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'user',
        'ip_address',
        'date_of_rating',
        'rating',
    )
    list_filter = ('user',)


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'image1',
        'image2',
        'image3',
        'brochure',
        'manual',
        'warranty',
        'asset_id',
        'template_id',
        'revision_date',
        'cache_timeout',
        'thank_you_message',
        'accessory_json',
        'benefit_json',
        'feature_json',
        'related_json',
        'specification_json',
        'variants_json',
        'is_shipping_required',
    )


class RichEditAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'ask_about_rich_edit',
        'preformatted',
        'editor_width',
        'editor_height',
        'source_editor_width',
        'source_editor_height',
        'use_br',
        'nowrap',
        'remove_line_breaks',
        'npwrap',
        'directionality',
        'toolbar_location',
        'css_file',
        'valid_elements',
        'toolbar_row1',
        'toolbar_row2',
        'toolbar_row3',
        'enable_context_menu',
        'revision_date',
        'disable_rich_editor',
        'inline_popups',
        'allow_media',
    )


class SQLReportAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'db_query1',
        'paginate_after',
        'preprocess_macros1',
        'debug_mode',
        'database_link_id1',
        'placeholder_params1',
        'preprocess_macros2',
        'db_query2',
        'placeholder_params2',
        'database_link_id2',
        'preprocess_macros3',
        'db_query3',
        'placeholder_params3',
        'database_link_id3',
        'preprocess_macros4',
        'db_query4',
        'placeholder_params4',
        'database_link_id4',
        'preprocess_macros5',
        'db_query5',
        'placeholder_params5',
        'database_link_id5',
        'asset_id',
        'template_id',
        'revision_date',
        'cache_timeout',
        'prequery_statements1',
        'prequery_statements2',
        'prequery_statements3',
        'prequery_statements4',
        'prequery_statements5',
        'download_type',
        'download_filename',
        'download_template_id',
        'download_mime_type',
        'download_user_group',
    )


class ShelfAdmin(admin.ModelAdmin):

    list_display = (u'id', 'asset_id', 'revision_date', 'template_id')


class ShortcutAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'override_title',
        'override_description',
        'override_template',
        'override_display_title',
        'override_template_id',
        'shortcut_by_criteria',
        'resolve_multiples',
        'shortcut_criteria',
        'asset_id',
        'template_id',
        'shortcut_to_asset_id',
        'disable_content_lock',
        'revision_date',
        'pref_fields_to_show',
        'pref_fields_to_import',
        'show_reload_icon',
    )


class ShortcutOverrideAdmin(admin.ModelAdmin):

    list_display = (u'id', 'asset_id', 'field_name', 'new_value')


class StockDataAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'template_id',
        'display_template_id',
        'default_stocks',
        'source',
        'failover',
        'revision_date',
    )


class StoryAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'headline',
        'subtitle',
        'byline',
        'location',
        'highlights',
        'story',
        'photo',
    )


class StoryArchiveAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'stories_per_page',
        'group_to_post',
        'template_id',
        'story_template_id',
        'edit_story_template_id',
        'keyword_list_template_id',
        'archive_after',
        'rich_editor_id',
        'approval_workflow_id',
        'photo_width',
    )


class StoryTopicAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'stories_per',
        'stories_short',
        'template_id',
        'story_template_id',
    )


class SubscriptionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'template_id',
        'thank_you_message',
        'price',
        'subscription_group',
        'duration',
        'execute_on_subscription',
        'karma',
        'redeem_subscription_code_template_id',
        'recurring_subscription',
    )


class SubscriptionCodeAdmin(admin.ModelAdmin):

    list_display = ('code', 'batch_id', 'status', 'date_used', 'used_by')


class SubscriptionCodeBatchAdmin(admin.ModelAdmin):

    list_display = (
        'batch_id',
        'name',
        'description',
        'subscription_id',
        'expiration_date',
        'date_created',
    )
    search_fields = ('name',)


class SurveyAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'group_to_take_survey',
        'group_to_edit_survey',
        'group_to_view_reports',
        'overview_template_id',
        'max_responses_per_user',
        'gradebook_template_id',
        'asset_id',
        'template_id',
        'revision_date',
        'survey_edit_template_id',
        'answer_edit_template_id',
        'question_edit_template_id',
        'section_edit_template_id',
        'survey_take_template_id',
        'survey_questions_id',
        'exit_url',
        'survey_json',
        'time_limit',
        'show_progress',
        'show_time_limit',
        'do_after_time_limit',
        'on_survey_end_workflow_id',
        'quiz_mode_summary',
        'survey_summary_template_id',
        'allow_back_btn',
        'feedback_template_id',
        'test_results_template_id',
    )


class SurveyAnswerOldAdmin(admin.ModelAdmin):

    list_display = (
        'survey_id',
        'survey_question_id',
        'survey_answer_id',
        'sequence_number',
        'goto_question',
        'answer',
        'is_correct',
    )


class SurveyOldAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'question_order',
        'group_to_take_survey',
        'group_to_view_reports',
        'mode',
        'survey_id',
        'anonymous',
        'questions_per_page',
        'response_template_id',
        'overview_template_id',
        'max_responses_per_user',
        'questions_per_response',
        'gradebook_template_id',
        'asset_id',
        'template_id',
        'revision_date',
        'default_section_id',
    )


class SurveyQuestionResponseOldAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'survey_id',
        'survey_question_id',
        'survey_answer_id',
        'survey_response_id',
        'response',
        'comment',
        'date_of_response',
    )


class SurveyQuestionTypeAdmin(admin.ModelAdmin):

    list_display = ('question_type', 'answers')


class SurveyQuestionOldAdmin(admin.ModelAdmin):

    list_display = (
        'survey_id',
        'survey_question_id',
        'question',
        'sequence_number',
        'allow_comment',
        'randomize_answers',
        'answer_field_type',
        'goto_question',
        'survey_section_id',
    )


class SurveyResponseAdmin(admin.ModelAdmin):

    list_display = (
        'asset_id',
        'survey_response_id',
        'user',
        'username',
        'ip_address',
        'start_date',
        'end_date',
        'is_complete',
        'anon_id',
        'response_json',
        'revision_date',
    )
    list_filter = ('user',)


class SurveyResponseOldAdmin(admin.ModelAdmin):

    list_display = (
        'survey_id',
        'survey_response_id',
        'user',
        'username',
        'ip_address',
        'start_date',
        'end_date',
        'is_complete',
    )
    list_filter = ('user',)


class SurveySectionOldAdmin(admin.ModelAdmin):

    list_display = (
        'survey_id',
        'survey_section_id',
        'section_name',
        'sequence_number',
    )


class SurveyTempReportAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'survey_response_id',
        'order',
        'section_number',
        'section_name',
        'question_number',
        'question_name',
        'question_comment',
        'answer_number',
        'answer_value',
        'answer_comment',
        'entry_date',
        'is_correct',
        'value',
        'file_storeage_id',
    )


class SurveyTestAdmin(admin.ModelAdmin):

    list_display = (
        'test_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'asset_id',
        'name',
        'test',
    )
    list_filter = ('date_created', 'last_updated')
    search_fields = ('name',)


class SyndicatedContentAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'rss_url',
        'max_headlines',
        'asset_id',
        'template_id',
        'revision_date',
        'has_terms',
        'cache_timeout',
        'process_macro_in_rss_url',
    )


class TTProjectListAdmin(admin.ModelAdmin):

    list_display = (
        'project_id',
        'asset_id',
        'project_name',
        'creation_date',
        'created_by',
        'last_updated_by',
        'last_update_date',
    )


class TTProjectResourceListAdmin(admin.ModelAdmin):

    list_display = (u'id', 'project_id', 'resource_id')


class TTProjectTaskAdmin(admin.ModelAdmin):

    list_display = ('task_id', 'project_id', 'task_name')


class TTReportAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'report_id',
        'asset_id',
        'start_date',
        'end_date',
        'report_complete',
        'resource_id',
        'creation_date',
        'created_by',
        'last_updated_by',
        'last_update_date',
    )


class TTTimeEntryAdmin(admin.ModelAdmin):

    list_display = (
        'entry_id',
        'project_id',
        'task_id',
        'task_date',
        'hours',
        'comments',
        'report_id',
    )


class TTWobjectAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'user_view_template_id',
        'manager_view_template_id',
        'time_row_template_id',
        'pm_asset_id',
        'group_to_manage',
        'revision_date',
        'pm_integration',
    )


class ThingyAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'template_id',
        'default_thing_id',
    )


class ThingyRecordAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'template_id_view',
        'thing_id',
        'thing_fields',
        'thank_you_text',
        'price',
        'duration',
        'field_price',
    )


class ThingyRecordRecordAdmin(admin.ModelAdmin):

    list_display = (
        'record_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'transaction_id',
        'asset_id',
        'expires',
        'user',
        'fields',
        'is_hidden',
        'sent_expires_notice',
    )
    list_filter = ('date_created', 'last_updated', 'user')


class ThingyFieldAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'thing_id',
        'field_id',
        'sequence_number',
        'date_created',
        'created_by',
        'date_updated',
        'updated_by',
        'label',
        'field_type',
        'default_value',
        'possible_values',
        'subtext',
        'status',
        'width',
        'height',
        'vertical',
        'extras',
        'display',
        'view_screen_title',
        'display_in_search',
        'search_in',
        'field_in_other_thing_id',
        'size',
        'pretext',
    )


class ThingyIkgQcHs3rCevOFoHUiU8kgAdmin(admin.ModelAdmin):

    list_display = (
        'thing_data_id',
        'date_created',
        'created_by_id',
        'updated_by_id',
        'updated_by_name',
        'last_updated',
        'ip_address',
        'field_bm1xw0ch6_xw_dmt_ssn_ny_ti_q',
        'field_c_w_cwp_s3rr_dcld1_ck2_vz_wtw',
        'field_es_k_aj8_dshl_miqdq_sw4i_ig',
        'field_7_u_zt5dzr_q_yj_sm_w_epk_cf_xya',
        'field_f_xc7_l2_rn_bqn8f_hej_ez3_ja',
    )


class ThingyThingAdmin(admin.ModelAdmin):

    list_display = (
        'asset_id',
        'thing_id',
        'label',
        'edit_screen_title',
        'edit_instructions',
        'group_id_add',
        'group_id_edit',
        'save_button_label',
        'after_save',
        'edit_template_id',
        'on_add_workflow_id',
        'on_edit_workflow_id',
        'on_delete_workflow_id',
        'group_id_view',
        'view_template_id',
        'default_view',
        'search_screen_title',
        'search_description',
        'group_id_search',
        'group_id_import',
        'group_id_export',
        'search_template_id',
        'things_per_page',
        'sort_by',
        'display',
        'export_meta_data',
        'max_entries_per_user',
    )


class ThreadAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'replies',
        'last_post_id',
        'last_post_date',
        'is_locked',
        'is_sticky',
        'subscription_group',
        'revision_date',
        'karma',
        'karma_scale',
        'karma_rank',
        'thread_rating',
    )
    list_filter = ('subscription_group',)


class ThreadReadAdmin(admin.ModelAdmin):

    list_display = (u'id', 'thread_id', 'user')
    list_filter = ('user',)


class WeatherDataAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'template_id',
        'locations',
        'partner_id',
        'license_key',
    )


class WikiMasterAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'group_to_edit_pages',
        'group_to_administer',
        'rich_editor',
        'front_page_template_id',
        'page_template_id',
        'page_edit_template_id',
        'recent_changes_template_id',
        'most_popular_template_id',
        'page_history_template_id',
        'search_template_id',
        'recent_changes_count',
        'recent_changes_count_front',
        'most_popular_count',
        'most_popular_count_front',
        'thumbnail_size',
        'max_image_size',
        'approval_workflow',
        'use_content_filter',
        'filter_code',
        'by_keyword_template_id',
        'allow_attachments',
    )


class WikiPageAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'content',
        'views',
        'is_protected',
        'action_taken',
        'action_taken_by',
    )


class WorkflowAdmin(admin.ModelAdmin):

    list_display = (
        'workflow_id',
        'title',
        'description',
        'enabled',
        'type',
        'mode',
    )


class WorkflowActivityAdmin(admin.ModelAdmin):

    list_display = (
        'activity_id',
        'workflow_id',
        'title',
        'description',
        'sequence_number',
        'class_name',
    )


class WorkflowActivityDataAdmin(admin.ModelAdmin):

    list_display = (u'id', 'activity_id', 'name', 'value')
    search_fields = ('name',)


class WorkflowInstanceAdmin(admin.ModelAdmin):

    list_display = (
        'instance_id',
        'workflow_id',
        'current_activity_id',
        'priority',
        'class_name',
        'method_name',
        'parameters',
        'running_since',
        'last_update',
        'last_status',
        'no_session',
    )


class WorkflowInstanceScratchAdmin(admin.ModelAdmin):

    list_display = (u'id', 'instance_id', 'name', 'value')
    search_fields = ('name',)


class WorkflowScheduleAdmin(admin.ModelAdmin):

    list_display = (
        'task_id',
        'title',
        'enabled',
        'run_once',
        'minute_of_hour',
        'hour_of_day',
        'day_of_month',
        'month_of_year',
        'day_of_week',
        'workflow_id',
        'class_name',
        'method_name',
        'priority',
        'parameters',
    )


class ZipArchiveAssetAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'template_id',
        'show_page',
        'revision_date',
    )


class AdSkuPurchaseAdmin(admin.ModelAdmin):

    list_display = (
        'ad_sku_purchase_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'is_deleted',
        'clicks_purchased',
        'date_of_purchase',
        'impressions_purchased',
        'transaction_item_id',
        'user',
        'ad_id',
        'stored_image',
    )
    list_filter = ('date_created', 'last_updated', 'user')


class AdSpaceAdmin(admin.ModelAdmin):

    list_display = (
        'ad_space_id',
        'name',
        'title',
        'description',
        'cost_per_impression',
        'minimum_impressions',
        'cost_per_click',
        'minimum_clicks',
        'width',
        'height',
        'group_to_purchase',
    )
    search_fields = ('name',)


class AddressAdmin(admin.ModelAdmin):

    list_display = (
        'address_id',
        'address_book_id',
        'label',
        'first_name',
        'last_name',
        'address1',
        'address2',
        'address3',
        'city',
        'state',
        'country',
        'code',
        'phone_number',
        'organization',
        'email',
    )


class AddressBookAdmin(admin.ModelAdmin):

    list_display = (
        'address_book_id',
        'session_id',
        'user',
        'default_address_id',
    )
    list_filter = ('user',)


class AdvertisementAdmin(admin.ModelAdmin):

    list_display = (
        'ad_id',
        'ad_space_id',
        'owner_user',
        'is_active',
        'title',
        'type',
        'storage_id',
        'ad_text',
        'url',
        'rich_media',
        'border_color',
        'text_color',
        'background_color',
        'clicks',
        'clicks_bought',
        'impressions',
        'impressions_bought',
        'priority',
        'next_in_priority',
        'rendered_ad',
    )
    list_filter = ('owner_user',)


class AnalyticRuleAdmin(admin.ModelAdmin):

    list_display = (
        'rule_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'bucket_name',
        'regexp',
    )
    list_filter = ('date_created', 'last_updated')


class AssetAdmin(admin.ModelAdmin):

    list_display = (
        'asset_id',
        'parent_id',
        'lineage',
        'state',
        'class_name',
        'creation_date',
        'created_by',
        'state_changed',
        'state_changed_by',
        'is_locked_by',
        'is_system',
        'last_exported_as',
    )


class AssetAspectCommentAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'comments',
        'average_comment_rating',
    )


class AssetAspectMailableAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'mail_style_template_id',
    )


class AssetAspectRssFeedAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'items_per_feed',
        'feed_copyright',
        'feed_title',
        'feed_description',
        'feed_image',
        'feed_image_link',
        'feed_image_description',
        'feed_header_links',
    )


class AssetAspectSubscriberAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'subscription_group',
        'subscription_enabled',
        'always_confirm_subscription',
        'allow_anonymous_subscription',
        'confirmation_required_template_id',
        'confirmation_email_template_id',
        'confirmation_email_subject',
        'no_mutation_email_template_id',
        'no_mutation_email_subject',
        'list_name',
        'confirm_mutation_template_id',
    )
    list_filter = ('subscription_group',)


class AssetAspectSubscriberLogAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'request_ip',
        'request_date',
        'confirmation_ip',
        'confirmation_date',
        'user',
        'email',
        'type',
        'anonymous',
        'confirmed',
        'code',
    )
    list_filter = ('user',)


class AssetDataAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'revised_by',
        'tag_id',
        'status',
        'title',
        'menu_title',
        'url',
        'owner_user',
        'group_id_view',
        'group_id_edit',
        'synopsis',
        'new_window',
        'is_hidden',
        'is_package',
        'is_prototype',
        'encrypt_page',
        'asset_size',
        'extra_head_tags',
        'skip_notification',
        'is_exportable',
        'inherit_url_from_parent',
        'last_modified',
        'extra_head_tags_packed',
        'use_packed_head_tags',
    )
    list_filter = ('owner_user',)


class AssetHistoryAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'user',
        'date_stamp',
        'action_taken',
        'url',
    )
    list_filter = ('user',)


class AssetIndexAdmin(admin.ModelAdmin):

    list_display = (
        'asset_id',
        'title',
        'synopsis',
        'url',
        'creation_date',
        'revision_date',
        'owner_user',
        'group_id_view',
        'group_id_edit',
        'lineage',
        'class_name',
        'is_public',
        'keywords',
    )
    list_filter = ('owner_user',)


class AssetKeywordAdmin(admin.ModelAdmin):

    list_display = (u'id', 'keyword', 'asset_id')


class AssetVersionTagAdmin(admin.ModelAdmin):

    list_display = (
        'tag_id',
        'name',
        'is_committed',
        'creation_date',
        'created_by',
        'commit_date',
        'committed_by',
        'is_locked',
        'locked_by',
        'group_to_use',
        'workflow_id',
        'workflow_instance_id',
        'comments',
        'start_time',
        'end_time',
        'is_site_wide',
    )
    list_filter = ('start_time', 'end_time')
    search_fields = ('name',)


class AuthenticationAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'user',
        'auth_method',
        'field_name',
        'password_base64',
    )
    list_filter = ('user',)


class BucketLogAdmin(admin.ModelAdmin):

    list_display = (u'id', 'user', 'bucket', 'duration', 'time_stamp')
    list_filter = ('user', 'time_stamp')


class CacheAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'namespace',
        'cachekey',
        'expires',
        'size',
        'content',
    )


class CartAdmin(admin.ModelAdmin):

    list_display = (
        'cart_id',
        'session_id',
        'shipping_address_id',
        'shipper_id',
        'pos_user',
        'creation_date',
    )
    list_filter = ('pos_user',)


class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        'item_id',
        'cart_id',
        'asset_id',
        'date_added',
        'options',
        'configured_title',
        'shipping_address_id',
        'quantity',
    )
    list_filter = ('date_added',)


class DatabaseLinkAdmin(admin.ModelAdmin):

    list_display = (
        'database_link_id',
        'title',
        'dsn',
        'username',
        'identifier',
        'allowed_keywords',
        'allow_macro_access',
        'additional_parameters',
    )


class DeltaLogAdmin(admin.ModelAdmin):

    list_display = (u'id', 'user', 'asset_id', 'delta', 'time_stamp', 'url')
    list_filter = ('user',)


class DonationAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'default_price',
        'thank_you_message',
        'template_id',
    )


class FilePumpBundleAdmin(admin.ModelAdmin):

    list_display = (
        'bundle_id',
        'sequence_number',
        'date_created',
        'last_updated',
        'bundle_name',
        'last_modified',
        'last_build',
        'js_files',
        'css_files',
        'other_files',
    )
    list_filter = ('date_created', 'last_updated')


class FriendInvitationAdmin(admin.ModelAdmin):

    list_display = (
        'invite_id',
        'inviter_id',
        'friend_id',
        'date_sent',
        'comments',
        'message_id',
    )
    list_filter = ('date_sent',)


class GroupGroupingAdmin(admin.ModelAdmin):

    list_display = (u'id', 'group', 'in_group')
    list_filter = ('group',)


class GroupingAdmin(admin.ModelAdmin):

    list_display = (u'id', 'group', 'user', 'expire_date', 'group_admin')
    list_filter = ('group', 'user')


class GroupAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'expire_offset',
        'karma_threshold',
        'ip_filter',
        'date_created',
        'last_updated',
        'delete_offset',
        'expire_notify_offset',
        'expire_notify_message',
        'expire_notify',
        'scratch_filter',
        'auto_add',
        'auto_delete',
        'database_link_id',
        'group_cache_timeout',
        'db_query',
        'is_editable',
        'show_in_forms',
        'ldap_group',
        'ldap_group_property',
        'ldap_recursive_property',
        'ldap_link_id',
        'ldap_recursive_filter',
        'is_ad_hoc_mail_group',
    )
    raw_id_fields = ('users',)
    search_fields = ('name',)


class ImageColorAdmin(admin.ModelAdmin):

    list_display = (
        'color_id',
        'name',
        'fill_triplet',
        'fill_alpha',
        'stroke_triplet',
        'stroke_alpha',
    )
    search_fields = ('name',)


class ImageFontAdmin(admin.ModelAdmin):

    list_display = ('font_id', 'name', 'storage_id', 'filename')
    search_fields = ('name',)


class ImagePaletteAdmin(admin.ModelAdmin):

    list_display = ('palette_id', 'name')
    search_fields = ('name',)


class ImagePaletteColorAdmin(admin.ModelAdmin):

    list_display = (u'id', 'palette_id', 'color_id', 'palette_order')


class InboxAdmin(admin.ModelAdmin):

    list_display = (
        'message_id',
        'status',
        'date_stamp',
        'completed_on',
        'completed_by',
        'user',
        'group',
        'subject',
        'message',
        'sent_by',
    )
    list_filter = ('user', 'group')


class InboxMessageStateAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'message_id',
        'user',
        'is_read',
        'replied_to',
        'deleted',
    )
    list_filter = ('user',)


class IncrementerAdmin(admin.ModelAdmin):

    list_display = ('incrementer_id', 'next_value')


class KarmaLogAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'user',
        'amount',
        'source',
        'description',
        'date_modified',
    )
    list_filter = ('user',)


class LdapLinkAdmin(admin.ModelAdmin):

    list_display = (
        'ldap_link_id',
        'ldap_link_name',
        'ldap_url',
        'connect_dn',
        'identifier',
        'ldap_user_rdn',
        'ldap_identity',
        'ldap_identity_name',
        'ldap_password_name',
        'ldap_send_welcome_message',
        'ldap_welcome_message',
        'ldap_account_template',
        'ldap_create_account_template',
        'ldap_login_template',
        'ldap_global_recursive_filter',
    )


class MailQueueAdmin(admin.ModelAdmin):

    list_display = ('message_id', 'message', 'to_group', 'is_inbox')


class MetaDataPropertiesAdmin(admin.ModelAdmin):

    list_display = (
        'field_id',
        'field_name',
        'description',
        'field_type',
        'possible_values',
        'default_value',
    )


class MetaDataValuesAdmin(admin.ModelAdmin):

    list_display = (u'id', 'field_id', 'value', 'asset_id')


class PassiveAnalyticsStatusAdmin(admin.ModelAdmin):

    list_display = (u'id', 'start_date', 'end_date', 'running', 'user')
    list_filter = ('start_date', 'end_date', 'user')


class PassiveLogAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'user',
        'asset_id',
        'session_id',
        'time_stamp',
        'url',
    )
    list_filter = ('user',)


class PassiveProfileAOIAdmin(admin.ModelAdmin):

    list_display = (u'id', 'user', 'field_id', 'value', 'count')
    list_filter = ('user',)


class PassiveProfileLogAdmin(admin.ModelAdmin):

    list_display = (
        'passive_profile_log_id',
        'user',
        'session_id',
        'asset_id',
        'date_of_entry',
    )
    list_filter = ('user',)


class PaymentGatewayAdmin(admin.ModelAdmin):

    list_display = ('payment_gateway_id', 'class_name', 'options')


class RedirectAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'redirect_url',
        'revision_date',
        'redirect_type',
    )


class ReplacementsAdmin(admin.ModelAdmin):

    list_display = ('replacement_id', 'search_for', 'replace_with')


class SearchAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'class_limiter',
        'search_root',
        'template_id',
        'use_containers',
        'paginate_after',
    )


class SettingsAdmin(admin.ModelAdmin):

    list_display = ('name', 'value')
    search_fields = ('name',)


class ShipperAdmin(admin.ModelAdmin):

    list_display = ('shipper_id', 'class_name', 'options')


class ShopCreditAdmin(admin.ModelAdmin):

    list_display = (
        'credit_id',
        'user',
        'amount',
        'comment',
        'date_of_adjustment',
    )
    list_filter = ('user', 'date_of_adjustment')


class SkuAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'revision_date',
        'description',
        'sku',
        'vendor',
        'display_title',
        'override_tax_rate',
        'tax_rate_override',
        'tax_configuration',
        'ships_separately',
    )
    list_filter = ('vendor',)


class SnippetAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'asset_id',
        'snippet',
        'process_as_template',
        'mime_type',
        'revision_date',
        'cache_timeout',
        'snippet_packed',
        'use_packed',
    )


class TaxDriverAdmin(admin.ModelAdmin):

    list_display = ('class_name', 'options')


class TaxEuVatNumbersAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'user',
        'country_code',
        'vat_number',
        'vies_validated',
        'vies_error_code',
        'approved',
    )
    list_filter = ('user',)


class TaxGenericRatesAdmin(admin.ModelAdmin):

    list_display = ('tax_id', 'country', 'state', 'city', 'code', 'tax_rate')


class TemplateAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'template',
        'namespace',
        'is_editable',
        'show_in_forms',
        'asset_id',
        'revision_date',
        'parser',
        'is_default',
        'template_packed',
        'use_packed',
    )


class TemplateAttachmentsAdmin(admin.ModelAdmin):

    list_display = (
        'template_id',
        'revision_date',
        'url',
        'type',
        'sequence',
        'attach_id',
    )


class TransactionItemAdmin(admin.ModelAdmin):

    list_display = (
        'item_id',
        'transaction_id',
        'asset_id',
        'configured_title',
        'options',
        'shipping_address_id',
        'shipping_name',
        'shipping_address1',
        'shipping_address2',
        'shipping_address3',
        'shipping_city',
        'shipping_state',
        'shipping_country',
        'shipping_code',
        'shipping_phone_number',
        'shipping_tracking_number',
        'order_status',
        'last_updated',
        'quantity',
        'price',
        'vendor',
        'vendor_payout_status',
        'vendor_payout_amount',
        'tax_rate',
        'tax_configuration',
    )
    list_filter = ('last_updated', 'vendor')


class UserLoginLogAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'user',
        'status',
        'time_stamp',
        'ip_address',
        'user_agent',
        'session_id',
        'last_page_viewed',
    )
    list_filter = ('user',)


class UserProfileCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'profile_category_id',
        'label',
        'short_label',
        'sequence_number',
        'visible',
        'editable',
        'protected',
    )


class UserProfileDataAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'email',
        'first_name',
        'middle_name',
        'last_name',
        'icq',
        'aim',
        'msn_im',
        'yahoo_im',
        'cell_phone',
        'pager',
        'email_to_pager',
        'language',
        'home_address',
        'home_city',
        'home_state',
        'home_zip',
        'home_country',
        'home_phone',
        'work_address',
        'work_city',
        'work_state',
        'work_zip',
        'work_country',
        'work_phone',
        'gender',
        'birthdate',
        'home_url',
        'work_url',
        'work_name',
        'time_zone',
        'date_format',
        'time_format',
        'discussion_layout',
        'first_day_of_week',
        'ui_level',
        'alias',
        'signature',
        'public_profile',
        'toolbar',
        'photo',
        'avatar',
        'department',
        'allow_private_messages',
        'able_to_be_friend',
        'show_message_on_login_seen',
        'show_online',
        'version_tag_mode',
        'wg_privacy_settings',
        'receive_inbox_email_notifications',
        'receive_inbox_sms_notifications',
    )
    list_filter = ('user',)


class UserProfileFieldAdmin(admin.ModelAdmin):

    list_display = (
        'field_name',
        'label',
        'visible',
        'required',
        'field_type',
        'possible_values',
        'data_default',
        'sequence_number',
        'profile_category_id',
        'protected',
        'editable',
        'force_image_only',
        'show_at_registration',
        'required_for_password_recovery',
        'extras',
        'default_privacy_setting',
    )


class UserSessionAdmin(admin.ModelAdmin):

    list_display = (
        'session_id',
        'expires',
        'last_page_view',
        'admin_on',
        'last_ip',
        'user',
    )
    list_filter = ('user',)


class UserSessionScratchAdmin(admin.ModelAdmin):

    list_display = (u'id', 'session_id', 'name', 'value')
    search_fields = ('name',)


class UserprefAdmin(admin.ModelAdmin):

    list_display = (u'id', 'username', 'preference', 'value')


class UserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'username',
        'auth_method',
        'date_created',
        'last_updated',
        'karma',
        'status',
        'referring_affiliate',
        'friends_group',
    )


class UsersSpecialStateAdmin(admin.ModelAdmin):

    list_display = (u'id', 'user', 'special_state')
    list_filter = ('user',)


class VendorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_created',
        'name',
        'user',
        'preferred_payment_type',
        'payment_information',
        'payment_address_id',
        'url',
    )
    list_filter = ('date_created', 'user')
    search_fields = ('name',)


class WebguiVersionAdmin(admin.ModelAdmin):

    list_display = (u'id', 'webgui_version', 'version_type', 'date_applied')


class WobjectAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'display_title',
        'description',
        'asset_id',
        'style_template_id',
        'printable_style_template_id',
        'revision_date',
        'mobile_style_template_id',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AdSku, AdSkuAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Calendar, CalendarAdmin)
_register(models.Carousel, CarouselAdmin)
_register(models.DataForm, DataFormAdmin)
_register(models.DataFormEntry, DataFormEntryAdmin)
_register(models.DataTable, DataTableAdmin)
_register(models.EMSBadge, EMSBadgeAdmin)
_register(models.EMSBadgeGroup, EMSBadgeGroupAdmin)
_register(models.EMSEventMetaField, EMSEventMetaFieldAdmin)
_register(models.EMSRegistrant, EMSRegistrantAdmin)
_register(models.EMSRegistrantRibbon, EMSRegistrantRibbonAdmin)
_register(models.EMSRegistrantTicket, EMSRegistrantTicketAdmin)
_register(models.EMSRegistrantToken, EMSRegistrantTokenAdmin)
_register(models.EMSRibbon, EMSRibbonAdmin)
_register(models.EMSTicket, EMSTicketAdmin)
_register(models.EMSToken, EMSTokenAdmin)
_register(models.Event, EventAdmin)
_register(models.EventManagementSystem, EventManagementSystemAdmin)
_register(models.EventRecur, EventRecurAdmin)
_register(models.EventRelatedlink, EventRelatedlinkAdmin)
_register(models.FileAsset, FileAssetAdmin)
_register(models.FlatDiscount, FlatDiscountAdmin)
_register(models.Folder, FolderAdmin)
_register(models.Gallery, GalleryAdmin)
_register(models.GalleryAlbum, GalleryAlbumAdmin)
_register(models.GalleryFile, GalleryFileAdmin)
_register(models.GalleryFileComment, GalleryFileCommentAdmin)
_register(models.HttpProxy, HttpProxyAdmin)
_register(models.ImageAsset, ImageAssetAdmin)
_register(models.KBAuth, KBAuthAdmin)
_register(models.Layout, LayoutAdmin)
_register(models.MacroAttendEvent, MacroAttendEventAdmin)
_register(models.Mailing, MailingAdmin)
_register(models.MailingEmail, MailingEmailAdmin)
_register(models.MailmanManager, MailmanManagerAdmin)
_register(models.MailmanManagerGroupsInList, MailmanManagerGroupsInListAdmin)
_register(models.MailmanManagerList, MailmanManagerListAdmin)
_register(
    models.MailmanManagerSubscribeConfirmation,
    MailmanManagerSubscribeConfirmationAdmin)
_register(models.Map, MapAdmin)
_register(models.MapPoint, MapPointAdmin)
_register(models.Matrix, MatrixAdmin)
_register(models.MatrixListing, MatrixListingAdmin)
_register(models.MatrixListingAttribute, MatrixListingAttributeAdmin)
_register(models.MatrixListingRating, MatrixListingRatingAdmin)
_register(models.MatrixListingRatingSummary, MatrixListingRatingSummaryAdmin)
_register(models.MatrixAttribute, MatrixAttributeAdmin)
_register(models.MessageBoard, MessageBoardAdmin)
_register(models.MultiSearch, MultiSearchAdmin)
_register(models.Navigation, NavigationAdmin)
_register(models.Newsletter, NewsletterAdmin)
_register(models.NewsletterCollection, NewsletterCollectionAdmin)
_register(models.NewsletterSubscription, NewsletterSubscriptionAdmin)
_register(models.PMProject, PMProjectAdmin)
_register(models.PMTask, PMTaskAdmin)
_register(models.PMTaskResource, PMTaskResourceAdmin)
_register(models.PMWobject, PMWobjectAdmin)
_register(models.Photo, PhotoAdmin)
_register(models.PhotoRating, PhotoRatingAdmin)
_register(models.Poll, PollAdmin)
_register(models.PollAnswer, PollAnswerAdmin)
_register(models.Post, PostAdmin)
_register(models.PostRating, PostRatingAdmin)
_register(models.Product, ProductAdmin)
_register(models.RichEdit, RichEditAdmin)
_register(models.SQLReport, SQLReportAdmin)
_register(models.Shelf, ShelfAdmin)
_register(models.Shortcut, ShortcutAdmin)
_register(models.ShortcutOverride, ShortcutOverrideAdmin)
_register(models.StockData, StockDataAdmin)
_register(models.Story, StoryAdmin)
_register(models.StoryArchive, StoryArchiveAdmin)
_register(models.StoryTopic, StoryTopicAdmin)
_register(models.Subscription, SubscriptionAdmin)
_register(models.SubscriptionCode, SubscriptionCodeAdmin)
_register(models.SubscriptionCodeBatch, SubscriptionCodeBatchAdmin)
_register(models.Survey, SurveyAdmin)
_register(models.SurveyAnswerOld, SurveyAnswerOldAdmin)
_register(models.SurveyOld, SurveyOldAdmin)
_register(models.SurveyQuestionResponseOld, SurveyQuestionResponseOldAdmin)
_register(models.SurveyQuestionType, SurveyQuestionTypeAdmin)
_register(models.SurveyQuestionOld, SurveyQuestionOldAdmin)
_register(models.SurveyResponse, SurveyResponseAdmin)
_register(models.SurveyResponseOld, SurveyResponseOldAdmin)
_register(models.SurveySectionOld, SurveySectionOldAdmin)
_register(models.SurveyTempReport, SurveyTempReportAdmin)
_register(models.SurveyTest, SurveyTestAdmin)
_register(models.SyndicatedContent, SyndicatedContentAdmin)
_register(models.TTProjectList, TTProjectListAdmin)
_register(models.TTProjectResourceList, TTProjectResourceListAdmin)
_register(models.TTProjectTask, TTProjectTaskAdmin)
_register(models.TTReport, TTReportAdmin)
_register(models.TTTimeEntry, TTTimeEntryAdmin)
_register(models.TTWobject, TTWobjectAdmin)
_register(models.Thingy, ThingyAdmin)
_register(models.ThingyRecord, ThingyRecordAdmin)
_register(models.ThingyRecordRecord, ThingyRecordRecordAdmin)
_register(models.ThingyField, ThingyFieldAdmin)
_register(
    models.ThingyIkgQcHs3rCevOFoHUiU8kg,
    ThingyIkgQcHs3rCevOFoHUiU8kgAdmin)
_register(models.ThingyThing, ThingyThingAdmin)
_register(models.Thread, ThreadAdmin)
_register(models.ThreadRead, ThreadReadAdmin)
_register(models.WeatherData, WeatherDataAdmin)
_register(models.WikiMaster, WikiMasterAdmin)
_register(models.WikiPage, WikiPageAdmin)
_register(models.Workflow, WorkflowAdmin)
_register(models.WorkflowActivity, WorkflowActivityAdmin)
_register(models.WorkflowActivityData, WorkflowActivityDataAdmin)
_register(models.WorkflowInstance, WorkflowInstanceAdmin)
_register(models.WorkflowInstanceScratch, WorkflowInstanceScratchAdmin)
_register(models.WorkflowSchedule, WorkflowScheduleAdmin)
_register(models.ZipArchiveAsset, ZipArchiveAssetAdmin)
_register(models.AdSkuPurchase, AdSkuPurchaseAdmin)
_register(models.AdSpace, AdSpaceAdmin)
_register(models.Address, AddressAdmin)
_register(models.AddressBook, AddressBookAdmin)
_register(models.Advertisement, AdvertisementAdmin)
_register(models.AnalyticRule, AnalyticRuleAdmin)
_register(models.Asset, AssetAdmin)
_register(models.AssetAspectComment, AssetAspectCommentAdmin)
_register(models.AssetAspectMailable, AssetAspectMailableAdmin)
_register(models.AssetAspectRssFeed, AssetAspectRssFeedAdmin)
_register(models.AssetAspectSubscriber, AssetAspectSubscriberAdmin)
_register(models.AssetAspectSubscriberLog, AssetAspectSubscriberLogAdmin)
_register(models.AssetData, AssetDataAdmin)
_register(models.AssetHistory, AssetHistoryAdmin)
_register(models.AssetIndex, AssetIndexAdmin)
_register(models.AssetKeyword, AssetKeywordAdmin)
_register(models.AssetVersionTag, AssetVersionTagAdmin)
_register(models.Authentication, AuthenticationAdmin)
_register(models.BucketLog, BucketLogAdmin)
_register(models.Cache, CacheAdmin)
_register(models.Cart, CartAdmin)
_register(models.CartItem, CartItemAdmin)
_register(models.DatabaseLink, DatabaseLinkAdmin)
_register(models.DeltaLog, DeltaLogAdmin)
_register(models.Donation, DonationAdmin)
_register(models.FilePumpBundle, FilePumpBundleAdmin)
_register(models.FriendInvitation, FriendInvitationAdmin)
_register(models.GroupGrouping, GroupGroupingAdmin)
_register(models.Grouping, GroupingAdmin)
_register(models.Group, GroupAdmin)
_register(models.ImageColor, ImageColorAdmin)
_register(models.ImageFont, ImageFontAdmin)
_register(models.ImagePalette, ImagePaletteAdmin)
_register(models.ImagePaletteColor, ImagePaletteColorAdmin)
_register(models.Inbox, InboxAdmin)
_register(models.InboxMessageState, InboxMessageStateAdmin)
_register(models.Incrementer, IncrementerAdmin)
_register(models.KarmaLog, KarmaLogAdmin)
_register(models.LdapLink, LdapLinkAdmin)
_register(models.MailQueue, MailQueueAdmin)
_register(models.MetaDataProperties, MetaDataPropertiesAdmin)
_register(models.MetaDataValues, MetaDataValuesAdmin)
_register(models.PassiveAnalyticsStatus, PassiveAnalyticsStatusAdmin)
_register(models.PassiveLog, PassiveLogAdmin)
_register(models.PassiveProfileAOI, PassiveProfileAOIAdmin)
_register(models.PassiveProfileLog, PassiveProfileLogAdmin)
_register(models.PaymentGateway, PaymentGatewayAdmin)
_register(models.Redirect, RedirectAdmin)
_register(models.Replacements, ReplacementsAdmin)
_register(models.Search, SearchAdmin)
_register(models.Settings, SettingsAdmin)
_register(models.Shipper, ShipperAdmin)
_register(models.ShopCredit, ShopCreditAdmin)
_register(models.Sku, SkuAdmin)
_register(models.Snippet, SnippetAdmin)
_register(models.TaxDriver, TaxDriverAdmin)
_register(models.TaxEuVatNumbers, TaxEuVatNumbersAdmin)
_register(models.TaxGenericRates, TaxGenericRatesAdmin)
_register(models.Template, TemplateAdmin)
_register(models.TemplateAttachments, TemplateAttachmentsAdmin)
_register(models.TransactionItem, TransactionItemAdmin)
_register(models.UserLoginLog, UserLoginLogAdmin)
_register(models.UserProfileCategory, UserProfileCategoryAdmin)
_register(models.UserProfileData, UserProfileDataAdmin)
_register(models.UserProfileField, UserProfileFieldAdmin)
_register(models.UserSession, UserSessionAdmin)
_register(models.UserSessionScratch, UserSessionScratchAdmin)
_register(models.Userpref, UserprefAdmin)
_register(models.User, UserAdmin)
_register(models.UsersSpecialState, UsersSpecialStateAdmin)
_register(models.Vendor, VendorAdmin)
_register(models.WebguiVersion, WebguiVersionAdmin)
_register(models.Wobject, WobjectAdmin)
