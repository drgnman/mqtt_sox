from sox_mqtt import Connection, PublishModule, Node

connection = Connection("localhost", 1883)
# client = connection.connect()

publisher = PublishModule("test")
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

publisher.create(node)
