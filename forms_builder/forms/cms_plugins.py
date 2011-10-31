from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from forms_builder.forms.models import CMSForm
from forms_builder.forms.views import process_form

class FormDesignerPlugin(CMSPluginBase):
    model = CMSForm
    name = _("Form")
    admin_preview = False
    render_template = 'forms/form_plugin.html'

    def render(self, context, instance, placeholder):
        return process_form(context['request'], instance.form, context, is_cms_plugin=True)

plugin_pool.register_plugin(FormDesignerPlugin)
