from mqtt_sox import Connection, SubscribeModule

connection = Connection("localhost", 1883, "subscribe_test")
client = connection.connect()
subscriber = SubscribeModule(client)
node_name = "test_node"
subscriber.subscribe(node_name)
subscriber.run()
