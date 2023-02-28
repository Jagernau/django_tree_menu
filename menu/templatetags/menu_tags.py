from django import template
from django.urls import reverse
from menu.models import MenuItem 
register = template.Library()


from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    # menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    # menu_dict = {}
    # for item in menu_items:
    #     menu_dict[item.id] = {
    #         'name': item.name,
    #         'url': item.url,
    #         'parent': item.parent_id,
    #         'children': [],
    #         'is_active': item.url == current_url
    #     }
    #     if item.parent_id:
    #         menu_dict[item.parent_id]['children'].append(menu_dict[item.id])
    #
    # # Determine which items to expand
    # current_item = None
    # for item in menu_dict.values():
    #     if item['is_active']:
    #         current_item = item
    #         while item['parent']:
    #             item = menu_dict[item['parent']]
    #             item['is_expanded'] = True
    #         break
    # if current_item:
    #     for item in current_item['children']:
    #         item['is_expanded'] = True
    #
    return f"{context}"
