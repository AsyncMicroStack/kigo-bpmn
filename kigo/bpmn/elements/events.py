from kigo.bpmn.elements import Element

class Event(Element):
    pass


class StartEvent(Event):
    item_name = "bpmn:startEvent"


class StartMessageEvent(Event):
    item_name = ""


class EndEvent(Event):
    item_name = "bpmn:endEvent"


class EndMessageEvent(Event):
    item_name = ""


class IntermediateMessageCatchingEvent(Event):
    item_name = ""


class IntermediateMessageThrowingEvent(Event):
    item_name = ""


class MessageEventDefinition(Event):
    item_name = "bpmn:messageEventDefinition"


class TimerEventDefinition(Event):
    item_name = "bpmn:timerEventDefinition"


class ConditionalEventDefinition(Event):
    item_name = "bpmn:conditionalEventDefinition"

class SignalEventDefinition(Event):
    item_name = "bpmn:signalEventDefinition"