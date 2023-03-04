from django import template
from menu.models import MenuItem
from .drop_down_style import style
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url: str = context['request'].path
    clear_curent = current_url.replace("/", "")
    if current_url == "/":
        menu_items = MenuItem.objects.select_related("parent")
    else:
        menu_items = MenuItem.objects.filter(url=clear_curent).select_related("parent")

    def is_active(item):
        return item.url == clear_curent

    def render_menu(menu_items):
        html_code = style
        for item in menu_items:
            is_item_act = "-active" if is_active(item) else ""
            has_child = item.children.exists()
            sub_menu = render_menu(item.children.all()) if has_child else ""
            html_code += f'<div class="dropdown">'
            html_code += f'<button class="dropbtn{is_item_act}">{item.name}</button>'
            html_code += f'<div class="dropdown-content{is_item_act}">'
            if has_child:
                html_code += sub_menu.replace('<div class="dropdown">', '<div class="sub_dropdown">').replace('<button class="dropbtn', '<button class="sub_dropbtn').replace('<div class="dropdown-content', '<div class="sub_dropdown-content')
            html_code += '</div>'
            html_code += '</div>'
        return html_code

    return mark_safe(render_menu(menu_items))
