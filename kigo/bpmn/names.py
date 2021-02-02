import kigo.bpmn.elements
from kigo.bpmn.elements import *

names = {}
element = kigo.bpmn.elements.element.Element
for module_name in kigo.bpmn.elements.__all__:
    names.update({clazz.item_name: clazz for clazz in [c for c in kigo.bpmn.elements.__dict__[module_name].__dict__.values() if isinstance(c, type) and issubclass(c, element)]})

