# -*- coding: utf8 -*-

from flask import Blueprint

from server.AI import controller

blueprint = Blueprint('AI', __name__)


@blueprint.route('/asr')
def asr():
    rsp = controller.asr().pop()

    return rsp


@blueprint.route('/online_asr')
def online_asr():
    rsp = controller.online_asr().pop()

    return rsp
