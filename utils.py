from enum import Enum

SEARCH_NAME = 'search_name'
SEARCH_CONTENT = 'search_content'
DOWNLOAD = 'download'
UPLOAD = 'upload'
LOGIN = 'login'
LOGOUT = 'logout'
LIST = 'list'

class STATE(Enum):
    CONNECTED = 1
    AUTHENTICATED = 2