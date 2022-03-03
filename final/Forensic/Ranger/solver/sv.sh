#!/bin/bash

tshark -r log.pcap -o "tls.keys_list:172.52.3.2,443,http,server/certs/cert.key" -Y 'http.request' -Tfields -e http.request.line | grep -oP '\d+\-\d+' > range
tshark -r log.pcap -o "tls.keys_list:172.52.3.2,443,http,server/certs/cert.key" -Y 'media' -Tfields -e media.type > content
paste range content | sort -n | awk '{print $2}' | xxd -r -p > flag.zip

7z x flag.zip
