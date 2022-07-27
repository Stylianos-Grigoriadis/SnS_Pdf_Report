from fpdf import FPDF
import webbrowser
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



#print("Write the name of the athlete")
#name = input()
First_Column =  'Name'+"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': Stylianos' + "\n"
First_Column += 'Surname'+"\t" +"\t" +"\t" +': Grigoriadis' + "\n"
First_Column += 'Date'+"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 24/8/22' + "\n"
First_Column += 'Height' +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 184' + "\n"
First_Column += 'Weight'+"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 104'
Right_Column = 'Age' + "\t" + "\t" + "\t" + "\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 22' + "\n"
Right_Column +='Athletic Age' + "\t" + "\t" + "\t" + "\t" + ': 10' + "\n"
Right_Column +='Sport'+ "\t" + "\t" + "\t" + "\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': Football' + "\n"
Right_Column +='Injury' + "\t" + "\t" + "\t" + "\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': Ankle Sping'

print(First_Column)
width = 210
height = 297
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 20)


#pdf.cell(40, 30, f'My name is {name} ')
pdf.cell(0, 15, 'Athletic Report', 1,1,'C')
pdf.set_font('Arial', '', 16)
# Save top coordinate
top = pdf.y

# Calculate x position of next cell
offset = pdf.x + 110
pdf.multi_cell(70, 9, First_Column, 0,0,'L')
# Reset y coordinate
pdf.y = top

# Move to computed offset
pdf.x = offset
pdf.multi_cell(0, 9, Right_Column,0,0,'R')
#pdf.cell(40, 9, 'Age: 22', 0,1,'R')
# pdf.cell(40, 9, 'Athletic Age   : 24/8/22', 0,1,'R')
# pdf.cell(40, 9, 'Injury  : 184', 0,1,'R')

# pdf.cell(100, 10, 'ATHLETIC REPORT')
# pdf.cell(40, 250, 'Name:              Stylianos')
# pdf.cell(40, 270, 'Surname:Grigoriadis')
#pdf.image(name="D:\Stavros & Stylian Corporation\Report\photos\Kinvent.png", x = 155, y = 5, w = 50, h = 50, type = "PNG" )
#fpdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')



pdf.set_font('Arial', 'BIU', 16)
pdf.cell(0, 15, '', 0,1,'L')
pdf.cell(0, 15, 'Force Test ', 1,1,'L')
pdf.cell(0, 9, '', 0,1,'L')
force_table = [['', 'Hip', '', 'Knee', '', 'Ankle'],
        ['Glutes', '10', 'H/Q', '1', 'T/C', '1'],
        ['Iliopsos', '10', 'H', '10', 'Calf', '10'],
        ['Abductors', '10', 'Q', '10', 'T.A.', '10'],
        ['Adductors', '10', '', '', 'InV', '10'],
        ['', '', '', '', 'EV', '10'],
        ['', '', '', '', 'P RoM', '10', ],
        ['', '', '', '','D RoM', '10']
        ]


pdf.set_font('Arial', '', 14)
pdf.ln(0.5)

th = pdf.font_size

for row in force_table:
    for datum in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/6,1.5* th, str(datum), border=0)

    pdf.ln(1.5*th)



pdf.cell(0, 9, '', 0,1,'L')
pdf.y = top

# Move to computed offset
pdf.x = offset
pdf.set_font('Arial', 'BIU', 16)
pdf.cell(0, 15, 'Jump Results', 1,1,'L')
pdf.cell(0, 9, '', 0,1,'L')

Jumps_table = [['Elastic index','',':',  '10'],
        ['', '','','', ''],
        ['Use of arms','',':', '10'],
        ['', '', ''],
        ['Reflective Power index','',':', '10']
        ]
pdf.set_font('Arial', '', 14)
pdf.ln(0.5)

th = pdf.font_size

for row in Jumps_table:
    for datu in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/8,1.5* th, str(datu), border=0)

    pdf.ln(1.5*th)

# ax = plt.subplot (211)
# plt.title("Jump Height")
# plt.xlabel("Jump Name")
# plt.ylabel("Height (cm)")
#
# ticks = 4.0
pdf.y = top

# Move to computed offset
pdf.x = offset
# pdf.multi_cell(0, 9, Right_Column,0,0,'R')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Jumps = ['Squat Jump', 'CounterMovment', 'CounterMovement with Hands', 'Drop']
Height_score = [23,32,35,29]
ax.set_ylabel('Height')
ax.set_title('Score of the Jumps')
ax.bar(Jumps,Height_score,color = 'r',width = 0.5)
plt.savefig("plot.png")
pdf.image("plot.png",x = 0, y = 10, w = 10, h = 10, type = 'PNG', link = '')

pdf.output('Athletic Report.pdf', 'F')
webbrowser.open_new('Athletic Report.pdf')