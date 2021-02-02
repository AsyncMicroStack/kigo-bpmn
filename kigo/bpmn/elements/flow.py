from kigo.bpmn.elements.element import Element

class SequenceFlow(Element):
    item_name = "bpmn:sequenceFlow"


class Incoming(Element):
    item_name = "bpmn:incoming"


class Outgoing(Element):
    item_name = "bpmn:outgoing"



