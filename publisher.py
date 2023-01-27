from mqtt_sox import Connection, PublishModule, Node

connection = Connection("localhost", 1883, "publish_test")
client = connection.connect()

publisher = PublishModule(client)
node = Node("test_node")
node.flushTransducers()

transducer = node.Transducer("test_transducer1")
transducer.setRawValue(10)
node.appendTransducer(transducer)

transducer = node.Transducer("test_transducer2")
transducer.setRawValue(20)
node.appendTransducer(transducer)

transducer = node.Transducer("test_transducer3")
transducer.setRawValue("sunny")
node.appendTransducer(transducer)

publisher.publish(node)
