from mqtt_sox import Connection, PublishModule, Node

connection = Connection("emqx.co.mqtt", 1883, "test")
# client = connection.connect()
node = Node("test_node")
node.setLocation(80.5, 123.4)
transducer = node.Transducer("test_transducer1")
transducer.setUnit("%")
transducer.setMinValue(0)
transducer.setMaxValue(100)
transducer.setDescription("hogehoge")
node.appendTransducer(transducer)

transducer = node.Transducer("test_transducer2")
transducer.setUnit("percentage")
transducer.setMinValue(1.2)
transducer.setMaxValue(99.9)
transducer.setDescription("fugafuga")
node.appendTransducer(transducer)

transducer = node.Transducer("test_transducer3")
transducer.setUnit("C")
transducer.setMinValue(-20)
transducer.setMaxValue(40)
transducer.setDescription("nugaaa")
node.appendTransducer(transducer)

publisher = PublishModule("hoge")
publisher.create(node)

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