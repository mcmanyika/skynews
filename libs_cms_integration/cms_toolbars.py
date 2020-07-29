from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from libs.models import t_case


class LibsToolbar(CMSToolbar):
    supported_apps = (
        'libs',
        'libs_cms_integration',
    )

    watch_models = [t_case]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('lib-app', _('Libs'))

        menu.add_sideframe_item(
            name=_('Libs list'),
            url=admin_reverse('libs_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new lib'),
            url=admin_reverse('libs_add'),
        )


toolbar_pool.register(LibsToolbar)  # register the toolbar
