from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from libs_cms_integration.models import LibsPluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class PollPluginPublisher(CMSPluginBase):
    model = LibsPluginModel  # model where plugin data are saved
    module = _("libs")
    name = _("Libs Plugin")  # name of the plugin in the interface
    render_template = "libs_cms_integration/libs_plugin.html"

    def render(self, context,  instance, placeholder):
        context.update({'instance': instance
                        })

        return context
