#!/usr/bin/python
# -*- coding: UTF-8 -*-
import TMEvent

class Employee(object):
	"""Employee class which contains all the employee information."""
	def Employee(self):
		pass

	def ApplyEvent(self, aTm_event):
		"""On the status checking moment, if the coming_event date is reaching. Then apply the event to the employee.
		1. AttritionEvent - the employee will leave the company (removed from list)
		2. PromotionEvent - the employee will get promoted to the next level. After adjust employee's status, will call EventPredictor to predict the next coming event for this employee.
		3. TransferEvent - will transfer to a new department. After adjust employee's status, will call EventPredictor to predict the next coming event for this employee.
		@ParamType aTm_event TMEvent"""
		pass

	def __init__(self):
		self._name = None
		"""@AttributeType string
		full name of employee"""
		self._empl_id = None
		"""@AttributeType string"""
		self._job_family_name = None
		"""@AttributeType string"""
		self._job_level = None
		"""@AttributeType int"""
		self._job_title_name = None
		"""@AttributeType string"""
		self._login = None
		"""@AttributeType string"""
		self._time_in_level = 0
		"""@AttributeType int
		time in current job level"""
		self._time_in_department = 0
		"""@AttributeType int"""
		self._event_history = None
		"""@AttributeType Class Diagram - Talent Force Opt System.TMEvent*"""
		self._coming_event = None
		"""@AttributeType TMEvent
		The predicted coming event for the employee."""

