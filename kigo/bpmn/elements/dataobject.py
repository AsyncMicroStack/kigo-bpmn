from kigo.bpmn.elements.element import Element


class DataObject(Element):
    item_name = "bpmn:dataObject"

    def __init__(self, eid=None):
        self.eid = eid

    def __repr__(self):
        return f"{type(self)} <id '{self.eid}'>"


class DataObjectReference(Element):
    item_name = "bpmn:dataObjectReference"

    def __init__(self, eid=None, name=None, data_object_ref=None,):
        self.eid = eid
        self.name = name
        self.data_object_ref = data_object_ref

    def __repr__(self):
        return f"{type(self)} <id '{self.eid}'> <name '{self.name}'> <reference '{self.data_object_ref}'>"




class DataStoreReference(Element):
    item_name = "bpmn:dataStoreReference"


class IoSpecification(Element):
    item_name = "bpmn:ioSpecification"


class DataInputAssociation(Element):
    item_name = "bpmn:dataInputAssociation"


class DataOutputAssociation(Element):
    item_name = "bpmn:dataOutputAssociation"


class DataInput(Element):
    item_name = "bpmn:dataInput"


class DataOutput(Element):
    item_name = "bpmn:dataOutput"


class OutputSet(Element):
    item_name = "bpmn:outputSet"


class InputSet(Element):
    item_name = "bpmn:inputSet"



