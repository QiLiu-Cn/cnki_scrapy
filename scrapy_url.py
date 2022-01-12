# -*- codeing = utf-8 -*-
# @Time : 2022/1/6 15:43
# @Author : LiuQi
# @File : scrapy_url.py
# @Software : PyCharm
import json

import requests
from lxml import etree
import re
import pandas as pd
import time


headers = {
        # 'Connection': 'keep-alive',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Cookie': 'Ecp_notFirstLogin=2vSZDh; cangjieConfig_NZKPT=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222021-12-23%22%2C%22endTime%22%3A%222022-01-18%22%2C%22type%22%3A%22mix%22%2C%22intervalTime%22%3A120000%2C%22persist%22%3Afalse%7D; Ecp_ClientId=1211116162303220634; Ecp_loginuserbk=sh0301; cnkiUserKey=ccf7f5b3-014b-a0e3-f26d-fcf938698df3; Ecp_ClientIp=114.212.129.207; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%7D; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1637647915,1638261741,1638512524,1640061028; UM_distinctid=17e29f2e10410ac-0471f1cfbd695c-4303066-13c680-17e29f2e10510ca; knsLeftGroupSelectItem=1%3B2%3B; yeswholedownload=%3Bgagd201404001; dstyle=listmode; dperpage=20; _pk_ref=%5B%22%22%2C%22%22%2C1641837044%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; LID=WEEvREcwSlJHSldSdmVqM1BLYmtFSThnVUkvMGFib05BbmpINE55ekdrST0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; ASP.NET_SessionId=wv25jsqhhxplq3adxwteghiv; SID_kns8=123110; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"sh0301","ShowName":"%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"2vSZDh"}; _pk_id=0cb5013b-bfb5-4c1e-a2c6-5f9b208809b8.1637051025.26.1641838651.1641837044.; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqM1BLYmtFSThnVUkvMGFib05BbmpINE55ekdrST0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=01/11/2022 02:37:31; c_m_expire=2022-01-11%2002%3A37%3A31',
        # 'Cookie': 'Ecp_notFirstLogin=vfFn8X; cangjieConfig_NZKPT=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222021-12-23%22%2C%22endTime%22%3A%222022-01-18%22%2C%22type%22%3A%22mix%22%2C%22intervalTime%22%3A120000%2C%22persist%22%3Afalse%7D; Ecp_ClientId=1211116162303220634; Ecp_loginuserbk=sh0301; cnkiUserKey=ccf7f5b3-014b-a0e3-f26d-fcf938698df3; Ecp_ClientIp=114.212.129.207; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%7D; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1637647915,1638261741,1638512524,1640061028; UM_distinctid=17e29f2e10410ac-0471f1cfbd695c-4303066-13c680-17e29f2e10510ca; knsLeftGroupSelectItem=1%3B2%3B; yeswholedownload=%3Bgagd201404001; dstyle=listmode; dperpage=20; _pk_ref=%5B%22%22%2C%22%22%2C1641901619%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; LID=WEEvREcwSlJHSldSdmVqMDh6cEFHNHhOSGhIOFl4eUxYd0JwOFkwY21xdz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; ASP.NET_SessionId=yv1aysmiblt4iyntimgcwe2k; SID_kns8=123115; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"sh0301","ShowName":"%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"vfFn8X"}; _pk_id=0cb5013b-bfb5-4c1e-a2c6-5f9b208809b8.1637051025.31.1641901656.1641901619.; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqMDh6cEFHNHhOSGhIOFl4eUxYd0JwOFkwY21xdz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=01%2f11%2f2022%2020%3a07%3a34; c_m_expire=2022-01-11%2020%3a07%3a34',
        # 'Cookie': 'Ecp_notFirstLogin=vfFn8X; cangjieConfig_NZKPT=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222021-12-23%22%2C%22endTime%22%3A%222022-01-18%22%2C%22type%22%3A%22mix%22%2C%22intervalTime%22%3A120000%2C%22persist%22%3Afalse%7D; Ecp_ClientId=1211116162303220634; Ecp_loginuserbk=sh0301; cnkiUserKey=ccf7f5b3-014b-a0e3-f26d-fcf938698df3; Ecp_ClientIp=114.212.129.207; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%7D; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1637647915,1638261741,1638512524,1640061028; UM_distinctid=17e29f2e10410ac-0471f1cfbd695c-4303066-13c680-17e29f2e10510ca; knsLeftGroupSelectItem=1%3B2%3B; yeswholedownload=%3Bgagd201404001; dstyle=listmode; dperpage=20; _pk_ref=%5B%22%22%2C%22%22%2C1641901619%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; LID=WEEvREcwSlJHSldSdmVqMDh6cEFHNHhOSGhIOFl4eUxYd0JwOFkwY21xdz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; ASP.NET_SessionId=yv1aysmiblt4iyntimgcwe2k; SID_kns8=123115; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"sh0301","ShowName":"%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"vfFn8X"}; _pk_id=0cb5013b-bfb5-4c1e-a2c6-5f9b208809b8.1637051025.31.1641902391.1641901619.; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqMDh6cEFHNHhOSGhIOFl4eUxYd0JwOFkwY21xdz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=01%2f11%2f2022%2020%3a19%3a49; c_m_expire=2022-01-11%2020%3a19%3a49',
        'Cookie': 'cangjieConfig_NZKPT=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222021-12-23%22%2C%22endTime%22%3A%222022-01-18%22%2C%22type%22%3A%22mix%22%2C%22intervalTime%22%3A120000%2C%22persist%22%3Afalse%7D; Ecp_ClientId=1211116162303220634; Ecp_loginuserbk=sh0301; cnkiUserKey=ccf7f5b3-014b-a0e3-f26d-fcf938698df3; Ecp_ClientIp=114.212.129.207; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2217d27db638cf41-0db4ebb3de01d38-57b1a33-1296000-17d27db638d9aa%22%7D; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1637647915,1638261741,1638512524,1640061028; UM_distinctid=17e29f2e10410ac-0471f1cfbd695c-4303066-13c680-17e29f2e10510ca; knsLeftGroupSelectItem=1%3B2%3B; yeswholedownload=%3Bgagd201404001; dstyle=listmode; dperpage=20; _pk_ref=%5B%22%22%2C%22%22%2C1641901619%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; LID=WEEvREcwSlJHSldSdmVqMDh6cEFHNHhOSGhIOFl4eUxYd0JwOFkwY21xdz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; ASP.NET_SessionId=yv1aysmiblt4iyntimgcwe2k; SID_kns8=123115; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"sh0301","ShowName":"%e5%8d%97%e4%ba%ac%e5%a4%a7%e5%ad%a6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"JSM12w"}; _pk_id=0cb5013b-bfb5-4c1e-a2c6-5f9b208809b8.1637051025.31.1641903566.1641901619.; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqMDh6cEFHNHhOSGhIOFl4eUxYd0JwOFkwY21xdz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=01%2f11%2f2022%2020%3a39%3a24; c_m_expire=2022-01-11%2020%3a39%3a24',
        # 'Cookie': '_ga=GA1.3.1041465585.1570580511; UM_distinctid=175da792dab443-00bd4c1ab04e6d-930346c-144000-175da792dad68c; Hm_lvt_5320013b20652def1496e4f154f179fa=1610423315,1610797230; ccsess=60b8a9a7b911f94263e73d9f6e0475d46f0ec791b09b8b909994dd9c24fc1fbf; acl-poly=s%3AWZSkfEC64gJumqRYT3QfnBdTPz6Wpqiu.3lMhgI%2FSV8PmPV9VCWZ%2FTkYdD%2FeMETO5ibj5hXvuqo8; _ga=GA1.3.1041465585.1570580511; UM_distinctid=175da792dab443-00bd4c1ab04e6d-930346c-144000-175da792dad68c; Hm_lvt_5320013b20652def1496e4f154f179fa=1610423315,1610797230; Ecp_ClientId=2210309195004223734; Ecp_session=1; ASP.NET_SessionId=3wkw4ad5v1afq0rnmghosuuk; SID_kns8=123121; cnkiUserKey=d3613661-6323-c0f2-c194-8eca81b718c0; SID_recommendapi=125141; CurrSortFieldType=desc; SID_kcms=124119; SID_kxreader_new=011123; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1615290685; SID_klogin=125144; Hm_lpvt_6e967eb120601ea41b9d312166416aa6=1615290753; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)+desc; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)+desc; CurrSortFieldType=desc; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"WH0023","ShowName":"%e4%b8%ad%e5%8d%97%e8%b4%a2%e7%bb%8f%e6%94%bf%e6%b3%95%e5%a4%a7%e5%ad%a6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"GPCSKa"}; LID=WEEvREcwSlJHSldSdmVqMDh6a1dqZVBYY0tJMXYxRlFHQml6ZUtUTDlhaz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; SID=088112; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqMDh6a1dqZVBYY0tJMXYxRlFHQml6ZUtUTDlhaz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=03/10/2021 00:08:05; c_m_expire=2021-03-10 00:08:05',
        # 'Referer': 'http://f3442d2d91cfa2485dde859ea753e903.3be401a9.libvpn.zuel.edu.cn/KNS8/AdvSearch?dbcode=CJFQ',
        'Referer': 'https://kns.cnki.net/KNS8/AdvSearch?id=26&dbcode=SCDB&searchtype=gradeSearch&ishistory=1',
        'Origin': 'https://kns.cnki.net',
        'Host': 'kns.cnki.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        # 'Host': 'f3442d2d91cfa2485dde859ea753e903.3be401a9.libvpn.zuel.edu.cn',
        # 'Origin': 'http://f3442d2d91cfa2485dde859ea753e903.3be401a9.libvpn.zuel.edu.cn',
    }
