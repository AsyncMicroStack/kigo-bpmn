class Element:
    item_name = "bpmn:element"

    def __init__(self, eid=None, name=None):
        self.eid = eid
        self.name = name

    def __repr__(self):
        return f"{type(self)} <id '{self.eid}'> <name '{self.name}'>"