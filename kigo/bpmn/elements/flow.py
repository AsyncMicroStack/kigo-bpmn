from kigo.bpmn.elements.element import Element

class SequenceFlow(Element):
    item_name = "bpmn:sequenceFlow"

    def __init__(self, id = None, name = None, source_ref = [], target_ref = []):
        self.id = id
        self.name = name
        self.source_ref = source_ref
        self.target_ref = target_ref
        self.condition_expression: ConditionExpression = None

    def add_condition_expression(self, expression_type=None, expression=None, language=None):
        self.condition_expression = ConditionExpression(expression_type=expression_type, language=language, expression=expression)

    def __repr__(self):
        if self.condition_expression:
            expression = self.condition_expression.expression
            return f"{type(self)} <id '{self.id}'> <name '{self.name}'> <sourceRef {self.source_ref}> <targetRef {self.target_ref}> <expression '{expression}'>"
        return f"{type(self)} <id '{self.id}'> <name '{self.name}'> <sourceRef {self.source_ref}> <targetRef {self.target_ref}>"


class ConditionExpression:
    item_name = "bpmn:conditionExpression"

    def __init__(self, expression_type=None, language=None, expression=None):
        self.expression_type = expression_type
        self.expression = expression
        self.language = language


class Incoming(Element):
    item_name = "bpmn:incoming"


class Outgoing(Element):
    item_name = "bpmn:outgoing"



