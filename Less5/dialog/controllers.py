import json


def start_message(request):
    name = request['name_client']
    answer = f'{name}, добро пожаловать в наш сервис'
    answer_data = {
        'code': 200,
        'data': answer
    }
    send_msg = json.dumps(answer_data)
    result = send_msg.encode()
    return answer_data


def event_message(request):
    name = request['name_client']
    answer = f'Уважаемый {name}, библиотека находится за углом'
    answer_data = {
        'code': 200,
        'data': answer
    }
    send_msg = json.dumps(answer_data)
    result = send_msg.encode()
    return answer_data


def error_answer(request):
    error_answer = {
        'code': 400,
        'data': 'Не верный формат запроса'
    }
    send_msg = json.dumps(error_answer)
    result = send_msg.encode()
    return error_answer
