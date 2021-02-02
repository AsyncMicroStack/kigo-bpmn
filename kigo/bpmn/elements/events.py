from kigo.bpmn.elements.element import Element

class Event(Element):
    item_name = "bpmn:event"


class StartEvent(Event):
    item_name = "bpmn:startEvent"


class StartMessageEvent(Event):
    item_name = "bpmn:startMessageEven"


class EndEvent(Event):
    item_name = "bpmn:endEvent"


class EndMessageEvent(Event):
    item_name = "bpmn:endMessageEvent"


class IntermediateMessageCatchingEvent(Event):
    item_name = "bpmn:intermediateMessageCatchingEvent"


class MessageEventDefinition(Event):
    item_name = "bpmn:messageEventDefinition"


class TimerEventDefinition(Event):
    item_name = "bpmn:timerEventDefinition"


class ConditionalEventDefinition(Event):
    item_name = "bpmn:conditionalEventDefinition"


class SignalEventDefinition(Event):
    item_name = "bpmn:signalEventDefinition"


class BoundaryEventn(Event):
    item_name = "bpmn:boundaryEvent"
