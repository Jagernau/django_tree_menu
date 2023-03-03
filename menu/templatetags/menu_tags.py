from django import template
from menu.models import MenuItem
from .drop_down_stule import stule
from django.utils.safestring import mark_safe

register = template.Library()


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent').order_by('id')
    active_url = request.path_info

    def is_active(item):
        return item.url == active_url or active_url.startswith(item.url) and len(active_url) > len(item.url)

    def render_menu(menu_items):
        output = ''
        for item in menu_items:
            is_item_active = is_active(item)
            has_children = item.children.exists()
            if has_children:
                submenu = render_menu(item.children.all())
            else:
                submenu = ''
            css_classes = []
            if is_item_active:
                css_classes.append('active')
            if has_children:
                css_classes.append('has-submenu')
            output += f'<li class="{ " ".join(css_classes) }">'
            if item.url:
                output += f'<a href="{ item.url }"{" class=/"active/"" if is_item_active else ""}>{ item.label }</a>'
            else:
                output += f'<span>{ item.label }</span>'
            output += submenu
            output += '</li>'
        return f'<ul>{ output }</ul>'

    return render_menu(menu_items)
