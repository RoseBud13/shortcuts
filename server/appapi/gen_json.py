'''
    input data template:
    {'template': template_name, '1': 'function1', '2': 'function2'}
'''


def gen_json(data_dict):
    # define template name dict
    dict_name = {
        'template_name' : data_dict['template']
    }
    # define step dict
    step_list = []
    for i in range(1, len(data_dict)):
        key_step = 'step' + str(i)
        value = data_dict[str(i)]
        dict_function = {
            "function": value
        }
        dict_step = {
            key_step: dict_function
        }
        step_list.append(dict_step)
    out_dict = {
        "step" : step_list
    }
    result = {k: v for d in [dict_name, out_dict] for k, v in d.items()}
    print(result)
    return result


# if __name__ == '__main__':
#     data_dict = {
#         'template' : 'template_name',
#         '1' : 'function1',
#         '2' : 'function2'
#     }
#     gen_json(data_dict)