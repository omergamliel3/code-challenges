import unittest
from parameterized import parameterized
from solutions.ai_detector import detect_ai


class TestAIDetector(unittest.TestCase):
    # ---------- HUMAN TEXT CASES ----------

    @parameterized.expand([
        ("The quick brown fox jumped over the lazy dog.",),
        ("The hypersonic brown fox - jumped (over) the lazy dog.",)
    ])
    def test_given_human_text_then_return_human(self, text):
        res = detect_ai(text)
        self.assertEqual(res, "Human")

    # ---------- AI TEXT CASES ----------

    @parameterized.expand([
        ("Yes - you're right! I made a mistake there - let me try again.",),
        ("The extraordinary students were studying vivaciously.",),
        ("The (excited) student was (coding) in the library.",)
    ])
    def test_given_AI_text_then_return_AI(self, text):
        res = detect_ai(text)
        self.assertEqual(res, "AI")


if __name__ == "__main__":
    unittest.main()
