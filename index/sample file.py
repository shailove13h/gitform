
def view_form_responses(request, code):

    form = get_object_or_404(Form, code=code)
    questions = form.questions.all().order_by('id')
    headers = [question.question for question in questions]
    data = []

    for response in form.response_to.all():
        row = []
        for question in questions:
            answer = response.response.filter(answer_to=question).first()
            if answer:
                row.append(answer.answer)
                print(answer.answer)
            else:
                row.append('')
        data.append(row)

    if 'export' in request.POST:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="responses.xlsx"'
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Responses'
        for index, header in enumerate(headers):
            worksheet.cell(row=1, column=index+1, value=header)
        for row_index, row in enumerate(data):
            for column_index, cell in enumerate(row):
                worksheet.cell(row=row_index+2, column=column_index+1, value=cell)
        workbook.save(response)
        return response

    return render(request, 'index/form_newresponse.html', {'form': form, 'headers': headers, 'data': data})
    # return render(request, 'index/form_newresponse.html', context)



for answer in answers:
            
                # choice = answer.answer_to.choices.get(id = answer.answer).choice
                choice = District.objects.filter(id=answer.answer).first()
                print("choce form dtrict")
                print(choice)