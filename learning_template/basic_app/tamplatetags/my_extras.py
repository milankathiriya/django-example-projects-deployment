from django import template

register = template.Library()

@register.filter(name = 'cut')  # also using decorator you can register your template filter
def cut(value, arg):    # declare and define your new custom template filter
    """
    function to cut-out args
    """
    return value.replace(args, '')

# register or define your custom template filter named 'cut'
# register.filter('cut', cut)   # also use to register your template filter
