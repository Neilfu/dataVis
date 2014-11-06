#coding=utf-8
import json
from django.http import HttpResponse, HttpResponseRedirect
from collections import namedtuple
from sqltool import SqlExecutorMgr
from models import ExternalDbModel
from common.tool import MyHttpJsonResponse
ConnArgsList = ['ip', 'port', 'db', 'user', 'pwd', 'kind']
ConnNamedtuple = namedtuple('ConnNamedtuple', ConnArgsList)




def connectDb(nt):
    hk  = hash(nt)
    st = SqlExecutorMgr.stCreate()
    succ, msg = st.connDb(nt)
    return succ, msg, hk, st

# Create your views here.
def getTableList(request):
    
    retJson = { 'succ' : False, 'msg' : '' }
    if 'POST' == request.method:
        post_data = json.loads(request.POST.get('data'))
        if not post_data:
            retJson['msg'] = 'user data error'
            return HttpResponse(json.dump(retJson), content_type='application/json')

        conn_list = map(lambda x: post_data.get(x), ConnArgsList)
        #conn_list[-1] = 'postgres'
        conn_nt = ConnNamedtuple(*conn_list)
        succ, msg, hk, st = connectDb(conn_nt)

        if succ:
            request.session['hk'] = hk
            SqlExecutorMgr.stStore(hk, st)

            ExternalDbModel.objects.get_or_create(pk = hk, m_kind = conn_nt.kind, m_user = conn_nt.user, m_pwd = conn_nt.pwd, m_ip = conn_nt.ip, m_port = conn_nt.port, m_db = conn_nt.db)
               
            tables_list = st.listTables()
        
            return MyHttpJsonResponse( {'succ': True, \
                                        'data': json.dumps(tables_list)} )
        else:
            retJson['msg'] = "can't connect db"
            return HttpResponse(json.dump(retJson), content_type='application/json')
        
