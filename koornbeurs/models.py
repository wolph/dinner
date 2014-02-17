import base64
from django.db import models


class AdSku(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    purchase_template = models.CharField(max_length=7L, db_column=u'purchaseTemplate')
    manage_template = models.CharField(max_length=7L, db_column=u'manageTemplate')
    ad_space = models.CharField(max_length=7L, db_column=u'adSpace')
    priority = models.IntegerField(null=True, blank=True)
    price_per_click = models.FloatField(null=True, db_column=u'pricePerClick', blank=True)
    price_per_impression = models.FloatField(null=True, db_column=u'pricePerImpression', blank=True)
    click_discounts = models.CharField(max_length=7L, db_column=u'clickDiscounts', blank=True)
    impression_discounts = models.CharField(max_length=7L, db_column=u'impressionDiscounts', blank=True)
    karma = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'AdSku'


class Article(models.Model):
    link_title = models.CharField(max_length=85L, db_column=u'linkTitle', blank=True)
    link_url = models.TextField(db_column=u'linkURL', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')
    storage_id = models.CharField(max_length=7L, db_column=u'storageId', blank=True)

    class Meta:
        db_table = u'Article'


class Calendar(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    default_date = models.CharField(max_length=2L, db_column=u'defaultDate', blank=True)
    default_view = models.CharField(max_length=1L, db_column=u'defaultView', blank=True)
    visitor_cache_timeout = models.IntegerField(null=True, db_column=u'visitorCacheTimeout', blank=True)
    template_id_month = models.CharField(max_length=7L, db_column=u'templateIdMonth', blank=True)
    template_id_week = models.CharField(max_length=7L, db_column=u'templateIdWeek', blank=True)
    template_id_day = models.CharField(max_length=7L, db_column=u'templateIdDay', blank=True)
    template_id_event = models.CharField(max_length=7L, db_column=u'templateIdEvent', blank=True)
    template_id_event_edit = models.CharField(max_length=7L, db_column=u'templateIdEventEdit', blank=True)
    template_id_search = models.CharField(max_length=7L, db_column=u'templateIdSearch', blank=True)
    template_id_print_month = models.CharField(max_length=7L, db_column=u'templateIdPrintMonth', blank=True)
    template_id_print_week = models.CharField(max_length=7L, db_column=u'templateIdPrintWeek', blank=True)
    template_id_print_day = models.CharField(max_length=7L, db_column=u'templateIdPrintDay', blank=True)
    template_id_print_event = models.CharField(max_length=7L, db_column=u'templateIdPrintEvent', blank=True)
    group_id_event_edit = models.CharField(max_length=7L, db_column=u'groupIdEventEdit', blank=True)
    group_id_subscribed = models.CharField(max_length=7L, db_column=u'groupIdSubscribed', blank=True)
    subscriber_notify_offset = models.IntegerField(null=True, db_column=u'subscriberNotifyOffset', blank=True)
    sort_events_by = models.CharField(max_length=4L, db_column=u'sortEventsBy', blank=True)
    list_view_page_interval = models.BigIntegerField(null=True, db_column=u'listViewPageInterval', blank=True)
    template_id_list = models.CharField(max_length=7L, db_column=u'templateIdList', blank=True)
    template_id_print_list = models.CharField(max_length=7L, db_column=u'templateIdPrintList', blank=True)
    ical_interval = models.BigIntegerField(null=True, db_column=u'icalInterval', blank=True)
    workflow_id_commit = models.CharField(max_length=7L, db_column=u'workflowIdCommit', blank=True)
    ical_feeds = models.TextField(db_column=u'icalFeeds', blank=True)

    class Meta:
        db_table = u'Calendar'


class Carousel(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    items = models.TextField(blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    slide_width = models.IntegerField(null=True, db_column=u'slideWidth', blank=True)

    class Meta:
        db_table = u'Carousel'


class Collaboration(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    post_group_id = models.CharField(max_length=7L, db_column=u'postGroupId', blank=True)
    can_start_thread_group_id = models.CharField(max_length=7L, db_column=u'canStartThreadGroupId', blank=True)
    karma_per_post = models.IntegerField(db_column=u'karmaPerPost')
    collaboration_template_id = models.CharField(max_length=7L, db_column=u'collaborationTemplateId', blank=True)
    thread_template_id = models.CharField(max_length=7L, db_column=u'threadTemplateId', blank=True)
    post_form_template_id = models.CharField(max_length=7L, db_column=u'postFormTemplateId', blank=True)
    search_template_id = models.CharField(max_length=7L, db_column=u'searchTemplateId', blank=True)
    notification_template_id = models.CharField(max_length=7L, db_column=u'notificationTemplateId', blank=True)
    sort_by = models.CharField(max_length=11L, db_column=u'sortBy', blank=True)
    sort_order = models.CharField(max_length=1L, db_column=u'sortOrder', blank=True)
    use_preview = models.IntegerField(db_column=u'usePreview')
    add_edit_stamp_to_posts = models.IntegerField(db_column=u'addEditStampToPosts')
    edit_timeout = models.IntegerField(db_column=u'editTimeout')
    attachments_per_post = models.IntegerField(db_column=u'attachmentsPerPost')
    filter_code = models.CharField(max_length=10L, db_column=u'filterCode', blank=True)
    use_content_filter = models.IntegerField(db_column=u'useContentFilter')
    threads = models.IntegerField()
    views = models.IntegerField()
    replies = models.IntegerField()
    rating = models.IntegerField()
    last_post_id = models.CharField(max_length=7L, db_column=u'lastPostId', blank=True)
    last_post_date = models.BigIntegerField(null=True, db_column=u'lastPostDate', blank=True)
    archive_after = models.IntegerField(db_column=u'archiveAfter')
    posts_per_page = models.IntegerField(db_column=u'postsPerPage')
    threads_per_page = models.IntegerField(db_column=u'threadsPerPage')
    subscription_group_id = models.CharField(max_length=7L, db_column=u'subscriptionGroupId', blank=True)
    allow_replies = models.IntegerField(db_column=u'allowReplies')
    display_last_reply = models.IntegerField(db_column=u'displayLastReply')
    rich_editor = models.CharField(max_length=7L, db_column=u'richEditor', blank=True)
    karma_rating_multiplier = models.IntegerField(db_column=u'karmaRatingMultiplier')
    karma_spent_to_rate = models.IntegerField(db_column=u'karmaSpentToRate')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    avatars_enabled = models.IntegerField(db_column=u'avatarsEnabled')
    approval_workflow = models.CharField(max_length=7L, db_column=u'approvalWorkflow', blank=True)
    thread_approval_workflow = models.CharField(max_length=7L, db_column=u'threadApprovalWorkflow', blank=True)
    default_karma_scale = models.IntegerField(db_column=u'defaultKarmaScale')
    mail_server = models.CharField(max_length=85L, db_column=u'mailServer', blank=True)
    mail_account = models.CharField(max_length=85L, db_column=u'mailAccount', blank=True)
    mail_password = models.CharField(max_length=85L, db_column=u'mailPassword', blank=True)
    mail_address = models.CharField(max_length=85L, db_column=u'mailAddress', blank=True)
    mail_prefix = models.CharField(max_length=85L, db_column=u'mailPrefix', blank=True)
    get_mail = models.IntegerField(db_column=u'getMail')
    get_mail_interval = models.IntegerField(db_column=u'getMailInterval')
    get_mail_cron_id = models.CharField(max_length=7L, db_column=u'getMailCronId', blank=True)
    visitor_cache_timeout = models.IntegerField(db_column=u'visitorCacheTimeout')
    auto_subscribe_to_thread = models.IntegerField(db_column=u'autoSubscribeToThread')
    require_subscription_for_email_posting = models.IntegerField(db_column=u'requireSubscriptionForEmailPosting')
    thumbnail_size = models.IntegerField(db_column=u'thumbnailSize')
    max_image_size = models.IntegerField(db_column=u'maxImageSize')
    enable_post_meta_data = models.IntegerField(db_column=u'enablePostMetaData')
    use_captcha = models.IntegerField(db_column=u'useCaptcha')
    group_to_edit_post = models.CharField(max_length=7L, db_column=u'groupToEditPost', blank=True)
    archive_enabled = models.IntegerField(null=True, db_column=u'archiveEnabled', blank=True)
    post_received_template_id = models.CharField(max_length=7L, db_column=u'postReceivedTemplateId', blank=True)
    reply_rich_editor = models.CharField(max_length=7L, db_column=u'replyRichEditor', blank=True)
    reply_filter_code = models.CharField(max_length=10L, db_column=u'replyFilterCode', blank=True)

    class Meta:
        db_table = u'Collaboration'


class Dashboard(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    admins_group_id = models.CharField(max_length=7L, db_column=u'adminsGroupId', blank=True)
    users_group_id = models.CharField(max_length=7L, db_column=u'usersGroupId', blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    is_initialized = models.IntegerField(db_column=u'isInitialized')
    assets_to_hide = models.TextField(db_column=u'assetsToHide', blank=True)

    class Meta:
        db_table = u'Dashboard'


class DataForm(models.Model):
    acknowledgement = models.TextField(blank=True)
    mail_data = models.IntegerField(db_column=u'mailData')
    email_template_id = models.CharField(max_length=7L, db_column=u'emailTemplateId', blank=True)
    acknowlegement_template_id = models.CharField(max_length=7L, db_column=u'acknowlegementTemplateId', blank=True)
    list_template_id = models.CharField(max_length=7L, db_column=u'listTemplateId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    default_view = models.IntegerField(db_column=u'defaultView')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    group_to_view_entries = models.CharField(max_length=7L, db_column=u'groupToViewEntries', blank=True)
    mail_attachments = models.IntegerField(null=True, db_column=u'mailAttachments', blank=True)
    use_captcha = models.IntegerField(null=True, db_column=u'useCaptcha', blank=True)
    store_data = models.IntegerField(null=True, db_column=u'storeData', blank=True)
    field_configuration = models.TextField(db_column=u'fieldConfiguration', blank=True)
    tab_configuration = models.TextField(db_column=u'tabConfiguration', blank=True)
    workflow_id_add_entry = models.CharField(max_length=7L, db_column=u'workflowIdAddEntry', blank=True)
    html_area_rich_editor = models.CharField(max_length=7L, db_column=u'htmlAreaRichEditor', blank=True)

    class Meta:
        db_table = u'DataForm'


class DataFormEntry(models.Model):
    data_form_entry_id = models.CharField(max_length=7L, primary_key=True, db_column=u'DataForm_entryId')
    user = models.ForeignKey('User', db_column='userId')
    username = models.CharField(max_length=85L, blank=True)
    ip_address = models.CharField(max_length=85L, db_column=u'ipAddress', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    entry_data = models.TextField(db_column=u'entryData', blank=True)
    submission_date = models.DateTimeField(null=True, db_column=u'submissionDate', blank=True)

    class Meta:
        db_table = u'DataForm_entry'


class DataTable(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    data = models.TextField(blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)

    class Meta:
        db_table = u'DataTable'


class EMSBadge(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    price = models.FloatField()
    seats_available = models.IntegerField(db_column=u'seatsAvailable')
    related_badge_groups = models.TextField(db_column=u'relatedBadgeGroups', blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    early_bird_price = models.FloatField(db_column=u'earlyBirdPrice')
    early_bird_price_end_date = models.BigIntegerField(null=True, db_column=u'earlyBirdPriceEndDate', blank=True)
    pre_registration_price = models.FloatField(db_column=u'preRegistrationPrice')
    pre_registration_price_end_date = models.BigIntegerField(null=True, db_column=u'preRegistrationPriceEndDate', blank=True)

    class Meta:
        db_table = u'EMSBadge'


class EMSBadgeGroup(models.Model):
    badge_group_id = models.CharField(max_length=7L, primary_key=True, db_column=u'badgeGroupId')
    ems_asset_id = models.CharField(max_length=7L, db_column=u'emsAssetId')
    name = models.CharField(max_length=33L, blank=True)

    class Meta:
        db_table = u'EMSBadgeGroup'


class EMSEventMetaField(models.Model):
    field_id = models.CharField(max_length=7L, primary_key=True, db_column=u'fieldId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    label = models.CharField(max_length=33L, blank=True)
    data_type = models.CharField(max_length=6L, db_column=u'dataType', blank=True)
    visible = models.IntegerField(null=True, blank=True)
    required = models.IntegerField(null=True, blank=True)
    possible_values = models.TextField(db_column=u'possibleValues', blank=True)
    default_values = models.TextField(db_column=u'defaultValues', blank=True)
    sequence_number = models.IntegerField(null=True, db_column=u'sequenceNumber', blank=True)

    class Meta:
        db_table = u'EMSEventMetaField'


class EMSRegistrant(models.Model):
    badge_id = models.CharField(max_length=7L, primary_key=True, db_column=u'badgeId')
    user = models.ForeignKey('User', db_column='userId')
    badge_number = models.IntegerField(unique=True, db_column=u'badgeNumber')
    badge_asset_id = models.CharField(max_length=7L, db_column=u'badgeAssetId')
    ems_asset_id = models.CharField(max_length=7L, db_column=u'emsAssetId')
    name = models.CharField(max_length=11L)
    address1 = models.CharField(max_length=11L, blank=True)
    address2 = models.CharField(max_length=11L, blank=True)
    address3 = models.CharField(max_length=11L, blank=True)
    city = models.CharField(max_length=11L, blank=True)
    state = models.CharField(max_length=11L, blank=True)
    zipcode = models.CharField(max_length=11L, blank=True)
    country = models.CharField(max_length=11L, blank=True)
    phone_number = models.CharField(max_length=11L, db_column=u'phoneNumber', blank=True)
    organization = models.CharField(max_length=11L, blank=True)
    email = models.CharField(max_length=85L, blank=True)
    notes = models.TextField(blank=True)
    purchase_complete = models.IntegerField(null=True, db_column=u'purchaseComplete', blank=True)
    has_checked_in = models.IntegerField(null=True, db_column=u'hasCheckedIn', blank=True)
    transaction_item_id = models.CharField(max_length=7L, db_column=u'transactionItemId', blank=True)

    class Meta:
        db_table = u'EMSRegistrant'


class EMSRegistrantRibbon(models.Model):
    badge_id = models.CharField(max_length=7L, db_column=u'badgeId')
    ribbon_asset_id = models.CharField(max_length=7L, db_column=u'ribbonAssetId')
    transaction_item_id = models.CharField(max_length=7L, db_column=u'transactionItemId', blank=True)

    class Meta:
        db_table = u'EMSRegistrantRibbon'


class EMSRegistrantTicket(models.Model):
    badge_id = models.CharField(max_length=7L, db_column=u'badgeId')
    ticket_asset_id = models.CharField(max_length=7L, db_column=u'ticketAssetId')
    purchase_complete = models.IntegerField(null=True, db_column=u'purchaseComplete', blank=True)
    transaction_item_id = models.CharField(max_length=7L, db_column=u'transactionItemId', blank=True)

    class Meta:
        db_table = u'EMSRegistrantTicket'


class EMSRegistrantToken(models.Model):
    badge_id = models.CharField(max_length=7L, db_column=u'badgeId')
    token_asset_id = models.CharField(max_length=7L, db_column=u'tokenAssetId')
    quantity = models.IntegerField(null=True, blank=True)
    transaction_item_ids = models.TextField(db_column=u'transactionItemIds', blank=True)

    class Meta:
        db_table = u'EMSRegistrantToken'


class EMSRibbon(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    percentage_discount = models.FloatField(db_column=u'percentageDiscount')
    price = models.FloatField()

    class Meta:
        db_table = u'EMSRibbon'


class EMSTicket(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    price = models.FloatField()
    seats_available = models.IntegerField(db_column=u'seatsAvailable')
    start_date = models.DateTimeField(null=True, db_column=u'startDate', blank=True)
    duration = models.FloatField()
    event_number = models.IntegerField(null=True, db_column=u'eventNumber', blank=True)
    location = models.CharField(max_length=33L, blank=True)
    related_badge_groups = models.TextField(db_column=u'relatedBadgeGroups', blank=True)
    related_ribbons = models.TextField(db_column=u'relatedRibbons', blank=True)
    event_meta_data = models.TextField(db_column=u'eventMetaData', blank=True)

    class Meta:
        db_table = u'EMSTicket'


class EMSToken(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    price = models.FloatField()

    class Meta:
        db_table = u'EMSToken'


class Event(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    feed_id = models.CharField(max_length=7L, db_column=u'feedId', blank=True)
    feed_uid = models.CharField(max_length=85L, db_column=u'feedUid', blank=True)
    start_date = models.DateField(null=True, db_column=u'startDate', blank=True)
    end_date = models.DateField(null=True, db_column=u'endDate', blank=True)
    user_defined1 = models.TextField(db_column=u'userDefined1', blank=True)
    user_defined2 = models.TextField(db_column=u'userDefined2', blank=True)
    user_defined3 = models.TextField(db_column=u'userDefined3', blank=True)
    user_defined4 = models.TextField(db_column=u'userDefined4', blank=True)
    user_defined5 = models.TextField(db_column=u'userDefined5', blank=True)
    recur_id = models.CharField(max_length=7L, db_column=u'recurId', blank=True)
    description = models.TextField(blank=True)
    start_time = models.TimeField(null=True, db_column=u'startTime', blank=True)
    end_time = models.TimeField(null=True, db_column=u'endTime', blank=True)
    related_links = models.TextField(db_column=u'relatedLinks', blank=True)
    location = models.CharField(max_length=85L, blank=True)
    storage_id = models.CharField(max_length=7L, db_column=u'storageId', blank=True)
    time_zone = models.CharField(max_length=85L, db_column=u'timeZone', blank=True)
    i_cal_sequence_number = models.IntegerField(null=True, db_column=u'iCalSequenceNumber', blank=True)
    sequence_number = models.BigIntegerField(null=True, db_column=u'sequenceNumber', blank=True)

    class Meta:
        db_table = u'Event'


class EventManagementSystem(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    group_to_approve_events = models.CharField(max_length=7L, db_column=u'groupToApproveEvents', blank=True)
    timezone = models.CharField(max_length=10L)
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    badge_builder_template_id = models.CharField(max_length=7L, db_column=u'badgeBuilderTemplateId')
    lookup_registrant_template_id = models.CharField(max_length=7L, db_column=u'lookupRegistrantTemplateId')
    print_badge_template_id = models.CharField(max_length=7L, db_column=u'printBadgeTemplateId')
    print_ticket_template_id = models.CharField(max_length=7L, db_column=u'printTicketTemplateId')
    badge_instructions = models.TextField(db_column=u'badgeInstructions', blank=True)
    ribbon_instructions = models.TextField(db_column=u'ribbonInstructions', blank=True)
    ticket_instructions = models.TextField(db_column=u'ticketInstructions', blank=True)
    token_instructions = models.TextField(db_column=u'tokenInstructions', blank=True)
    registration_staff_group_id = models.CharField(max_length=7L, db_column=u'registrationStaffGroupId')
    schedule_template_id = models.CharField(max_length=7L, db_column=u'scheduleTemplateId', blank=True)
    schedule_columns_per_page = models.IntegerField(null=True, db_column=u'scheduleColumnsPerPage', blank=True)

    class Meta:
        db_table = u'EventManagementSystem'


class EventRecur(models.Model):
    recur_id = models.CharField(max_length=7L, primary_key=True, db_column=u'recurId')
    recur_type = models.CharField(max_length=5L, db_column=u'recurType', blank=True)
    pattern = models.CharField(max_length=85L, blank=True)
    start_date = models.DateField(null=True, db_column=u'startDate', blank=True)
    end_date = models.CharField(max_length=3L, db_column=u'endDate', blank=True)

    class Meta:
        db_table = u'Event_recur'


class EventRelatedlink(models.Model):
    eventlink_id = models.CharField(max_length=7L, db_column=u'eventlinkId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    link_url = models.TextField(db_column=u'linkURL', blank=True)
    linktext = models.CharField(max_length=26L, blank=True)
    group_id_view = models.CharField(max_length=7L, db_column=u'groupIdView', blank=True)
    sequence_number = models.BigIntegerField(null=True, db_column=u'sequenceNumber', blank=True)

    class Meta:
        db_table = u'Event_relatedlink'


class FileAsset(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    storage_id = models.CharField(max_length=7L, db_column=u'storageId', blank=True)
    filename = models.CharField(max_length=85L, blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')

    class Meta:
        db_table = u'FileAsset'


class FlatDiscount(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    must_spend = models.FloatField(db_column=u'mustSpend')
    percentage_discount = models.IntegerField(db_column=u'percentageDiscount')
    price_discount = models.FloatField(db_column=u'priceDiscount')
    thank_you_message = models.TextField(db_column=u'thankYouMessage', blank=True)

    class Meta:
        db_table = u'FlatDiscount'


class Folder(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    visitor_cache_timeout = models.IntegerField(db_column=u'visitorCacheTimeout')
    sort_alphabetically = models.IntegerField(db_column=u'sortAlphabetically')
    sort_order = models.CharField(max_length=1L, db_column=u'sortOrder', blank=True)

    class Meta:
        db_table = u'Folder'


class Gallery(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    group_id_add_comment = models.CharField(max_length=7L, db_column=u'groupIdAddComment', blank=True)
    group_id_add_file = models.CharField(max_length=7L, db_column=u'groupIdAddFile', blank=True)
    image_resolutions = models.TextField(db_column=u'imageResolutions', blank=True)
    image_view_size = models.IntegerField(null=True, db_column=u'imageViewSize', blank=True)
    image_thumbnail_size = models.IntegerField(null=True, db_column=u'imageThumbnailSize', blank=True)
    max_space_per_user = models.CharField(max_length=6L, db_column=u'maxSpacePerUser', blank=True)
    rich_edit_id_comment = models.CharField(max_length=7L, db_column=u'richEditIdComment', blank=True)
    template_id_add_archive = models.CharField(max_length=7L, db_column=u'templateIdAddArchive', blank=True)
    template_id_delete_album = models.CharField(max_length=7L, db_column=u'templateIdDeleteAlbum', blank=True)
    template_id_delete_file = models.CharField(max_length=7L, db_column=u'templateIdDeleteFile', blank=True)
    template_id_edit_album = models.CharField(max_length=7L, db_column=u'templateIdEditAlbum', blank=True)
    template_id_edit_file = models.CharField(max_length=7L, db_column=u'templateIdEditFile', blank=True)
    template_id_list_albums = models.CharField(max_length=7L, db_column=u'templateIdListAlbums', blank=True)
    template_id_list_albums_rss = models.CharField(max_length=7L, db_column=u'templateIdListAlbumsRss', blank=True)
    template_id_list_files_for_user = models.CharField(max_length=7L, db_column=u'templateIdListFilesForUser', blank=True)
    template_id_list_files_for_user_rss = models.CharField(max_length=7L, db_column=u'templateIdListFilesForUserRss', blank=True)
    template_id_make_shortcut = models.CharField(max_length=7L, db_column=u'templateIdMakeShortcut', blank=True)
    template_id_search = models.CharField(max_length=7L, db_column=u'templateIdSearch', blank=True)
    template_id_view_slideshow = models.CharField(max_length=7L, db_column=u'templateIdViewSlideshow', blank=True)
    template_id_view_thumbnails = models.CharField(max_length=7L, db_column=u'templateIdViewThumbnails', blank=True)
    template_id_view_album = models.CharField(max_length=7L, db_column=u'templateIdViewAlbum', blank=True)
    template_id_view_album_rss = models.CharField(max_length=7L, db_column=u'templateIdViewAlbumRss', blank=True)
    template_id_view_file = models.CharField(max_length=7L, db_column=u'templateIdViewFile', blank=True)
    view_album_asset_id = models.CharField(max_length=7L, db_column=u'viewAlbumAssetId', blank=True)
    view_default = models.CharField(max_length=1L, db_column=u'viewDefault', blank=True)
    view_list_order_by = models.CharField(max_length=13L, db_column=u'viewListOrderBy', blank=True)
    view_list_order_direction = models.CharField(max_length=1L, db_column=u'viewListOrderDirection', blank=True)
    workflow_id_commit = models.CharField(max_length=7L, db_column=u'workflowIdCommit', blank=True)
    template_id_edit_comment = models.CharField(max_length=7L, db_column=u'templateIdEditComment', blank=True)
    rich_edit_id_album = models.CharField(max_length=7L, db_column=u'richEditIdAlbum', blank=True)
    rich_edit_id_file = models.CharField(max_length=7L, db_column=u'richEditIdFile', blank=True)
    default_files_per_page = models.IntegerField(null=True, db_column=u'defaultFilesPerPage', blank=True)
    image_density = models.IntegerField(null=True, db_column=u'imageDensity', blank=True)

    class Meta:
        db_table = u'Gallery'


class GalleryAlbum(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    allow_comments = models.IntegerField(null=True, db_column=u'allowComments', blank=True)
    asset_id_thumbnail = models.CharField(max_length=7L, db_column=u'assetIdThumbnail', blank=True)
    user_defined1 = models.TextField(db_column=u'userDefined1', blank=True)
    user_defined2 = models.TextField(db_column=u'userDefined2', blank=True)
    user_defined3 = models.TextField(db_column=u'userDefined3', blank=True)
    user_defined4 = models.TextField(db_column=u'userDefined4', blank=True)
    user_defined5 = models.TextField(db_column=u'userDefined5', blank=True)
    others_can_add = models.IntegerField(null=True, db_column=u'othersCanAdd', blank=True)

    class Meta:
        db_table = u'GalleryAlbum'


class GalleryFile(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    user_defined1 = models.TextField(db_column=u'userDefined1', blank=True)
    user_defined2 = models.TextField(db_column=u'userDefined2', blank=True)
    user_defined3 = models.TextField(db_column=u'userDefined3', blank=True)
    user_defined4 = models.TextField(db_column=u'userDefined4', blank=True)
    user_defined5 = models.TextField(db_column=u'userDefined5', blank=True)
    views = models.BigIntegerField(null=True, blank=True)
    friends_only = models.IntegerField(null=True, db_column=u'friendsOnly', blank=True)
    rating = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'GalleryFile'


class GalleryFileComment(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    comment_id = models.CharField(max_length=7L, db_column=u'commentId')
    user = models.ForeignKey('User', db_column='userId')
    visitor_ip = models.CharField(max_length=85L, db_column=u'visitorIp', blank=True)
    creation_date = models.DateTimeField(null=True, db_column=u'creationDate', blank=True)
    body_text = models.TextField(db_column=u'bodyText', blank=True)

    class Meta:
        db_table = u'GalleryFile_comment'


class HttpProxy(models.Model):
    proxied_url = models.TextField(db_column=u'proxiedUrl', blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    remove_style = models.IntegerField(null=True, db_column=u'removeStyle', blank=True)
    filter_html = models.CharField(max_length=10L, db_column=u'filterHtml', blank=True)
    follow_external = models.IntegerField(null=True, db_column=u'followExternal', blank=True)
    follow_redirect = models.IntegerField(null=True, db_column=u'followRedirect', blank=True)
    cache_http = models.IntegerField(null=True, db_column=u'cacheHttp', blank=True)
    use_cache = models.IntegerField(null=True, db_column=u'useCache', blank=True)
    debug = models.IntegerField(null=True, blank=True)
    rewrite_urls = models.IntegerField(null=True, db_column=u'rewriteUrls', blank=True)
    search_for = models.CharField(max_length=85L, db_column=u'searchFor', blank=True)
    stop_at = models.CharField(max_length=85L, db_column=u'stopAt', blank=True)
    cookie_jar_storage_id = models.CharField(max_length=7L, db_column=u'cookieJarStorageId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')
    use_ampersand = models.IntegerField(db_column=u'useAmpersand')
    url_pattern_filter = models.TextField(db_column=u'urlPatternFilter', blank=True)

    class Meta:
        db_table = u'HttpProxy'


class ImageAsset(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    thumbnail_size = models.IntegerField(db_column=u'thumbnailSize')
    parameters = models.TextField(blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    annotations = models.TextField(blank=True)

    class Meta:
        db_table = u'ImageAsset'


class InOutBoard(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    status_list = models.TextField(db_column=u'statusList', blank=True)
    report_viewer_group = models.CharField(max_length=7L, db_column=u'reportViewerGroup', blank=True)
    in_out_group = models.CharField(max_length=7L, db_column=u'inOutGroup', blank=True)
    in_out_template_id = models.CharField(max_length=7L, db_column=u'inOutTemplateId', blank=True)
    report_template_id = models.CharField(max_length=7L, db_column=u'reportTemplateId', blank=True)
    paginate_after = models.IntegerField(db_column=u'paginateAfter')
    report_paginate_after = models.IntegerField(db_column=u'reportPaginateAfter')

    class Meta:
        db_table = u'InOutBoard'


class InOutBoardDelegates(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    delegate_user = models.ForeignKey('User', db_column='userId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)

    class Meta:
        db_table = u'InOutBoard_delegates'


class InOutBoardStatus(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    status = models.CharField(max_length=85L, blank=True)
    date_stamp = models.IntegerField(db_column=u'dateStamp')
    message = models.TextField(blank=True)

    class Meta:
        db_table = u'InOutBoard_status'


class InOutBoardStatusLog(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    status = models.CharField(max_length=85L, blank=True)
    date_stamp = models.IntegerField(db_column=u'dateStamp')
    message = models.TextField(blank=True)
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)

    class Meta:
        db_table = u'InOutBoard_statusLog'


class KBAuth(models.Model):
    username = models.CharField(max_length=33L, blank=True)
    password = models.TextField(blank=True)

    class Meta:
        db_table = u'KB_auth'


class Layout(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    content_positions = models.TextField(db_column=u'contentPositions', blank=True)
    assets_to_hide = models.TextField(db_column=u'assetsToHide', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    asset_order = models.CharField(max_length=6L, db_column=u'assetOrder', blank=True)
    mobile_template_id = models.CharField(max_length=7L, db_column=u'mobileTemplateId', blank=True)

    class Meta:
        db_table = u'Layout'


class MacroAttendEvent(models.Model):
    guid = models.CharField(max_length=7L)
    user = models.ForeignKey('User', db_column='userId')

    class Meta:
        db_table = u'MacroAttendEvent'


class Mailing(models.Model):
    mailing_id = models.CharField(max_length=7L, primary_key=True, db_column=u'mailingId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    issue_id = models.CharField(max_length=7L, db_column=u'issueId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    send_date = models.BigIntegerField(null=True, db_column=u'sendDate', blank=True)
    configuration = models.TextField()
    state = models.CharField(max_length=85L)

    class Meta:
        db_table = u'Mailing'


class MailingEmail(models.Model):
    mail_id = models.CharField(max_length=7L, primary_key=True, db_column=u'mailId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    bounce_reason = models.CharField(max_length=85L, db_column=u'bounceReason', blank=True)
    status = models.CharField(max_length=85L)
    user = models.ForeignKey('User', db_column='userId')
    mailing_id = models.CharField(max_length=7L, db_column=u'mailingId', blank=True)
    error_message = models.CharField(max_length=85L, db_column=u'errorMessage', blank=True)
    sent_to = models.CharField(max_length=85L, db_column=u'sentTo', blank=True)
    is_test = models.IntegerField(db_column=u'isTest')
    send_date = models.BigIntegerField(null=True, db_column=u'sendDate', blank=True)
    recipient_email = models.CharField(max_length=85L, db_column=u'recipientEmail', blank=True)

    class Meta:
        db_table = u'Mailing_email'


class MailmanManager(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')

    class Meta:
        db_table = u'MailmanManager'


class MailmanManagerGroupsInList(models.Model):
    list_id = models.CharField(max_length=7L, db_column=u'listId')
    group_id = models.CharField(max_length=7L, db_column=u'groupId')

    class Meta:
        db_table = u'MailmanManager_groupsInList'


class MailmanManagerLists(models.Model):
    list_id = models.CharField(max_length=7L, primary_key=True, db_column=u'listId')
    is_alias = models.IntegerField(null=True, db_column=u'isAlias', blank=True)
    list_name = models.CharField(max_length=85L, db_column=u'listName', blank=True)
    list_title = models.CharField(max_length=85L, db_column=u'listTitle', blank=True)
    list_address = models.CharField(unique=True, max_length=85L, db_column=u'listAddress', blank=True)
    extra_addresses = models.TextField(db_column=u'extraAddresses', blank=True)
    config_overrides = models.TextField(db_column=u'configOverrides', blank=True)
    exclude_group = models.CharField(max_length=7L, db_column=u'excludeGroup', blank=True)

    class Meta:
        db_table = u'MailmanManager_lists'


class MailmanManagerSubscribeConfirmation(models.Model):
    list_id = models.CharField(max_length=7L, db_column=u'listId')
    confirmation_code = models.CharField(max_length=7L, db_column=u'confirmationCode')
    email = models.CharField(max_length=85L, blank=True)
    date_added = models.DateTimeField(db_column=u'dateAdded')

    class Meta:
        db_table = u'MailmanManager_subscribeConfirmation'


class Map(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    group_id_add_point = models.CharField(max_length=7L, db_column=u'groupIdAddPoint', blank=True)
    map_api_key = models.TextField(db_column=u'mapApiKey', blank=True)
    map_height = models.CharField(max_length=4L, db_column=u'mapHeight', blank=True)
    map_width = models.CharField(max_length=4L, db_column=u'mapWidth', blank=True)
    start_latitude = models.FloatField(null=True, db_column=u'startLatitude', blank=True)
    start_longitude = models.FloatField(null=True, db_column=u'startLongitude', blank=True)
    start_zoom = models.IntegerField(null=True, db_column=u'startZoom', blank=True)
    template_id_edit_point = models.CharField(max_length=7L, db_column=u'templateIdEditPoint', blank=True)
    template_id_view = models.CharField(max_length=7L, db_column=u'templateIdView', blank=True)
    template_id_view_point = models.CharField(max_length=7L, db_column=u'templateIdViewPoint', blank=True)
    workflow_id_point = models.CharField(max_length=7L, db_column=u'workflowIdPoint', blank=True)

    class Meta:
        db_table = u'Map'


class MapPoint(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    website = models.CharField(max_length=85L, blank=True)
    address1 = models.CharField(max_length=11L, blank=True)
    address2 = models.CharField(max_length=11L, blank=True)
    city = models.CharField(max_length=11L, blank=True)
    state = models.CharField(max_length=11L, blank=True)
    zip_code = models.CharField(max_length=11L, db_column=u'zipCode', blank=True)
    country = models.CharField(max_length=11L, blank=True)
    phone = models.CharField(max_length=7L, blank=True)
    fax = models.CharField(max_length=7L, blank=True)
    email = models.CharField(max_length=11L, blank=True)
    storage_id_photo = models.CharField(max_length=7L, db_column=u'storageIdPhoto', blank=True)
    user_defined1 = models.TextField(db_column=u'userDefined1', blank=True)
    user_defined2 = models.TextField(db_column=u'userDefined2', blank=True)
    user_defined3 = models.TextField(db_column=u'userDefined3', blank=True)
    user_defined4 = models.TextField(db_column=u'userDefined4', blank=True)
    user_defined5 = models.TextField(db_column=u'userDefined5', blank=True)

    class Meta:
        db_table = u'MapPoint'


class Matrix(models.Model):
    detail_template_id = models.CharField(max_length=7L, db_column=u'detailTemplateId', blank=True)
    compare_template_id = models.CharField(max_length=7L, db_column=u'compareTemplateId', blank=True)
    search_template_id = models.CharField(max_length=7L, db_column=u'searchTemplateId', blank=True)
    categories = models.TextField(blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    max_comparisons = models.IntegerField(db_column=u'maxComparisons')
    max_comparisons_privileged = models.IntegerField(db_column=u'maxComparisonsPrivileged')
    group_to_add = models.CharField(max_length=7L, db_column=u'groupToAdd', blank=True)
    default_sort = models.CharField(max_length=7L, db_column=u'defaultSort')
    compare_color_no = models.CharField(max_length=7L, db_column=u'compareColorNo', blank=True)
    compare_color_limited = models.CharField(max_length=7L, db_column=u'compareColorLimited')
    compare_color_costs_extra = models.CharField(max_length=7L, db_column=u'compareColorCostsExtra')
    compare_color_free_add_on = models.CharField(max_length=7L, db_column=u'compareColorFreeAddOn')
    compare_color_yes = models.CharField(max_length=7L, db_column=u'compareColorYes')
    submission_approval_workflow_id = models.CharField(max_length=7L, db_column=u'submissionApprovalWorkflowId')
    ratings_duration = models.IntegerField(db_column=u'ratingsDuration')
    edit_listing_template_id = models.CharField(max_length=7L, db_column=u'editListingTemplateId', blank=True)
    screenshots_config_template_id = models.CharField(max_length=7L, db_column=u'screenshotsConfigTemplateId', blank=True)
    screenshots_template_id = models.CharField(max_length=7L, db_column=u'screenshotsTemplateId', blank=True)
    statistics_cache_timeout = models.IntegerField(db_column=u'statisticsCacheTimeout')
    max_comparisons_group = models.CharField(max_length=7L, db_column=u'maxComparisonsGroup', blank=True)
    max_comparisons_group_int = models.IntegerField(null=True, db_column=u'maxComparisonsGroupInt', blank=True)
    max_screenshot_width = models.IntegerField(null=True, db_column=u'maxScreenshotWidth', blank=True)
    max_screenshot_height = models.IntegerField(null=True, db_column=u'maxScreenshotHeight', blank=True)
    listings_cache_timeout = models.IntegerField(db_column=u'listingsCacheTimeout')

    class Meta:
        db_table = u'Matrix'


class MatrixListing(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    screenshots = models.CharField(max_length=7L, blank=True)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=85L, blank=True)
    views = models.IntegerField(null=True, blank=True)
    compares = models.IntegerField(null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    views_last_ip = models.CharField(max_length=85L, db_column=u'viewsLastIp', blank=True)
    compares_last_ip = models.CharField(max_length=85L, db_column=u'comparesLastIp', blank=True)
    clicks_last_ip = models.CharField(max_length=85L, db_column=u'clicksLastIp', blank=True)
    last_updated = models.IntegerField(null=True, db_column=u'lastUpdated', blank=True)
    maintainer = models.CharField(max_length=7L, blank=True)
    manufacturer_name = models.CharField(max_length=85L, db_column=u'manufacturerName', blank=True)
    manufacturer_url = models.CharField(max_length=85L, db_column=u'manufacturerURL', blank=True)
    product_url = models.CharField(max_length=85L, db_column=u'productURL', blank=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'MatrixListing'


class MatrixListingAttribute(models.Model):
    matrix_id = models.CharField(max_length=7L, db_column=u'matrixId')
    matrix_listing_id = models.CharField(max_length=7L, db_column=u'matrixListingId')
    attribute_id = models.CharField(max_length=7L, db_column=u'attributeId')
    value = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'MatrixListing_attribute'


class MatrixListingRating(models.Model):
    time_stamp = models.IntegerField(db_column=u'timeStamp')
    category = models.CharField(max_length=85L, blank=True)
    rating = models.IntegerField()
    listing_id = models.CharField(max_length=7L, db_column=u'listingId', blank=True)
    ip_address = models.CharField(max_length=5L, db_column=u'ipAddress', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    user = models.ForeignKey('User', db_column='userId')

    class Meta:
        db_table = u'MatrixListing_rating'


class MatrixListingRatingSummary(models.Model):
    listing_id = models.CharField(max_length=7L, db_column=u'listingId')
    category = models.CharField(max_length=85L)
    mean_value = models.DecimalField(decimal_places=2, null=True, max_digits=3, db_column=u'meanValue', blank=True)
    median_value = models.IntegerField(null=True, db_column=u'medianValue', blank=True)
    count_value = models.IntegerField(null=True, db_column=u'countValue', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)

    class Meta:
        db_table = u'MatrixListing_ratingSummary'


class MatrixAttribute(models.Model):
    attribute_id = models.CharField(max_length=7L, primary_key=True, db_column=u'attributeId')
    category = models.CharField(max_length=85L, blank=True)
    name = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    field_type = models.CharField(max_length=85L, db_column=u'fieldType')
    default_value = models.CharField(max_length=85L, db_column=u'defaultValue', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    options = models.TextField(blank=True)

    class Meta:
        db_table = u'Matrix_attribute'


class MessageBoard(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    visitor_cache_timeout = models.IntegerField(db_column=u'visitorCacheTimeout')

    class Meta:
        db_table = u'MessageBoard'


class MultiSearch(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    predefined_searches = models.TextField(db_column=u'predefinedSearches', blank=True)
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')

    class Meta:
        db_table = u'MultiSearch'


class Navigation(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    assets_to_include = models.TextField(db_column=u'assetsToInclude', blank=True)
    start_type = models.CharField(max_length=11L, db_column=u'startType', blank=True)
    start_point = models.CharField(max_length=85L, db_column=u'startPoint', blank=True)
    descendant_end_point = models.IntegerField(db_column=u'descendantEndPoint')
    show_system_pages = models.IntegerField(db_column=u'showSystemPages')
    show_hidden_pages = models.IntegerField(db_column=u'showHiddenPages')
    show_unprivileged_pages = models.IntegerField(db_column=u'showUnprivilegedPages')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    ancestor_end_point = models.IntegerField(db_column=u'ancestorEndPoint')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    mime_type = models.CharField(max_length=16L, db_column=u'mimeType', blank=True)
    reverse_page_loop = models.IntegerField(null=True, db_column=u'reversePageLoop', blank=True)

    class Meta:
        db_table = u'Navigation'


class Newsletter(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    newsletter_template_id = models.CharField(max_length=7L, db_column=u'newsletterTemplateId', blank=True)
    my_subscriptions_template_id = models.CharField(max_length=7L, db_column=u'mySubscriptionsTemplateId', blank=True)
    newsletter_header = models.TextField(db_column=u'newsletterHeader', blank=True)
    newsletter_footer = models.TextField(db_column=u'newsletterFooter', blank=True)
    newsletter_categories = models.TextField(db_column=u'newsletterCategories', blank=True)

    class Meta:
        db_table = u'Newsletter'


class NewsletterCollection(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    view_template_id = models.CharField(max_length=7L, db_column=u'viewTemplateId')
    recent_issue_count = models.IntegerField(db_column=u'recentIssueCount')

    class Meta:
        db_table = u'NewsletterCollection'


class NewsletterSubscriptions(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    user = models.ForeignKey('User', db_column='userId')
    subscriptions = models.TextField(blank=True)
    last_time_sent = models.BigIntegerField(db_column=u'lastTimeSent')

    class Meta:
        db_table = u'Newsletter_subscriptions'


class PMProject(models.Model):
    project_id = models.CharField(max_length=7L, primary_key=True, db_column=u'projectId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    name = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    start_date = models.BigIntegerField(null=True, db_column=u'startDate', blank=True)
    end_date = models.BigIntegerField(null=True, db_column=u'endDate', blank=True)
    project_manager = models.CharField(max_length=7L, db_column=u'projectManager', blank=True)
    duration_units = models.CharField(max_length=1L, db_column=u'durationUnits', blank=True)
    hours_per_day = models.FloatField(null=True, db_column=u'hoursPerDay', blank=True)
    target_budget = models.FloatField(null=True, db_column=u'targetBudget', blank=True)
    percent_complete = models.FloatField(db_column=u'percentComplete')
    parent_id = models.CharField(max_length=7L, db_column=u'parentId', blank=True)
    creation_date = models.BigIntegerField(db_column=u'creationDate')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)
    last_updated_by = models.CharField(max_length=7L, db_column=u'lastUpdatedBy', blank=True)
    last_update_date = models.BigIntegerField(db_column=u'lastUpdateDate')
    project_observer = models.CharField(max_length=7L, db_column=u'projectObserver', blank=True)

    class Meta:
        db_table = u'PM_project'


class PMTask(models.Model):
    task_id = models.CharField(max_length=7L, primary_key=True, db_column=u'taskId')
    project_id = models.CharField(max_length=7L, db_column=u'projectId', blank=True)
    task_name = models.CharField(max_length=85L, db_column=u'taskName', blank=True)
    duration = models.FloatField(null=True, blank=True)
    start_date = models.BigIntegerField(null=True, db_column=u'startDate', blank=True)
    end_date = models.BigIntegerField(null=True, db_column=u'endDate', blank=True)
    dependants = models.CharField(max_length=16L, blank=True)
    parent_id = models.CharField(max_length=7L, db_column=u'parentId', blank=True)
    percent_complete = models.FloatField(null=True, db_column=u'percentComplete', blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    creation_date = models.BigIntegerField(db_column=u'creationDate')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)
    last_updated_by = models.CharField(max_length=7L, db_column=u'lastUpdatedBy', blank=True)
    last_update_date = models.BigIntegerField(db_column=u'lastUpdateDate')
    lag_time = models.BigIntegerField(null=True, db_column=u'lagTime', blank=True)
    task_type = models.CharField(max_length=3L, db_column=u'taskType')

    class Meta:
        db_table = u'PM_task'


class PMTaskResource(models.Model):
    task_resource_id = models.CharField(max_length=7L, primary_key=True, db_column=u'taskResourceId')
    task_id = models.CharField(max_length=7L, db_column=u'taskId', blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    resource_kind = models.CharField(max_length=1L, db_column=u'resourceKind')
    resource_id = models.CharField(max_length=7L, db_column=u'resourceId', blank=True)

    class Meta:
        db_table = u'PM_taskResource'


class PMWobject(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    project_dashboard_template_id = models.CharField(max_length=7L, db_column=u'projectDashboardTemplateId', blank=True)
    project_display_template_id = models.CharField(max_length=7L, db_column=u'projectDisplayTemplateId', blank=True)
    gantt_chart_template_id = models.CharField(max_length=7L, db_column=u'ganttChartTemplateId', blank=True)
    edit_task_template_id = models.CharField(max_length=7L, db_column=u'editTaskTemplateId', blank=True)
    group_to_add = models.CharField(max_length=7L, db_column=u'groupToAdd', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    resource_popup_template_id = models.CharField(max_length=7L, db_column=u'resourcePopupTemplateId', blank=True)
    resource_list_template_id = models.CharField(max_length=7L, db_column=u'resourceListTemplateId', blank=True)

    class Meta:
        db_table = u'PM_wobject'


class Photo(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    exif_data = models.TextField(db_column=u'exifData', blank=True)
    location = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'Photo'


class PhotoRating(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    visitor_ip = models.CharField(max_length=85L, db_column=u'visitorIp', blank=True)
    rating = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'Photo_rating'


class Poll(models.Model):
    active = models.IntegerField()
    graph_width = models.IntegerField(db_column=u'graphWidth')
    vote_group = models.CharField(max_length=7L, db_column=u'voteGroup', blank=True)
    question = models.CharField(max_length=85L, blank=True)
    a1 = models.CharField(max_length=85L, blank=True)
    a2 = models.CharField(max_length=85L, blank=True)
    a3 = models.CharField(max_length=85L, blank=True)
    a4 = models.CharField(max_length=85L, blank=True)
    a5 = models.CharField(max_length=85L, blank=True)
    a6 = models.CharField(max_length=85L, blank=True)
    a7 = models.CharField(max_length=85L, blank=True)
    a8 = models.CharField(max_length=85L, blank=True)
    a9 = models.CharField(max_length=85L, blank=True)
    a10 = models.CharField(max_length=85L, blank=True)
    a11 = models.CharField(max_length=85L, blank=True)
    a12 = models.CharField(max_length=85L, blank=True)
    a13 = models.CharField(max_length=85L, blank=True)
    a14 = models.CharField(max_length=85L, blank=True)
    a15 = models.CharField(max_length=85L, blank=True)
    a16 = models.CharField(max_length=85L, blank=True)
    a17 = models.CharField(max_length=85L, blank=True)
    a18 = models.CharField(max_length=85L, blank=True)
    a19 = models.CharField(max_length=85L, blank=True)
    a20 = models.CharField(max_length=85L, blank=True)
    karma_per_vote = models.IntegerField(db_column=u'karmaPerVote')
    randomize_answers = models.IntegerField(db_column=u'randomizeAnswers')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    graph_configuration = models.TextField(db_column=u'graphConfiguration', blank=True)
    generate_graph = models.IntegerField(null=True, db_column=u'generateGraph', blank=True)

    class Meta:
        db_table = u'Poll'


class PollAnswer(models.Model):
    answer = models.CharField(max_length=1L, blank=True)
    user = models.ForeignKey('User', db_column='userId')
    ip_address = models.CharField(max_length=16L, db_column=u'ipAddress', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)

    class Meta:
        db_table = u'Poll_answer'


class Post(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    thread_id = models.CharField(max_length=7L, db_column=u'threadId', blank=True)
    username = models.CharField(max_length=10L, blank=True)
    content = models.TextField(blank=True)
    views = models.IntegerField()
    content_type = models.CharField(max_length=11L, db_column=u'contentType', blank=True)
    user_defined1 = models.TextField(db_column=u'userDefined1', blank=True)
    user_defined2 = models.TextField(db_column=u'userDefined2', blank=True)
    user_defined3 = models.TextField(db_column=u'userDefined3', blank=True)
    user_defined4 = models.TextField(db_column=u'userDefined4', blank=True)
    user_defined5 = models.TextField(db_column=u'userDefined5', blank=True)
    storage_id = models.CharField(max_length=7L, db_column=u'storageId', blank=True)
    rating = models.IntegerField()
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    original_email = models.TextField(db_column=u'originalEmail', blank=True)

    class Meta:
        db_table = u'Post'


class PostRating(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    ip_address = models.CharField(max_length=5L, db_column=u'ipAddress', blank=True)
    date_of_rating = models.BigIntegerField(null=True, db_column=u'dateOfRating', blank=True)
    rating = models.IntegerField()

    class Meta:
        db_table = u'Post_rating'


class Product(models.Model):
    image1 = models.CharField(max_length=85L, blank=True)
    image2 = models.CharField(max_length=85L, blank=True)
    image3 = models.CharField(max_length=85L, blank=True)
    brochure = models.CharField(max_length=85L, blank=True)
    manual = models.CharField(max_length=85L, blank=True)
    warranty = models.CharField(max_length=85L, blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')
    thank_you_message = models.TextField(db_column=u'thankYouMessage', blank=True)
    accessory_json = models.TextField(db_column=u'accessoryJSON', blank=True)
    benefit_json = models.TextField(db_column=u'benefitJSON', blank=True)
    feature_json = models.TextField(db_column=u'featureJSON', blank=True)
    related_json = models.TextField(db_column=u'relatedJSON', blank=True)
    specification_json = models.TextField(db_column=u'specificationJSON', blank=True)
    variants_json = models.TextField(db_column=u'variantsJSON', blank=True)
    is_shipping_required = models.IntegerField(null=True, db_column=u'isShippingRequired', blank=True)

    class Meta:
        db_table = u'Product'


class RichEdit(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    ask_about_rich_edit = models.IntegerField(db_column=u'askAboutRichEdit')
    preformatted = models.IntegerField()
    editor_width = models.IntegerField(db_column=u'editorWidth')
    editor_height = models.IntegerField(db_column=u'editorHeight')
    source_editor_width = models.IntegerField(db_column=u'sourceEditorWidth')
    source_editor_height = models.IntegerField(db_column=u'sourceEditorHeight')
    use_br = models.IntegerField(db_column=u'useBr')
    nowrap = models.IntegerField()
    remove_line_breaks = models.IntegerField(db_column=u'removeLineBreaks')
    npwrap = models.IntegerField()
    directionality = models.CharField(max_length=1L)
    toolbar_location = models.CharField(max_length=2L, db_column=u'toolbarLocation', blank=True)
    css_file = models.CharField(max_length=85L, db_column=u'cssFile', blank=True)
    valid_elements = models.TextField(db_column=u'validElements', blank=True)
    toolbar_row1 = models.TextField(db_column=u'toolbarRow1', blank=True)
    toolbar_row2 = models.TextField(db_column=u'toolbarRow2', blank=True)
    toolbar_row3 = models.TextField(db_column=u'toolbarRow3', blank=True)
    enable_context_menu = models.IntegerField(db_column=u'enableContextMenu')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    disable_rich_editor = models.IntegerField(null=True, db_column=u'disableRichEditor', blank=True)
    inline_popups = models.IntegerField(db_column=u'inlinePopups')
    allow_media = models.IntegerField(null=True, db_column=u'allowMedia', blank=True)

    class Meta:
        db_table = u'RichEdit'


class SQLReport(models.Model):
    db_query1 = models.TextField(db_column=u'dbQuery1', blank=True)
    paginate_after = models.IntegerField(db_column=u'paginateAfter')
    preprocess_macros1 = models.IntegerField(null=True, db_column=u'preprocessMacros1', blank=True)
    debug_mode = models.IntegerField(db_column=u'debugMode')
    database_link_id1 = models.CharField(max_length=7L, db_column=u'databaseLinkId1', blank=True)
    placeholder_params1 = models.TextField(db_column=u'placeholderParams1', blank=True)
    preprocess_macros2 = models.IntegerField(null=True, db_column=u'preprocessMacros2', blank=True)
    db_query2 = models.TextField(db_column=u'dbQuery2', blank=True)
    placeholder_params2 = models.TextField(db_column=u'placeholderParams2', blank=True)
    database_link_id2 = models.CharField(max_length=7L, db_column=u'databaseLinkId2', blank=True)
    preprocess_macros3 = models.IntegerField(null=True, db_column=u'preprocessMacros3', blank=True)
    db_query3 = models.TextField(db_column=u'dbQuery3', blank=True)
    placeholder_params3 = models.TextField(db_column=u'placeholderParams3', blank=True)
    database_link_id3 = models.CharField(max_length=7L, db_column=u'databaseLinkId3', blank=True)
    preprocess_macros4 = models.IntegerField(null=True, db_column=u'preprocessMacros4', blank=True)
    db_query4 = models.TextField(db_column=u'dbQuery4', blank=True)
    placeholder_params4 = models.TextField(db_column=u'placeholderParams4', blank=True)
    database_link_id4 = models.CharField(max_length=7L, db_column=u'databaseLinkId4', blank=True)
    preprocess_macros5 = models.IntegerField(null=True, db_column=u'preprocessMacros5', blank=True)
    db_query5 = models.TextField(db_column=u'dbQuery5', blank=True)
    placeholder_params5 = models.TextField(db_column=u'placeholderParams5', blank=True)
    database_link_id5 = models.CharField(max_length=7L, db_column=u'databaseLinkId5', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')
    prequery_statements1 = models.TextField(db_column=u'prequeryStatements1', blank=True)
    prequery_statements2 = models.TextField(db_column=u'prequeryStatements2', blank=True)
    prequery_statements3 = models.TextField(db_column=u'prequeryStatements3', blank=True)
    prequery_statements4 = models.TextField(db_column=u'prequeryStatements4', blank=True)
    prequery_statements5 = models.TextField(db_column=u'prequeryStatements5', blank=True)
    download_type = models.CharField(max_length=85L, db_column=u'downloadType', blank=True)
    download_filename = models.CharField(max_length=85L, db_column=u'downloadFilename', blank=True)
    download_template_id = models.CharField(max_length=7L, db_column=u'downloadTemplateId', blank=True)
    download_mime_type = models.CharField(max_length=85L, db_column=u'downloadMimeType', blank=True)
    download_user_group = models.CharField(max_length=7L, db_column=u'downloadUserGroup', blank=True)

    class Meta:
        db_table = u'SQLReport'


class Shelf(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId')

    class Meta:
        db_table = u'Shelf'


class Shortcut(models.Model):
    override_title = models.IntegerField(db_column=u'overrideTitle')
    override_description = models.IntegerField(db_column=u'overrideDescription')
    override_template = models.IntegerField(db_column=u'overrideTemplate')
    override_display_title = models.IntegerField(db_column=u'overrideDisplayTitle')
    override_template_id = models.CharField(max_length=7L, db_column=u'overrideTemplateId', blank=True)
    shortcut_by_criteria = models.IntegerField(db_column=u'shortcutByCriteria')
    resolve_multiples = models.CharField(max_length=10L, db_column=u'resolveMultiples', blank=True)
    shortcut_criteria = models.TextField(db_column=u'shortcutCriteria', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    shortcut_to_asset_id = models.CharField(max_length=7L, db_column=u'shortcutToAssetId', blank=True)
    disable_content_lock = models.IntegerField(db_column=u'disableContentLock')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    pref_fields_to_show = models.TextField(db_column=u'prefFieldsToShow', blank=True)
    pref_fields_to_import = models.TextField(db_column=u'prefFieldsToImport', blank=True)
    show_reload_icon = models.IntegerField(db_column=u'showReloadIcon')

    class Meta:
        db_table = u'Shortcut'


class ShortcutOverrides(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    field_name = models.CharField(max_length=85L, db_column=u'fieldName')
    new_value = models.TextField(db_column=u'newValue', blank=True)

    class Meta:
        db_table = u'Shortcut_overrides'


class StockData(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    display_template_id = models.CharField(max_length=7L, db_column=u'displayTemplateId', blank=True)
    default_stocks = models.TextField(db_column=u'defaultStocks', blank=True)
    source = models.CharField(max_length=16L, blank=True)
    failover = models.IntegerField(null=True, blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')

    class Meta:
        db_table = u'StockData'


class Story(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    headline = models.CharField(max_length=85L, blank=True)
    subtitle = models.CharField(max_length=85L, blank=True)
    byline = models.CharField(max_length=85L, blank=True)
    location = models.CharField(max_length=85L, blank=True)
    highlights = models.TextField(blank=True)
    story = models.TextField(blank=True)
    photo = models.TextField(blank=True)

    class Meta:
        db_table = u'Story'


class StoryArchive(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    stories_per_page = models.IntegerField(null=True, db_column=u'storiesPerPage', blank=True)
    group_to_post = models.CharField(max_length=7L, db_column=u'groupToPost', blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    story_template_id = models.CharField(max_length=7L, db_column=u'storyTemplateId', blank=True)
    edit_story_template_id = models.CharField(max_length=7L, db_column=u'editStoryTemplateId', blank=True)
    keyword_list_template_id = models.CharField(max_length=7L, db_column=u'keywordListTemplateId', blank=True)
    archive_after = models.IntegerField(null=True, db_column=u'archiveAfter', blank=True)
    rich_editor_id = models.CharField(max_length=7L, db_column=u'richEditorId', blank=True)
    approval_workflow_id = models.CharField(max_length=7L, db_column=u'approvalWorkflowId', blank=True)
    photo_width = models.IntegerField(null=True, db_column=u'photoWidth', blank=True)

    class Meta:
        db_table = u'StoryArchive'


class StoryTopic(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    stories_per = models.IntegerField(null=True, db_column=u'storiesPer', blank=True)
    stories_short = models.IntegerField(null=True, db_column=u'storiesShort', blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    story_template_id = models.CharField(max_length=7L, db_column=u'storyTemplateId', blank=True)

    class Meta:
        db_table = u'StoryTopic'


class Subscription(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    thank_you_message = models.TextField(db_column=u'thankYouMessage', blank=True)
    price = models.FloatField()
    subscription_group = models.CharField(max_length=7L, db_column=u'subscriptionGroup')
    duration = models.CharField(max_length=4L)
    execute_on_subscription = models.CharField(max_length=85L, db_column=u'executeOnSubscription', blank=True)
    karma = models.IntegerField(null=True, blank=True)
    redeem_subscription_code_template_id = models.CharField(max_length=7L, db_column=u'redeemSubscriptionCodeTemplateId')
    recurring_subscription = models.IntegerField(db_column=u'recurringSubscription')

    class Meta:
        db_table = u'Subscription'


class SubscriptionCode(models.Model):
    code = models.CharField(max_length=21L, primary_key=True)
    batch_id = models.CharField(max_length=7L, db_column=u'batchId')
    status = models.CharField(max_length=3L)
    date_used = models.BigIntegerField(null=True, db_column=u'dateUsed', blank=True)
    used_by = models.CharField(max_length=7L, db_column=u'usedBy', blank=True)

    class Meta:
        db_table = u'Subscription_code'


class SubscriptionCodeBatch(models.Model):
    batch_id = models.CharField(max_length=7L, primary_key=True, db_column=u'batchId')
    name = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    subscription_id = models.CharField(max_length=7L, db_column=u'subscriptionId')
    expiration_date = models.BigIntegerField(db_column=u'expirationDate')
    date_created = models.BigIntegerField(db_column=u'dateCreated')

    class Meta:
        db_table = u'Subscription_codeBatch'


class Survey(models.Model):
    group_to_take_survey = models.CharField(max_length=7L, db_column=u'groupToTakeSurvey')
    group_to_edit_survey = models.CharField(max_length=7L, db_column=u'groupToEditSurvey')
    group_to_view_reports = models.CharField(max_length=7L, db_column=u'groupToViewReports')
    overview_template_id = models.CharField(max_length=7L, db_column=u'overviewTemplateId')
    max_responses_per_user = models.IntegerField(db_column=u'maxResponsesPerUser')
    gradebook_template_id = models.CharField(max_length=7L, db_column=u'gradebookTemplateId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    survey_edit_template_id = models.CharField(max_length=7L, db_column=u'surveyEditTemplateId', blank=True)
    answer_edit_template_id = models.CharField(max_length=7L, db_column=u'answerEditTemplateId', blank=True)
    question_edit_template_id = models.CharField(max_length=7L, db_column=u'questionEditTemplateId', blank=True)
    section_edit_template_id = models.CharField(max_length=7L, db_column=u'sectionEditTemplateId', blank=True)
    survey_take_template_id = models.CharField(max_length=7L, db_column=u'surveyTakeTemplateId', blank=True)
    survey_questions_id = models.CharField(max_length=7L, db_column=u'surveyQuestionsId', blank=True)
    exit_url = models.TextField(db_column=u'exitURL', blank=True)
    survey_json = models.TextField(db_column=u'surveyJSON', blank=True)
    time_limit = models.IntegerField(db_column=u'timeLimit')
    show_progress = models.IntegerField(db_column=u'showProgress')
    show_time_limit = models.IntegerField(db_column=u'showTimeLimit')
    do_after_time_limit = models.CharField(max_length=7L, db_column=u'doAfterTimeLimit', blank=True)
    on_survey_end_workflow_id = models.CharField(max_length=7L, db_column=u'onSurveyEndWorkflowId', blank=True)
    quiz_mode_summary = models.IntegerField(null=True, db_column=u'quizModeSummary', blank=True)
    survey_summary_template_id = models.CharField(max_length=7L, db_column=u'surveySummaryTemplateId', blank=True)
    allow_back_btn = models.IntegerField(null=True, db_column=u'allowBackBtn', blank=True)
    feedback_template_id = models.CharField(max_length=7L, db_column=u'feedbackTemplateId', blank=True)
    test_results_template_id = models.CharField(max_length=7L, db_column=u'testResultsTemplateId', blank=True)

    class Meta:
        db_table = u'Survey'


class SurveyAnswerOld(models.Model):
    survey_id = models.CharField(max_length=7L, db_column=u'Survey_id', blank=True)
    survey_question_id = models.CharField(max_length=7L, db_column=u'Survey_questionId', blank=True)
    survey_answer_id = models.CharField(max_length=7L, primary_key=True, db_column=u'Survey_answerId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    goto_question = models.CharField(max_length=7L, db_column=u'gotoQuestion', blank=True)
    answer = models.CharField(max_length=85L, blank=True)
    is_correct = models.IntegerField(db_column=u'isCorrect')

    class Meta:
        db_table = u'Survey_answer_old'


class SurveyOld(models.Model):
    question_order = models.CharField(max_length=10L, db_column=u'questionOrder', blank=True)
    group_to_take_survey = models.CharField(max_length=7L, db_column=u'groupToTakeSurvey', blank=True)
    group_to_view_reports = models.CharField(max_length=7L, db_column=u'groupToViewReports', blank=True)
    mode = models.CharField(max_length=10L, blank=True)
    survey_id = models.CharField(max_length=7L, db_column=u'Survey_id', blank=True)
    anonymous = models.CharField(max_length=0L)
    questions_per_page = models.IntegerField(db_column=u'questionsPerPage')
    response_template_id = models.CharField(max_length=7L, db_column=u'responseTemplateId', blank=True)
    overview_template_id = models.CharField(max_length=7L, db_column=u'overviewTemplateId', blank=True)
    max_responses_per_user = models.IntegerField(db_column=u'maxResponsesPerUser')
    questions_per_response = models.IntegerField(db_column=u'questionsPerResponse')
    gradebook_template_id = models.CharField(max_length=7L, db_column=u'gradebookTemplateId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    default_section_id = models.CharField(max_length=7L, db_column=u'defaultSectionId', blank=True)

    class Meta:
        db_table = u'Survey_old'


class SurveyQuestionResponseOld(models.Model):
    survey_id = models.CharField(max_length=7L, db_column=u'Survey_id', blank=True)
    survey_question_id = models.CharField(max_length=7L, db_column=u'Survey_questionId')
    survey_answer_id = models.CharField(max_length=7L, db_column=u'Survey_answerId')
    survey_response_id = models.CharField(max_length=7L, db_column=u'Survey_responseId')
    response = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    date_of_response = models.BigIntegerField(db_column=u'dateOfResponse')

    class Meta:
        db_table = u'Survey_questionResponse_old'


class SurveyQuestionTypes(models.Model):
    question_type = models.CharField(max_length=18L, primary_key=True, db_column=u'questionType')
    answers = models.TextField()

    class Meta:
        db_table = u'Survey_questionTypes'


class SurveyQuestionOld(models.Model):
    survey_id = models.CharField(max_length=7L, db_column=u'Survey_id', blank=True)
    survey_question_id = models.CharField(max_length=7L, primary_key=True, db_column=u'Survey_questionId')
    question = models.TextField(blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    allow_comment = models.IntegerField(db_column=u'allowComment')
    randomize_answers = models.IntegerField(db_column=u'randomizeAnswers')
    answer_field_type = models.CharField(max_length=11L, db_column=u'answerFieldType', blank=True)
    goto_question = models.CharField(max_length=7L, db_column=u'gotoQuestion', blank=True)
    survey_section_id = models.CharField(max_length=7L, db_column=u'Survey_sectionId', blank=True)

    class Meta:
        db_table = u'Survey_question_old'


class SurveyResponse(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    survey_response_id = models.CharField(max_length=7L, primary_key=True, db_column=u'Survey_responseId')
    user = models.ForeignKey('User', db_column='userId')
    username = models.CharField(max_length=85L, blank=True)
    ip_address = models.CharField(max_length=5L, db_column=u'ipAddress', blank=True)
    start_date = models.BigIntegerField(db_column=u'startDate')
    end_date = models.BigIntegerField(db_column=u'endDate')
    is_complete = models.IntegerField(db_column=u'isComplete')
    anon_id = models.CharField(max_length=85L, db_column=u'anonId', blank=True)
    response_json = models.TextField(db_column=u'responseJSON', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')

    class Meta:
        db_table = u'Survey_response'


class SurveyResponseOld(models.Model):
    survey_id = models.CharField(max_length=7L, db_column=u'Survey_id', blank=True)
    survey_response_id = models.CharField(max_length=7L, primary_key=True, db_column=u'Survey_responseId')
    user = models.ForeignKey('User', db_column='userId')
    username = models.CharField(max_length=85L, blank=True)
    ip_address = models.CharField(max_length=5L, db_column=u'ipAddress', blank=True)
    start_date = models.BigIntegerField(db_column=u'startDate')
    end_date = models.BigIntegerField(db_column=u'endDate')
    is_complete = models.IntegerField(db_column=u'isComplete')

    class Meta:
        db_table = u'Survey_response_old'


class SurveySectionOld(models.Model):
    survey_id = models.CharField(max_length=7L, db_column=u'Survey_id', blank=True)
    survey_section_id = models.CharField(max_length=7L, primary_key=True, db_column=u'Survey_sectionId')
    section_name = models.TextField(db_column=u'sectionName', blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')

    class Meta:
        db_table = u'Survey_section_old'


class SurveyTempReport(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    survey_response_id = models.CharField(max_length=7L, db_column=u'Survey_responseId')
    order = models.IntegerField()
    section_number = models.IntegerField(db_column=u'sectionNumber')
    section_name = models.TextField(db_column=u'sectionName', blank=True)
    question_number = models.IntegerField(db_column=u'questionNumber')
    question_name = models.TextField(db_column=u'questionName', blank=True)
    question_comment = models.TextField(db_column=u'questionComment', blank=True)
    answer_number = models.IntegerField(null=True, db_column=u'answerNumber', blank=True)
    answer_value = models.TextField(db_column=u'answerValue', blank=True)
    answer_comment = models.TextField(db_column=u'answerComment', blank=True)
    entry_date = models.BigIntegerField(db_column=u'entryDate')
    is_correct = models.IntegerField(null=True, db_column=u'isCorrect', blank=True)
    value = models.IntegerField(null=True, blank=True)
    file_storeage_id = models.CharField(max_length=7L, db_column=u'fileStoreageId', blank=True)

    class Meta:
        db_table = u'Survey_tempReport'


class SurveyTest(models.Model):
    test_id = models.CharField(max_length=7L, primary_key=True, db_column=u'testId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    asset_id = models.CharField(max_length=85L, db_column=u'assetId', blank=True)
    name = models.CharField(max_length=85L, blank=True)
    test = models.TextField()

    class Meta:
        db_table = u'Survey_test'


class SyndicatedContent(models.Model):
    rss_url = models.TextField(db_column=u'rssUrl', blank=True)
    max_headlines = models.IntegerField(db_column=u'maxHeadlines')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    has_terms = models.CharField(max_length=85L, db_column=u'hasTerms', blank=True)
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')
    process_macro_in_rss_url = models.IntegerField(null=True, db_column=u'processMacroInRssUrl', blank=True)

    class Meta:
        db_table = u'SyndicatedContent'


class TTProjectList(models.Model):
    project_id = models.CharField(max_length=7L, primary_key=True, db_column=u'projectId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    project_name = models.CharField(max_length=85L, db_column=u'projectName', blank=True)
    creation_date = models.BigIntegerField(db_column=u'creationDate')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)
    last_updated_by = models.CharField(max_length=7L, db_column=u'lastUpdatedBy', blank=True)
    last_update_date = models.BigIntegerField(db_column=u'lastUpdateDate')

    class Meta:
        db_table = u'TT_projectList'


class TTProjectResourceList(models.Model):
    project_id = models.CharField(max_length=7L, db_column=u'projectId')
    resource_id = models.CharField(max_length=7L, db_column=u'resourceId')

    class Meta:
        db_table = u'TT_projectResourceList'


class TTProjectTasks(models.Model):
    task_id = models.CharField(max_length=7L, primary_key=True, db_column=u'taskId')
    project_id = models.CharField(max_length=7L, db_column=u'projectId', blank=True)
    task_name = models.CharField(max_length=85L, db_column=u'taskName', blank=True)

    class Meta:
        db_table = u'TT_projectTasks'


class TTReport(models.Model):
    report_id = models.CharField(max_length=7L, db_column=u'reportId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    start_date = models.CharField(max_length=3L, db_column=u'startDate', blank=True)
    end_date = models.CharField(max_length=3L, db_column=u'endDate', blank=True)
    report_complete = models.IntegerField(db_column=u'reportComplete')
    resource_id = models.CharField(max_length=7L, db_column=u'resourceId', blank=True)
    creation_date = models.BigIntegerField(db_column=u'creationDate')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)
    last_updated_by = models.CharField(max_length=7L, db_column=u'lastUpdatedBy', blank=True)
    last_update_date = models.BigIntegerField(db_column=u'lastUpdateDate')

    class Meta:
        db_table = u'TT_report'


class TTTimeEntry(models.Model):
    entry_id = models.CharField(max_length=7L, primary_key=True, db_column=u'entryId')
    project_id = models.CharField(max_length=7L, db_column=u'projectId', blank=True)
    task_id = models.CharField(max_length=7L, db_column=u'taskId', blank=True)
    task_date = models.CharField(max_length=3L, db_column=u'taskDate', blank=True)
    hours = models.FloatField(null=True, blank=True)
    comments = models.TextField(blank=True)
    report_id = models.CharField(max_length=7L, db_column=u'reportId', blank=True)

    class Meta:
        db_table = u'TT_timeEntry'


class TTWobject(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    user_view_template_id = models.CharField(max_length=7L, db_column=u'userViewTemplateId', blank=True)
    manager_view_template_id = models.CharField(max_length=7L, db_column=u'managerViewTemplateId', blank=True)
    time_row_template_id = models.CharField(max_length=7L, db_column=u'timeRowTemplateId', blank=True)
    pm_asset_id = models.CharField(max_length=7L, db_column=u'pmAssetId', blank=True)
    group_to_manage = models.CharField(max_length=7L, db_column=u'groupToManage', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    pm_integration = models.IntegerField(db_column=u'pmIntegration')

    class Meta:
        db_table = u'TT_wobject'


class Thingy(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    default_thing_id = models.CharField(max_length=7L, db_column=u'defaultThingId', blank=True)

    class Meta:
        db_table = u'Thingy'


class ThingyRecord(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id_view = models.CharField(max_length=7L, db_column=u'templateIdView', blank=True)
    thing_id = models.CharField(max_length=7L, db_column=u'thingId', blank=True)
    thing_fields = models.TextField(db_column=u'thingFields', blank=True)
    thank_you_text = models.TextField(db_column=u'thankYouText', blank=True)
    price = models.FloatField(null=True, blank=True)
    duration = models.BigIntegerField(null=True, blank=True)
    field_price = models.TextField(db_column=u'fieldPrice', blank=True)

    class Meta:
        db_table = u'ThingyRecord'


class ThingyRecordRecord(models.Model):
    record_id = models.CharField(max_length=7L, primary_key=True, db_column=u'recordId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    transaction_id = models.CharField(max_length=85L, db_column=u'transactionId', blank=True)
    asset_id = models.CharField(max_length=85L, db_column=u'assetId', blank=True)
    expires = models.BigIntegerField()
    user = models.ForeignKey('User', db_column='userId')
    fields = models.TextField(blank=True)
    is_hidden = models.IntegerField(db_column=u'isHidden')
    sent_expires_notice = models.IntegerField(db_column=u'sentExpiresNotice')

    class Meta:
        db_table = u'ThingyRecord_record'


class ThingyFields(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    thing_id = models.CharField(max_length=7L, db_column=u'thingId')
    field_id = models.CharField(max_length=7L, db_column=u'fieldId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.BigIntegerField(db_column=u'dateCreated')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy')
    date_updated = models.BigIntegerField(db_column=u'dateUpdated')
    updated_by = models.CharField(max_length=7L, db_column=u'updatedBy')
    label = models.CharField(max_length=85L)
    field_type = models.CharField(max_length=85L, db_column=u'fieldType')
    default_value = models.TextField(db_column=u'defaultValue', blank=True)
    possible_values = models.TextField(db_column=u'possibleValues', blank=True)
    subtext = models.CharField(max_length=85L, blank=True)
    status = models.CharField(max_length=85L)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    vertical = models.IntegerField(null=True, blank=True)
    extras = models.CharField(max_length=85L, blank=True)
    display = models.IntegerField(null=True, blank=True)
    view_screen_title = models.IntegerField(null=True, db_column=u'viewScreenTitle', blank=True)
    display_in_search = models.IntegerField(null=True, db_column=u'displayInSearch', blank=True)
    search_in = models.IntegerField(null=True, db_column=u'searchIn', blank=True)
    field_in_other_thing_id = models.CharField(max_length=7L, db_column=u'fieldInOtherThingId', blank=True)
    size = models.IntegerField(null=True, blank=True)
    pretext = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'Thingy_fields'


class ThingyIkgQcHs3rCevOFoHUiU8kg(models.Model):
    thing_data_id = models.CharField(max_length=7L, primary_key=True, db_column=u'thingDataId')
    date_created = models.IntegerField(db_column=u'dateCreated')
    created_by_id = models.CharField(max_length=7L, db_column=u'createdById')
    updated_by_id = models.CharField(max_length=7L, db_column=u'updatedById')
    updated_by_name = models.CharField(max_length=85L, db_column=u'updatedByName')
    last_updated = models.IntegerField(db_column=u'lastUpdated')
    ip_address = models.CharField(max_length=85L, db_column=u'ipAddress', blank=True)
    field_bm1xw0ch6_xw_dmt_ssn_ny_ti_q = models.CharField(max_length=85L, db_column=u'field_bm1xw0ch6XwDmtSSNNyTiQ', blank=True)
    field_c_w_cwp_s3rr_dcld1_ck2_vz_wtw = models.TextField(db_column=u'field_cWCwpS3rrDCLD1CK2VZWtw', blank=True)
    field_es_k_aj8_dshl_miqdq_sw4i_ig = models.BigIntegerField(null=True, db_column=u'field_-esKAj8DshlMIQDQSw4iIg', blank=True)
    field_7_u_zt5dzr_q_yj_sm_w_epk_cf_xya = models.TextField(db_column=u'field_7UZt5dzrQYjSmWEpkCfXYA', blank=True)
    field_f_xc7_l2_rn_bqn8f_hej_ez3_ja = models.TextField(db_column=u'field_FXc7_l2RnBQN8fHejEz3JA', blank=True)

    class Meta:
        db_table = u'Thingy_ikgQcHs3rCevOFoHUiU8kg'


class ThingyThings(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    thing_id = models.CharField(max_length=7L, primary_key=True, db_column=u'thingId')
    label = models.CharField(max_length=85L)
    edit_screen_title = models.CharField(max_length=85L, db_column=u'editScreenTitle')
    edit_instructions = models.TextField(db_column=u'editInstructions', blank=True)
    group_id_add = models.CharField(max_length=7L, db_column=u'groupIdAdd')
    group_id_edit = models.CharField(max_length=7L, db_column=u'groupIdEdit')
    save_button_label = models.CharField(max_length=85L, db_column=u'saveButtonLabel')
    after_save = models.CharField(max_length=85L, db_column=u'afterSave')
    edit_template_id = models.CharField(max_length=7L, db_column=u'editTemplateId')
    on_add_workflow_id = models.CharField(max_length=7L, db_column=u'onAddWorkflowId', blank=True)
    on_edit_workflow_id = models.CharField(max_length=7L, db_column=u'onEditWorkflowId', blank=True)
    on_delete_workflow_id = models.CharField(max_length=7L, db_column=u'onDeleteWorkflowId', blank=True)
    group_id_view = models.CharField(max_length=7L, db_column=u'groupIdView')
    view_template_id = models.CharField(max_length=7L, db_column=u'viewTemplateId')
    default_view = models.CharField(max_length=85L, db_column=u'defaultView')
    search_screen_title = models.CharField(max_length=85L, db_column=u'searchScreenTitle')
    search_description = models.TextField(db_column=u'searchDescription', blank=True)
    group_id_search = models.CharField(max_length=7L, db_column=u'groupIdSearch')
    group_id_import = models.CharField(max_length=7L, db_column=u'groupIdImport')
    group_id_export = models.CharField(max_length=7L, db_column=u'groupIdExport')
    search_template_id = models.CharField(max_length=7L, db_column=u'searchTemplateId')
    things_per_page = models.IntegerField(db_column=u'thingsPerPage')
    sort_by = models.CharField(max_length=7L, db_column=u'sortBy', blank=True)
    display = models.IntegerField(null=True, blank=True)
    export_meta_data = models.IntegerField(null=True, db_column=u'exportMetaData', blank=True)
    max_entries_per_user = models.IntegerField(null=True, db_column=u'maxEntriesPerUser', blank=True)

    class Meta:
        db_table = u'Thingy_things'


class Thread(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    replies = models.IntegerField()
    last_post_id = models.CharField(max_length=7L, db_column=u'lastPostId', blank=True)
    last_post_date = models.BigIntegerField(null=True, db_column=u'lastPostDate', blank=True)
    is_locked = models.IntegerField(db_column=u'isLocked')
    is_sticky = models.IntegerField(db_column=u'isSticky')
    subscription_group_id = models.CharField(max_length=7L, db_column=u'subscriptionGroupId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    karma = models.IntegerField()
    karma_scale = models.IntegerField(db_column=u'karmaScale')
    karma_rank = models.FloatField(null=True, db_column=u'karmaRank', blank=True)
    thread_rating = models.IntegerField(null=True, db_column=u'threadRating', blank=True)

    class Meta:
        db_table = u'Thread'


class ThreadRead(models.Model):
    thread_id = models.CharField(max_length=7L, db_column=u'threadId', blank=True)
    user = models.ForeignKey('User', db_column='userId')

    class Meta:
        db_table = u'Thread_read'


class UserList(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    show_group_id = models.CharField(max_length=7L, db_column=u'showGroupId', blank=True)
    hide_group_id = models.CharField(max_length=7L, db_column=u'hideGroupId', blank=True)
    users_per_page = models.IntegerField(null=True, db_column=u'usersPerPage', blank=True)
    alphabet = models.TextField(blank=True)
    alphabet_search_field = models.CharField(max_length=42L, db_column=u'alphabetSearchField', blank=True)
    show_only_visible_as_named = models.IntegerField(null=True, db_column=u'showOnlyVisibleAsNamed', blank=True)
    sort_by = models.CharField(max_length=42L, db_column=u'sortBy', blank=True)
    sort_order = models.CharField(max_length=1L, db_column=u'sortOrder', blank=True)
    override_public_email = models.IntegerField(null=True, db_column=u'overridePublicEmail', blank=True)
    override_public_profile = models.IntegerField(null=True, db_column=u'overridePublicProfile', blank=True)

    class Meta:
        db_table = u'UserList'


class WeatherData(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    locations = models.TextField(blank=True)
    partner_id = models.CharField(max_length=33L, db_column=u'partnerId', blank=True)
    license_key = models.CharField(max_length=33L, db_column=u'licenseKey', blank=True)

    class Meta:
        db_table = u'WeatherData'


class WikiMaster(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    group_to_edit_pages = models.CharField(max_length=7L, db_column=u'groupToEditPages', blank=True)
    group_to_administer = models.CharField(max_length=7L, db_column=u'groupToAdminister', blank=True)
    rich_editor = models.CharField(max_length=7L, db_column=u'richEditor', blank=True)
    front_page_template_id = models.CharField(max_length=7L, db_column=u'frontPageTemplateId', blank=True)
    page_template_id = models.CharField(max_length=7L, db_column=u'pageTemplateId', blank=True)
    page_edit_template_id = models.CharField(max_length=7L, db_column=u'pageEditTemplateId', blank=True)
    recent_changes_template_id = models.CharField(max_length=7L, db_column=u'recentChangesTemplateId', blank=True)
    most_popular_template_id = models.CharField(max_length=7L, db_column=u'mostPopularTemplateId', blank=True)
    page_history_template_id = models.CharField(max_length=7L, db_column=u'pageHistoryTemplateId', blank=True)
    search_template_id = models.CharField(max_length=7L, db_column=u'searchTemplateId', blank=True)
    recent_changes_count = models.IntegerField(db_column=u'recentChangesCount')
    recent_changes_count_front = models.IntegerField(db_column=u'recentChangesCountFront')
    most_popular_count = models.IntegerField(db_column=u'mostPopularCount')
    most_popular_count_front = models.IntegerField(db_column=u'mostPopularCountFront')
    thumbnail_size = models.IntegerField(db_column=u'thumbnailSize')
    max_image_size = models.IntegerField(db_column=u'maxImageSize')
    approval_workflow = models.CharField(max_length=7L, db_column=u'approvalWorkflow', blank=True)
    use_content_filter = models.IntegerField(null=True, db_column=u'useContentFilter', blank=True)
    filter_code = models.CharField(max_length=10L, db_column=u'filterCode', blank=True)
    by_keyword_template_id = models.CharField(max_length=7L, db_column=u'byKeywordTemplateId', blank=True)
    allow_attachments = models.IntegerField(db_column=u'allowAttachments')

    class Meta:
        db_table = u'WikiMaster'


class WikiPage(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    content = models.TextField(blank=True)
    views = models.BigIntegerField()
    is_protected = models.IntegerField(db_column=u'isProtected')
    action_taken = models.CharField(max_length=11L, db_column=u'actionTaken', blank=True)
    action_taken_by = models.CharField(max_length=7L, db_column=u'actionTakenBy', blank=True)

    class Meta:
        db_table = u'WikiPage'


class Workflow(models.Model):
    workflow_id = models.CharField(max_length=7L, primary_key=True, db_column=u'workflowId')
    title = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    enabled = models.IntegerField()
    type = models.CharField(max_length=85L, blank=True)
    mode = models.CharField(max_length=6L, blank=True)

    class Meta:
        db_table = u'Workflow'


class WorkflowActivity(models.Model):
    activity_id = models.CharField(max_length=7L, primary_key=True, db_column=u'activityId')
    workflow_id = models.CharField(max_length=7L, db_column=u'workflowId', blank=True)
    title = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)

    class Meta:
        db_table = u'WorkflowActivity'


class WorkflowActivityData(models.Model):
    activity_id = models.CharField(max_length=7L, db_column=u'activityId')
    name = models.CharField(max_length=85L)
    value = models.TextField(blank=True)

    class Meta:
        db_table = u'WorkflowActivityData'


class WorkflowInstance(models.Model):
    instance_id = models.CharField(max_length=7L, primary_key=True, db_column=u'instanceId')
    workflow_id = models.CharField(max_length=7L, db_column=u'workflowId', blank=True)
    current_activity_id = models.CharField(max_length=7L, db_column=u'currentActivityId', blank=True)
    priority = models.IntegerField()
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)
    method_name = models.CharField(max_length=85L, db_column=u'methodName', blank=True)
    parameters = models.TextField(blank=True)
    running_since = models.BigIntegerField(null=True, db_column=u'runningSince', blank=True)
    last_update = models.BigIntegerField(null=True, db_column=u'lastUpdate', blank=True)
    last_status = models.CharField(max_length=5L, db_column=u'lastStatus', blank=True)
    no_session = models.IntegerField(db_column=u'noSession')

    class Meta:
        db_table = u'WorkflowInstance'


class WorkflowInstanceScratch(models.Model):
    instance_id = models.CharField(max_length=7L, db_column=u'instanceId')
    name = models.CharField(max_length=85L)
    value = models.TextField(blank=True)

    class Meta:
        db_table = u'WorkflowInstanceScratch'


class WorkflowSchedule(models.Model):
    task_id = models.CharField(max_length=7L, primary_key=True, db_column=u'taskId')
    title = models.CharField(max_length=85L, blank=True)
    enabled = models.IntegerField()
    run_once = models.IntegerField(db_column=u'runOnce')
    minute_of_hour = models.CharField(max_length=85L, db_column=u'minuteOfHour')
    hour_of_day = models.CharField(max_length=85L, db_column=u'hourOfDay')
    day_of_month = models.CharField(max_length=85L, db_column=u'dayOfMonth')
    month_of_year = models.CharField(max_length=85L, db_column=u'monthOfYear')
    day_of_week = models.CharField(max_length=85L, db_column=u'dayOfWeek')
    workflow_id = models.CharField(max_length=7L, db_column=u'workflowId', blank=True)
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)
    method_name = models.CharField(max_length=85L, db_column=u'methodName', blank=True)
    priority = models.IntegerField()
    parameters = models.TextField(blank=True)

    class Meta:
        db_table = u'WorkflowSchedule'


class ZipArchiveAsset(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    show_page = models.CharField(max_length=85L, db_column=u'showPage', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')

    class Meta:
        db_table = u'ZipArchiveAsset'


class AdSkuPurchase(models.Model):
    ad_sku_purchase_id = models.CharField(max_length=7L, primary_key=True, db_column=u'adSkuPurchaseId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    is_deleted = models.IntegerField(db_column=u'isDeleted')
    clicks_purchased = models.BigIntegerField(null=True, db_column=u'clicksPurchased', blank=True)
    date_of_purchase = models.BigIntegerField(null=True, db_column=u'dateOfPurchase', blank=True)
    impressions_purchased = models.BigIntegerField(null=True, db_column=u'impressionsPurchased', blank=True)
    transaction_item_id = models.CharField(max_length=7L, db_column=u'transactionItemId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    ad_id = models.CharField(max_length=7L, db_column=u'adId', blank=True)
    stored_image = models.CharField(max_length=7L, db_column=u'storedImage', blank=True)

    class Meta:
        db_table = u'adSkuPurchase'


class AdSpace(models.Model):
    ad_space_id = models.CharField(max_length=7L, primary_key=True, db_column=u'adSpaceId')
    name = models.CharField(unique=True, max_length=11L, blank=True)
    title = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    cost_per_impression = models.DecimalField(decimal_places=2, max_digits=11, db_column=u'costPerImpression')
    minimum_impressions = models.IntegerField(db_column=u'minimumImpressions')
    cost_per_click = models.DecimalField(decimal_places=2, max_digits=11, db_column=u'costPerClick')
    minimum_clicks = models.IntegerField(db_column=u'minimumClicks')
    width = models.IntegerField()
    height = models.IntegerField()
    group_to_purchase = models.CharField(max_length=7L, db_column=u'groupToPurchase', blank=True)

    class Meta:
        db_table = u'adSpace'


class Address(models.Model):
    address_id = models.CharField(max_length=7L, primary_key=True, db_column=u'addressId')
    address_book_id = models.CharField(max_length=7L, db_column=u'addressBookId')
    label = models.CharField(max_length=11L, blank=True)
    first_name = models.CharField(max_length=11L, db_column=u'firstName', blank=True)
    last_name = models.CharField(max_length=11L, db_column=u'lastName', blank=True)
    address1 = models.CharField(max_length=11L, blank=True)
    address2 = models.CharField(max_length=11L, blank=True)
    address3 = models.CharField(max_length=11L, blank=True)
    city = models.CharField(max_length=11L, blank=True)
    state = models.CharField(max_length=11L, blank=True)
    country = models.CharField(max_length=11L, blank=True)
    code = models.CharField(max_length=11L, blank=True)
    phone_number = models.CharField(max_length=11L, db_column=u'phoneNumber', blank=True)
    organization = models.CharField(max_length=85L, blank=True)
    email = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'address'


class AddressBook(models.Model):
    address_book_id = models.CharField(max_length=7L, primary_key=True, db_column=u'addressBookId')
    session_id = models.CharField(max_length=7L, db_column=u'sessionId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    default_address_id = models.CharField(max_length=7L, db_column=u'defaultAddressId', blank=True)

    class Meta:
        db_table = u'addressBook'


class Advertisement(models.Model):
    ad_id = models.CharField(max_length=7L, primary_key=True, db_column=u'adId')
    ad_space_id = models.CharField(max_length=7L, db_column=u'adSpaceId', blank=True)
    owner_user = models.ForeignKey('User', db_column='userId')
    is_active = models.IntegerField(db_column=u'isActive')
    title = models.CharField(max_length=85L, blank=True)
    type = models.CharField(max_length=5L, blank=True)
    storage_id = models.CharField(max_length=7L, db_column=u'storageId', blank=True)
    ad_text = models.CharField(max_length=85L, db_column=u'adText', blank=True)
    url = models.TextField(blank=True)
    rich_media = models.TextField(db_column=u'richMedia', blank=True)
    border_color = models.CharField(max_length=2L, db_column=u'borderColor', blank=True)
    text_color = models.CharField(max_length=2L, db_column=u'textColor', blank=True)
    background_color = models.CharField(max_length=2L, db_column=u'backgroundColor', blank=True)
    clicks = models.IntegerField()
    clicks_bought = models.IntegerField(db_column=u'clicksBought')
    impressions = models.IntegerField()
    impressions_bought = models.IntegerField(db_column=u'impressionsBought')
    priority = models.IntegerField()
    next_in_priority = models.BigIntegerField(db_column=u'nextInPriority')
    rendered_ad = models.TextField(db_column=u'renderedAd', blank=True)

    class Meta:
        db_table = u'advertisement'


class AnalyticRule(models.Model):
    rule_id = models.CharField(max_length=7L, primary_key=True, db_column=u'ruleId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    bucket_name = models.CharField(max_length=85L, db_column=u'bucketName', blank=True)
    regexp = models.CharField(max_length=85L)

    class Meta:
        db_table = u'analyticRule'


class Asset(models.Model):
    asset_id = models.CharField(max_length=7L, primary_key=True, db_column=u'assetId')
    parent_id = models.CharField(max_length=7L, db_column=u'parentId', blank=True)
    lineage = models.CharField(unique=True, max_length=85L, blank=True)
    state = models.CharField(max_length=11L, blank=True)
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)
    creation_date = models.BigIntegerField(db_column=u'creationDate')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)
    state_changed = models.CharField(max_length=7L, db_column=u'stateChanged', blank=True)
    state_changed_by = models.CharField(max_length=7L, db_column=u'stateChangedBy', blank=True)
    is_locked_by = models.CharField(max_length=7L, db_column=u'isLockedBy', blank=True)
    is_system = models.IntegerField(db_column=u'isSystem')
    last_exported_as = models.CharField(max_length=85L, db_column=u'lastExportedAs', blank=True)

    class Meta:
        db_table = u'asset'


class AssetAspectComments(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    comments = models.TextField(blank=True)
    average_comment_rating = models.IntegerField(null=True, db_column=u'averageCommentRating', blank=True)

    class Meta:
        db_table = u'assetAspectComments'


class AssetAspectMailable(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    mail_style_template_id = models.CharField(max_length=7L, db_column=u'mailStyleTemplateId')

    class Meta:
        db_table = u'assetAspectMailable'


class AssetAspectRssFeed(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    items_per_feed = models.IntegerField(null=True, db_column=u'itemsPerFeed', blank=True)
    feed_copyright = models.TextField(db_column=u'feedCopyright', blank=True)
    feed_title = models.TextField(db_column=u'feedTitle', blank=True)
    feed_description = models.TextField(db_column=u'feedDescription', blank=True)
    feed_image = models.CharField(max_length=7L, db_column=u'feedImage', blank=True)
    feed_image_link = models.TextField(db_column=u'feedImageLink', blank=True)
    feed_image_description = models.TextField(db_column=u'feedImageDescription', blank=True)
    feed_header_links = models.CharField(max_length=10L, db_column=u'feedHeaderLinks', blank=True)

    class Meta:
        db_table = u'assetAspectRssFeed'


class AssetAspectSubscriber(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    subscription_group_id = models.CharField(max_length=7L, db_column=u'subscriptionGroupId', blank=True)
    subscription_enabled = models.IntegerField(db_column=u'subscriptionEnabled')
    always_confirm_subscription = models.IntegerField(db_column=u'alwaysConfirmSubscription')
    allow_anonymous_subscription = models.IntegerField(db_column=u'allowAnonymousSubscription')
    confirmation_required_template_id = models.CharField(max_length=7L, db_column=u'confirmationRequiredTemplateId', blank=True)
    confirmation_email_template_id = models.CharField(max_length=7L, db_column=u'confirmationEmailTemplateId', blank=True)
    confirmation_email_subject = models.CharField(max_length=85L, db_column=u'confirmationEmailSubject', blank=True)
    no_mutation_email_template_id = models.CharField(max_length=7L, db_column=u'noMutationEmailTemplateId', blank=True)
    no_mutation_email_subject = models.CharField(max_length=85L, db_column=u'noMutationEmailSubject', blank=True)
    list_name = models.CharField(max_length=85L, db_column=u'listName', blank=True)
    confirm_mutation_template_id = models.CharField(max_length=7L, db_column=u'confirmMutationTemplateId')

    class Meta:
        db_table = u'assetAspectSubscriber'


class AssetAspectSubscriberLog(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    request_ip = models.CharField(max_length=5L, db_column=u'requestIp')
    request_date = models.BigIntegerField(db_column=u'requestDate')
    confirmation_ip = models.CharField(max_length=5L, db_column=u'confirmationIp', blank=True)
    confirmation_date = models.BigIntegerField(null=True, db_column=u'confirmationDate', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    email = models.CharField(max_length=85L)
    type = models.CharField(max_length=10L)
    anonymous = models.IntegerField()
    confirmed = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=7L, blank=True)

    class Meta:
        db_table = u'assetAspectSubscriber_log'


class AssetData(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    revised_by = models.CharField(max_length=7L, db_column=u'revisedBy', blank=True)
    tag_id = models.CharField(max_length=7L, db_column=u'tagId', blank=True)
    status = models.CharField(max_length=11L, blank=True)
    title = models.CharField(max_length=85L, blank=True)
    menu_title = models.CharField(max_length=85L, db_column=u'menuTitle', blank=True)
    url = models.CharField(max_length=85L, blank=True)
    owner_user = models.ForeignKey('User', db_column='userId')
    group_id_view = models.CharField(max_length=7L, db_column=u'groupIdView', blank=True)
    group_id_edit = models.CharField(max_length=7L, db_column=u'groupIdEdit', blank=True)
    synopsis = models.TextField(blank=True)
    new_window = models.IntegerField(db_column=u'newWindow')
    is_hidden = models.IntegerField(db_column=u'isHidden')
    is_package = models.IntegerField(db_column=u'isPackage')
    is_prototype = models.IntegerField(db_column=u'isPrototype')
    encrypt_page = models.IntegerField(db_column=u'encryptPage')
    asset_size = models.IntegerField(db_column=u'assetSize')
    extra_head_tags = models.TextField(db_column=u'extraHeadTags', blank=True)
    skip_notification = models.IntegerField(db_column=u'skipNotification')
    is_exportable = models.IntegerField(db_column=u'isExportable')
    inherit_url_from_parent = models.IntegerField(db_column=u'inheritUrlFromParent')
    last_modified = models.BigIntegerField(null=True, db_column=u'lastModified', blank=True)
    extra_head_tags_packed = models.TextField(db_column=u'extraHeadTagsPacked', blank=True)
    use_packed_head_tags = models.IntegerField(null=True, db_column=u'usePackedHeadTags', blank=True)

    class Meta:
        db_table = u'assetData'


class AssetHistory(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    date_stamp = models.BigIntegerField(db_column=u'dateStamp')
    action_taken = models.CharField(max_length=85L, db_column=u'actionTaken', blank=True)
    url = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'assetHistory'


class AssetIndex(models.Model):
    asset_id = models.CharField(max_length=7L, primary_key=True, db_column=u'assetId')
    title = models.CharField(max_length=85L, blank=True)
    synopsis = models.TextField(blank=True)
    url = models.CharField(max_length=85L, blank=True)
    creation_date = models.BigIntegerField(null=True, db_column=u'creationDate', blank=True)
    revision_date = models.BigIntegerField(null=True, db_column=u'revisionDate', blank=True)
    owner_user = models.ForeignKey('User', db_column='userId')
    group_id_view = models.CharField(max_length=7L, db_column=u'groupIdView', blank=True)
    group_id_edit = models.CharField(max_length=7L, db_column=u'groupIdEdit', blank=True)
    lineage = models.CharField(max_length=85L, blank=True)
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)
    is_public = models.IntegerField(db_column=u'isPublic')
    keywords = models.TextField(blank=True)

    class Meta:
        db_table = u'assetIndex'


class AssetKeyword(models.Model):
    keyword = models.CharField(max_length=21L)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')

    class Meta:
        db_table = u'assetKeyword'


class AssetVersionTag(models.Model):
    tag_id = models.CharField(max_length=7L, primary_key=True, db_column=u'tagId')
    name = models.CharField(max_length=85L, blank=True)
    is_committed = models.IntegerField(db_column=u'isCommitted')
    creation_date = models.BigIntegerField(db_column=u'creationDate')
    created_by = models.CharField(max_length=7L, db_column=u'createdBy', blank=True)
    commit_date = models.BigIntegerField(db_column=u'commitDate')
    committed_by = models.CharField(max_length=7L, db_column=u'committedBy', blank=True)
    is_locked = models.IntegerField(db_column=u'isLocked')
    locked_by = models.CharField(max_length=7L, db_column=u'lockedBy', blank=True)
    group_to_use = models.CharField(max_length=7L, db_column=u'groupToUse', blank=True)
    workflow_id = models.CharField(max_length=7L, db_column=u'workflowId', blank=True)
    workflow_instance_id = models.CharField(max_length=7L, db_column=u'workflowInstanceId', blank=True)
    comments = models.TextField(blank=True)
    start_time = models.DateTimeField(null=True, db_column=u'startTime', blank=True)
    end_time = models.DateTimeField(null=True, db_column=u'endTime', blank=True)
    is_site_wide = models.IntegerField(db_column=u'isSiteWide')

    class Meta:
        db_table = u'assetVersionTag'


class Base64Field(models.TextField):

    def contribute_to_class(self, cls, name):
        if self.db_column is None:
            self.db_column = name
        self.field_name = name + '_base64'
        super(Base64Field, self).contribute_to_class(cls, self.field_name)
        setattr(cls, name, property(self.get_data, self.set_data))

    def get_data(self, obj):
        return base64.decodestring(getattr(obj, self.field_name) + '==')

    def set_data(self, obj, data):
        setattr(obj, self.field_name, base64.encodestring(data).rstrip('=='))


class AuthenticationQueryset(models.db.QuerySet):
    pass


class AuthenticationManager(models.Manager):
    def get_queryset(self):
        # Filter to only get the passwords, might want to expand this later but
        # this makes joining easier
        return AuthenticationQueryset(self.model, using=self._db).filter(
            auth_method__exact='WebGUI',
            field_name__exact='identifier',
        )


class Authentication(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    auth_method = models.CharField(max_length=10L, db_column=u'authMethod')
    field_name = models.CharField(max_length=42L, db_column=u'fieldName')
    password = models.Base64Field(db_column=u'fieldData', blank=True)

    objects = AuthenticationManager()

    class Meta:
        db_table = u'authentication'


class BucketLog(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    bucket = models.CharField(max_length=7L, db_column=u'Bucket')
    duration = models.IntegerField(null=True, blank=True)
    time_stamp = models.DateTimeField(null=True, db_column=u'timeStamp', blank=True)

    class Meta:
        db_table = u'bucketLog'


class Cache(models.Model):
    namespace = models.CharField(max_length=42L)
    cachekey = models.CharField(max_length=42L)
    expires = models.BigIntegerField()
    size = models.IntegerField()
    content = models.TextField(blank=True)

    class Meta:
        db_table = u'cache'


class Cart(models.Model):
    cart_id = models.CharField(max_length=7L, primary_key=True, db_column=u'cartId')
    session_id = models.CharField(max_length=7L, db_column=u'sessionId')
    shipping_address_id = models.CharField(max_length=7L, db_column=u'shippingAddressId', blank=True)
    shipper_id = models.CharField(max_length=7L, db_column=u'shipperId', blank=True)
    pos_user = models.ForeignKey('User', db_column='userId')
    creation_date = models.IntegerField(null=True, db_column=u'creationDate', blank=True)

    class Meta:
        db_table = u'cart'


class CartItem(models.Model):
    item_id = models.CharField(max_length=7L, primary_key=True, db_column=u'itemId')
    cart_id = models.CharField(max_length=7L, db_column=u'cartId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    date_added = models.DateTimeField(db_column=u'dateAdded')
    options = models.TextField(blank=True)
    configured_title = models.CharField(max_length=85L, db_column=u'configuredTitle', blank=True)
    shipping_address_id = models.CharField(max_length=7L, db_column=u'shippingAddressId', blank=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = u'cartItem'


class DatabaseLink(models.Model):
    database_link_id = models.CharField(max_length=7L, primary_key=True, db_column=u'databaseLinkId')
    title = models.CharField(max_length=85L, blank=True)
    dsn = models.CharField(max_length=85L, db_column=u'DSN', blank=True)
    username = models.CharField(max_length=85L, blank=True)
    identifier = models.CharField(max_length=85L, blank=True)
    allowed_keywords = models.TextField(db_column=u'allowedKeywords', blank=True)
    allow_macro_access = models.IntegerField(db_column=u'allowMacroAccess')
    additional_parameters = models.CharField(max_length=85L, db_column=u'additionalParameters', blank=True)

    class Meta:
        db_table = u'databaseLink'


class DeltaLog(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    delta = models.IntegerField(null=True, blank=True)
    time_stamp = models.BigIntegerField(null=True, db_column=u'timeStamp', blank=True)
    url = models.CharField(max_length=85L)

    class Meta:
        db_table = u'deltaLog'


class Donation(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    default_price = models.FloatField(db_column=u'defaultPrice')
    thank_you_message = models.TextField(db_column=u'thankYouMessage', blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId')

    class Meta:
        db_table = u'donation'


class FilePumpBundle(models.Model):
    bundle_id = models.CharField(max_length=7L, primary_key=True, db_column=u'bundleId')
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    bundle_name = models.CharField(max_length=85L, db_column=u'bundleName')
    last_modified = models.BigIntegerField(db_column=u'lastModified')
    last_build = models.BigIntegerField(db_column=u'lastBuild')
    js_files = models.TextField(db_column=u'jsFiles')
    css_files = models.TextField(db_column=u'cssFiles')
    other_files = models.TextField(db_column=u'otherFiles')

    class Meta:
        db_table = u'filePumpBundle'


class FriendInvitations(models.Model):
    invite_id = models.CharField(max_length=7L, primary_key=True, db_column=u'inviteId')
    inviter_id = models.CharField(max_length=7L, db_column=u'inviterId', blank=True)
    friend_id = models.CharField(max_length=7L, db_column=u'friendId', blank=True)
    date_sent = models.DateTimeField(db_column=u'dateSent')
    comments = models.CharField(max_length=85L, blank=True)
    message_id = models.CharField(max_length=7L, db_column=u'messageId', blank=True)

    class Meta:
        db_table = u'friendInvitations'


class GroupGroupings(models.Model):
    group_id = models.CharField(max_length=7L, db_column=u'groupId', blank=True)
    in_group = models.CharField(max_length=7L, db_column=u'inGroup', blank=True)

    class Meta:
        db_table = u'groupGroupings'


class Groupings(models.Model):
    group_id = models.CharField(max_length=7L, db_column=u'groupId')
    user = models.ForeignKey('User', db_column='userId')
    expire_date = models.BigIntegerField(db_column=u'expireDate')
    group_admin = models.IntegerField(db_column=u'groupAdmin')

    class Meta:
        db_table = u'groupings'


class Groups(models.Model):
    group_id = models.CharField(max_length=7L, primary_key=True, db_column=u'groupId')
    group_name = models.CharField(max_length=33L, db_column=u'groupName', blank=True)
    description = models.CharField(max_length=85L, blank=True)
    expire_offset = models.IntegerField(db_column=u'expireOffset')
    karma_threshold = models.IntegerField(db_column=u'karmaThreshold')
    ip_filter = models.TextField(db_column=u'ipFilter', blank=True)
    date_created = models.IntegerField(db_column=u'dateCreated')
    last_updated = models.IntegerField(db_column=u'lastUpdated')
    delete_offset = models.IntegerField(db_column=u'deleteOffset')
    expire_notify_offset = models.IntegerField(db_column=u'expireNotifyOffset')
    expire_notify_message = models.TextField(db_column=u'expireNotifyMessage', blank=True)
    expire_notify = models.IntegerField(db_column=u'expireNotify')
    scratch_filter = models.TextField(db_column=u'scratchFilter', blank=True)
    auto_add = models.IntegerField(db_column=u'autoAdd')
    auto_delete = models.IntegerField(db_column=u'autoDelete')
    database_link_id = models.CharField(max_length=7L, db_column=u'databaseLinkId', blank=True)
    group_cache_timeout = models.IntegerField(db_column=u'groupCacheTimeout')
    db_query = models.TextField(db_column=u'dbQuery', blank=True)
    is_editable = models.IntegerField(db_column=u'isEditable')
    show_in_forms = models.IntegerField(db_column=u'showInForms')
    ldap_group = models.CharField(max_length=85L, db_column=u'ldapGroup', blank=True)
    ldap_group_property = models.CharField(max_length=85L, db_column=u'ldapGroupProperty', blank=True)
    ldap_recursive_property = models.CharField(max_length=85L, db_column=u'ldapRecursiveProperty', blank=True)
    ldap_link_id = models.CharField(max_length=7L, db_column=u'ldapLinkId', blank=True)
    ldap_recursive_filter = models.TextField(db_column=u'ldapRecursiveFilter', blank=True)
    is_ad_hoc_mail_group = models.IntegerField(db_column=u'isAdHocMailGroup')

    class Meta:
        db_table = u'groups'


class ImageColor(models.Model):
    color_id = models.CharField(max_length=7L, primary_key=True, db_column=u'colorId')
    name = models.CharField(max_length=85L, blank=True)
    fill_triplet = models.CharField(max_length=2L, db_column=u'fillTriplet')
    fill_alpha = models.CharField(max_length=0L, db_column=u'fillAlpha')
    stroke_triplet = models.CharField(max_length=2L, db_column=u'strokeTriplet')
    stroke_alpha = models.CharField(max_length=0L, db_column=u'strokeAlpha')

    class Meta:
        db_table = u'imageColor'


class ImageFont(models.Model):
    font_id = models.CharField(max_length=7L, primary_key=True, db_column=u'fontId')
    name = models.CharField(max_length=85L, blank=True)
    storage_id = models.CharField(max_length=7L, db_column=u'storageId', blank=True)
    filename = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'imageFont'


class ImagePalette(models.Model):
    palette_id = models.CharField(max_length=7L, primary_key=True, db_column=u'paletteId')
    name = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'imagePalette'


class ImagePaletteColors(models.Model):
    palette_id = models.CharField(max_length=7L, db_column=u'paletteId')
    color_id = models.CharField(max_length=7L, db_column=u'colorId', blank=True)
    palette_order = models.IntegerField(db_column=u'paletteOrder')

    class Meta:
        db_table = u'imagePaletteColors'


class Inbox(models.Model):
    message_id = models.CharField(max_length=7L, primary_key=True, db_column=u'messageId')
    status = models.CharField(max_length=5L, blank=True)
    date_stamp = models.BigIntegerField(db_column=u'dateStamp')
    completed_on = models.BigIntegerField(null=True, db_column=u'completedOn', blank=True)
    completed_by = models.CharField(max_length=7L, db_column=u'completedBy', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    group_id = models.CharField(max_length=7L, db_column=u'groupId', blank=True)
    subject = models.CharField(max_length=85L, blank=True)
    message = models.TextField(blank=True)
    sent_by = models.CharField(max_length=7L, db_column=u'sentBy', blank=True)

    class Meta:
        db_table = u'inbox'


class InboxMessageState(models.Model):
    message_id = models.CharField(max_length=7L, db_column=u'messageId')
    user = models.ForeignKey('User', db_column='userId')
    is_read = models.IntegerField(db_column=u'isRead')
    replied_to = models.IntegerField(db_column=u'repliedTo')
    deleted = models.IntegerField()

    class Meta:
        db_table = u'inbox_messageState'


class Incrementer(models.Model):
    incrementer_id = models.CharField(max_length=16L, primary_key=True, db_column=u'incrementerId')
    next_value = models.IntegerField(db_column=u'nextValue')

    class Meta:
        db_table = u'incrementer'


class KarmaLog(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    amount = models.IntegerField()
    source = models.CharField(max_length=85L, blank=True)
    description = models.TextField(blank=True)
    date_modified = models.BigIntegerField(db_column=u'dateModified')

    class Meta:
        db_table = u'karmaLog'


class KbAuth(models.Model):
    username = models.CharField(max_length=33L, blank=True)
    pw = models.TextField(blank=True)

    class Meta:
        db_table = u'kb_auth'


class LdapLink(models.Model):
    ldap_link_id = models.CharField(max_length=7L, primary_key=True, db_column=u'ldapLinkId')
    ldap_link_name = models.CharField(max_length=85L, db_column=u'ldapLinkName', blank=True)
    ldap_url = models.CharField(max_length=85L, db_column=u'ldapUrl', blank=True)
    connect_dn = models.CharField(max_length=85L, db_column=u'connectDn', blank=True)
    identifier = models.CharField(max_length=85L, blank=True)
    ldap_user_rdn = models.CharField(max_length=85L, db_column=u'ldapUserRDN', blank=True)
    ldap_identity = models.CharField(max_length=85L, db_column=u'ldapIdentity', blank=True)
    ldap_identity_name = models.CharField(max_length=85L, db_column=u'ldapIdentityName', blank=True)
    ldap_password_name = models.CharField(max_length=85L, db_column=u'ldapPasswordName', blank=True)
    ldap_send_welcome_message = models.CharField(max_length=0L, db_column=u'ldapSendWelcomeMessage', blank=True)
    ldap_welcome_message = models.TextField(db_column=u'ldapWelcomeMessage', blank=True)
    ldap_account_template = models.CharField(max_length=7L, db_column=u'ldapAccountTemplate', blank=True)
    ldap_create_account_template = models.CharField(max_length=7L, db_column=u'ldapCreateAccountTemplate', blank=True)
    ldap_login_template = models.CharField(max_length=7L, db_column=u'ldapLoginTemplate', blank=True)
    ldap_global_recursive_filter = models.TextField(db_column=u'ldapGlobalRecursiveFilter', blank=True)

    class Meta:
        db_table = u'ldapLink'


class MailQueue(models.Model):
    message_id = models.CharField(max_length=7L, primary_key=True, db_column=u'messageId')
    message = models.TextField(blank=True)
    to_group = models.CharField(max_length=7L, db_column=u'toGroup', blank=True)
    is_inbox = models.IntegerField(null=True, db_column=u'isInbox', blank=True)

    class Meta:
        db_table = u'mailQueue'


class MetaDataProperties(models.Model):
    field_id = models.CharField(max_length=7L, primary_key=True, db_column=u'fieldId')
    field_name = models.CharField(unique=True, max_length=33L, db_column=u'fieldName', blank=True)
    description = models.TextField(blank=True)
    field_type = models.CharField(max_length=10L, db_column=u'fieldType', blank=True)
    possible_values = models.TextField(db_column=u'possibleValues', blank=True)
    default_value = models.CharField(max_length=85L, db_column=u'defaultValue', blank=True)

    class Meta:
        db_table = u'metaData_properties'


class MetaDataValues(models.Model):
    field_id = models.CharField(max_length=7L, db_column=u'fieldId')
    value = models.CharField(max_length=85L, blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')

    class Meta:
        db_table = u'metaData_values'


class PassiveAnalyticsStatus(models.Model):
    start_date = models.DateTimeField(null=True, db_column=u'startDate', blank=True)
    end_date = models.DateTimeField(null=True, db_column=u'endDate', blank=True)
    running = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey('User', db_column='userId')

    class Meta:
        db_table = u'passiveAnalyticsStatus'


class PassiveLog(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    session_id = models.CharField(max_length=7L, db_column=u'sessionId')
    time_stamp = models.BigIntegerField(null=True, db_column=u'timeStamp', blank=True)
    url = models.CharField(max_length=85L)

    class Meta:
        db_table = u'passiveLog'


class PassiveProfileAOI(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    field_id = models.CharField(max_length=7L, db_column=u'fieldId')
    value = models.CharField(max_length=33L)
    count = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'passiveProfileAOI'


class PassiveProfileLog(models.Model):
    passive_profile_log_id = models.CharField(max_length=7L, primary_key=True, db_column=u'passiveProfileLogId')
    user = models.ForeignKey('User', db_column='userId')
    session_id = models.CharField(max_length=7L, db_column=u'sessionId', blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    date_of_entry = models.BigIntegerField(db_column=u'dateOfEntry')

    class Meta:
        db_table = u'passiveProfileLog'


class PaymentGateway(models.Model):
    payment_gateway_id = models.CharField(max_length=7L, primary_key=True, db_column=u'paymentGatewayId')
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)
    options = models.TextField(blank=True)

    class Meta:
        db_table = u'paymentGateway'


class Redirect(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    redirect_url = models.TextField(db_column=u'redirectUrl', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    redirect_type = models.IntegerField(db_column=u'redirectType')

    class Meta:
        db_table = u'redirect'


class Replacements(models.Model):
    replacement_id = models.CharField(max_length=7L, primary_key=True, db_column=u'replacementId')
    search_for = models.CharField(max_length=85L, db_column=u'searchFor', blank=True)
    replace_with = models.TextField(db_column=u'replaceWith', blank=True)

    class Meta:
        db_table = u'replacements'


class Search(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    class_limiter = models.TextField(db_column=u'classLimiter', blank=True)
    search_root = models.CharField(max_length=7L, db_column=u'searchRoot', blank=True)
    template_id = models.CharField(max_length=7L, db_column=u'templateId', blank=True)
    use_containers = models.IntegerField(db_column=u'useContainers')
    paginate_after = models.IntegerField(db_column=u'paginateAfter')

    class Meta:
        db_table = u'search'


class Settings(models.Model):
    name = models.CharField(max_length=85L, primary_key=True)
    value = models.TextField(blank=True)

    class Meta:
        db_table = u'settings'


class Shipper(models.Model):
    shipper_id = models.CharField(max_length=7L, primary_key=True, db_column=u'shipperId')
    class_name = models.CharField(max_length=85L, db_column=u'className', blank=True)
    options = models.TextField(blank=True)

    class Meta:
        db_table = u'shipper'


class ShopCredit(models.Model):
    credit_id = models.CharField(max_length=7L, primary_key=True, db_column=u'creditId')
    user = models.ForeignKey('User', db_column='userId')
    amount = models.FloatField()
    comment = models.TextField(blank=True)
    date_of_adjustment = models.DateTimeField(null=True, db_column=u'dateOfAdjustment', blank=True)

    class Meta:
        db_table = u'shopCredit'


class Sku(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=11L)
    vendor = models.ForeignKey('User', db_column='vendorId')
    display_title = models.IntegerField(db_column=u'displayTitle')
    override_tax_rate = models.IntegerField(db_column=u'overrideTaxRate')
    tax_rate_override = models.FloatField(db_column=u'taxRateOverride')
    tax_configuration = models.TextField(db_column=u'taxConfiguration', blank=True)
    ships_separately = models.IntegerField(db_column=u'shipsSeparately')

    class Meta:
        db_table = u'sku'


class Snippet(models.Model):
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    snippet = models.TextField(blank=True)
    process_as_template = models.IntegerField(db_column=u'processAsTemplate')
    mime_type = models.CharField(max_length=16L, db_column=u'mimeType', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    cache_timeout = models.IntegerField(db_column=u'cacheTimeout')
    snippet_packed = models.TextField(db_column=u'snippetPacked', blank=True)
    use_packed = models.IntegerField(null=True, db_column=u'usePacked', blank=True)

    class Meta:
        db_table = u'snippet'


class TaxDriver(models.Model):
    class_name = models.CharField(max_length=85L, primary_key=True, db_column=u'className')
    options = models.TextField(blank=True)

    class Meta:
        db_table = u'taxDriver'


class TaxEuVatNumbers(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    country_code = models.CharField(max_length=1L, db_column=u'countryCode')
    vat_number = models.CharField(max_length=6L, db_column=u'vatNumber')
    vies_validated = models.IntegerField(null=True, db_column=u'viesValidated', blank=True)
    vies_error_code = models.IntegerField(null=True, db_column=u'viesErrorCode', blank=True)
    approved = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'tax_eu_vatNumbers'


class TaxGenericRates(models.Model):
    tax_id = models.CharField(max_length=7L, primary_key=True, db_column=u'taxId')
    country = models.CharField(max_length=33L)
    state = models.CharField(max_length=33L, blank=True)
    city = models.CharField(max_length=33L, blank=True)
    code = models.CharField(max_length=33L, blank=True)
    tax_rate = models.FloatField(db_column=u'taxRate')

    class Meta:
        db_table = u'tax_generic_rates'


class Template(models.Model):
    template = models.TextField(blank=True)
    namespace = models.CharField(max_length=11L, blank=True)
    is_editable = models.IntegerField(db_column=u'isEditable')
    show_in_forms = models.IntegerField(db_column=u'showInForms')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    parser = models.CharField(max_length=85L, blank=True)
    is_default = models.IntegerField(null=True, db_column=u'isDefault', blank=True)
    template_packed = models.TextField(db_column=u'templatePacked', blank=True)
    use_packed = models.IntegerField(null=True, db_column=u'usePacked', blank=True)

    class Meta:
        db_table = u'template'


class TemplateAttachments(models.Model):
    template_id = models.CharField(max_length=7L, db_column=u'templateId')
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    url = models.CharField(max_length=85L)
    type = models.CharField(max_length=6L, blank=True)
    sequence = models.IntegerField(null=True, blank=True)
    attach_id = models.CharField(max_length=7L, primary_key=True, db_column=u'attachId')

    class Meta:
        db_table = u'template_attachments'


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=7L, primary_key=True, db_column=u'transactionId')
    originating_transaction_id = models.CharField(max_length=7L, db_column=u'originatingTransactionId', blank=True)
    is_successful = models.IntegerField(db_column=u'isSuccessful')
    order_number = models.IntegerField(unique=True, db_column=u'orderNumber')
    transaction_code = models.CharField(max_length=33L, db_column=u'transactionCode', blank=True)
    status_code = models.CharField(max_length=11L, db_column=u'statusCode', blank=True)
    status_message = models.CharField(max_length=85L, db_column=u'statusMessage', blank=True)
    user = models.ForeignKey('User', db_column='userId')
    username = models.CharField(max_length=11L)
    amount = models.FloatField(null=True, blank=True)
    shop_credit_deduction = models.FloatField(null=True, db_column=u'shopCreditDeduction', blank=True)
    shipping_address_id = models.CharField(max_length=7L, db_column=u'shippingAddressId', blank=True)
    shipping_address_name = models.CharField(max_length=11L, db_column=u'shippingAddressName', blank=True)
    shipping_address1 = models.CharField(max_length=11L, db_column=u'shippingAddress1', blank=True)
    shipping_address2 = models.CharField(max_length=11L, db_column=u'shippingAddress2', blank=True)
    shipping_address3 = models.CharField(max_length=11L, db_column=u'shippingAddress3', blank=True)
    shipping_city = models.CharField(max_length=11L, db_column=u'shippingCity', blank=True)
    shipping_state = models.CharField(max_length=11L, db_column=u'shippingState', blank=True)
    shipping_country = models.CharField(max_length=11L, db_column=u'shippingCountry', blank=True)
    shipping_code = models.CharField(max_length=11L, db_column=u'shippingCode', blank=True)
    shipping_phone_number = models.CharField(max_length=11L, db_column=u'shippingPhoneNumber', blank=True)
    shipping_driver_id = models.CharField(max_length=7L, db_column=u'shippingDriverId', blank=True)
    shipping_driver_label = models.CharField(max_length=11L, db_column=u'shippingDriverLabel', blank=True)
    shipping_price = models.FloatField(null=True, db_column=u'shippingPrice', blank=True)
    payment_address_id = models.CharField(max_length=7L, db_column=u'paymentAddressId', blank=True)
    payment_address_name = models.CharField(max_length=11L, db_column=u'paymentAddressName', blank=True)
    payment_address1 = models.CharField(max_length=11L, db_column=u'paymentAddress1', blank=True)
    payment_address2 = models.CharField(max_length=11L, db_column=u'paymentAddress2', blank=True)
    payment_address3 = models.CharField(max_length=11L, db_column=u'paymentAddress3', blank=True)
    payment_city = models.CharField(max_length=11L, db_column=u'paymentCity', blank=True)
    payment_state = models.CharField(max_length=11L, db_column=u'paymentState', blank=True)
    payment_country = models.CharField(max_length=11L, db_column=u'paymentCountry', blank=True)
    payment_code = models.CharField(max_length=11L, db_column=u'paymentCode', blank=True)
    payment_phone_number = models.CharField(max_length=11L, db_column=u'paymentPhoneNumber', blank=True)
    payment_driver_id = models.CharField(max_length=7L, db_column=u'paymentDriverId', blank=True)
    payment_driver_label = models.CharField(max_length=11L, db_column=u'paymentDriverLabel', blank=True)
    taxes = models.FloatField(null=True, blank=True)
    date_of_purchase = models.DateTimeField(null=True, db_column=u'dateOfPurchase', blank=True)
    is_recurring = models.IntegerField(null=True, db_column=u'isRecurring', blank=True)
    notes = models.TextField(blank=True)
    cashier_user = models.ForeignKey('User', db_column='userId')

    class Meta:
        db_table = u'transaction'


class TransactionItem(models.Model):
    item_id = models.CharField(max_length=7L, primary_key=True, db_column=u'itemId')
    transaction_id = models.CharField(max_length=7L, db_column=u'transactionId')
    asset_id = models.CharField(max_length=7L, db_column=u'assetId', blank=True)
    configured_title = models.CharField(max_length=85L, db_column=u'configuredTitle', blank=True)
    options = models.TextField(blank=True)
    shipping_address_id = models.CharField(max_length=7L, db_column=u'shippingAddressId', blank=True)
    shipping_name = models.CharField(max_length=11L, db_column=u'shippingName', blank=True)
    shipping_address1 = models.CharField(max_length=11L, db_column=u'shippingAddress1', blank=True)
    shipping_address2 = models.CharField(max_length=11L, db_column=u'shippingAddress2', blank=True)
    shipping_address3 = models.CharField(max_length=11L, db_column=u'shippingAddress3', blank=True)
    shipping_city = models.CharField(max_length=11L, db_column=u'shippingCity', blank=True)
    shipping_state = models.CharField(max_length=11L, db_column=u'shippingState', blank=True)
    shipping_country = models.CharField(max_length=11L, db_column=u'shippingCountry', blank=True)
    shipping_code = models.CharField(max_length=11L, db_column=u'shippingCode', blank=True)
    shipping_phone_number = models.CharField(max_length=11L, db_column=u'shippingPhoneNumber', blank=True)
    shipping_tracking_number = models.CharField(max_length=85L, db_column=u'shippingTrackingNumber', blank=True)
    order_status = models.CharField(max_length=11L, db_column=u'orderStatus')
    last_updated = models.DateTimeField(null=True, db_column=u'lastUpdated', blank=True)
    quantity = models.IntegerField()
    price = models.FloatField(null=True, blank=True)
    vendor = models.ForeignKey('User', db_column='vendorId')
    vendor_payout_status = models.CharField(max_length=3L, db_column=u'vendorPayoutStatus', blank=True)
    vendor_payout_amount = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column=u'vendorPayoutAmount', blank=True)
    tax_rate = models.DecimalField(decimal_places=3, null=True, max_digits=6, db_column=u'taxRate', blank=True)
    tax_configuration = models.TextField(db_column=u'taxConfiguration', blank=True)

    class Meta:
        db_table = u'transactionItem'


class UserInvitations(models.Model):
    invite_id = models.CharField(max_length=7L, primary_key=True, db_column=u'inviteId')
    user = models.ForeignKey('User', db_column='userId')
    date_sent = models.DateField(null=True, db_column=u'dateSent', blank=True)
    email = models.CharField(max_length=85L, blank=True)
    new_user = models.ForeignKey('User', db_column='userId')
    date_created = models.DateField(null=True, db_column=u'dateCreated', blank=True)

    class Meta:
        db_table = u'userInvitations'


class UserLoginLog(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    status = models.CharField(max_length=10L, blank=True)
    time_stamp = models.IntegerField(null=True, db_column=u'timeStamp', blank=True)
    ip_address = models.CharField(max_length=42L, db_column=u'ipAddress', blank=True)
    user_agent = models.TextField(db_column=u'userAgent', blank=True)
    session_id = models.CharField(max_length=7L, db_column=u'sessionId', blank=True)
    last_page_viewed = models.IntegerField(null=True, db_column=u'lastPageViewed', blank=True)

    class Meta:
        db_table = u'userLoginLog'


class UserProfileCategory(models.Model):
    profile_category_id = models.CharField(max_length=7L, primary_key=True, db_column=u'profileCategoryId')
    label = models.CharField(max_length=85L, blank=True)
    short_label = models.CharField(max_length=85L, db_column=u'shortLabel', blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    visible = models.IntegerField()
    editable = models.IntegerField()
    protected = models.IntegerField()

    class Meta:
        db_table = u'userProfileCategory'


class UserProfileData(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    email = models.CharField(max_length=85L, blank=True)
    first_name = models.CharField(max_length=85L, db_column=u'firstName', blank=True)
    middle_name = models.CharField(max_length=85L, db_column=u'middleName', blank=True)
    last_name = models.CharField(max_length=85L, db_column=u'lastName', blank=True)
    icq = models.CharField(max_length=85L, blank=True)
    aim = models.CharField(max_length=85L, blank=True)
    msn_im = models.CharField(max_length=85L, db_column=u'msnIM', blank=True)
    yahoo_im = models.CharField(max_length=85L, db_column=u'yahooIM', blank=True)
    cell_phone = models.CharField(max_length=85L, db_column=u'cellPhone', blank=True)
    pager = models.CharField(max_length=85L, blank=True)
    email_to_pager = models.CharField(max_length=85L, db_column=u'emailToPager', blank=True)
    language = models.CharField(max_length=85L, blank=True)
    home_address = models.CharField(max_length=85L, db_column=u'homeAddress', blank=True)
    home_city = models.CharField(max_length=85L, db_column=u'homeCity', blank=True)
    home_state = models.CharField(max_length=85L, db_column=u'homeState', blank=True)
    home_zip = models.CharField(max_length=85L, db_column=u'homeZip', blank=True)
    home_country = models.CharField(max_length=85L, db_column=u'homeCountry', blank=True)
    home_phone = models.CharField(max_length=85L, db_column=u'homePhone', blank=True)
    work_address = models.CharField(max_length=85L, db_column=u'workAddress', blank=True)
    work_city = models.CharField(max_length=85L, db_column=u'workCity', blank=True)
    work_state = models.CharField(max_length=85L, db_column=u'workState', blank=True)
    work_zip = models.CharField(max_length=85L, db_column=u'workZip', blank=True)
    work_country = models.CharField(max_length=85L, db_column=u'workCountry', blank=True)
    work_phone = models.CharField(max_length=85L, db_column=u'workPhone', blank=True)
    gender = models.CharField(max_length=85L, blank=True)
    birthdate = models.BigIntegerField(null=True, blank=True)
    home_url = models.CharField(max_length=85L, db_column=u'homeURL', blank=True)
    work_url = models.CharField(max_length=85L, db_column=u'workURL', blank=True)
    work_name = models.CharField(max_length=85L, db_column=u'workName', blank=True)
    time_zone = models.CharField(max_length=85L, db_column=u'timeZone', blank=True)
    date_format = models.CharField(max_length=85L, db_column=u'dateFormat', blank=True)
    time_format = models.CharField(max_length=85L, db_column=u'timeFormat', blank=True)
    discussion_layout = models.CharField(max_length=85L, db_column=u'discussionLayout', blank=True)
    first_day_of_week = models.CharField(max_length=85L, db_column=u'firstDayOfWeek', blank=True)
    ui_level = models.CharField(max_length=85L, db_column=u'uiLevel', blank=True)
    alias = models.CharField(max_length=85L, blank=True)
    signature = models.TextField(blank=True)
    public_profile = models.TextField(db_column=u'publicProfile', blank=True)
    toolbar = models.CharField(max_length=85L, blank=True)
    photo = models.CharField(max_length=7L, blank=True)
    avatar = models.CharField(max_length=7L, blank=True)
    department = models.CharField(max_length=85L, blank=True)
    allow_private_messages = models.TextField(db_column=u'allowPrivateMessages', blank=True)
    able_to_be_friend = models.IntegerField(null=True, db_column=u'ableToBeFriend', blank=True)
    show_message_on_login_seen = models.BigIntegerField(null=True, db_column=u'showMessageOnLoginSeen', blank=True)
    show_online = models.IntegerField(null=True, db_column=u'showOnline', blank=True)
    version_tag_mode = models.CharField(max_length=85L, db_column=u'versionTagMode', blank=True)
    wg_privacy_settings = models.TextField(db_column=u'wg_privacySettings', blank=True)
    receive_inbox_email_notifications = models.IntegerField(null=True, db_column=u'receiveInboxEmailNotifications', blank=True)
    receive_inbox_sms_notifications = models.IntegerField(null=True, db_column=u'receiveInboxSmsNotifications', blank=True)

    class Meta:
        db_table = u'userProfileData'


class UserProfileField(models.Model):
    field_name = models.CharField(max_length=42L, primary_key=True, db_column=u'fieldName')
    label = models.CharField(max_length=85L, blank=True)
    visible = models.IntegerField()
    required = models.IntegerField()
    field_type = models.CharField(max_length=42L, db_column=u'fieldType', blank=True)
    possible_values = models.TextField(db_column=u'possibleValues', blank=True)
    data_default = models.TextField(db_column=u'dataDefault', blank=True)
    sequence_number = models.IntegerField(db_column=u'sequenceNumber')
    profile_category_id = models.CharField(max_length=7L, db_column=u'profileCategoryId', blank=True)
    protected = models.IntegerField()
    editable = models.IntegerField()
    force_image_only = models.IntegerField(null=True, db_column=u'forceImageOnly', blank=True)
    show_at_registration = models.IntegerField(db_column=u'showAtRegistration')
    required_for_password_recovery = models.IntegerField(db_column=u'requiredForPasswordRecovery')
    extras = models.TextField(blank=True)
    default_privacy_setting = models.CharField(max_length=42L, db_column=u'defaultPrivacySetting', blank=True)

    class Meta:
        db_table = u'userProfileField'


class UserSession(models.Model):
    session_id = models.CharField(max_length=7L, primary_key=True, db_column=u'sessionId')
    expires = models.IntegerField(null=True, blank=True)
    last_page_view = models.IntegerField(null=True, db_column=u'lastPageView', blank=True)
    admin_on = models.IntegerField(db_column=u'adminOn')
    last_ip = models.CharField(max_length=16L, db_column=u'lastIP', blank=True)
    user = models.ForeignKey('User', db_column='userId')

    class Meta:
        db_table = u'userSession'


class UserSessionScratch(models.Model):
    session_id = models.CharField(max_length=7L, db_column=u'sessionId')
    name = models.CharField(max_length=85L)
    value = models.TextField(blank=True)

    class Meta:
        db_table = u'userSessionScratch'


class Userpref(models.Model):
    username = models.CharField(max_length=2L)
    preference = models.CharField(max_length=4L)
    value = models.CharField(max_length=85L, blank=True)

    class Meta:
        db_table = u'userpref'


class UserManager(models.Manager):
    def get_queryset(self):
        return (super(UserManager, self)
            .exclude(id__in=('1', '3'))
            .filter(status='Active')
        )


class User(models.Model):
    id = models.CharField(max_length=7L, primary_key=True, db_column=u'userId')
    username = models.CharField(unique=True, max_length=33L, blank=True)
    auth_method = models.CharField(max_length=10L, db_column=u'authMethod', blank=True)
    date_created = models.IntegerField(db_column=u'dateCreated')
    last_updated = models.IntegerField(db_column=u'lastUpdated')
    karma = models.IntegerField()
    status = models.CharField(max_length=11L, blank=True)
    referring_affiliate = models.CharField(max_length=7L, db_column=u'referringAffiliate', blank=True)
    friends_group = models.CharField(max_length=7L, db_column=u'friendsGroup', blank=True)

    class Meta:
        db_table = u'users'


class UsersSpecialState(models.Model):
    user = models.ForeignKey('User', db_column='userId')
    special_state = models.CharField(max_length=10L, db_column=u'specialState')

    class Meta:
        db_table = u'users_specialState'


class Vendor(models.Model):
    id = models.CharField(max_length=7L, primary_key=True, db_column=u'vendorId')
    date_created = models.DateTimeField(null=True, db_column=u'dateCreated', blank=True)
    name = models.CharField(max_length=85L, blank=True)
    user = models.ForeignKey('User', db_column='userId')
    preferred_payment_type = models.CharField(max_length=85L, db_column=u'preferredPaymentType', blank=True)
    payment_information = models.TextField(db_column=u'paymentInformation', blank=True)
    payment_address_id = models.CharField(max_length=7L, db_column=u'paymentAddressId', blank=True)
    url = models.TextField(blank=True)

    class Meta:
        db_table = u'vendor'


class WebguiVersion(models.Model):
    webgui_version = models.CharField(max_length=3L, db_column=u'webguiVersion', blank=True)
    version_type = models.CharField(max_length=10L, db_column=u'versionType', blank=True)
    date_applied = models.IntegerField(null=True, db_column=u'dateApplied', blank=True)

    class Meta:
        db_table = u'webguiVersion'


class Wobject(models.Model):
    display_title = models.IntegerField(db_column=u'displayTitle')
    description = models.TextField(blank=True)
    asset_id = models.CharField(max_length=7L, db_column=u'assetId')
    style_template_id = models.CharField(max_length=7L, db_column=u'styleTemplateId', blank=True)
    printable_style_template_id = models.CharField(max_length=7L, db_column=u'printableStyleTemplateId', blank=True)
    revision_date = models.BigIntegerField(db_column=u'revisionDate')
    mobile_style_template_id = models.CharField(max_length=7L, db_column=u'mobileStyleTemplateId', blank=True)

    class Meta:
        db_table = u'wobject'
