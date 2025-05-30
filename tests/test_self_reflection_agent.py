import asyncio
import unittest

from yaaf.components.client import OllamaClient
from yaaf.components.data_types import Messages
from yaaf.components.agents.reflection_agent import ReflectionAgent


class TestSelfReflectionAgent(unittest.TestCase):
    def test_simple_output(self):
        client = OllamaClient(
            model="gemma3:4b",
            temperature=0.7,
            max_tokens=100,
        )
        messages = Messages().add_user_utterance("What is the capital of France?")
        agent = ReflectionAgent(client)
        answer = asyncio.run(
            agent.query(
                messages=messages,
            )
        )
        expected = "Paris"
        self.assertIn(expected, answer)
