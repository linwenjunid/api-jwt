from flask import Blueprint

plus=Blueprint('plus',__name__)

from . import views
