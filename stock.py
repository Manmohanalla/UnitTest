


stock_prices_yesterday = [7, 5, 7, 8, 1, 2]

def get_max_profit(stock_prices_yesterday):
	if len(stock_prices_yesterday) < 2:
		return stock_prices_yesterday
	min_price = min(stock_prices_yesterday)
	rest_of_day = [i for index,i in enumerate(stock_prices_yesterday) if index > stock_prices_yesterday.index(min_price) ]
	
	max_price = max(rest_of_day)

	max_profit = max_price - min_price

	print max_profit

def get_max_profit1(stock_prices_yesterday):

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        print max_profit

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)
        print min_price

    print max_profit


#get_max_profit(stock_prices_yesterday)
get_max_profit1(stock_prices_yesterday)