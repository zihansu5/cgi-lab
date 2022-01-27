#!/user/bin/env python3

import os
import json

# Q1: How do you inspect all environment variables in Python
# plain text
#print("Content-Type: text/plain")
#print()
#print(os.environ)
# json - part1
#print("Content-Type: application/json")
#print()                                 
#print(json.dumps(dict(os.environ), indent=2))
# query - part2
print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# Q2 - QUERY_STRING
# Q3 - HTTP_USER_AGENT  browser info
#print("Content-Type: text/html")
#print()
#print(f"<p>QUERY_STRING={os.environ['HTTP_USER_AGENT']}</p>")

