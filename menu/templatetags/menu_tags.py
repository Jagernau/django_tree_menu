from django import template
from menu.models import MenuItem
from .drop_down_stule import stule
from django.utils.safestring import mark_safe
register = template.Library()


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url: str = context['request'].path
    menu_name = current_url.replace("/", "")
    menu_items = MenuItem.objects.all()
    menu_dict = {}
    html_code = stule
    for item in menu_items:
         menu_dict[item.id] = {
             'name': item.name,
             'url': item.url,
             'parent': item.parent_id,
             'children': [],
             'is_active': item.url == current_url
         }
         if item.parent_id:
             menu_dict[item.parent_id]['children'].append(menu_dict[item.id])
    html_code += '<div class="dropdown">'
    for i in menu_dict.values():
        html_code += f'<button class="dropbtn">{i["name"]}</button>'


        html_code += "</div>"
    html_code += "</div>"


    return mark_safe(html_code)
