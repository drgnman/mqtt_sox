from sox_mqtt import Connection, PublishModule, Node

connection = Connection("localhost", 1883)
client = connection.connect()

publisher = PublishModule(client)
node = Node("test_node")
node.flushTransducers()  # node.transducersの中身を空のdictに再セット
                         # createメソッド後とかに使う

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
