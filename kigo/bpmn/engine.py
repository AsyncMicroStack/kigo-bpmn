from kigo.bpmn.loaders.bpmn import ModelDefinition
from kigo.bpmn.elements.flow import SequenceFlow
from kigo.bpmn.elements.tasks import *
from kigo.bpmn.elements.events import *
from kigo.bpmn.elements.gateways import *
from kigo.bpmn.names import names

class ProcessInstance:
    def __init__(self, process, env = {}):
        self.process = process
        self.env = env
        self.current_element_id = None
        self.__process = {func : getattr(self, func, None) for func in dir(ProcessInstance) if callable(getattr(ProcessInstance, func)) and func.startswith("process_")}

    def run(self, env = {}):
        if env:
            self.env = env
        if len(self.process.start_events) != 1:
            raise Exception("Not support more than one start event!")
        start_event = next(iter(self.process.start_events.values()))
        element_id = start_event.outgoing[0]
        self.__run__(element_id)

    def __run__(self, element_id):
        self.current_element_id = element_id
        while self.current_element_id:
            element = self.process.elements[self.current_element_id]
            element_name = f"process_{names[element.__class__.__name__]}"
            call = getattr(self, element_name, None)
            if not call:
                raise Exception(f"Unknown BPMN element: <{element.__class__.__name__}> call: <{element_name}>")
            self.current_element_id = call(element)
            if not self.current_element_id and not isinstance(element, EndEvent):
                raise Exception(f"Finalized process without End Event! {element}")


    def process_sequence_flow(self, element: SequenceFlow):
        return element.target_ref

    def process_script_task(self, element: ScriptTask):
        try:
            exec(element.script.script, None, self.env)
        except Exception as ex:
            message = f"{element}: {ex} --> {element.script.script}"
            raise Exception(message)
        return element.outgoing

    def process_end_event(self, element: Event):
        return None

    def process_exclusive_gateway(self, element: Gateway):
        default_ids = []
        for flow_id in element.outgoing:
            flow = self.process.elements[flow_id]
            if flow.condition_expression:
                try:
                    if eval(flow.condition_expression.expression, None, self.env):
                        return flow_id
                except Exception as ex:
                    message = f"{ex}: {flow} {flow.condition_expression.expression}"
                    raise Exception(message)
            else:
                default_ids.append(flow_id)
        if len(default_ids) > 1:
            raise Exception(f"Duplicate default flow <{element}>")
        elif not default_ids:
            raise Exception(f"Unknown default flow <{element}>")
        return default_ids[0]



class ProcessRuntime:

    def __init__(self, process_model):
        self.process_model = process_model
        self.env = None

    def create_process_instance(self, process_id: str, env = {}):
        process = self.process_model[process_id]
        return ProcessInstance(process, env)





import time
model = ModelDefinition().load("c:/workspace/python/kigo-bpmn/BPMN/tests/test-03.bpmn", decode="Windows-1250")
runtime = ProcessRuntime(process_model=model)
process = runtime.create_process_instance("process")
c0 =time.time()
process.run()
print(process.env)
print(time.time() - c0)

