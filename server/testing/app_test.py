import io
import sys

from app import app

class TestApp:
    '''Flask application in flask_app.py'''

    def test_count_range_10(self):
        '''counts through range of parameter in "/count/<parameter>" on separate lines.'''
        response = app.test_client().get('/count/10')
        count = '1\n2\n3\n4\n5\n6\n7\n8\n9\n10'
        assert response.data.decode() == count

    def test_math_add(self):
        '''adds parameters in "/math/" resource when operation is "+".'''
        response = app.test_client().get('/math/5/+/5')
        assert response.data.decode() == '<h1>Result: 10</h1>'

    def test_math_subtract(self):
        '''subtracts parameters in "/math/" resource when operation is "-".'''
        response = app.test_client().get('/math/5/-/5')
        assert response.data.decode() == '<h1>Result: 0</h1>'

    def test_math_multiply(self):
        '''multiplies parameters in "/math/" resource when operation is "*".'''
        response = app.test_client().get('/math/5/*/5')
        assert response.data.decode() == '<h1>Result: 25</h1>'

    def test_math_divide(self):
        '''divides parameters in "/math/" resource when operation is "div".'''
        response = app.test_client().get('/math/5/div/5')
        assert response.data.decode() == '<h1>Result: 1.0</h1>'

    def test_math_modulo(self):
        '''finds remainder of parameters in "/math/" resource when operation is "%".'''
        response = app.test_client().get('/math/5/%/5')
        assert response.data.decode() == '<h1>Result: 0</h1>'
