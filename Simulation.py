#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from datetime import datetime, timedelta
from random import seed

import numpy as np
import pandas as pd
# import simpy

import EventPredictor
import Optimizer


class Simulation(object):
    def Initialize(self):
        self._start_datetime = self._configuration["start_datetime"]
        self._end_datetime = self._configuration["end_datetime"]
        self._time_step = self._configuration["time_step"]
        self._optimizer = self._configuration["optimizer"]
        # self._event_predictor = self._configuration["event_predictor"]
        # self._employees = self._configuration["employees"]

    def RunSimulation(self):
        """Run simulation and return simulation result as a data frame."""
        pass

    def WriteSummary(self):
        pass

    def WriteDetail(self):
        pass

    def Optimize(self):
        pass

    def logEvent(self, empl, eventTime, eventType):
        eventInfo = [eventTime, eventType] + empl.getAttributes()
        self._eventLog.append(eventInfo)

    def movement(self, env, empl):
        # we can change the while condition to while an employee is active etc.
        while True:
            yield env.timeout(empl._coming_event.time)
            coming_event = empl._coming_event.event
            if coming_event == "promo":
                empl.promotion()
            elif coming_event == "transfer":
                empl.transfer()
            elif coming_event == "term":
                empl.term()
            self._event_predictor(empl)
            self.logEvent(empl, env.now, coming_event)

    def Simulation(self):
        """key value dictionary contains all input, output parameters."""
        env = simpy.Environment()
        self._eventLog = []
        simulation_duration = (self._end_datetime - self._start_datetime).days

        for empl in self._employees:
            self.logEvent(empl, 0, "initialized")
            env.process(self.movement(env, empl))
        env.run(until=simulation_duration)

    def __init__(self, configuration):
        self._configuration = configuration
        """@ReturnType void"""
        self._start_datetime = None
        """@AttributeType double"""
        self._end_datetime = None
        """@AttributeType double"""
        self._time_step = None
        """@AttributeType double"""
        self._optimizer = None
        """@AttributeType Class Diagram - Talent Force Opt System.Optimizer"""
        self._event_predictor = None
        """@AttributeType Class Diagram - Talent Force Opt System.EventPredictor"""
        self._employees = None
        self._eventLog = []
