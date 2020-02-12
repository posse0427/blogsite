from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from django.utils.translation import gettext_lazy as _


class HomePage(Page):
    template = "home/home_page.html"

    banner_image = models.ForeignKey(  # 外部キー,画像
        "wagtailimages.Image",  # 結びつける
        verbose_name=_('banner image'),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,  # deleteしたらnullにする
        related_name="+"  # 複数のフィールドで同じモデルを参照する
    )

    banner_cta = models.ForeignKey(  # 他の自分て作るwagtailページとリンクさせる
        "wagtailcore.Page",  # アプリ名.モデル名
        verbose_name=_('banner cta'),
        help_text=_(
            "CTA refers to buttons and links that call on users to visit your website. "),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [  # デフォルトのパネル +
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]
