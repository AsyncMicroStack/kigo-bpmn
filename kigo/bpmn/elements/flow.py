from kigo.bpmn.elements.element import Element

class SequenceFlow(Element):
    item_name = "bpmn:sequenceFlow"

    def __init__(self, id = None, name = None, source_ref = [], target_ref = []):
        self.id = id
        self.name = name
        self.source_ref = source_ref
        self.target_ref = target_ref

    def __repr__(self):
        return f"{type(self)} <id '{self.id}'> <name '{self.name}'> <sourceRef {self.source_ref}> <targetRef {self.target_ref}>"


class Incoming(Element):
    item_name = "bpmn:incoming"


class Outgoing(Element):
    item_name = "bpmn:outgoing"



