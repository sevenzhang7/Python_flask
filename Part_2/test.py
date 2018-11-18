#i/usr/bin/python3
#_*_ conding "UTF-8" _*_
# Date: 2018-11-18
# author Haichao Yang

import csv
import xlwt
import operator

def csv_to_xlsx(csvfile):
	with open(csvfile,"r",encoding="UTF-8") as file:
		read_csv = csv.reader(file)
		rows = [row for row in read_csv if len(row) > 0]
		print(rows)
		print(rows[0])
		#print(type(rows[0]))
		first_line = rows[0][0].split("，")
		print(first_line)
		
		rows.remove(rows[0])
		print(rows)
		rows.sort(key=operator.itemgetter(0))
		print(rows)

		WB = xlwt.Workbook(encoding = "UTF-8")
		sheet = WB.add_sheet("库存状态")

        head_style = xlwt.XFStyle()
        pattern = xlwt.pattern()
        pattern.pattern = xlwt.pattern.SOLID_PATIERN
        pattern.pattern_fore_colour = xlwt.Style.colour_map['blue']
        font = xlwt.Font()
        font.bold = True
        head_style.font = font

        Style2 = xlwt.XFStyle()
        pattern2 = xlwt.pattern()
        pattern2.pattern = xlwt.pattern.SOLID_PATIERN
        pattern2.pattern_fore_colour = xlwt.Style.colour_map['yellow']
        Style2.pattern = pattern2

        Style3 = xlwt.XFStyle()
        pattern3 = xlwt.pattern()
        pattern3.pattern = xlwt.pattern.SOLID_PATIERN
        pattern3.pattern_fore_colour = xlwt.Style.colour_map['red']
        Style3.pattern = pattern3

        i = 0
        for x in first_line:
        	sheet.write(0, i, x, head_style)
        	i += 1
  






if __name__ == '__main__':
	csv_to_xlsx("库存状态.csv")