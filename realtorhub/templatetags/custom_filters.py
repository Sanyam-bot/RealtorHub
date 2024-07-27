from django import template

register = template.Library()

def indian_number_format(value):
    value_str = str(value)
    if len(value_str) <= 3:
        return value_str
    else:
        # Split the number into two parts: the last three digits and the remaining digits
        last_three = value_str[-3:]
        remaining = value_str[:-3]
        # Format the remaining digits into groups of two
        remaining = ','.join([remaining[max(i-2, 0):i] for i in range(len(remaining), 0, -2)][::-1])
        return remaining + ',' + last_three

@register.filter
def intcomma_in(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    return indian_number_format(value)
