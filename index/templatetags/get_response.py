from django import template
register = template.Library()

@register.filter
def get_response(responses, pk):
    
    
    try:
        answer=responses.response.get(answer_to__pk = pk).answer
        print("printing get response")
        print(answer)
        return answer

    except:
        print("printing get null response")
        return ""
