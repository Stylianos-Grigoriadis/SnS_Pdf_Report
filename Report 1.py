from fpdf import FPDF
import webbrowser
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from PIL import Image


# #Start with the Athlete's characteristics
# First_Column =  'Name'+"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': Stylianos' + "\n"
# First_Column += 'Surname'+"\t" +"\t" +"\t" +': Grigoriadis' + "\n"
# First_Column += 'Date'+"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 24/8/22' + "\n"
# First_Column += 'Height' +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 184' + "\n"
# First_Column += 'Weight'+"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 104'
# Right_Column = 'Age' + "\t" + "\t" + "\t" + "\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': 22' + "\n"
# Right_Column +='Athletic Age' + "\t" + "\t" + "\t" + "\t" + ': 10' + "\n"
# Right_Column +='Sport'+ "\t" + "\t" + "\t" + "\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': Football' + "\n"
# Right_Column +='Injury' + "\t" + "\t" + "\t" + "\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +"\t" +': Ankle Sping'

#write the width and the height which may be usefull
width = 210
height = 297

#Start the pdf document
pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 15, 'Athletic Report', 1,1,'C')
pdf.cell(0, 5, '', 0,1,'C')

#Start the writting of Athlets characteristics
pdf.set_font('Arial', '', 16)

Charactiristics_table = [['Name', ':', 'Stylianos', '', 'Age', ':', '26'],
                ['Surname', ':', 'Grigoriadis', '', 'Athletic Age', ':', '22'],
                ['Date', ':', '24/8/22', '', 'Sport', ':', 'Football'],
                ['Height', ':', '184', '', 'Injury', '=>', ''],
                ['Weight', ':', '104', '', 'Both Legs Ankle Spring', '', '']
                ]
pdf.set_font('Arial', '', 14)
list_for_alingnment_in_charactiristics_table = ['L','C','L','L','L','C','L','L','C','L','L','L','C','L','L','C','L','L','L','C','L','L','C','L','L','L','C','L','L','C','L','L','L','C','L',]

th = pdf.font_size

for row in Charactiristics_table:
    for datum,align in zip(row, list_for_alingnment_in_charactiristics_table):
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/8,1.5 * th, str(datum), border= 0, align = str(align))

    pdf.ln(1.5*th)

#Start the writting of Force and RoM
pdf.set_font('Arial', 'BUI', 26)
pdf.cell(0, 15, 'Force and Range of Motion', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')

force_table = [['', 'Hip', '', 'Knee', '', 'Ankle'],
        ['Glutes', '10', 'H/Q', '1', 'T/C', '1'],
        ['Iliopsos', '10', 'H', '10', 'Calf', '10'],
        ['Abductors', '10', 'Q', '10', 'T.A.', '10'],
        ['Adductors', '10', '', '', 'InV', '10'],
        ['', '', '', '', 'EV', '10'],
        ['', '', '', '', 'P RoM', '10', ],
        ['', '', '', '','D RoM', '10']
        ]

pdf.set_font('Arial', '', 16)
list_for_alingnment_in_force_table = ['C','C','C','C','C','C',
                                    'L','C','L','C','L','C',
                                    'L','C','L','C','L','C',
                                      'L','C','L','C','L','C',
                                      'L','C','L','C','L','C',
                                      'L','C','L','C','L','C',
                                      'L','C','L','C','L','C',
                                      'L','C','L','C','L','C',]

th = pdf.font_size

for row in force_table:
    for datum,align in zip(row, list_for_alingnment_in_force_table):
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/6.7,1.5* th, str(datum), border=0, align = str(align))

    pdf.ln(1.5 * th)

#Start the writting of jumps and Yoyo test
pdf.set_font('Arial', 'BUI', 26)
pdf.cell(0, 15, 'Jumps and YoYo test', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')

top = pdf.y

pdf.set_font('Arial', '', 16)
Jumps_table = [['Elastic index','',':',  '10'],
        ['', '','','', ''],
        ['Use of arms','',':', '10'],
        ['', '', ''],
        ['Reflective Power index','',':', '10']
        ]

th = pdf.font_size

for row in Jumps_table:
    for datu in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/7,1.5* th, str(datu), border=0)

    pdf.ln(1.5*th)
print(pdf.x)
offset = pdf.x + 120
pdf.x = offset
print(pdf.y)
pdf.y = top
print(pdf.y)
print(pdf.x)


data = {'Squat': 20, 'Counter-Movement': 25, 'Counter-Movement with Hands': 30,
        'Drop': 22}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='maroon',
        width=0.4)
y = list(range(1, 50, 5))
plt.xlabel("Jumps")
plt.ylabel("Height (cm)")
plt.title("Max Height in different Jumps")
plt.yticks(fontsize=20)
plt.savefig("plot.png")
plt.show()



pdf.image("plot.png",x = pdf.x -20, y = pdf.y, w = 100, h = 40, type = 'PNG', link = '')










pdf.output('Report 1.pdf', 'F')
webbrowser.open_new('Report 1.pdf')

























