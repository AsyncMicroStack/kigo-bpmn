from kigo.bpmn.elements import Element

class SequenceFlow(Element):
    item_name = "bpmn:sequenceFlow"


    def __init__(self, destination_element:Element,  condition: str = None):
        pass
