from kigo.bpmn.elements.element import Element

class Process(Element):
    item_name = "bpmn:process"

    def __init__(self, eid=None, name=None, file_name = None):
        self.file_name = file_name
        self.eid = eid
        self.name = name
        self.elements = {}
        self.start_events = {}
