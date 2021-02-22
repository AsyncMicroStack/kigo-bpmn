from kigo.bpmn.loaders.bpmn import ModelDefinition
from kigo.bpmn.elements.flow import SequenceFlow
from kigo.bpmn.elements.tasks import *
from kigo.bpmn.names import names

class ProcessInstance:
    def __init__(self, process, env = {}):
        self.process = process
        self.env = env
        self.current_tag = None

    def run(self, env = {}):
        if env:
            self.env = env
        if len(self.process.start_events) != 1:
            raise Exception("Not support more than one start event!")
        start_event = next(iter(self.process.start_events.values()))
        element_id = start_event.outgoing[0]
        self.__run__(element_id)

    def __run__(self, element_id):
        while element_id:
            element = self.process.elements[element_id]
            element_name = f"process_{names[element.__class__.__name__]}"
            print(element_name)
            call = getattr(self, element_name, None)
            element_id = call(element)


    def process_sequence_flow(self, element: SequenceFlow):
        return element.target_ref

    def process_script_task(self, element: ScriptTask):
        print(element)



class ProcessRuntime:

    def __init__(self, process_model):
        self.process_model = process_model
        self.env = None

    def create_process_instance(self, process_id: str, env = {}):
        process = self.process_model[process_id]
        return ProcessInstance(process, env)





import pprint
model = ModelDefinition().load("c:/workspace/kigo-bpmn/BPMN/tests/test-04.bpmn", decode="Windows-1250")
runtime = ProcessRuntime(process_model=model)
process = runtime.create_process_instance("Process_0d0kncd")
process.run()

"""
pprint.pprint(runtime.process_model.defs)
print()
pprint.pprint(engine.model.defs["Process_0d0kncd"].elements)
print(engine.model.defs["Process_0d0kncd"].start_events)
print(engine.model.defs["Process_0d0kncd"].elements["Flow_0xnqvit"])
print()
print(engine.model.defs)
print()
print(engine.run("Process_0d0kncd"))
"""