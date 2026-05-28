import unittest
from packages.utils import logging
from packages.utils import metrics

class TestRuntime(unittest.TestCase):
    def test_logging(self):
        log_manager = logging.LogManager('test')
        log_manager.info('test')
        log_manager.error('test')

    def test_metrics(self):
        metrics_manager = metrics.MetricsManager()
        elapsed_time = metrics_manager.get_elapsed_time()
        self.assertIsInstance(elapsed_time, float)

if __name__ == '__main__':
    unittest.main()