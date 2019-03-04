#Enter the Webhook URL in 'WEBHOOK_HERE'
from dhooks import Webhook
hook = Webhook('WEBHOOK_HERE')
print ('Enter the message you would like to send')
src = input()
hook.send ("`" + src + "`")
