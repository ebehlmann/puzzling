import input
from datetime import datetime
from operator import itemgetter

def parse_input(puzzle_input):
	logs = []
	puzzle_input = puzzle_input.split('\n')
	for i in puzzle_input:
		date = i[1:17]
		event = i[19:]
		start = event.find('#')
		if(start == -1):
			logs.append([date, event])
		else:
			stop = event.find(' ', start)
			guard = event[start+1:stop]
			logs.append([date, 'begins shift', guard])
	logs.sort(key=itemgetter(0))
	return logs

def find_minutes_per_guard(logs):
	guards = {}
	current_guard = 0
	i = 0
	while i < len(logs):
		if logs[i][1] == 'begins shift':
			current_guard = logs[i][2]
			i += 1
		else:
			if logs[i][1] == 'falls asleep':
				sleep_time = datetime.strptime(logs[i][0], "%Y-%m-%d %H:%M")
				wake_time = datetime.strptime(logs[i+1][0], "%Y-%m-%d %H:%M")
				diff = (wake_time - sleep_time).seconds / 60
				if current_guard in guards:
					guards[current_guard] += diff
				else:
					guards[current_guard] = diff
				i += 2
	return guards

def find_max(guards):
	max = 0
	max_key = 0
	for key, value in guards.items():
		if value > max:
			max = value
			max_key = key
	return max_key

def find_guard_logs(logs, guard):
	guard_logs = []
	target_guard = False
	for i in logs:
		if i[1] == 'begins shift':
			if int(i[2]) == int(guard):
				target_guard = True
			else:
				target_guard = False
		if target_guard == True:
			guard_logs.append(i)
	return guard_logs

def find_sleepiest_minute(guard_logs):
	minutes = {}
	i = 0
	while i < len(guard_logs):
		if guard_logs[i][1] == 'falls asleep':
			sleeps = int(guard_logs[i][0][-2:])
			wakes = int(guard_logs[i+1][0][-2:])
			while sleeps < wakes:
				if sleeps in minutes:
					minutes[sleeps] += 1
				else:
					minutes[sleeps] = 1
				sleeps += 1
			i += 2
		else:
			i += 1
	return minutes

def find_max_overall_minute(logs, guards):
	strategy_2_guard = 0
	strategy_2_minute = 0
	minute_max = 0
	for guard in guards:
		guard_logs = find_guard_logs(logs, int(guard))
		minutes = find_sleepiest_minute(guard_logs)
		top_minute = find_max(minutes)
		if(minutes[top_minute] > minute_max):
			strategy_2_guard = guard
			strategy_2_minute = top_minute
			minute_max = minutes[top_minute]
	return int(strategy_2_guard), strategy_2_minute

logs = parse_input(input.puzzle_input)
minutes_per_guard = find_minutes_per_guard(logs)
guards = minutes_per_guard.keys()
top_sleeper = int(find_max(minutes_per_guard))
top_sleeper_logs = find_guard_logs(logs, top_sleeper)
top_sleeper_minutes = find_sleepiest_minute(top_sleeper_logs)
top_sleeper_top_minute = find_max(top_sleeper_minutes)
print('Strategy 1: ' + str(top_sleeper * top_sleeper_top_minute))
strategy_2_guard, strategy_2_minute = find_max_overall_minute(logs, guards)
print('Strategy 2: ' + str(strategy_2_guard * strategy_2_minute))