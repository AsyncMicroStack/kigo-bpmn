from kigo.bpmn.elements.element import Element


class DataObject(Element):
    item_name = "bpmn:dataObject"


class DataObjectReference(Element):
    item_name = "bpmn:dataObjectReference"


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



