from django import template

register = template.Library()

@register.filter
def thousand_separator(value):
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")