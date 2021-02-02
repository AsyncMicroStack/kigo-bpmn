from kigo.bpmn.elements.element import Element

class Task(Element):
    item_name = "bpmn:task"


class ServiceTask(Task):
    item_name = "bpmn:serviceTask"


class ScriptTask(Task):
    item_name = "bpmn:scriptTask"


class SendTask(Task):
    item_name = "bpmn:sendTask"


class ReceiveTask(Task):
    item_name = "bpmn:receiveTask"


class UserTask(Task):
    item_name = "bpmn:userTask"


class ManualTask(Task):
    item_name = "bpmn:manualTask"


class BusinessRuleTask(Task):
    item_name = "bpmn:businessRuleTask"


class CallActivityTask(Task):
    item_name = "bpmn:callActivity"


class SubProcessTask(Task):
    item_name = "bpmn:subProcess"

