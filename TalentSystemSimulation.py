from Simulation import Simulation
from Organization import Organization
from PromotionPredictor import PromotionPredictor
from TransferPredictor import TransferPredictor
from AttritionPredictor import AttritionPredictor


class TalentSystemSimulation(Simulation):
    def __init__(self, configuration):
        # self._optimizer = self._configuration["optimizer"]
        # self._event_predictor = self._configuration["event_predictor"]
        # self._employees = self._configuration["employees"]
        """@AttributeType dictionary"""
        self._configuration = configuration
        """@AttributeType string"""
        self._title = configuration["title"]
        """@AttributeType string"""
        self._projectPath = configuration["projectPath"]
        """@AttributeType datetime"""
        self._startTime = configuration["startTime"]
        """@AttributeType datetime"""
        self._endTime = configuration["endTime"]
        """@AttributeType int"""
        self._timeStep = configuration["timeStep"]
        """@AttributeType int"""
        self._outputTimeStep = configuration["outputTimeStep"]
        """@AttributeType string. Values in ['d', 'w', 'm', 'q', 'y'] """
        # self._outputTimeStepUnit = configuration["outputTimeStepUnit"]
        """@AttributeType double"""
        self._sampleSize = configuration["MCSampleSize"]
        """@AttributeType double"""
        self._outputQuantile = configuration["MCOutQuantiles"]
        self._rootOrg = None
        """@AttributeType dictionary. Predictive models"""
        self._talentEventPredictors = None
        self.loadWorkforceData()
        self.loadWorkforceDemand()
        self.loadTalentEventModels()

    def loadWorkforceData(self):
        """Load organzization data"""
        self._rootOrg = Organization()
        pass

    def loadWorkforceDemand(self):
        """Load workforce demand data"""
        pass

    def loadEventModel(self, modelName):
        modelInfo = self._configuration['eventPreditionModels'][modelName]
        #{model: "attritionModel", type: "survival", file: "attrition_model.csv"}
        if modelInfo['model'] == 'promotionModel':
            return PromotionPredictor(modelInfo)
        elif modelInfo['model'] == 'transferModel':
            return TransferPredictor(modelInfo)
        elif modelInfo['model'] == 'attritionModel':
            return AttritionPredictor(modelInfo)

    def loadTalentEventModels(self):
        """Load Talent Event Predictors"""
        """TODO: Put Model Name List in a Common Place"""
        models = ['promotionModel', 'transferModel', 'attritionModel']
        self._talentEventPredictors = {}
        for model in models:
            self._talentEventPredictors[model] = self.loadEventModel(model)
        """TODO: Where to Access Models"""
        self._rootOrg.loadTalentEventModels(self._talentEventPredictors)
        pass

    def processTalentEvents(self, curTime, timePeriod):
        self._rootOrg.processTalentEvents(curTime, timePeriod)
        pass

    def predictTalentEvents(self):
        pass

    def outputTalentStatus(self):
        pass

    def getTimePeriod(self, curTime):
        return int(curTime / self._outputTimeStep) + 1

    def RunBaselineSimulation(self):
        """Run simulation and return simulation result as a data frame."""
        curTime = self._startTime
        timePeriod = 1
        while curTime <= self._endTime:
            # run simulation
            self.processTalentEvents(curTime, timePeriod)
            self.outputTalentStatus()
            curTime = self.getNextTime(curTime)
            timePeriod = self.getTimePeriod(curTime)
        pass

    def getNextTime(self, curTime):
        newTime = curTime + self._timeStep
        return newTime

    def runMonteCarloSimulation(self):
        """Run simulation and return simulation result as a data frame."""
        pass

    def runOptimization(self):
        pass
