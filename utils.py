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
    ADMIN = 3
    EXIT = 4

class STATUS(Enum):
    OK = 1
    ERROR = 2
    PARAMNULL = 3

class MESSAGES(Enum):
    LOGIN = 1
    LOGINREPLY = 2
    ADMINLOGINREPLY = 3
    LOGOUT = 4
    LOGOUTREPLY = 5 
    ADDCANDIDATO = 6
    ADDCANDIDATOREPLY = 7
    STARTVOTE = 8
    STARTVOTEREPLY = 9
    LISTCANDIDATOS = 10
    LISTCANDIDATOSREPLY = 11
    ENDVOTE = 12
    ENDVOTEREPLY = 13
    CONSULTRESULT = 14
    CONSULTRESULTREPLY = 15
    VOTE = 16
    VOTEREPLY = 17
