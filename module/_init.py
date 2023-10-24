from _gv import g
from module.classes import conf_class, state_class

def init_config():
    g.MY_CONF = conf_class.ConfClass()

def init_state():
    g.MY_STATE = state_class.StateClass()