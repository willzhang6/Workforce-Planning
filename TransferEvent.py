#!/usr/bin/python
# -*- coding: UTF-8 -*-
import TMEvent

class TransferEvent(TMEvent):
	def __init__(self):
		self._dest_department = None

