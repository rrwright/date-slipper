def date_slipper(ttc):
	from datetime import date, timedelta
	from math import ceil
	
	portions = ["early ", "mid ", "late "]
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	quarters = ["Q1", "Q2", "Q3", "Q4"]

	future_date = lambda days: date.today() + timedelta(days=days)
	month_idx = lambda days: future_date(days).month - 1

	# This function approximates the time-to-completion (in days) for 3 of each category of estimates:
	# Difference => 1 specific, 3 partial months, 3 partial quarters (months), 3 quarters (partial years), years...
	# Example: [0, 10, 21, 37, 59, 91, 137, 200, 283, 388, ...]
	intervals = lambda x: int(round( 11 * x - 1.2 * x**2 + 0.53 * x**3 ))

	precision = [
		lambda days: months[month_idx(days) % len(months)] + " " + str(future_date(days).day),  # day
		lambda days: portions[int(future_date(days).day // 10.34)] + months[month_idx(days)],   # part month
		lambda days: portions[month_idx(days) % 3] + quarters[month_idx(days) // 3],            # part quarter
		lambda days: quarters[month_idx(days) // 3] + " " + str(future_date(days).year),        # quarter
		lambda days: str(future_date(days).year),                                               # year
		lambda days: "probably never"                                                           # never
	]
	
	ttc = int(ttc)  # time_to_completion
	
	# This equation returns a value which, when rounded UP (math.ceil), is the index to _intervals_ resulting in a properly conservative time period.
	y = 13 * ttc ** 0.113 - 16.5
	idx = int(ceil(max(y, 0)))  # y might be a value below zero, so we take the max of y or 0 and round it up.

	level_of_precision = min(int(ceil(idx/3.)), len(precision) - 1)  # use min() to make sure the index into the precision array never overruns.
	adjusted_estimate = max(intervals(idx), ttc)
	return precision[level_of_precision](adjusted_estimate)

if __name__ == "__main__":
    import sys
    print date_slipper(int(sys.argv[1]))