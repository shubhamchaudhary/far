#!/usr/bin/env python

from __future__ import print_function

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
    from unittest.mock import call
except ImportError as e:
    import mock
    from mock import patch
    from mock import call

from far import Far


class TestFar(unittest.TestCase):
    def setUp(self):
        self.old = 'asdfadfas'
        self.new = 'asdfadfas'

    def tearDown(self):
        pass

    @patch('os.system')
    def test_should_run_system_command(self, mock_system):
        mock_system.return_value = 0

        obj = Far()
        obj.find_and_replace(self.old, self.new)

        cmd = "find . -type f -not -path '*/\.git*' -exec sed -i 's/" + self.old + "/" + self.new + "/g' {} +  "
        mock_system.assert_called_once_with(cmd)

class AnyStringContaining(str):
    def __eq__(self, other):
        return self in other


if __name__ == '__main__':
    unittest.main()
