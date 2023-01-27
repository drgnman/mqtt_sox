from mqtt_sox import Connection, SubscribeModule

# サブスクライブした時の処理をOverrideする方法
class OriginalSubscribeModule(SubscribeModule):
    def __init__(self, client):
        super().__init__(client)

    def setProcessOnMessage(self):
        def on_message(client, userdata, msg):
            print(f"hogeeeee!!!! Received {msg.payload} from {msg.topic} topic")
        self.client.on_message = on_message

connection = Connection("localhost", 1883, "subscribe_test")
client = connection.connect()
node_name = "test_node2"

# 単純にreceiveするだけの時はこっちでよし
# subscriber = SubscribeModule(client)
# subscriber.subscribe(node_name)
# subscriber.setProcessOnMessage()
subscriber = OriginalSubscribeModule(client)
subscriber.subscribe(node_name)
subscriber.setProcessOnMessage()

subscriber.run()