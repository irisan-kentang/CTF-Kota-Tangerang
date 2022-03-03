from binascii import unhexlify
from zipfile import ZipFile

import pyshark
import base64
import re
import os


os.system("tshark -r db.pcap -Y 'frame.time_delta > 0.3' | awk '{print $1-2}' > ans")
packets = pyshark.FileCapture(
    'db.pcap',
    include_raw=True, use_json=True
)

answer = open('ans').read().split()[:-1]

r1 = re.compile(rb'set|prepare|execute', re.I)
r2 = re.compile(rb'.set @(\w+)=cast\(0x(\w+) as char\)', re.I)
r3 = re.compile(rb'.prepare (\w+) from @(\w+)', re.I)
r4 = re.compile(rb'.execute (\w+)', re.I)
r5 = re.compile(rb'.*note\), (\d+),.*0x(\w+)', re.I)

declared_variable = {}
prepared_statement = {}
executed_statement = {}

contents = [b''] * 72

for e, packet in enumerate(packets):
    if hasattr(packet, 'mysql'):
        sql_field = packet.mysql

        if hasattr(sql_field, 'payload'):
            sql_payload = re.sub(':', '', sql_field.payload)
            sql_payload = unhexlify(sql_payload)

            if r1.findall(sql_payload):
                if r2.match(sql_payload):
                    key, val = r2.findall(sql_payload)[0]
                    declared_variable[key] = unhexlify(val)

                elif r3.match(sql_payload):
                    key, val = r3.findall(sql_payload)[0]
                    prepared_statement[key] = val

                elif r4.match(sql_payload):
                    val = r4.findall(sql_payload)[0]
                    executed_statement[e] = val


for k, v in executed_statement.items():
    if (str(k+1) in answer):
        key = prepared_statement.get(v)
        query = declared_variable.get(key)

        offset, char = r5.findall(query)[0]
        # print(offset, query)
        contents[int(offset)-1] = unhexlify(char)

links = b''.join(contents).decode('utf-8').split(',')
print(links)
