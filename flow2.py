[{"id":"34631e2d.3295a2","type":"inject","z":"23f371b1.a715de","name":"","topic":"","payload":"","payloadType":"date","repe

at":"5","crontab":"","once":true,"x":129,"y":100,"wires":[["20cd4f34.e4636"]]},

{"id":"20cd4f34.e4636","type":"function","z":"23f371b1.a715de","name":"Payload","func":"msg.headers={\n    devicekey:

\"O9azxaA6wEEku7dV\"\n};\n\nreturn msg;","outputs":1,"noerr":0,"x":259,"y":180,"wires":

[["4cefae2.56e855","1160984f.8079b8"]]},{"id":"4cefae2.56e855","type":"http 

request","z":"23f371b1.a715de","name":"","method":"GET","ret":"txt","url":"http://api.mediatek.com/mcs/v2/devices/DNP2KUBy/

datachannels/Temperature/datapoints.csv","tls":"","x":448,"y":167,"wires":[["52f42f2b.50d91","965690be.15069"]]},

{"id":"52f42f2b.50d91","type":"http response","z":"23f371b1.a715de","name":"","statusCode":"","headers":

{},"x":614,"y":168,"wires":[]},

{"id":"965690be.15069","type":"debug","z":"23f371b1.a715de","name":"","active":true,"console":"false","complete":"false","x

":614,"y":270,"wires":[]},{"id":"1160984f.8079b8","type":"http 

request","z":"23f371b1.a715de","name":"","method":"GET","ret":"txt","url":"http://api.mediatek.com/mcs/v2/devices/DNP2KUBy/

datachannels/Humidity/datapoints.csv","tls":"","x":320,"y":318,"wires":[["965690be.15069","52f42f2b.50d91"]]}]
