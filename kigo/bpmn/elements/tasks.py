from kigo.bpmn.elements.element import Element

class Task(Element):
    item_name = "bpmn:task"

    def __init__(self, eid=None, name=None, incoming=[], outgoing=[]):
        self.eid = eid
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing

    def __repr__(self):
        return f"{type(self)} <id '{self.eid}'> <name '{self.name}'> <incoming '{self.incoming}'> <outgoing '{self.outgoing}'>"


class Script:

    def __init__(self, script, script_format, resource):
        self.script = script
        self.script_format = script_format
        self.resource = resource

    def __repr__(self):
        return f"{type(self)} <format '{self.script_format}'> <resource: '{self.resource}'> <script '{self.script}'>"


class ServiceTask(Task):
    item_name = "bpmn:serviceTask"


class ScriptTask(Task):
    item_name = "bpmn:scriptTask"

    def __init__(self, eid=None, name=None, script=None, script_format=None, resource=None, incoming=[], outgoing=[]):
        self.eid = eid
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
        self.script = script
        if script or resource:
            self.script = Script(script, script_format, resource)

    def __repr__(self):
        return f"{type(self)} <id '{self.eid}'> <name '{self.name}'> <incoming '{self.incoming}'> <outgoing '{self.outgoing}'> <script '{self.script}'>"



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

    def __init__(self, eid=None, name=None, called_element=None, incoming=[], outgoing=[]):
        self.eid = eid
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
        self.called_element = called_element

    def __repr__(self):
        return f"{type(self)} <id '{self.eid}'> <name '{self.name}'> <incoming '{self.incoming}'> <outgoing '{self.outgoing}'> <called '{self.called_element}'>"



class SubProcessTask(Task):
    item_name = "bpmn:subProcess"

