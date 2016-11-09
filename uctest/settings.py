from models.request import AccessRequest

SERVERS = {
    'TEST1': 'ad-test1.sm.cn'
}

USERS = {
    'dingbei': {
        'userName': 'dingbei', 'password': 'pd123456'
    }
}

SQLSERVER = {
    'crm': '',
    'uc': '',
    'authorization': {
        'ip': '11.251.199.207',
        'port': 3307,
        'username': 'qa',
        'password': 'pd123456',
        'db': 'cdn_monitor'
    },
    'uc_security': {
        'ip':'11.251.207.148',
        'port': 3307,
        'username': 'admin',
        'password':'3tdnk2Z1Ak',
        'db': 'usercenter'
    }
}

request_dict = {
    'getUserInfor': AccessRequest(method='get', uri='/user/get'),
    'test': AccessRequest(method='get', uri='/console/user/getAllSourcePromotion')
}

SERVER = SERVERS['TEST1']
PROTOCOL = 'https://'
USER = USERS['dingbei']
DATABASE = SQLSERVER['uc_security']
