from wagtail.wagtailcore import blocks


FAIR_BUTTON_CHOICES = (
    ('primary', 'primary'),
    ('secondary', 'secondary'),
    ('info', 'info'),
    ('warning', 'warning'),
    ('danger', 'danger'),
    ('success', 'success'),
)



class URLOrPageBlock(blocks.StructBlock):

    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)

    class Meta:
        icon = 'link'
        template = "pages/blocks/url_or_page.html"


class ThreeColumnsBlock(blocks.StructBlock):
    """
    Shows a callout. Can be used in several positions of a StreamField.
    """

    column_1_text = blocks.RichTextBlock()
    column_1_link_url = URLOrPageBlock(required=False)
    column_1_link_text = blocks.CharBlock(required=False)
    column_1_link_button = blocks.ChoiceBlock(choices=FAIR_BUTTON_CHOICES, required=False)

    column_2_text = blocks.RichTextBlock()
    column_2_link_url = URLOrPageBlock(required=False)
    column_2_link_text = blocks.CharBlock(required=False)
    column_2_link_button = blocks.ChoiceBlock(choices=FAIR_BUTTON_CHOICES, required=False)

    column_3_text = blocks.RichTextBlock()
    column_3_link_url = URLOrPageBlock(required=False)
    column_3_link_text = blocks.CharBlock(required=False)
    column_3_link_button = blocks.ChoiceBlock(choices=FAIR_BUTTON_CHOICES, required=False)

    class Meta:
        icon = 'openquote'
        template = "pages/blocks/three_columns.html"


class FeatureMessageBlock(blocks.StructBlock):
    """
    Shows a callout. Can be used in several positions of a StreamField.
    """

    text = blocks.RichTextBlock()
    link_url = URLOrPageBlock(required=False)
    link_text = blocks.CharBlock(required=False)
    link_button = blocks.ChoiceBlock(choices=FAIR_BUTTON_CHOICES, required=False)

    class Meta:
        icon = 'openquote'
        template = "pages/blocks/feature_message.html"
