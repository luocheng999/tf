[{"id":"25e1c09d.5bf29","type":"rpi-gpio 

out","z":"6c956eec.d026b","name":"LED","pin":"18","set":true,"level":"0","freq":"","out":"out","x":790,"y":400,"wires":

[]},

{"id":"b39e0571.f59818","type":"debug","z":"6c956eec.d026b","name":"","active":true,"console":"false","complete":"payload",

"x":357,"y":134,"wires":[]},{"id":"28d1ea26.ed2a66","type":"rpi-gpio 

in","z":"6c956eec.d026b","name":"Button","pin":"7","intype":"up","debounce":"25","read":true,"x":126,"y":355,"wires":

[["b39e0571.f59818","1e3dd167.0a3cbf"]]},{"id":"1e3dd167.0a3cbf","type":"switch","z":"6c956eec.d026b","name":"if input is 

1","property":"payload","propertyType":"msg","rules":[{"t":"eq","v":"1","vt":"str"},

{"t":"else"}],"checkall":"true","outputs":2,"x":395,"y":390,"wires":[["2f006e5b.e389f2"],["4fea7ccc.47b174"]]},

{"id":"2f006e5b.e389f2","type":"change","z":"6c956eec.d026b","name":"change to 0","rules":

[{"t":"set","p":"payload","pt":"msg","to":"0","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":610

,"y":380,"wires":[["25e1c09d.5bf29"]]},{"id":"4fea7ccc.47b174","type":"change","z":"6c956eec.d026b","name":"change to 

1","rules":

[{"t":"set","p":"payload","pt":"msg","to":"1","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":610

,"y":440,"wires":[["25e1c09d.5bf29"]]}]
