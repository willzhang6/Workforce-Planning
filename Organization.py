#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Employee


class Organization(object):
    """Organization which contains employees and sub-organizations."""

	def setOrgDictionary(self, orgDict):
		self._org_dict = orgDict

    def Organization(self):
        pass

    def Hire(self):
        """@ReturnType void"""
        pass

    def Promote(self):
        pass

    def PlannedTransfer(self, aTransfer_request_list):
        """This is an organization level planned transfer. Transfer certain number of Employee to another department."""
        pass

    def loadTalentEventModels(self, talentPredictors):
		self._promoPredictor = talentPredictors['promotionModel']
		self._transferPredictor = talentPredictors['transferModel']
		self._attritionPredictor = talentPredictors['attritionModel']
        
	def predictEvent(self, empl, curTime):
		promoEvent = self._promoPredictor(empl, curTime)
		transferEvent = self._transferPredictor(empl, curTime)
		attritionEvent = self._attritionPredictor(empl, curTime)
		firstEvent = None
		empl._coming_event = firstEvent

	def promote(self, empl, curTime, timePeriod):
		# _org_id, timePeriod, jobFamily, joblevel
		key = empl._org_id+'-'+str(timePeriod)+'-'+empl._job_family_name+'-'+empl._job_level
		empl._job_level += 1
		empl._time_in_level = 0
		if key in self._promotionLog:
			self._promotionLog[key] += 1
		else:
			self._promotionLog[key] = 1

	def transferInEmployee(self, empl, curTime, timePeriod, org_id):
		key = str(timePeriod)+'-'+empl._job_family_name+'-'+empl._job_level+'-'+org_id
		if key in self._transferInLog:
			self._transferInLog[key] += 1
		else:
			self._transferInLog[key] = 1

	def removeEmployee(self, empl):
		# TODO: remove empl id from Organization
		pass

	def transfer(self, empl, curTime, timePeriod):
		
		to_org_id = empl._coming_event._to_org_id
		# _org_id, timePeriod, jobFamily, joblevel, to_org_id"""
		key = str(timePeriod)+'-'+empl._job_family_name+'-'+empl._job_level+'-'+to_org_id
		# TODO: implement transfer to organization. Need to a dictionary of Organization using org_id as key.

		if to_org_id in self._org_dict:
			to_org = self._org_dict[to_org_id]
			self.removeEmployee(empl)
			to_org.transferInEmployee(empl, curTime, timePeriod, to_org_id)

		if key in self._transferOutLog:
			self._transferOutLog[key] += 1
		else:
			self._transferOutLog[key] = 1

	def attrition(self, empl, curTime, timePeriod):
		# _org_id, timePeriod, jobFamily, joblevel
		key = empl._org_id+'-'+str(timePeriod)+'-'+empl._job_family_name+'-'+empl._job_level
		# TODO: implement transfer to organization. Need to a dictionary of Organization using org_id as key.
		if key in self._attritionLog:
			self._attritionLog[key] += 1
		else:
			self._attritionLog[key] = 1
		self.removeEmployee(empl)

	def processEvent(self, empl, curTime, timePeriod):
		event = empl._coming_event
		if curTime < event._eventTime:
			return 
		else:
			if event._eventType == 'promotion':
				self.promote(empl, curTime, timePeriod)
			elif event._eventType == 'transfer':
				self.transfer(empl, curTime, timePeriod)
			elif event._eventType == 'attrition':
				self.attrition(empl, curTime, timePeriod)

    def processTalentEvents(self, curTime, timePeriod):
		
		for empl in self._employees:
			if empl._coming_event == None:
				self.predictEvent(empl, curTime)
			else:
				self.processEvent(empl, curtTime, timePeriod)

	def getOrganizationMetrics(self):
		"""Table: orgId, level, jobFamily, timePeriod, promoIn, promoOut, transferIn, transferOut, hireIn, attrition, startingHC, endingHC
		"""
		min_level = min(levels)
		for level in levels:
			for jobFamily in jobFamilies:
				for timePeriod in timePeriods:
					status = [self._org_id, level, jobFamily, timePeriod]

					# StartingHC
					startingHC = 100
					endingHC = startingHC

					# Promotion In
					promoIn = 0
					if level > min_level:
						promoKey = self._org_id+'-'+str(timePeriod)+'-'+jobFamily+'-'+str(level-1)
						if promoKey in self._promotionLog:
							promoIn = self._promotionLog[promoKey]
							endingHC += promoIn
					status.append(promoIn)

					# Promotion Out
					promoOut = 0
					promoKey = self._org_id+'-'+str(timePeriod)+'-'+jobFamily+'-'+str(level)
					if promoKey in self._promotionLog:
						promoOut = self._promotionLog[promoKey]
						endingHC -= promoOut
					status.append(promoOut)

					# Transfer In
					transferIn = 0
					transferKey = str(timePeriod)+'-'+jobFamily+'-'+str(level)+'-'+self._org_id
					if transferKey in self._transferInLog:
						transferIn = self._transferInLog[transferKey]
						endingHC += tranferIn
					status.append(transferIn)

					# Transfer Out
					transferKeyPrefix = str(timePeriod) + '-' + jobFamily + '-' + str(level)
					transferOut = 0
					for key, value in self._transferOutLog.iteritems():   # iter on both keys and values
						if key.startswith(transferKeyPrefix):
							transferOut += value
					endingHC -= transferOut
					status.append(transferOut)

					# Attrition
				    attrition = 0
				    attritionKey = self._org_id+'-'+str(timePeriod)+'-'+jobFamily+'-'+str(level)
					if attritionKey in self._attritionLog:
						attrition = self._attritionLog[attritionKey]
						endingHC -= attrition
					status.append(attrition)


		

    def __init__(self, startTime):

        """@AttributeType string
		Name of the department"""
        self._org_name = None
        """@AttributeType string"""
        self._org_id = None
        """@AttributeType int
		level of organization"""
        self._org_level = None
        """@AttributeType Class Diagram - Talent Force Opt System.Employee"""
        self._org_leader = None
        """@AttributeType Employee*"""
        self._employees = None
		self.processTalentEvents(startTime)
		"""Promotion key: _org_id, timePeriod, jobFamily, jobLevel"""
		self._promotionLog = {}
		"""Transfer key: timePeriod, jobFamily, joblevel, from_org_id"""
		self._transferInLog = {}
		"""Transfer key: timePeriod, jobFamily, joblevel, to_org_id"""
		self._transferOutLog = {}
		"""Attrition key: _org_id, timePeriod, jobFamily, joblevel"""
		self._attritionLog = {}
		"""@AttributeType dictionary"""
		self._org_dict = None
		"""@AttributeType pandas DataFrame"""
		self._orgTalentEventSummary = pd.DataFrame(columns=['orgId', 'jobLevel', 'jobFamily', 'timePeriod', 'promoIn', 'promoOut', 'transferIn', 'transferOut', 'hireIn', 'attrition', 'startingHC', 'endingHC'])




