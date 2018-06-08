import pytest
from monitor_service import MonitorService, Monitor

appname = 'my_first_app'

def test_all():
    '''This test checks if the all method returns an empty array when no monitors are specified'''
    monitor_service = MonitorService()
    assert monitor_service.all() == []

def test_create():
    '''This test checks if the creation of a monitor is done succesfull and that the monitor matches specs'''
    monitor_service = MonitorService()
    app = monitor_service.create(appname)
    assert_presence(app, 'id')
    assert_presence(app, 'name')
    assert app['name'] == appname
    assert_presence(app, 'priority')
    assert_presence(app, 'status')
    assert len(monitor_service.all()) == 1

def test_find():
    monitor_service = MonitorService()
    app = monitor_service.create(appname)
    assert app == monitor_service.find(app['id'])

def test_update():
    assert True

def remove():
    assert True

def assert_presence(object_to_check, key):
    try:
        object_to_check[key]
        assert True
    except KeyError:
        assert False
