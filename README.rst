Kigo asynchronous event framework for RabbitMQ
==============================================

.. image:: https://travis-ci.org/AsyncMicroStack/kigo-bpmn.svg?branch=master
   :target: http://travis-ci.org/AsyncMicroStack/kigo-bpmn

.. pull-quote ::
   BPMN engine for technicals processes.

.. code-block:: python

   # helloworld.py

   runtime = ProcessRuntime(process_model=ModelDefinition().load("process.bpmn"))
   process = runtime.create_process_instance("my_process")
   process.run()


Documentation
-------------

Documentation and links to additional resources are available at
https://www.asyncstack.org/kigo-bpmn


License
-------

Apache 2.0. See LICENSE for details.