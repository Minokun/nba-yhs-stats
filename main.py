import lazyllm
import os 

kimi_api_key = os.environ.get('LAZYLLM_KIMI_API_KEY')
chat = lazyllm.OnlineChatModule(api_key=kimi_api_key, source='kimi', model='kimi-k2-0905-preview')
lazyllm.WebModule(chat, port=23333).start().wait()
