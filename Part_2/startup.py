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
		#print(rows)
		#print(rows[0])
		#print(type(rows[0]))
		first_line = rows[0][0].split("，")
		#print(first_line)
		
		rows.remove(rows[0])
		#print(rows)
		rows.sort(key=operator.itemgetter(0))
		#print(rows)

		WB = xlwt.Workbook(encoding = "UTF-8")
		sheet = WB.add_sheet("库存状态")

		style1 = xlwt.XFStyle()
		pattern = xlwt.Pattern()
		pattern.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern.pattern_fore_colour = xlwt.Style.colour_map["green"]
		font = xlwt.Font()
		font.bold = 'on'
		font.height = 260
		style1.pattern = pattern
		style1.font = font

		style2 = xlwt.XFStyle()
		pattern2 = xlwt.Pattern()
		pattern2.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern2.pattern_fore_colour = xlwt.Style.colour_map["yellow"]
		style2.pattern = pattern2

		style3 = xlwt.XFStyle()
		pattern3 = xlwt.Pattern()
		pattern3.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern3.pattern_fore_colour = xlwt.Style.colour_map["red"]
		style3.pattern = pattern3

		i = 0 
		for x in first_line:
			sheet.write(0, i , x, style1)
			i += 1

		i = 1
		for list_1 in rows:
			line_list = list_1[0].split("，")
			print(line_list)
			j = 0
			for y in line_list:
				if line_list[2] == "无货" and j == 1:
					sheet.write(i,j,y,style2)
					j += 1
					continue
				elif len(line_list) < 4 and j == 1:
					sheet.write(i,j,y,style3)
					j += 1
					continue
				else:
					sheet.write(i,j, y)
					j += 1
					continue
			i += 1
		WB.save("Workbook.xls")






if __name__ == '__main__':
	csv_to_xlsx("库存状态.csv")