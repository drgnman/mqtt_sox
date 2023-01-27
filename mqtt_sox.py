from paho.mqtt import client as mqtt_client
from copy import copy
import json


class Connection:
    def __init__(self, broker, port, client_id, username=None, password=None):
        self.__broker = broker
        self.__port = port
        self.__client_id = client_id
        self.__username = username
        self.__password = password

    def connect(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!\n")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.__client_id)
        if self.__broker == None or self.__port == None:
            print("Broker or Port is not found!\n \
                Please Enter Broker and Port!\n")
            return
        
        if self.__username != None or self.__password != None:
            if self.__username == None or self.__password == None:
                print("Username or Password is not found!\n \
                    Please Enter Username and Password!\n")
                return
            client.username_pw_set(self.__username, self.__password)
        
        client.on_connect = on_connect
        client.connect(self.__broker, self.__port)
        return client
    def disconnect(self, client):
        client.disconnection()
    
class PublishModule:
    def __init__(self, client):
        self.__client = client
    
    # transducerをどう設計するか
    def create(self, node):
        copy_node = copy(node)
        copy_node.setNodeName(f"{copy_node.getNodeName()}_meta")
        msg = json.dumps({
            "node_name": copy_node.getNodeName(),
            "location": copy_node.getLocation(),
            "transducers": copy_node.getTransducers(),
            "descrption": copy_node.getDescription()
        })
        # print(msg)
        self.__publishExecution(copy_node.getNodeName(), msg, 2)

    def publish(self, node, qos=0):
        print(node.getNodeName())
        print(node.getTransducers())
        self.__publishExecution(node.getNodeName(), json.dumps(node.getTransducers()), qos)

    def __publishExecution(self, topic, msg="", qos=0):
        try:
            self.__client.loop_start()
            print(topic)
            print(msg)
            result = self.__client.publish(topic, msg, qos, True)
            status = result[0]
            if status == 0:
                print(f"Successfully process!")
            else:
                print(f"Failed to process!")
        finally:
            self.__client.loop_stop()

class SubscribeModule:
    def __init__(self, client):
        self.__client = client
    
    def subscribe(self, node_name, qos=0):
        def on_message(client, userdata, msg):
            print(f"Received {msg.payload} from {msg.topic} topic")
        
        meta_node = f"{node_name}_meta"
        self.__client.subscribe(meta_node, 2)
        self.__client.subscribe(node_name, qos)
        self.__client.on_message = on_message
    
    def run(self):
        self.__client.loop_forever()

    def unsubscribe(self):
        self.__client.disconnect()

class Node:
    def __init__(self, node_name):
        self.__node_name = node_name
        self.__longitude = 0.0
        self.__latitude = 0.0
        self.__transducers = []
        self.__description = ""

    def setNodeName(self, node_name):
        self.__node_name = node_name

    def setLocation(self, longitude, latitude):
        self.__longitude = longitude
        self.__latitude = latitude
    def setTransducers(self, transducers):
        self.__transducers = transducers
    def setDescription(self, description):
        self.__description = description
    
    def getNodeName(self):
        return self.__node_name
    def getLocation(self):
        return (self.__longitude, self.__latitude)
    def getTransducers(self):
        return self.__transducers
    def getDescription(self):
        return self.__description

    def appendTransducer(self, transducer):
        if transducer.getMetaflag():
            self.__transducers.append({
                                    "transducer" : transducer.getTransducerName(),
                                    "unit" : transducer.getUnit(),
                                    "min_value" : transducer.getMinValue(),
                                    "max_value" : transducer.getMaxValue(),
                                    "description" : transducer.getDescription()
            })
    
        else:
            self.__transducers.append({
                "transducer" : transducer.getTransducerName(),
                "raw_value": transducer.getRawValue() 
            })

    def flushTransducers(self):
        self.setTransducers([])

    class Transducer:
        def __init__(self, transducer_name):
            self.__transducer_name = transducer_name
            self.__unit = ""
            self.__min_value = None
            self.__max_value = None
            self.__description = ""
            self.__raw_value = None
            self.__meta_flag = True

        def setUnit(self, unit):
            self.__unit = unit
        def setMinValue(self, min_value):
            self.__min_value = min_value
        def setMaxValue(self, max_vale):
            self.__max_value = max_vale
        def setDescription(self, description):
            self.__description = description
        def setRawValue(self, raw_value):
            self.__raw_value = raw_value
            self.__meta_flag = False
        
        def getTransducerName(self):
            return self.__transducer_name
        def getUnit(self):
            return self.__unit
        def getMinValue(self):
            return self.__min_value
        def getMaxValue(self):
            return self.__max_value
        def getDescription(self):
            return self.__description
        def getMetaflag(self):
            return self.__meta_flag
        def getRawValue(self):
            return self.__raw_value
