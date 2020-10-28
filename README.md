# TCPySocket
A TCP Socket that supports multiple users using Python 3.

### How to run
```
git clone https://github.com/diegosoriarios/TCPySocket
cd TCPySocket
python3 server.py
# Em outros terminais
python3 client.py
```

### Protocolo

#### Login
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | String |
| Login | Array |

#### Logout
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | String |
| Token | String |

#### Search Name
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | String |
| SearchName | String |
| Token | String |

#### Search Name
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | String |
| SearchContent | String |
| Token | String |

#### Upload
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | String |
| Upload | [String] |
| Token | String |

#### Upload
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | String |
| Download | [String] |
| Token | String |

#### Response
| Name  | Value  |
| --- | --- |
| Status | Int |
| Message | Any |
| Operation | String |