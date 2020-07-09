from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def sendsms(phone, code_j):
   client = AcsClient('AccessKey', 'Secret Key', 'cn-hangzhou') #AccessKey 阿里云公钥 Secret Key 阿里云私钥  cn-hangzhou  阿里云短信接口节点
   req = CommonRequest()
   req.set_accept_format('json')
   req.set_domain('dysmsapi.aliyuncs.com')
   req.set_method('POST')
   req.set_protocol_type('https')  # https | http
   req.set_version('2017-05-25')
   req.set_action_name('SendSms')
   req.add_query_param('RegionId', 'cn-hangzhou')
   req.add_query_param('PhoneNumbers', phone)
   req.add_query_param('SignName', '藏书阁')
   req.add_query_param('TemplateCode', 'SMS_162635987')
   req.add_query_param('TemplateParam', code_j)
   response = client.do_action(req)
   return response