#-*-coding: utf-8-*-
from itertools import groupby
from operator import itemgetter
robots = [
	{
	"Name": "r1",
	"Faction": "good"
	},
	{
	"Name": "r2",
	"Faction": "bad"
	},
	{
	"Name": "r3",
	"Faction": "good"
	},
	{
	"Name": "r4",
	"Faction": "bad"
	}
]
bots = sorted(robots, key=itemgetter("Faction"))
for key, group in groupby(bots, lambda x: x["Faction"]):
	print(key)
	print(list(group))