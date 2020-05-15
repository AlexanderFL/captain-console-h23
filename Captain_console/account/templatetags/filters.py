from django import template

register = template.Library()

@register.filter
def next(some_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        # return some_list[int(current_index) + 1] # access the next element
        # print(some_list[current_index]['id'])
        return some_list[current_index+1]['id']
    except:
        return 'next failed' # return empty string in case of exception

@register.filter
def previous(some_list, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        # return some_list[int(current_index) - 1] # access the previous element
        if current_index == 0 :
            return ''
        # print(some_list[current_index-1]['id'])
        # print(next(some_list['id']))
        # print("Filter: {}".format(next(some_list)))
        return some_list[current_index - 1]['id']
    except:
        return 'previous failed' # return empty string in case of exception