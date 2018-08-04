"""
The MIT License (MIT)

Copyright (c) 2015 kelsoncm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from unittest import TestCase
from python_brfied.env import env, env_as_list, env_as_list_of_maps, env_as_bool


class TestPythonBrfiedEnv(TestCase):

    def test_env(self):
        self.assertEqual('ASDF', env('DUMMY_ENV', 'ASDF'))

    def test_env_as_list(self):
        self.assertListEqual([], env_as_list('DUMMY_ENV'))
        self.assertListEqual([], env_as_list('DUMMY_ENV', ''))
        self.assertListEqual([], env_as_list('DUMMY_ENV', ' '))

        self.assertListEqual(['a'], env_as_list('DUMMY_ENV', 'a'))
        self.assertListEqual(['a', 'b'], env_as_list('DUMMY_ENV', 'a,b'))

        self.assertListEqual(['a', 'b'], env_as_list('DUMMY_ENV', 'a;b', delimiter=';'))

    def test_env_as_list_of_maps(self):
        self.assertListEqual([], env_as_list_of_maps('DUMMY_ENV', 'K'))
        self.assertListEqual([], env_as_list_of_maps('DUMMY_ENV', 'K', ''))
        self.assertListEqual([], env_as_list_of_maps('DUMMY_ENV', 'K', ' '))

        self.assertListEqual([{'K': 'a'}], env_as_list_of_maps('DUMMY_ENV', 'K', 'a'))
        self.assertListEqual([{'K': 'a'}, {'K': 'b'}], env_as_list_of_maps('DUMMY_ENV', 'K', 'a,b'))

        self.assertListEqual([{'K': 'a'}, {'K': 'b'}], env_as_list_of_maps('DUMMY_ENV', 'K', 'a;b', delimiter=';'))

    def test_env_as_bool(self):
        self.assertTrue(env_as_bool('DUMMY_ENV', 'true'))
        self.assertTrue(env_as_bool('DUMMY_ENV', True))

        self.assertFalse(env_as_bool('DUMMY_ENV', 'FALSE'))
        self.assertFalse(env_as_bool('DUMMY_ENV', False))

        self.assertIsNone(env_as_bool('DUMMY_ENV'))
        self.assertIsNone(env_as_bool('DUMMY_ENV', None))
        self.assertIsNone(env_as_bool('DUMMY_ENV', ' '))