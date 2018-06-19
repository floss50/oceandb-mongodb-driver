#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oceandb_driver_interface.oceandb import OceanDb



mongo = OceanDb('/home/eruiz/Projects/oceandb-mongodb-driver/tests/oceandb.ini').plugin

def test_plugin_type_is_mongodb():
    assert mongo.type == 'MongoDB'


def test_plugin_write_and_read():
    mongo.write({"id": 1, "value": "test"})
    assert mongo.read(1)['id'] == 1
    assert mongo.read(1)['value'] == 'test'
    mongo.delete(1)


def test_update():
    mongo.write({"id": 1, "value": "test"})
    assert mongo.read(1)['value'] == 'test'
    mongo.update(1, {"id": 1, "value": "testUpdated"})
    assert mongo.read(1)['value'] == 'testUpdated'
    mongo.delete(1)


def test_plugin_list():
    mongo.write({"id": 1, "value": "test1"})
    mongo.write({"id": 2, "value": "test2"})
    mongo.write({"id": 3, "value": "test3"})
    assert mongo.list().count() == 3
    assert mongo.list()[0]['value'] == 'test1'
    mongo.delete(1)
    mongo.delete(2)
    mongo.delete(3)
