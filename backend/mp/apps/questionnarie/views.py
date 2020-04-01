from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView

from libs.question_template import get_all_question
from questionnarie.forms import QuestionnaireForm
from questionnarie.models import Questionnaire, QuestionnaireField, QuestionnaireChoiceField


class QuestionnaireView(View):
    form_class = QuestionnaireForm
    template_name = 'questionnaire/questionnaire_make.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            try:
                title = form.cleaned_data['title']
                brief = form.cleaned_data['brief']
                fb = form.cleaned_data['file'].read().decode()
                all_question = get_all_question(fb)

                # 入库
                q = Questionnaire.add(name=title, brief=brief)

                for i in all_question:
                    if '[多选题]' in i[0] or '【多选题】' in i[0]:
                        q_f_is_mul = True
                    else:
                        q_f_is_mul = False
                    q_f = QuestionnaireField.add(questionnaire_id=q.id, content=i[0], is_multiple=q_f_is_mul)

                    number = 1
                    for j in i[1:]:
                        QuestionnaireChoiceField.add(number=number, field_id=q_f.id, content=j)
                        number += 1
                        
                return redirect('questionnarie:make')
            except Exception as e:
                print(e)
                message = '创建失败'
                return render(request, self.template_name, locals())
        else:
            message = '输入有误'
            return render(request, self.template_name, locals())
