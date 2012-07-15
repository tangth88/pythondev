# Simple SMTP mail reader
# Example

import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com')

# prompt for gmail account id and password
pop_conn.user(username)
pop_conn.pass_(passwd)

# Get messages from server
print 'connecting '
# messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# get first 10 email
messages = [pop_conn.retr(i) for i in 10]

# Concat message pieces
print 'joining message ..'
messages = ["\n".join(mssg[1]) for mssg in messages]

# Parse message intom an email object:
print 'parsing email...'
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
print 'parsing done'

#
pop_conn.quit()


