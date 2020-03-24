import EventPredictor
import pandas as pd
import numpy as np
from random import random

class PromotionPredictor(EventPredictor):

    def __init__(self, modelInfo):
        self.modelInfo = modelInfo
        self.loadModel(modelInfo['file'])

    def loadModel(self, fileName):
        self.cumulative_density_df = pd.read_csv(fileName)
        self.time_to_event = self.cumulative_density_df.index.to_numpy()
        self.cumulative = self.cumulative_density_df['cumulative'].to_numpy()

    def predictNextEventTime(self):
        prob = random()
        eventTime = np.interp(prob, self.cumulative, self.time_to_event)

        return prob, eventTime
