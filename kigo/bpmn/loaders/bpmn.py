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


class BPMNFileLoader:

    def __init__(self):
        self.xml = None
        self.decode = None
        self.file_name = None
        self.defs = {}


    def load(self, file_name, decode="utf-8"):
        self.file_name = file_name
        self.decode = decode
        self.defs = {}
        self.xml = load_xml2dict(file_name, decode=decode)
        self.parse(self.xml)
        return self.defs

    def parse(self, xml):
        for name in xml:
            if name.startswith("@"):
                continue
            if name.startswith("bpmndi:"):
                continue

            attr_name = f"load_{self.name2snake(name)}"
            call = getattr(self, attr_name, None)
            if call:
                call(name, xml[name])
            else:
                raise Exception(f"Not implemented: {attr_name}")

    def name2snake(self, name):
        name = name.replace("bpmn:", "")
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        return name

    def load_definitions(self, name, xml):
        if not name in names:
            raise Exception(f"Not implemented tag: <{name}>")
        self.defs[xml["@id"]] = names[name]()
        self.parse(xml)

    def load_process(self, name, xml):
        self.defs[xml["@id"]] = names[name](eid=xml["@id"], name=xml.get("@name", None), version = xml.get("@camunda:versionTag", (0,0,0)), file_name = self.file_name)
        self.process = self.defs[xml["@id"]]
        self.parse(xml)

    def load_sub_process(self, name, xml):
        self.defs[xml["@id"]] = names[name]()
        self.parse(xml)

    def load_service_task(self, name, xml):
        for task in xml:
            self.process.elements[task["@id"]] = names[name]()

    def load_script_task(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]
        for task in xml:
            self.process.elements[task["@id"]] = names[name](eid=task["@id"],
                                                             name=task.get("@name", "unnamed"),
                                                             incoming=task["bpmn:incoming"],
                                                             outgoing=task["bpmn:outgoing"],
                                                             script=task.get("bpmn:script", None),
                                                             script_format = task.get("@scriptFormat", None),
                                                             resource = task.get("@camunda:resource", None))

    def load_call_activity(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]
        for task in xml:
            self.process.elements[task["@id"]] = names[name](eid=task["@id"],
                                                             name=task["@name"],
                                                             incoming=task["bpmn:incoming"],
                                                             outgoing=task["bpmn:outgoing"],
                                                             called_element=task.get("@calledElement", None))

    def load_data_object_reference(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]
        for data_object in xml:
            self.process.elements[data_object["@id"]] = names[name](eid=data_object["@id"],
                                                                    name=data_object.get("@name", None),
                                                                    data_object_ref=data_object.get("@dataObjectRef", None))

    def load_data_object(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]
        for data_object in xml:
            self.process.elements[data_object["@id"]] = names[name](eid=data_object["@id"])

    def load_exclusive_gateway(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]
        for gateway in xml:
            incoming = gateway.get("bpmn:incoming", [])
            if incoming and not type(incoming) is list:
                incoming = [incoming]
            outgoing = gateway.get("bpmn:outgoing", [])
            if outgoing and not type(outgoing) is list:
                outgoing = [outgoing]
            self.process.elements[gateway["@id"]] = names[name](eid=gateway["@id"],
                                                                name=gateway.get("@name", None),
                                                                incoming=incoming,
                                                                outgoing=outgoing)


    def load_sequence_flow(self, name, xml):
        for flow in xml:
            sequence_flow = names[name](eid=flow["@id"],
                                        name=flow.get("@name", None),
                                        source_ref=flow["@sourceRef"],
                                        target_ref=flow["@targetRef"])

            if "bpmn:conditionExpression" in flow:
                expression_type = flow["bpmn:conditionExpression"].get("@xsi:type", None)
                expression_lang = flow["bpmn:conditionExpression"].get("@language", None)
                expression = flow["bpmn:conditionExpression"].get("#text", None)
                sequence_flow.add_condition_expression(expression_type=expression_type, language=expression_lang, expression=expression)
            self.process.elements[flow["@id"]] = sequence_flow


    def load_start_event(self, name, xml):
        outgoing = xml["bpmn:outgoing"]
        if type(xml) is collections.OrderedDict:
            outgoing = [outgoing]
        self.process.elements[xml["@id"]] = names[name](eid=xml["@id"],
                                                        name=xml.get("@name", None),
                                                        outgoing=outgoing)
        if name == "bpmn:startEvent":
            self.process.start_events[xml["@id"]] = self.process.elements[xml["@id"]]


    def load_end_event(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]

        for event in xml:
            incoming = event.get("bpmn:incoming", [])
            if incoming and not type(incoming) is list:
                incoming = [incoming]
            self.process.elements[event["@id"]] = names[name](eid=event["@id"],
                                                              name=event.get("@name", None),
                                                              incoming=incoming)


    def load_boundary_event(self, name, xml):
        if type(xml) is collections.OrderedDict:
            xml = [xml]

        for event in xml:
            o = names[name]()
            o.id = event["@id"]
            self.defs[o.id] = o
