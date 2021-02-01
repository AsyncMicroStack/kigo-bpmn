from kigo.bpmn.elements import Element

class Gateway(Element):
    item_name = "bpmn:gateway"
    pass


class ExclusiveGateway(Gateway):
    item_name = "bpmn:exclusiveGateway"


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