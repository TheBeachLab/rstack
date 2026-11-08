import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("check_plan", Path(__file__).resolve().parents[1] / "scripts/check_plan.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.plan = {"goal": "Fix a parser", "scope": "Parser and its tests", "stop_condition": "Regression and existing checks pass", "steps": [
            {"id": "reproduce", "deliverable": "Reproduction", "write_scope": "tests/parser", "verification": "Original bug fails the assertion"},
            {"id": "fix", "depends_on": ["reproduce"], "deliverable": "Fixed parser", "write_scope": "src/parser", "verification": "Reproduction and existing suite pass"},
        ]}

    def test_valid_dependency_order(self):
        self.assertEqual(module.check(self.plan), 2)

    def test_cycles_or_unknown_dependencies_are_rejected(self):
        for dep in ("fix", "missing"):
            plan = copy.deepcopy(self.plan)
            plan["steps"][0]["depends_on"] = [dep]
            with self.assertRaisesRegex(ValueError, "Dependencies"):
                module.check(plan)

    def test_duplicate_ownership_identity_is_rejected(self):
        self.plan["steps"][1]["id"] = "reproduce"
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            module.check(self.plan)

    def test_missing_verification_is_rejected(self):
        del self.plan["steps"][1]["verification"]
        with self.assertRaisesRegex(ValueError, "verification"):
            module.check(self.plan)

    def test_unbounded_plan_is_rejected(self):
        self.plan["stop_condition"] = " "
        with self.assertRaisesRegex(ValueError, "stop_condition"):
            module.check(self.plan)


if __name__ == "__main__":
    unittest.main()
