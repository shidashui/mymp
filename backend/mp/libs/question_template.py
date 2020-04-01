


del_text = ['1、题目与题目之间需空一行，题目可以不加题号，题干中间不得换行', '2、题干与选项，及各选项之间需回车换行，选项不得以数字开头（会被识别为题干）', '3、题目无选项直接空一行，会默认识别为文本型题目']

def get_all_question(text):
    question = []
    all_question = []
    text_list = text.split('\r\n')
    text_list.append('')
    for i in text_list:
        if i:
            question.append(i)
        else:
            if question:
                all_question.append(question)
            question = []
    if del_text in all_question:
        all_question.pop(0)
    return all_question


if __name__ == '__main__':
    with open('test.txt', 'r', encoding='utf8') as f:
        get_all_question(f.read())
