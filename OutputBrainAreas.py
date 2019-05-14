import nibabel as nib
import numpy as np
import xlsxwriter
import sys

filename = sys.argv[1]
outname = sys.argv[2].replace("/", "-")
outname += ".xlsx"

print outname
workbook = xlsxwriter.Workbook(outname)
worksheet = workbook.add_worksheet()

voxvol = 0.1*0.1*0.1 ##cubic mm

img = nib.load(filename)
roivol = np.array(img.dataobj).flatten()

roistats=np.zeros([117,3])
brvox = 0

for i in range(116):
    mask = roivol == i
    numvox=mask.sum()
#    print("i: {}, numvox {}".format(i, numvox))
    roistats[i,0] = i
    roistats[i,1] = numvox
    roistats[i,2] = numvox*voxvol
    brvox += numvox

brvol=brvox*voxvol

roistats[116,0] = 999
roistats[116,1] = brvox
roistats[116,2] = brvol


col = 0
for row, data in enumerate(roistats):
    worksheet.write_row(row,col,data)

workbook.close()
