from mqtt_sox import Connection, SubscribeModule

connection = Connection("emqx.co.mqtt", 1883, "test")
# client = connection.connect()
subscriber = SubscribeModule("client")
node_name = "test_node"
subscriber.subscribe(node_name)
subscriber.run()