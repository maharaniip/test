import unittest
from odoo.tests.common import TransactionCase
from odoo.exceptions import Warning

class TestMyModule(TransactionCase):

    def test_my_method(self):

        def setUp(self):
            super().setUp()
            self.my_model = self.env['material.material']

        def test_create(self):
            record = self.my_model.create(
                {'name': 'Test Record',
                 'code': 'A',
                 'type': 'Cotton',
                 'price': 1000})
            self.assertTrue(record)
            self.assertEqual(record.name, 'Test Record')
            print('Created Record Successful')


        def test_write(self):
            record = self.my_model.create({'name': 'Test Record'})
            record.write(
                {'name': 'Updated Record',
                 'code': 'A',
                 'type': 'Cotton',
                 'price': 1000
                 })
            self.assertEqual(record.name, 'Updated Record')
            print('Updated Record Successful')