#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Optimizer(object):
	def Optimizer(self):
		pass

	def Setup(self):
		pass

	def EvalConstraints(self):
		pass

	def GetNewValue(self):
		pass

	def EvalObjective(self):
		pass

	def GetOptimal(self):
		pass

	def WriteOptimizationSummary(self):
		pass

	def __init__(self):
		self._objective = None
		"""objective variable for optimization."""
		self._constraints = None
		self._design_vars = None

