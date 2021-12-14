from django import template

register = template.Library()

@register.simple_tag()
def returnTitle(text):
    
    start = text.find('[')
    text = text[:start]

    return text

@register.simple_tag()
def returnHref(text):

    start = text.find('[') + 1
    end = text.find(']')
    text = text[start:end]
    return text


@register.filter(name='genCollection') 
def genCollection(Page):

    items = [1]
    for i in range(1,Page):
        items.append(1)
    return items