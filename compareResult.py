#-*- coding:utf-8 - *-


def compareResultForQueryAndRules(segQuery, ruleList):
	containedFlag = False
	containedResults = []
	ruleToCeck = []
	for rule in ruleList:
		ruleToCeck = rule[0] + rule[1]
		print "rules: ", ruleToCeck 
		print "segQuery: ", segQuery
		if set(segQuery) == set(ruleToCeck):
			containedFlag = True
			print "Found :", containedFlag
			containedResults.append(ruleToCeck)
		else:
			print "Not found, go ahread!"
			continue
	return containedFlag, ruleToCeck


