from kigo.bpmn.elements import Element


class DataObject(Element):
    item_name = "bpmn:dataObject"


class DataObjectReference(Element):
    item_name = "bpmn:dataObjectReference"


class DataStoreReference(Element):
    item_name = "bpmn:dataStoreReference"


