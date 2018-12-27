# -*- coding: utf8 -*-

from flask import current_app

from aip import AipSpeech

from uploads import uploads_path


def read_file(path):
    """
    read file content
    :param path:
    :return:
    """
    with open(path, 'rb') as f:
        return f.read()


def asr():
    """
    automatic speech recognition
    :return:
    """
    # Baidu Cloud AI
    app_id = current_app.config['APP_ID']
    api_key = current_app.config['API_KEY']
    secret_key = current_app.config['SECRET_KEY']

    client = AipSpeech(app_id, api_key, secret_key)
    rsp = client.asr(read_file(f'{uploads_path}/stock.wav'), 'wav', 16000, {'dev_pid': 1536})

    return rsp['result']