# headers = {        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',

# url = "http://f3442d2d91cfa2485dde859ea753e903.3be401a9.libvpn.zuel.edu.cn/KNS8/Brief/GetGridTableHtml"
url = "https://kns.cnki.net/KNS8/Brief/GetGridTableHtml"
# url = 'https://kns.cnki.net/kns8/AdvSearch?dbprefix=SCDB&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCJD%2CCCVD%2CCJFN/KNS8/Brief/GetGridTableHtml'
def get_page(totalPage):
    for page in range(32,int(totalPage)+1):
        print(page)
        params = {
            'IsSearch': 'true',
            'QueryJson': '{"Platform": "", "DBCode": "SCDB","KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD", "QNode": {"QGroup": [{"Key": "Subject", "Title": "", "Logic": 4, "Items": [], "ChildItems": [{"Key": "input[data-tipid=gradetxt-1]", "Title": "主题", "Logic": 0, "Items": [{"Key": "", "Title": "南海", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南海","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-2]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "东沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "东沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-3]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "西沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "西沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-4]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "南沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-5]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "中沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "中沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []}]},{"Key": "ControlGroup", "Title": "", "Logic": 1, "Items": [], "ChildItems": [{"Key": "span[value=PT]", "Title": "", "Logic": 1, "Items": [{"Key": "span[value=PT]", "Title": "发表时间", "Logic": 1, "Name": "PT","Operate": "", "Value": "2010-01-01", "ExtendType": 2, "ExtendValue": "","Value2": "2010-12-31", "BlurType": ""}], "ChildItems": []}]},{"Key": "NaviParam", "Title": "", "Logic": 1, "Items": [{"Key": "navi", "Title": "", "Logic": 1, "Name": "专题子栏目代码", "Operate": "=","Value": "F?+G?+H?+I?+J?", "ExtendType": 13, "ExtendValue": "", "Value2": "","BlurType": ""}], "ChildItems": []}]}}',

            # 'QueryJson':'{"Platform": "", "DBCode": "SCDB", "KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode": {"QGroup": [{"Key": "Subject", "Title": "", "Logic": 4, "Items": [], "ChildItems": [{"Key": "input[data-tipid=gradetxt-1]", "Title": "主题", "Logic": 0, "Items": [{"Key": "", "Title": "南海", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南海","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-4]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "中沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "中沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-5]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "西沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "西沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-6]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "南沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-7]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "东沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "东沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []}]},{"Key": "ControlGroup", "Title": "", "Logic": 1, "Items": [], "ChildItems": [{"Key": "span[value=PT]", "Title": "", "Logic": 1, "Items": [{"Key": "span[value=PT]", "Title": "发表时间", "Logic": 1, "Name": "PT","Operate": "", "Value": "2010-01-01", "ExtendType": 2, "ExtendValue": "","Value2": "2010-12-31", "BlurType": ""}], "ChildItems": []}]},{"Key": "NaviParam", "Title": "", "Logic": 1, "Items": [{"Key": "navi", "Title": "", "Logic": 1, "Name": "专题子栏目代码", "Operate": "=","Value": "F?+G?+H?+I?+J?", "ExtendType": 13, "ExtendValue": "", "Value2": "","BlurType": ""}], "ChildItems": []}]}}',
            # 'QueryJson': '{"Platform": "", "DBCode": "SCDB","KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD", "QNode": {"QGroup": [{"Key": "Subject", "Title": "", "Logic": 4, "Items": [], "ChildItems": [{"Key": "input[data-tipid=gradetxt-1]", "Title": "主题", "Logic": 0, "Items": [{"Key": "", "Title": "南海", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南海","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-2]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "西沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "西沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-3]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "东沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "东沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-4]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "南沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-5]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "中沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "中沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []}]},{"Key": "ControlGroup", "Title": "", "Logic": 1, "Items": [], "ChildItems": [{"Key": "span[value=PT]", "Title": "", "Logic": 1, "Items": [{"Key": "span[value=PT]", "Title": "发表时间", "Logic": 1, "Name": "PT","Operate": "", "Value": "2010-01-01", "ExtendType": 2, "ExtendValue": "","Value2": "2010-12-31", "BlurType": ""}], "ChildItems": []}]},{"Key": "NaviParam", "Title": "", "Logic": 1, "Items": [{"Key": "navi", "Title": "", "Logic": 1, "Name": "专题子栏目代码", "Operate": "=","Value": "F?+G?+H?+I?+J?", "ExtendType": 13, "ExtendValue": "", "Value2": "", "BlurType": ""}], "ChildItems": []}]}}',
            'PageName': 'AdvSearch',
            'DBCode': 'SCDB',
            '_VIEWSTATE':'',
            # 'KuaKuCodes': 'CJFQ, CDMD, CIPD, CCND, CISD, SNAD, BDZK, CCJD, CCVD, CJFN',
            'CurPage': page,
            'RecordsCntPerPage': '20',
            'HandlerId': '0',
            'CurDisplayMode': 'listmode',
            # # CurrSortField:
            'CurrSortFieldType': 'desc',
            'IsSortSearch': 'false',
            'IsSentenceSearch': 'false',
        }
        params2 = {
            'IsSearch': 'false',
            'QueryJson': '{"Platform": "", "DBCode": "SCDB","KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD", "QNode": {"QGroup": [{"Key": "Subject", "Title": "", "Logic": 4, "Items": [], "ChildItems": [{"Key": "input[data-tipid=gradetxt-1]", "Title": "主题", "Logic": 0, "Items": [{"Key": "", "Title": "南海", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南海","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-2]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "东沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "东沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-3]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "西沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "西沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-4]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "南沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-5]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "中沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "中沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []}]},{"Key": "ControlGroup", "Title": "", "Logic": 1, "Items": [], "ChildItems": [{"Key": "span[value=PT]", "Title": "", "Logic": 1, "Items": [{"Key": "span[value=PT]", "Title": "发表时间", "Logic": 1, "Name": "PT","Operate": "", "Value": "2010-01-01", "ExtendType": 2, "ExtendValue": "","Value2": "2010-12-31", "BlurType": ""}], "ChildItems": []}]},{"Key": "NaviParam", "Title": "", "Logic": 1, "Items": [{"Key": "navi", "Title": "", "Logic": 1, "Name": "专题子栏目代码", "Operate": "=","Value": "F?+G?+H?+I?+J?", "ExtendType": 13, "ExtendValue": "", "Value2": "","BlurType": ""}], "ChildItems": []}]}}',

            # 'QueryJson':'{"Platform": "", "DBCode": "SCDB", "KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode": {"QGroup": [{"Key": "Subject", "Title": "", "Logic": 4, "Items": [], "ChildItems": [{"Key": "input[data-tipid=gradetxt-1]", "Title": "主题", "Logic": 0, "Items": [{"Key": "", "Title": "南海", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南海","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-4]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "中沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "中沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-5]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "西沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "西沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-6]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "南沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-7]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "东沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "东沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []}]},{"Key": "ControlGroup", "Title": "", "Logic": 1, "Items": [], "ChildItems": [{"Key": "span[value=PT]", "Title": "", "Logic": 1, "Items": [{"Key": "span[value=PT]", "Title": "发表时间", "Logic": 1, "Name": "PT","Operate": "", "Value": "2010-01-01", "ExtendType": 2, "ExtendValue": "","Value2": "2010-12-31", "BlurType": ""}], "ChildItems": []}]},{"Key": "NaviParam", "Title": "", "Logic": 1, "Items": [{"Key": "navi", "Title": "", "Logic": 1, "Name": "专题子栏目代码", "Operate": "=","Value": "F?+G?+H?+I?+J?", "ExtendType": 13, "ExtendValue": "", "Value2": "","BlurType": ""}], "ChildItems": []}]}}',
            # 'QueryJson': '{"Platform": "", "DBCode": "SCDB","KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD", "QNode": {"QGroup": [{"Key": "Subject", "Title": "", "Logic": 4, "Items": [], "ChildItems": [{"Key": "input[data-tipid=gradetxt-1]", "Title": "主题", "Logic": 0, "Items": [{"Key": "", "Title": "南海", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南海","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-2]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "西沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "西沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-3]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "东沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "东沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-4]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "南沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "南沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []},{"Key": "input[data-tipid=gradetxt-5]", "Title": "主题", "Logic": 2, "Items": [{"Key": "", "Title": "中沙群岛", "Logic": 1, "Name": "SU", "Operate": "%=", "Value": "中沙群岛","ExtendType": 14, "ExtendValue": "", "Value2": ""}], "ChildItems": []}]},{"Key": "ControlGroup", "Title": "", "Logic": 1, "Items": [], "ChildItems": [{"Key": "span[value=PT]", "Title": "", "Logic": 1, "Items": [{"Key": "span[value=PT]", "Title": "发表时间", "Logic": 1, "Name": "PT","Operate": "", "Value": "2010-01-01", "ExtendType": 2, "ExtendValue": "","Value2": "2010-12-31", "BlurType": ""}], "ChildItems": []}]},{"Key": "NaviParam", "Title": "", "Logic": 1, "Items": [{"Key": "navi", "Title": "", "Logic": 1, "Name": "专题子栏目代码", "Operate": "=","Value": "F?+G?+H?+I?+J?", "ExtendType": 13, "ExtendValue": "", "Value2": "", "BlurType": ""}], "ChildItems": []}]}}',
            'PageName': 'AdvSearch',
            'DBCode': 'SCDB',
            # '_VIEWSTATE':'',
            # 'KuaKuCodes': 'CJFQ, CDMD, CIPD, CCND, CISD, SNAD, BDZK, CCJD, CCVD, CJFN',
            'CurPage': page,
            'RecordsCntPerPage': '20',
            'HandlerId': '0',
            # 'CurDisplayMode': 'listmode',
            # # # CurrSortField:
            # 'CurrSortFieldType': 'desc',
            # 'IsSortSearch': 'false',
            # 'IsSentenceSearch': 'false',
        }
        data = json.dumps(params2)
        proxies = {
            'http': 'http://172.29.40.156:8752',
            'https': 'https://172.29.40.156:8752'
        }
        if page > 1:
            r = requests.post(url=url, data=params2, headers=headers).text
        else:
            r = requests.post(url=url, data=params, headers=headers).text
        if page > 30 :
            time.sleep(5)
        parse_page(r)
        # print(1)
        # print(r)


