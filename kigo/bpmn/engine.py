import glob
import os
import pickle

from kigo.bpmn.loaders.bpmn import BPMNFileLoader
from kigo.bpmn.elements.flow import SequenceFlow
from kigo.bpmn.elements.tasks import *
from kigo.bpmn.elements.events import *
from kigo.bpmn.elements.gateways import *
from kigo.bpmn.elements.process import *
from kigo.bpmn.names import names
from kigo.bpmn.exceptions import BPMNException


class ProcessRegistry:
    process_definition = {}


class ProcessInstance:
    def __init__(self, process, env = {}):
        self.process = process
        self.env = env
        self.current_element_id = None
        self.tokens = {}
        self.__process = {func : getattr(self, func, None) for func in dir(ProcessInstance) if callable(getattr(ProcessInstance, func)) and func.startswith("process_")}

    def run(self, env = {}):
        if env:
            self.env = env
        if len(self.process.start_events) != 1:
            raise BPMNException("Not support more than one start event!")
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
                raise BPMNException(f"Not implemented BPMN element: <{element.__class__.__name__}> call: <{element_name}>", bpmn_element=element)
            self.current_element_id = call(element)
            if not self.current_element_id and not isinstance(element, EndEvent):
                raise BPMNException(f"Finalized process without End Event! {element}", bpmn_element=element)


    def process_sequence_flow(self, element: SequenceFlow):
        return element.target_ref

    def process_script_task(self, element: ScriptTask):
        try:
            exec(element.script.script, None, self.env)
        except Exception as ex:
            message = f"{element}: {ex} --> {element.script.script}"
            raise BPMNException(message, bpmn_element=element)
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
                    raise BPMNException(message, bpmn_element=element)
            else:
                default_ids.append(flow_id)
        if len(default_ids) > 1:
            raise BPMNException(f"Duplicate default flow <{element}>", bpmn_element=element)
        elif not default_ids:
            raise BPMNException(f"Unknown default flow <{element}>", bpmn_element=element)
        return default_ids[0]

    def process_call_activity_task(self, element: CallActivityTask):
        if not element.called_element in ProcessRegistry.process_definition:
            raise BPMNException(f"Unknown process id <{element.called_element}>", bpmn_element=element)
        process_model = ProcessRegistry.process_definition[element.called_element]
        process_instance = ProcessInstance(process_model)
        process_instance.run(env=self.env)
        return element.outgoing


class ProcessRuntime:

    def __init__(self):
        self.env = None

    def load(self, file_path):
        """
        Directory with bpmn files or path to bpmn file.
        :param file_path:
        :return:
        """
        files = [file_path]
        if not file_path.endswith(".bpmn"):
            path = os.path.join(file_path, "**/*.bpmn")
            files = glob.glob(path, recursive=True)

        bpmn_loader = BPMNFileLoader()
        for file in files:
            model = bpmn_loader.load(file)
            for element_id in model:
                clazz = model[element_id]
                if isinstance(clazz, Process):
                    if element_id in ProcessRegistry.process_definition:
                        raise Exception(f"Duplicate process id <{element_id}> file <{file}>.")
                    ProcessRegistry.process_definition[element_id] = model[element_id]


    def save(self, file_path):
        for process_id in ProcessRegistry.process_definition:
            process = ProcessRegistry.process_definition[process_id]
            fdir = os.path.join(file_path, str(process.version))
            fpath = os.path.join(fdir, f"{process.eid}.cbpmn")
            if not os.path.exists(fdir):
                os.makedirs(fdir, exist_ok=True)
            with open(fpath, "wb") as f:
                pickle.dump(ProcessRegistry.process_definition[process_id], f)


    def create_process_instance(self, process_id: str, env = {}):
        process = ProcessRegistry.process_definition[process_id]
        return ProcessInstance(process, env)




import pprint
import time

runtime = ProcessRuntime()
runtime.load("c:/workspace/python/kigo-bpmn/BPMN/tests")
pprint.pprint(ProcessRegistry.process_definition)
process = runtime.create_process_instance("ProcessCallActivity")
c0 =time.time()
process.run()
print(process.env)
print(time.time() - c0)

