#!/usr/bin/python3
# -*- coding:UTF-8 -*-
#
# Writer: zhaiazh
# Date: 2018/11/8
#

import csv

with open("test.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)

    rows = [row for row in reader]


print(rows)
