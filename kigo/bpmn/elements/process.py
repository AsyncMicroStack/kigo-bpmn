from kigo.bpmn.elements.element import Element

class Process(Element):
    item_name = "bpmn:process"

    def __init__(self):
        self.diagram = None
        self.references = {}

