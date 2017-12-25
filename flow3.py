[{"id":"cac7c3c1.98804","type":"inject","z":"11a531e2.69be8e","name":"","topic":"","payload":"","payloadType":"date","repea

t":"5","crontab":"","once":true,"x":151,"y":175,"wires":[["8351143e.ac8148"]]},

{"id":"8351143e.ac8148","type":"function","z":"11a531e2.69be8e","name":"Payload","func":"msg.headers={\n    devicekey:

\"O9azxaA6wEEku7dV\"\n};\n\nmsg.payload=\"Temperature,,39.8\";\nreturn 

msg;","outputs":1,"noerr":0,"x":363,"y":241,"wires":[["c4955dec.28b9d"]]},{"id":"c4955dec.28b9d","type":"http 

request","z":"11a531e2.69be8e","name":"","method":"POST","ret":"txt","url":"https://api.mediatek.com/mcs/v2/devices/DNP2KUB

y/datapoints.csv","tls":"","x":548,"y":240,"wires":[["66d9a362.b9972c","d2ba42f4.f3db1"]]},

{"id":"66d9a362.b9972c","type":"http response","z":"11a531e2.69be8e","name":"","statusCode":"","headers":

{},"x":737,"y":239,"wires":[]},

{"id":"d2ba42f4.f3db1","type":"debug","z":"11a531e2.69be8e","name":"","active":true,"console":"false","complete":"false","x

":728,"y":327,"wires":[]}]
