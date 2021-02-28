

class BPMNException(Exception):

    def __init__(self, message, bpmn_element = None):
        self.message = message
        self.bpmn_element = bpmn_element
        super().__init__(self.message)