

offers = [11,9,12,9,23,8]
target = 10
def best_offers(offers,target):
	if offers:
		match = [x for x in offers if x == target or x < target]
		
		if match :
			new_offer = max(match)
		else:
			match = [x for x in offers if x > target]
			new_offer = min(match)
		return new_offer
	else:
		return 'No Offers'
		
	
offer = best_offers(offers,target)
print offer

def other_best_offers(offers,target):
	if offers:
		
		offers = sorted(offers)
		new_offer = min(offers, key=lambda x:abs(x-target))
		return new_offer
	else:
		return 'No Offers'

offer = other_best_offers(offers,target)
print offer