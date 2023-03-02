from django import template
from menu.models import MenuItem
from .drop_down_style import style
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url: str = context['request'].path
    clear_curent = current_url.replace("/", "")
    menu_items = MenuItem.objects.all()
    menu_dict = {}
    html_code = style
    for item in menu_items:
         menu_dict[item.id] = {
             'name': item.name,
             'url': item.url,
             'parent': item.parent_id,
             'children': [],
             'is_active': item.url == clear_curent
         }
         if item.parent_id:
             menu_dict[item.parent_id]['children'].append(menu_dict[item.id])
    for i in menu_dict.values():
        active = "-active" if i["is_active"] else ""
        html_code += f'<div class="dropdown">'
        html_code += f'<button class="dropbtn{active}">{i["name"]}</button>'

        if i["children"]:
            html_code += f'<div class="dropdown-content{active}">'
            for n in i["children"]:
                html_code += f'<a href="{n["url"]}">{n["name"]}</a>'
            html_code += '</div>'
        html_code += '</div>'

    return mark_safe(html_code)
