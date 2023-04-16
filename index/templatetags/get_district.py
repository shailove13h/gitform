from django import template
register = template.Library()

@register.filter
def get_district(responses, pk):

    answeid=  responses.response.get(answer_to = pk).answer

    
    return pk