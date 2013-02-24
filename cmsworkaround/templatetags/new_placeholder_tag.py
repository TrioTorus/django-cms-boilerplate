# Because the placeholder_render tag can't be used as asTag, I need to use this snippet
# recommended by oji and based on a gist found here: https://gist.github.com/988703
# Oji plans on making all cms templatetag asTags for django-cms 2.4

from cms.templatetags.placeholder_tags import RenderPlaceholder
from classytags.helpers import AsTag
from classytags.core import Options
from classytags.arguments import Argument

from django import template

register = template.Library()

class NewRenderPlaceholder(AsTag, RenderPlaceholder):
    name = 'new_render_placeholder'

    options = Options(
        Argument('placeholder'),
        Argument('width', default=None, required=False),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def get_value(self, context, placeholder, width, nodelist=None):
        return RenderPlaceholder.render_tag(self, context, placeholder, width)

register.tag(NewRenderPlaceholder)