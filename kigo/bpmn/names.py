import kigo.bpmn.elements
import re
from kigo.bpmn.elements import *


def name2snake(name):
    name = name.replace("bpmn:", "")
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name

names = {}
element = kigo.bpmn.elements.element.Element
for module_name in kigo.bpmn.elements.__all__:
    names.update({clazz.item_name: clazz for clazz in [c for c in kigo.bpmn.elements.__dict__[module_name].__dict__.values() if isinstance(c, type) and issubclass(c, element)]})
    names.update({clazz.item_name.split(":")[-1]: clazz for clazz in [c for c in kigo.bpmn.elements.__dict__[module_name].__dict__.values() if isinstance(c, type) and issubclass(c, element)]})
    names.update({clazz.__name__: name2snake(clazz.__name__) for clazz in [c for c in kigo.bpmn.elements.__dict__[module_name].__dict__.values() if isinstance(c, type) and issubclass(c, element)]})
