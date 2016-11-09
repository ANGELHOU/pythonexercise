#-*- coding:utf-8 –*-
import requests


class Cookie:
    def __init__(self, user):
        print 'inside cookie'
        self._login = {'captchaCode': 'a', 'submit': '登录'}
        self._login.update(user)
        print self._login
        self._cookie = self._get_session_idt()

    def _get_session_idt(self):
        self._session = requests.Session()
        # step1: login and get sso_session
        LOGIN_URL = 'https://ad-test1.sm.cn/sso/v1/login/wlsso/form?authorizeUrl=https:// \
                 ad-test1.sm.cn/sso/v1/authorize?response_type=code&scope=openid&client_id= \
                 eyJhbGciOiJBMTI4S1ciLCJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.kZM1onG \
                 f5b-BeIcLhevONe-OZ_bZkGFccxuDMbHVvfJJMSzq0oo9GA.Y-82VBPEt4HTePQAcTq6EA.-O_f \
                 Uub68KGo9t82jGDtU4qiEiN8BeqNfwdxW3l6wwtz78gxSJhsh_n1D5F6TJ2AKfhyQjI1UUkOCHCuH7 \
                 neM-EOaKVk4X_Ye98C3OnKQ2dlBLGTaCQbYp6YkeDW_0rIQNja6IUSj-2UOT8nqz1mklVjFNxXtcBM_x \
                 -plcmHQ-Ztd2vNGzTAWn3ajqB98yQh0TGEWnI5Xt899uOSXYumNRGUf3G5ZN1IPn2sKZOE-uft_GrxPUSPn \
                 05DWlM8xdOAuQUY0CyPZ2xnMxSjhB928A3MWPhPpFSLofj5gSIE1jzmkf8z1XIKvtJmXSlNfUjWD4sXE2_u_M1 \
                 HN00qK2dkwwdt8ipmqHXG7qnjbglXc3Ah12l06IsuO2Q7_tMimEuB1txGS5CfD8VqA-6TTcxTw1G6GRwkWEMDhkU4 \
                 XO94Jh1ZzPuj-wBlHAf4mHO1fIeaCD-_D8lO-UZSE1w0FWOLdFdVjC5v8CSUb_UhtlRgRltxtwXSebWihdysvBKoOWP \
                 G_Rnk7BncKDiLBjh6wNMC6PjVI7RO3QgRY34i_bCQ6E6z6GSfKd2Ha1HARYBn8irFgcKO-SWLI9Nal6fxFYmNSI3n5h0fHJpk\
                 9_aDlfRLgWYN53LEVhySc7MSq-Dpdc1Wm7hrR41zLdugiUIjL_8J3jfggwmPrH-PtkJ_E42ATKF5R_hP48CMscnb86eY\
                 n8IK2aLQ_dI3RlfsLWdu6lcB08_EwzEKn3O2WYlkymcabKU.FfGFZ6iT9lSR0w2wVq8JWg&redirect_uri=https:// \
                 ad-test1.sm.cn/uc/sso_auth_code&target_url=http://ad-test1.sm.cn/uc/?isFromPortal=0'
        login_res = self._session.post(LOGIN_URL, data=self._login)
        print login_res.cookies.keys()
        sso_session = login_res.cookies['SSO_SESSION']

        # step2: login sso and get sso_idt
        payload_sso = {'sso_session': sso_session}
        SSO_URL = 'https://ad-test1.sm.cn/sso/v1/cors/1231124112/login'
        sso_res = self._session.get(SSO_URL, params=payload_sso)
        sso_idt = 'SSO_IDT=' + sso_res.headers['Authorization']
        return dict(Cookie=sso_idt)

    def session_and_cookie(self):
        return self._session, self._cookie


# if __name__ == '__main__':
#     user = {'userName': 'dingbei', 'password': 'pd123456'}
#     test = Cookie(user)
#     s, cookie = test.session_and_cookie()
#     print s.get('http://ad-test1.sm.cn/console/user/getAllSourcePromotion', headers=cookie).text

# header = dict(Cookie=sso_idt)
# res = s.get(
#     "http://ad-test1.sm.cn/console/user/getAllSourcePromotion", headers=header)
# print res.text
