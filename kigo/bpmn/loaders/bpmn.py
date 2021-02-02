from kigo.bpmn.loaders import load_xml2dict
from kigo.bpmn.names import names
from enum import Enum
import collections
import re


class Provider(Enum):
    BPMN_2_0_2 = "BPMN 2.0.2"
    CAMUNDA    = "Camunda"
    JBPM       = "JBPM"
    ACTIVITI   = "Activiti"
    EA         = "Enterprise Architect"




class CamundaLoader:

    def __init__(self):
        pass

    def load_file(self, fname):
        self.fname = fname
        xml = load_xml2dict(self.fname)
        return xml

    def load_xml(self, sxml: str):
        self.sxml = sxml


class EALoader:

    def __init__(self):
        pass

    def load_file(self, fname):
        self.fname = fname
        xml = load_xml2dict(self.fname)
        return xml

    def load_xml(self, sxml: str):
        self.sxml = sxml



#xml = load_xml2dict("c:/workspace/resources/test1.bpmn")
xml = load_xml2dict("c:/workspace/resources/example.xml", decode="Windows-1250")

import pprint
#pprint.pprint(names)
#for element in xml["bpmn:definitions"]["bpmn:process"]:
#    print(xml["bpmn:definitions"]["bpmn:process"][element])
#    for item in xml["bpmn:definitions"]["bpmn:process"][element]:
#        print(item)


class LoadDefinition:

    def load(self, fname, decode="utf-8"):
        self.xml = load_xml2dict(fname, decode=decode)
        self.defs = {}
        self.parse(self.xml)

    def parse(self, xml):
        for name in xml:
            if name.startswith("@"):
                continue
            if name.startswith("bpmndi:"):
                continue

            attr_name = f"load_{self.get_name(name)}"
            call = getattr(self, attr_name, None)
            if call:
                call(name, xml[name])
            else:
                print(f"Not implemented: {attr_name}")

    def get_name(self, name):
        name = name.replace("bpmn:", "")
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        return name

    def load_definitions(self, name, xml):
        self.defs[xml["@id"]] = names[name]()
        self.parse(xml)

    def load_process(self, name, xml):
        self.defs[xml["@id"]] = names[name]()
        self.parse(xml)

    def load_sub_process(self, name, xml):
        self.defs[xml["@id"]] = names[name]()
        self.parse(xml)

    def load_service_task(self, name, xml):
        for task in xml:
            self.defs[task["@id"]] = names[name]()

    def load_exclusive_gateway(self, name, xml):
        for task in xml:
            o = names[name]()
            o.id = task["@id"]
            self.defs[o.id] = o

    def load_sequence_flow(self, name, xml):
        for task in xml:
            o = names[name]()
            o.id = task["@id"]
            self.defs[o.id] = o

    def load_start_event(self, name, xml):
        self.defs[xml["@id"]] = names[name]()


    def load_end_event(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]

        for event in xml:
            o = names[name]()
            o.id = event["@id"]
            self.defs[o.id] = o

    def load_boundary_event(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]

        for event in xml:
            o = names[name]()
            o.id = event["@id"]
            self.defs[o.id] = o



loader = LoadDefinition()
loader.load("c:/workspace/resources/example.xml", decode="Windows-1250")
pprint.pprint(loader.defs)

#parse(xml)
#pprint.pprint(defs)
#print()
#print(xml["bpmn:definitions"]["bpmn:process"]["bpmn:serviceTask"])
#print(xml["bpmn:definitions"]["bpmn:process"].keys()) # ["bpmn:process"]["bpmn:serviceTask"])
#print(len(xml["bpmn:definitions"]["bpmn:process"]["bpmn:serviceTask"]))