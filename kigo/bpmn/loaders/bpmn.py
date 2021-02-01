from kigo.bpmn.loaders import load_xml2dict
from kigo.bpmn.elements.references import bpmn_elements
from enum import Enum


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
pprint.pprint(bpmn_elements)
for item in xml["bpmn:definitions"]["bpmn:process"]:
    print(item)

for item in xml["bpmn:definitions"]["bpmn:process"]["bpmn:serviceTask"]:
    print(item)