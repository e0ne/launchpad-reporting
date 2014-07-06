PROJECT_NAME = 'fuel'

AVAILABLE_PROJECTS = ['fuel']

try:
    from settings_local import *
except ImportError:
    pass
