class Element:
    item_name = "bpmn:element"

    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{type(self)} <id '{self.id}'> <name '{self.name}'>"