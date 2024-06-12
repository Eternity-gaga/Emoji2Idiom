

import json
import pdb
import jsonlines
import os
import random
random.seed(2024)
def build_example(problem,id):
    answer = 'Answer: ' + problem['choices'][problem['answer']] + '\n'
    question = problem['question']
    rationale = problem['lecture'] + problem['solution']
    choices = problem['choices'].copy()
    choices.remove(problem['choices'][problem['answer']])
    distractors = ''
    for i, choice in enumerate(choices):
        distractors += f'({i + 1}) {choice}\n'
    if problem['image'] != None:
        image = 'Picture: <img>' + \
                os.path.join(data_root, problem['split'], str(id), problem[
                    'image']) + f'</img>\n'
        context = f'Context: ' + problem['hint'] + '\n' if problem['hint'] != '' else ''

        qg = '\nExample:\n' + image + context + answer + f'Question: {question}'
        rg = '\nExample:\n' + image + context + f'Question: {question}\n' + answer + f'Reasoning: {rationale}'
        dg = '\nExample:\n' + image + context + f'Question: {question}\n' + f'Reasoning: {rationale}\n' + answer + f'Distractors: {distractors}'
    else:
        context = 'Context: ' + problem['hint'] + '\n' if problem['hint'] != '' else ''
        qg = '\nExample:\n' + context + answer + f'Question: {question}'
        rg = '\nExample:\n' + context + f'Question: {question}\n' + answer + f'Reasoning: {rationale}'
        dg = '\nExample:\n' + context + f'Question: {question}\n' + f'Reasoning: {rationale}\n' + answer + f'Distractors: {distractors}'
    return qg, rg, dg


data_root = 'file_path'
tgt_list = []
save_list = []
save_root = f'save_file_path'
with open(os.path.join(data_root, 'tgt_new.txt'), 'r') as file:
    lines = file.readlines()
    for line in lines:
        tgt_list.append(line.split()[1])
with open(os.path.join(data_root, 'src_new.txt'), 'r') as file:
    lines = file.readlines()
    for num, line in enumerate(lines):
        if num >= 8000:
            dict = {"id": f"identity_{num}"}
            example = line.split()
            image, target = example[0], example[1]
            image_input = 'Picture: <img>' + \
                    os.path.join(data_root, 'pic', image) + f'</img>\n'
            error = ''
            prompt = '<prompt>'
            user_value = image_input + prompt
            conversations = [
                {
                    'from': 'user',
                    'value': user_value
                },
                {
                    'from': 'assistant',
                    'value': assistant_value
                }
            ]
            # true_sentence = tgt_list[num]
            dict.update({'conversations': conversations})
            # print(dict)
            # pdb.set_trace()
            save_list.append(dict)
with open(save_root, 'w') as fp:
    json.dump(save_list, fp)
pdb.set_trace()
save_list = []
split = 'val'
save_root = f'path'
id = 0
sample_ids = []
for qid in problems:
    if problems[qid]['split'] == split:
        sample_ids.append(qid)

with open(save_root, 'w') as fp:
    json.dump(save_list, fp)
# with jsonlines.open(save_root, mode='w') as writer:
#     for item in save_list:
#         writer.write(item)