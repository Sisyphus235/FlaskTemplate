# -*- coding: utf8 -*-

from flask import current_app

from aip import AipSpeech

from uploads import uploads_path
import sounddevice as sd


def read_file(path):
    """
    read file content
    :param path:
    :return:
    """
    with open(path, 'rb') as f:
        return f.read()


def get_baidu_client():
    """
    set up baidu asr client
    :return:
    """
    # Baidu Cloud AI
    app_id = current_app.config['APP_ID']
    api_key = current_app.config['API_KEY']
    secret_key = current_app.config['SECRET_KEY']

    client = AipSpeech(app_id, api_key, secret_key)

    return client


def asr():
    """
    automatic speech recognition
    :return:
    """
    client = get_baidu_client()

    data = read_file(f'{uploads_path}/stock.wav')
    rsp = client.asr(data, 'wav', 16000, {'dev_pid': 1536})

    return rsp['result']


def online_asr():
    """
    online automatic speech recognition
    :return:
    """
    client = get_baidu_client()

    duration = 10  # set record time as 10s, will be transferred from frontend in the future
    fs = 44100  # sampling frequency, in most cases this will be 44100 or 48000 frames per second
    ndarray_data = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    bytes_data = ndarray_data.tobytes()

    rsp = client.asr(bytes_data)

    return rsp['result']
