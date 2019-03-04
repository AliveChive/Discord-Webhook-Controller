#Enter the Webhook URL in 'WEBHOOK_HERE'
from dhooks import Webhook
try:
    hook = Webhook('WEBHOOK_HERE')
    print ('Enter the message you would like to send')
    src = input()
    hook.send (src)
except Exception as e:
    print ('Please provide a valid Webhook')
    input()

