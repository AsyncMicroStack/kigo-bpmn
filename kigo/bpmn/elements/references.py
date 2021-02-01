import kigo.bpmn.elements.events as bpmn_events
import kigo.bpmn.elements.gateways as bpmn_gateways
import kigo.bpmn.elements.flow as bpmn_flow
import kigo.bpmn.elements.tasks as bpmn_tasks
import kigo.bpmn.elements.dataobject as bpmn_dataobjects
from kigo.bpmn.elements import Element

bpmn_elements = {}
bpmn_elements.update({clazz.item_name: clazz for clazz in [c for c in bpmn_events.__dict__.values()         if isinstance(c, type) and issubclass(c, Element)]})
bpmn_elements.update({clazz.item_name: clazz for clazz in [c for c in bpmn_gateways.__dict__.values()       if isinstance(c, type) and issubclass(c, Element)]})
bpmn_elements.update({clazz.item_name: clazz for clazz in [c for c in bpmn_flow.__dict__.values()           if isinstance(c, type) and issubclass(c, Element)]})
bpmn_elements.update({clazz.item_name: clazz for clazz in [c for c in bpmn_tasks.__dict__.values()          if isinstance(c, type) and issubclass(c, Element)]})
bpmn_elements.update({clazz.item_name: clazz for clazz in [c for c in bpmn_dataobjects.__dict__.values()    if isinstance(c, type) and issubclass(c, Element)]})
