#!/usr/bin/env python
# coding=utf-8
'''
 File Name: ajax.py
 Author: shenlian
 Created Time: 2014年03月29日 星期六 14时52分26秒
'''


from django.utils import  simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def dajaxice_example(request):
	print "ajax hehdde"
	return simplejson.dumps({'message':'Hello from Python!'})



