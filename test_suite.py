"""
EcoNexo Test Suite
Unit and integration tests for robust validation
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))


class TestDatabase(unittest.TestCase):
    """Test database operations"""
    
    def setUp(self):
        """Set up test database"""
        pass
    
    def test_module_imports(self):
        """Test that database module imports correctly"""
        import database as db
        self.assertTrue(hasattr(db, 'init_database'))
        self.assertTrue(hasattr(db, 'create_user'))
        self.assertTrue(hasattr(db, 'authenticate_user'))


class TestAgent(unittest.TestCase):
    """Test AI Agent functionality"""
    
    def setUp(self):
        """Set up test agent"""
        from agent import ProductivityAgent
        
        self.user_profile = {
            "profile": "Executor",
            "iap_score": 85,
            "tasks_completed": 2
        }
        
        self.agent = ProductivityAgent(self.user_profile)
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.user_profile["profile"], "Executor")
        self.assertGreater(len(self.agent.tools), 0)
    
    def test_break_down_task_tool(self):
        """Test task breakdown tool"""
        result = self.agent.execute_tool(
            "break_down_task",
            task="Launch new product",
            num_steps=5
        )
        
        self.assertTrue(result["success"])
        self.assertIn("steps", result["result"])
        self.assertEqual(len(result["result"]["steps"]), 5)
    
    def test_pomodoro_tool(self):
        """Test Pomodoro planning tool"""
        result = self.agent.execute_tool(
            "create_pomodoro_plan",
            task="Deep work session",
            duration_minutes=100
        )
        
        self.assertTrue(result["success"])
        self.assertIn("schedule", result["result"])


class TestI18n(unittest.TestCase):
    """Test internationalization"""
    
    def test_module_imports(self):
        """Test i18n module imports"""
        try:
            from i18n import t, QUESTIONS, TASKS, PROFILE_INFO
            self.assertIsNotNone(t)
            self.assertIsNotNone(QUESTIONS)
            self.assertIsNotNone(TASKS)
        except ImportError:
            self.skipTest("i18n module not available")


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDatabase))
    suite.addTests(loader.loadTestsFromTestCase(TestAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestI18n))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
