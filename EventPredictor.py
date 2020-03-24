#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Employee

class EventPredictor(object):
	"""Predict the event(promotion,attrition,transfer) happen to one employee at given time."""
	def PredictEvent(self, aEmployee, aCur_time):
		"""@ParamType aEmployee Employee"""
		pass

def predictNextEventTime(self, df):
        prob = random()
        #df = model.cumulative_density_.copy()
        x = df.index.to_numpy()
        y = df['KM_estimate'].to_numpy()
        eventTime = np.interp(prob, y, x)
        return prob, eventTime

model = ura_predictor.fitDevlistModelSinglevents()
print(model.cumulative_density_)
df = model.cumulative_density_.copy()