from fpdf import FPDF
import webbrowser
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os
import math
from datetime import date
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
#
# force_table = [['', 'Hip', '', 'Knee', '', 'Ankle'],
#         ['Glutes', '10', 'H/Q', '1', 'T/C', '1'],
#         ['Iliopsos', '10', 'H', '10', 'Calf', '10'],
#         ['Abductors', '10', 'Q', '10', 'T.A.', '10'],
#         ['Adductors', '10', '', '', 'InV', '10'],
#         ['', '', '', '', 'EV', '10'],
#         ['', '', '', '', 'P RoM', '10', ],
#         ['', '', '', '','D RoM', '10']
#         ]
#
# pdf.set_font('Arial', '', 16)
# list_for_alingnment_in_force_table = ['C','C','C','C','C','C',
#                                     'L','C','L','C','L','C',
#                                     'L','C','L','C','L','C',
#                                       'L','C','L','C','L','C',
#                                       'L','C','L','C','L','C',
#                                       'L','C','L','C','L','C',
#                                       'L','C','L','C','L','C',
#                                       'L','C','L','C','L','C',]
#
# th = pdf.font_size
#
# for row in force_table:
#     for datum,align in zip(row, list_for_alingnment_in_force_table):
#         # Enter data in colums
#         # Notice the use of the function str to coerce any input to the
#         # string type. This is needed
#         # since pyFPDF expects a string, not a number.
#         pdf.cell(width/6.7,1.5* th, str(datum), border=0, align = str(align))
#
#     pdf.ln(1.5 * th)
def Spider_plot(dataL, dataR, DaL,DaR, Number_of_Variables_PLotted, Joint):

    ANGLESL = [i * math.radians(360/Number_of_Variables_PLotted) - 0.25 for i in range(Number_of_Variables_PLotted)]
    ANGLESR = [i * math.radians(360/Number_of_Variables_PLotted) + 0.25 for i in range(Number_of_Variables_PLotted)]

    GREY12 = "#1f1f1f"

    # Set default font to Bell MT
    plt.rcParams.update({"font.family": "Bell MT"})
    plt.rcParams.update({"font.size": 16})

    # Set default font color to GREY12
    plt.rcParams["text.color"] = GREY12

    # The minus glyph is not available in Bell MT
    # This disables it, and uses a hyphen
    plt.rc("axes", unicode_minus=False)

    # Colors
    COLORS = ["#6C5B7B", "#C06C84", "#F67280", "#F8B195"]
    today = date.today()

    fig, ax = plt.subplots(figsize=(9
                                    , 7), subplot_kw={"projection": "polar"})
    # fig,ax = plt.subplots()


    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    # ax.set_title(Joint + "\n", fontsize = 30, fontweight='bold')
    if Number_of_Variables_PLotted == 4:
        xTicks_names = ['Glutes\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[0], 1), R=round(DaR[0], 1), c='Kg'),
                        'Iliopsoas\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[1], 1), R=round(DaR[1], 1), c='Kg'),
                        'Abductors\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[2], 1), R=round(DaR[2], 1), c='Kg'),
                        'Adductors\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[3], 1), R=round(DaR[3], 1), c='Kg')]
    elif Number_of_Variables_PLotted == 6:
        xTicks_names = ['Calf\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[0], 1), R=round(DaR[0], 1), c='Kg'),
                        'Tibialis Anterior\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[1], 1), R=round(DaR[1], 1), c='Kg'),
                        'Inversion\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[2], 1), R=round(DaR[2], 1), c='Kg'),
                        'Eversion\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[3], 1), R=round(DaR[3], 1), c='Kg'),
                        'Plantar Flexion RoM\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[3], 1), R=round(DaR[3], 1), c='Kg'),
                        'Dorsi Flexion RoM\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[3], 1), R=round(DaR[3], 1), c='Kg')]
    xTicks = [i * math.radians(360/Number_of_Variables_PLotted) for i in range(Number_of_Variables_PLotted)]
    plt.xticks(ticks=xTicks, labels='')
    ax.bar(ANGLESR, dataR, color="#6C5B7B", alpha=0.9, width=0.45, zorder=10, label='Right')
    ax.bar(ANGLESL, dataL, color="#F8B195", alpha=0.9, width=0.45, zorder=10, label='Left')
    plt.legend(loc='upper left', bbox_to_anchor=(0.8, 1.10),
          ncol=1, fancybox=True, shadow=True, prop={'size': 14})
    plt.tight_layout()
    plt.savefig("plot_" + Joint + ".png")
    # plt.show()


#Call Spider_plot for the hip

R = [20, 30, 12, 14]
L = [22, 27, 14, 14]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Hip')




#Put it on the report



pdf.image("plot_Hip.png",x = pdf.x -20, y = pdf.y, w = 110, h = 75, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)
print(pdf.lasth)
pdf.cell(6,100, 'Glutes', 0,1,'L')
pdf.cell(6,1, 'L = 22', 0,1,'L')
pdf.cell(6,1, 'R = 20', 0,1,'L')

# pdf.cell(h = pdf.y , txt ="Glutes")
# pdf.cell(h = pdf.y , txt ="L = 22")
# pdf.cell(h = pdf.y , txt ="R = 20")


#Start the writting of jumps and Yoyo test
# pdf.set_font('Arial', 'BUI', 26)
# pdf.cell(0, 15, 'Jumps and YoYo test', 0,1,'L')
# pdf.cell(0, 5, '', 0,1,'C')
#
# top = pdf.y
#
# pdf.set_font('Arial', '', 16)
# Jumps_table = [['Elastic index','',':',  '10'],
#         ['', '','','', ''],
#         ['Use of arms','',':', '10'],
#         ['', '', ''],
#         ['Reflective Power index','',':', '10'],
#         ['', '', ''],
#         ['YoYo test score', '',':','14']
#         ]
#
# th = pdf.font_size
#
# for row in Jumps_table:
#     for datu in row:
#         # Enter data in colums
#         # Notice the use of the function str to coerce any input to the
#         # string type. This is needed
#         # since pyFPDF expects a string, not a number.
#         pdf.cell(width/7,th, str(datu), border=0)
#
#     pdf.ln(1.5*th)
# print(pdf.x)
# offset = pdf.x + 120
# pdf.x = offset
# print(pdf.y)
# pdf.y = top
# print(pdf.y)
# print(pdf.x)
#
#
# data = {'Squat Jump': 20, 'Counter-Movement\nJump        ': 25, 'Counter-Movement\nJump with Hands': 30,
#         'Drop Jump': 22}
# courses = list(data.keys())
# values = list(data.values())
#
# fig = plt.figure(figsize=(10, 7))
#
# # creating the bar plot
# plt.bar(courses, values, color='maroon',
#         width=0.4)
# y = list(range(1, 50, 5))
#
# plt.ylabel("Height (cm)",fontsize=20)
# plt.title("Maximum Height in different Jumps",fontsize=30)
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=20, rotation=45,ha='right')
# plt.tight_layout()
# plt.savefig("plot.png")
# # plt.show()
#
#
#
# pdf.image("plot.png",x = pdf.x -20, y = pdf.y, w = 100, h = 60, type = 'PNG', link = '')
#
#
#
#
#
#
#
#
#

pdf.output('Report_1.pdf', 'F')
webbrowser.open_new('Report_1.pdf')

























