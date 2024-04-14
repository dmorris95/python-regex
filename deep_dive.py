#Task 1

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@emails.com"
#add(?!exlcude) in order to exclude the specificed email address
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{3,}\b", text)
print(emails)


