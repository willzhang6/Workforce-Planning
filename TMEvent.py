#!/usr/bin/python
# -*- coding: UTF-8 -*-
class TMEvent(object):
	"""A talent movement event including: promotion,transfer,attrition."""
	def __init__(self):
		self._tm_event_type = None
		"""@AttributeType int
		from enum import Enum
		class TMEventType(Rum):
		promotion = 1
		attrition = 2
		transfer = 3"""
		self._event_time = None
		"""Datetime of the event"""

