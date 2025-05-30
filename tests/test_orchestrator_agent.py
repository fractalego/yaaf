import asyncio
import unittest

from yaaf.components.agents.artefact_utils import get_artefacts_from_utterance_content
from yaaf.components.agents.orchestrator_agent import OrchestratorAgent
from yaaf.components.agents.sql_agent import SqlAgent
from yaaf.components.agents.visualization_agent import VisualizationAgent
from yaaf.components.client import OllamaClient
from yaaf.components.data_types import Messages
from yaaf.components.agents.reflection_agent import ReflectionAgent
from tests.test_sql_agent import sqlite_source

text_client = OllamaClient(
    model="qwen2.5:32b",
    temperature=0.4,
    max_tokens=100,
)
code_client = OllamaClient(
    model="gemma3:12b",
    temperature=0.4,
    max_tokens=1000,
)
agent = OrchestratorAgent(client=text_client)
agent.subscribe_agent(ReflectionAgent(client=text_client))
agent.subscribe_agent(VisualizationAgent(client=text_client))
agent.subscribe_agent(SqlAgent(client=code_client, source=sqlite_source))


class TestOrchestratorAgent(unittest.TestCase):
    def test_query1(self):
        message_queue: list[str] = []
        messages = Messages().add_user_utterance(
            "How many archaeological findings are there in the dataset?"
        )
        asyncio.run(agent.query(
            messages=messages,
            message_queue=message_queue,
        ))
        artefacts = get_artefacts_from_utterance_content("\n".join(message_queue))
        assert len(artefacts) > 0
        expected = "1015"
        self.assertIn(expected, artefacts[0].data.to_markdown())

    def test_query2(self):
        message_queue: list[str] = []
        messages = Messages().add_user_utterance(
            "What is the most common description of archeological finding? visualize the top5 and give me the answer in a single sentence."
        )
        asyncio.run(
            agent.query(
                messages=messages,
                message_queue=message_queue,
            )
        )
        artefacts = get_artefacts_from_utterance_content("\n".join(message_queue))
        expected = "prehistoric deposits"
        self.assertIn(expected, artefacts[0].data.to_markdown().lower())
