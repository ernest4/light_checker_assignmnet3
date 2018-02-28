#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `light_counter` package."""

import pytest


from light_counter import light_counter


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
    lt = light_counter.LightTester(3)
    assert lt.count() == 9
    
def test_LightTester_apply():
    lt = light_counter.LightTester(3)
    #start:            Coordinates
    #F, F, F      (0,0), (0,1), (0,2)
    #F, F, F      (1,0), (1,1), (1,2)
    #F, F, F      (2,0), (2,1), (2,2)
    
    #switch on middle one (1,1)
    #F, F, F
    #F, T, F
    #F, F, F
    lt.apply(["turn on", "1", "1", "1", "1"])
    for row in range(len(lt.lights)):
        for col in range(len(lt.lights[row])):
            if row == 1 and col == 1:
                if lt.lights[row][col] == False: #check if middle light is on as required
                    assert False
            elif lt.lights[row][col] == True: # check if any other light is off as required
                assert False
                 
    #toggle the middle row (1,0), (1,1), (1,2)
    #F, F, F
    #T, F, T
    #F, F, F
    lt.apply(["switch", "1","0","1","2"])
    for row in range(len(lt.lights)):
        for col in range(len(lt.lights[row])):
            if row == 1 and col == 1:
                if lt.lights[row][col] == True: #check if middle light is off as required
                    assert False
            elif row == 1 and (col == 0 or col == 2): #check if (1,0) and (1,2) are on as required
                if lt.lights[row][col] == False:
                    assert False
            elif lt.lights[row][col] == True: # check if any other light is off as required
                assert False
    
    #turn them all off (0,0) ... (2,2)
    #F, F, F
    #F, F, F
    #F, F, F
    lt.apply(["turn off", "0","0","2","2"])
    for row in range(len(lt.lights)):
        for col in range(len(lt.lights[row])):
            if lt.lights[row][col] == True: #check if off as required
                assert False
