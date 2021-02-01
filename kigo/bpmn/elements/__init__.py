
class Element:
    item_name = "bpmn:element"

    def __init__(self, incoming = None, outgoing = None):
        self.incoming = incoming
        self.outgoing = outgoing
