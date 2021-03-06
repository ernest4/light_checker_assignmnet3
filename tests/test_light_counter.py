#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `light_counter` package."""

import pytest


from light_counter import lightTester
from light_counter import fileParser


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


#def test_content(response):
#    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    
def test_LightTester_count():
    lt = lightTester.LightTester(3)
    assert lt.count() == 0
    
def test_LightTester_apply():
    lt = lightTester.LightTester(3)
    #start:            Coordinates
    #F, F, F      (0,0), (1,0), (2,0)
    #F, F, F      (0,1), (1,1), (2,1)
    #F, F, F      (0,2), (2,2), (2,2)
    
    #switch on middle one (1,1)
    #F, F, F
    #F, T, F
    #F, F, F
    lt.apply(["turn on", 1, 1, 1, 1])
    for row in range(len(lt.lights)):
        for col in range(len(lt.lights[row])):
            if row == 1 and col == 1:
                assert lt.lights[row][col] == True #check if middle light is on as required
            else:
                assert lt.lights[row][col] == False #check if any other light is off as required
                 
    #toggle the middle row (1,0), (1,1), (1,2)
    #F, F, F
    #T, F, T
    #F, F, F
    lt.apply(["switch", 0, 1, 2, 1])
    for row in range(len(lt.lights)):
        for col in range(len(lt.lights[row])):
            if row == 1 and col == 1:
                assert lt.lights[row][col] == False #check if middle light is off as required
            elif row == 1 and (col == 0 or col == 2): #check if (1,0) and (1,2) are on as required
                assert lt.lights[row][col] == True
            else:
                assert lt.lights[row][col] == False # check if any other light is off as required
    
    #turn them all off (0,0) ... (2,2)
    #F, F, F
    #F, F, F
    #F, F, F
    lt.apply(["turn off", 0, 0, 2, 2])
    for row in range(len(lt.lights)):
        for col in range(len(lt.lights[row])):
            assert lt.lights[row][col] == False #check if off as required
            
def test_parseFile_read_local_file():
    #Testing proper data
    inputFile = "tests/testData/test_data.txt"
    size, instructions = fileParser.fileParser(inputFile)
    assert size == 10
    assert instructions[0] == ['turn on', 0, 0, 9, 9]
    assert instructions[1] == ['turn off', 0, 0, 9, 9]
    assert instructions[2] == ['switch', 0, 0, 9, 9]
    assert instructions[3] == ['turn off', 0, 0, 9, 9]
    assert instructions[4] == ['turn on', 2, 2, 7, 7]
    
    #Testing invalid data (invalid size)
    inputFile = "tests/testData/test_data2.txt"
    size, instructions = fileParser.fileParser(inputFile)
    assert size == None
    
    #Testing invalid data (invalid instructions)
    inputFile = "tests/testData/test_data3.txt"
    size, instructions = fileParser.fileParser(inputFile)
    assert len(instructions) == 3
    assert size == 10
    assert instructions[0] == ['turn on', 0, 0, 9, 9]
    assert instructions[1] == ['turn off', 0, 0, 9, 9]
    assert instructions[2] == ['turn on', 0, 2, 0, 7]
    