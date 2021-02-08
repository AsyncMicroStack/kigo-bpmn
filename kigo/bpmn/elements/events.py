from kigo.bpmn.elements.element import Element

class Event(Element):
    item_name = "bpmn:event"


class StartEvent(Event):
    item_name = "bpmn:startEvent"

    def __init__(self, id = None, name = None, outgoing = []):
        self.id = id
        self.name = name
        self.outgoing = outgoing

    def __repr__(self):
        return f"{type(self)} <id '{self.id}'> <name '{self.name}'> <outgoing {self.outgoing}>"


class StartMessageEvent(Event):
    item_name = "bpmn:startMessageEvent"


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
