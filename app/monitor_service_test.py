import pytest
from monitor_service import MonitorService

monitor = MonitorService()

def test_this():
    assert monitor.all() == []
