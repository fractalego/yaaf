Getting Started
===============

This guide will help you get YAAAF up and running on your system.

Installation
------------

Prerequisites
~~~~~~~~~~~~~

* Python 3.11 or higher
* Node.js 18 or higher (for frontend development)
* pnpm (for frontend package management)
* **Ollama** - Required for LLM integration

Ollama Setup
~~~~~~~~~~~~

**Important**: YAAAF currently supports Ollama only for LLM integration.

1. **Install Ollama**:

   Visit `https://ollama.ai/ <https://ollama.ai/>`_ and follow the installation instructions for your operating system.

2. **Download a model**:

   .. code-block:: bash

      ollama pull qwen2.5:32b

   Or use a smaller model for testing:

   .. code-block:: bash

      ollama pull qwen2.5:7b

3. **Start Ollama**:

   Ollama should start automatically after installation. Verify it's running:

   .. code-block:: bash

      ollama list

   Ollama typically runs on ``http://localhost:11434``.

.. note::
   YAAAF uses the ``OllamaClient`` for all LLM interactions. Support for other LLM providers (OpenAI, Anthropic, etc.) may be added in future versions.

Backend Setup
~~~~~~~~~~~~~

1. **Clone the repository**:

   .. code-block:: bash

      git clone <repository-url>
      cd agents_framework

2. **Install Python dependencies**:

   .. code-block:: bash

      pip install -r requirements.txt

3. **Set up environment variables** (optional):

   .. code-block:: bash

      export YAAAF_CONFIG=path/to/your/config.json

Frontend Setup
~~~~~~~~~~~~~~

1. **Navigate to frontend directory**:

   .. code-block:: bash

      cd frontend

2. **Install dependencies**:

   .. code-block:: bash

      pnpm install

3. **Build the registry** (if needed):

   .. code-block:: bash

      pnpm build:registry

Running YAAAF
------------

Using the CLI
~~~~~~~~~~~~~

The easiest way to run YAAAF is using the command-line interface:

**Start the backend server**:

.. code-block:: bash

   python -m yaaaf backend

This starts the backend server on the default port 4000.

**Start the frontend server**:

.. code-block:: bash

   python -m yaaaf frontend

This starts the frontend server on the default port 3000.

**HTTPS Support**:

.. code-block:: bash

   python -m yaaaf frontend https

This starts the frontend server with HTTPS using self-signed certificates.

**Custom ports and HTTPS**:

.. code-block:: bash

   python -m yaaaf backend 8080         # Backend on port 8080
   python -m yaaaf frontend 3001        # Frontend on port 3001
   python -m yaaaf frontend 3001 https  # Frontend with HTTPS on port 3001
   python -m yaaaf frontend https       # Frontend with HTTPS on port 3000

.. note::
   When using HTTPS, self-signed certificates are automatically generated. You may see a security warning in your browser on first access. This is normal for development use.

**Custom SSL Certificates**:

If you have your own SSL certificates, you can specify them using environment variables:

.. code-block:: bash

   export YAAAF_CERT_PATH=/path/to/your/certificate.pem
   export YAAAF_KEY_PATH=/path/to/your/private-key.pem
   python -m yaaaf frontend https

Or use the programmatic interface:

.. code-block:: python

   from yaaaf.client.run import run_frontend
   
   # Use custom certificates
   run_frontend(
       port=3000, 
       use_https=True, 
       cert_path="/path/to/cert.pem",
       key_path="/path/to/key.pem"
   )

Manual Setup
~~~~~~~~~~~~

You can also run the servers manually:

**Backend**:

.. code-block:: python

   from yaaaf.server.run import run_server
   run_server(host="0.0.0.0", port=4000)

**Frontend**:

.. code-block:: bash

   cd frontend
   pnpm dev

Configuration
-------------

YAAAF can be configured through environment variables or a configuration file.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

* ``YAAAF_CONFIG``: Path to configuration JSON file

Configuration File
~~~~~~~~~~~~~~~~~~

Create a JSON configuration file:

.. code-block:: json
    {
      "client": {
        "model": "qwen2.5:32b",
        "temperature": 0.7,
        "max_tokens": 1024
      },
      "agents": [
        "reflection",
        "visualization",
        "sql",
        "reviewer",
        "websearch",
        "url_reviewer"
      ],
      "sources": [
        {
          "name": "london_archaeological_data",
          "type": "sqlite",
          "path": "../../data/london_archaeological_data.db"
        }
      ]
    }

First Steps
-----------

Once both servers are running:

1. **Open your browser** to ``http://localhost:3000`` (or ``https://localhost:3000`` if using HTTPS)
2. **Start a conversation** with the AI system
3. **Try different queries**:

   * "How many records are in the database?"
   * "Create a visualization of the sales data"
   * "Search for recent AI developments"
   * "Analyze the customer demographics"

Understanding the Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The chat interface displays messages with agent identifiers:

* Messages are wrapped in agent tags: ``<sqlagent>...</sqlagent>``
* Artifacts are shown as: ``<Artefact>artifact_id</Artefact>``
* Each agent specializes in different types of tasks

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Backend won't start**:

* Check if port 4000 is already in use
* Verify Python dependencies are installed
* Check for configuration file errors

**Frontend build errors**:

* Ensure Node.js 18+ is installed
* Try deleting ``node_modules`` and running ``pnpm install`` again
* Check for TypeScript compilation errors

**No agents responding**:

* Verify the backend is running and accessible
* Check browser console for API errors
* Ensure the correct model is configured and available

Getting Help
~~~~~~~~~~~~

* Check the logs for error messages
* Verify all dependencies are correctly installed
* Ensure configuration matches your environment