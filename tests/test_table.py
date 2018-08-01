# coding=utf-8

import unittest
import os

from contils.table import Table, Column


class TestColumn(unittest.TestCase):
    def test_template(self):
        pass

    pass


class TestTable(unittest.TestCase):
    def test_render(self):
        expected = os.linesep.join([
            '+----+',
            '| id |',
            '+----+',
            '| 1  |',
            '| 2  |',
            '| 5  |',
            '| 6  |',
            '+----+'
        ])

        table = Table(order_by='id')
        table.columns.append(Column('id'))
        table.rows.append({'id': 1})
        table.rows.append({'id': 6})
        table.rows.append({'id': 2})
        table.rows.append({'id': 5})

        self.assertEqual(expected, table.render())

    def test_stringable_template(self):
        expected = os.linesep.join([
            '+-----+',
            '| id  |',
            '+-----+',
            '| 1.0 |',
            '| 2.0 |',
            '| 5.0 |',
            '| 6.0 |',
            '+-----+'
        ])

        table = Table(order_by='id')
        table.columns.append(Column('id', template='{0:.1f}'))
        table.rows.append({'id': 1})
        table.rows.append({'id': 6})
        table.rows.append({'id': 2})
        table.rows.append({'id': 5})

        self.assertEqual(expected, table.render())

    def test_callable_template(self):
        def template(value: int):
            return '-' if value == 0 else f'{value:.1f}'

        expected = os.linesep.join([
            '+-----+',
            '| id  |',
            '+-----+',
            '| 1.0 |',
            '| 6.0 |',
            '| -   |',
            '| 5.0 |',
            '+-----+'
        ])

        table = Table()
        table.columns.append(Column('id', template=template))
        table.rows.append({'id': 1})
        table.rows.append({'id': 6})
        table.rows.append({'id': 0})
        table.rows.append({'id': 5})

        self.assertEqual(expected, table.render())

    pass
