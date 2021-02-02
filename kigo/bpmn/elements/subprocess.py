from kigo.bpmn.elements.element import Element

class SubProcess(Element):
    item_name = "bpmn:subprocess"

    def __init__(self):
        self.diagram = None
        self.references = {}