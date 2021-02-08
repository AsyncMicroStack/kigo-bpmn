from kigo.bpmn.elements.element import Element

class Process(Element):
    item_name = "bpmn:process"

    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name
        self.elements = {}
        self.start_events = {}