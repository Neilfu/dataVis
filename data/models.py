#coding=utf-8
from django.db import models

# Create your models here.
class ExternalDbModel(models.Model):
    """
    数据库连接类
    """
    m_hk            = models.IntegerField(primary_key = True)
    m_kind          = models.CharField(max_length=20)
    m_ip            = models.IPAddressField(max_length=20)
    m_port          = models.IntegerField(default=5432)
    m_user          = models.CharField(max_length=20)
    m_pwd           = models.CharField(max_length=20)
    m_db            = models.CharField(max_length=20)

    def getConnTuple(self):
        return (self.m_kind, self.m_ip, self.m_port, self.m_db   \
                , self.m_user, self.m_pwd)

    def getConnDict(self):
        return {
            u'kind': self.m_kind, u'ip': self.m_ip, u'port': self.m_port \
            , u'user': self.m_user, u'pwd': self.m_pwd, u'db': self.m_db  \
        }

    def getCntHk(self):
        cnt = str.format(   \
            kind = self.m_kind, user = self.m_user, pwd = self.m_pwd, \
            ip = self.m_ip,   port = self.m_port, db = self.m_db   \
        )
        return hash(cnt)

    def getPk(self):
        return self.m_hk

    class Meta:
        db_table = 'externaldb'