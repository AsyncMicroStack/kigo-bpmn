from kigo.bpmn.elements.element import Element

class Gateway(Element):
    item_name = "bpmn:gateway"
    pass


class ExclusiveGateway(Gateway):
    item_name = "bpmn:exclusiveGateway"

    def __init__(self, id=None, name=None, incoming=[], outgoing=[]):
        self.id = id
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing

    def __repr__(self):
        return f"{type(self)} <id '{self.id}'> <name '{self.name}'> <incoming '{self.incoming}'> <outgoing '{self.outgoing}'>"


class EventBasedGateway(Gateway):
    item_name = "bpmn:eventBasedGateway"


class ParallelEventGateway(Gateway):
    item_name = "bpmn:parallelEventGateway"


class InclusiveGateway(Gateway):
    item_name = "bpmn:inclusiveGateway"


class ComplexGateway(Gateway):
    item_name = "bpmn:complexGateway"


class ParallelGateway(Gateway):
    item_name = "bpmn:parallelGateway"