def parse_page(html):
    # 提取filename
    tree = etree.HTML(html)
    IDList = tree.xpath('//td[@class="name"]/a/@href')
    # print(IDList)
    dbname1 = re.compile('&DbName=(.*?)&DbCode=')
    dbcode1 = re.compile('&DbCode=(.*?)&yx=')
    dbcode2 = re.compile('&DbCode=(.*?)')
    pattern = re.compile('&FileName=(.*?)&DbName=')
    base_url = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFD2010&filename='

    a = 1
    for i in IDList:
        # print(i)
        dbname = re.findall(dbname1, i)[0]
        # print('dbname=%s'%dbname)
        dbcode = re.findall(dbcode1, i)
        if len(dbcode) != 0:
            dbcode = dbcode[0]
        else:
            dbcode = re.findall(dbcode2, i)[0]
        # print('dbcode=%s' % dbcode)
        ID = re.findall(pattern, i)[0]
        pageUrl = base_url + ID
        # print(pageUrl)
        r1 = requests.get(pageUrl, headers=headers).text

        tree1 = etree.HTML(r1)
        # 标题
        title = tree1.xpath('//div[@class="wx-tit"]/h1/text()')
        # print(title)

        if len(title) == 0:
            pageUrl ='https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=' + dbcode + '&dbname=' + dbname + '&filename=' + ID
            print('pageurl=%s'%pageUrl)
            r1 = requests.get(pageUrl, headers=headers).text
            tree1 = etree.HTML(r1)
            title = tree1.xpath('//div[@class="wx-tit"]/h1/text()')


        if len(title) == 0:
            pageUrl = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CCND&dbname=CCNDLAST2011&filename=' + ID
            print('pageurl2=%s' % pageUrl)
            r1 = requests.get(pageUrl, headers=headers).text
            tree1 = etree.HTML(r1)
            title = tree1.xpath('//div[@class="wx-tit"]/h1/text()')

        if len(title) == 0:
            pageUrl = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD2012&filename=' + ID
            print('pageurl3=%s' % pageUrl)
            r1 = requests.get(pageUrl, headers=headers).text
            tree1 = etree.HTML(r1)
            title = tree1.xpath('//div[@class="wx-tit"]/h1/text()')

        if len(title) == 0:
            pageUrl = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CCJD&dbname=CCJDLAST2&filename=' + ID
            print('pageurl4=%s' % pageUrl)
            r1 = requests.get(pageUrl, headers=headers).text
            tree1 = etree.HTML(r1)
            title = tree1.xpath('//div[@class="wx-tit"]/h1/text()')

        if len(title) == 0:
            pageUrl = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CPFD&dbname=CPFD0914&filename=' + ID
            print('pageurl5=%s' % pageUrl)
            r1 = requests.get(pageUrl, headers=headers).text
            tree1 = etree.HTML(r1)
            title = tree1.xpath('//div[@class="wx-tit"]/h1/text()')

        title = title[0]
        # 下载链接
        Download = tree1.xpath('//li[@class="btn-dlpdf"]/a/@href')
        if Download is None:
            Download = tree1.xpath('//li[@class="btn-dlcaj"]/a/@href')
        Download = Download[0]
        # print(Download)


        pdfUrl = Download

        data = pd.DataFrame({
            '文献标题': [title],
            '文章观看链接': [pageUrl],
            "文献下载链接": [pdfUrl]
        })


        save_page(data)
        # data.to_csv('./文献.csv', mode='a', encoding='ANSI', index=False, header=False)
        print(f"第{a}篇论文写入完毕")
        a += 1


def save_page(data):
    data.to_csv('./1.csv', mode='a', encoding='utf-8', index=False, header=False)


def main():
    get_page(58)

if __name__ == '__main__':
    main()

