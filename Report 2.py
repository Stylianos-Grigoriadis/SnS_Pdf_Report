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

    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw={"projection": "polar"})
    # fig,ax = plt.subplots()


    fig.patch.set_facecolor("white")
    ax.set_facecolor("black")
    ax.set_title(Joint + "\n", fontsize = 30, fontweight='bold')
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
    ax.bar(ANGLESR, dataR, color="#f40800", alpha=0.9, width=0.45, zorder=10, label='Right')
    ax.bar(ANGLESL, dataL, color="#7a7a7a", alpha=0.9, width=0.45, zorder=10, label='Left')
    if Joint == 'Ankle':
        plt.legend(loc='upper left', bbox_to_anchor=(0.8, 1.10),
        ncol=1, fancybox=True, shadow=True, prop={'size': 14})
    # plt.tight_layout()
    plt.savefig("plot_" + Joint + ".png")
    # plt.show()

width = 210
height = 297

pdf = FPDF()
pdf.add_page()


pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 15, 'Athletic Report', 1,1,'C')
pdf.cell(0, 5, '', 0,1,'C')


pdf.set_font('Arial', '', 16)

Charactiristics_table = [['Name', ':', 'Stylianos', '', 'Age', ':', '26'],
                ['Surname', ':', 'Grigoriadis', '', 'Athletic Age', ':', '22'],
                ['Date', ':', date.today(), '', 'Sport', ':', 'Football'],
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
        pdf.cell(width/8,1.5 * 14, str(datum), border= 0, align = str(align))
    pdf.ln(1.5 * th)

pdf.cell(0, 5, '', 0,1,'C')
pdf.cell(0, 5, '', 0,1,'C')
#Start the writting of Force and RoM
pdf.set_font('Arial', 'BUI', 18)
pdf.cell(0, 15, 'Force and Range of Motion', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')


#Call Spider_plot for the hip
R = [20, 30, 12, 14]
L = [22, 27, 14, 14]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Hip')


print(pdf.x)
print(pdf.y)
#save the y, x so that you can use it after to place the other diagrams
save_x = pdf.x
save_y = pdf.y

pdf.image("plot_Hip.png",x = pdf.x -26, y = pdf.y,  w = 90, h = 67.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)




#Call Spider_plot for the knee
R = [30, 20, 30/20]
L = [28, 15, 28/15]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,3,'Knee')

pdf.y = save_y
print(pdf.y)
pdf.x = save_x + 80

pdf.image("plot_Knee.png",x = pdf.x -32, y = pdf.y,  w = 90, h = 67.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)



#save the y, x so that you can use it after to place the other diagrams


print(pdf.x)
print(pdf.y)
#Call Spider_plot for the ankle

R = [30, 20, 12, 14]
L = [28, 15, 15, 18]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Ankle')


print(pdf.y)
pdf.x = save_x + 160
pdf.y = save_y
pdf.image("plot_Ankle.png",x = pdf.x -38, y = pdf.y , w = 90, h = 67.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)

pdf.x = save_x
print(pdf.y)
print(pdf.x)

pdf.y = save_y + 65
# Start the writting of jumps and Yoyo test

pdf.set_font('Arial', 'BUI', 18)
pdf.cell(0, 15, 'Jumps and YoYo test', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')

pdf.set_font('Arial', '', 16)
Jumps_table = [['Elastic index','',':',  '10'],
        ['', '','','', ''],
        ['Use of arms','',':', '10'],
        ['', '', ''],
        ['Reflective Power index','',':', '10'],
        ['', '', ''],
        ['YoYo test score', '',':','14']
        ]
save_y = pdf.y
print(pdf.y)
th = pdf.font_size

for row in Jumps_table:
    for datu in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/7,th, str(datu), border=0)
    pdf.ln(1.5*th)

print(pdf.x)
print(pdf.y)
save_y_2 = pdf.y
pdf.y = save_y
print(pdf.y)
save_x_2 = pdf.x
pdf.x = pdf.x +100

data = {'Squat Jump': 20, 'Counter-Movement\nJump        ': 25, 'Counter-Movement\nJump with Hands': 30,
        'Drop Jump': 22}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 7))

# creating the bar plot
plt.bar(courses, values, color='#f40800',
        width=0.4)
y = list(range(1, 50, 5))

plt.ylabel("Height (cm)",fontsize=20)
plt.title("Maximum Height in different Jumps",fontsize=30)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20, rotation=45,ha='center')
plt.tight_layout()
plt.savefig("plot.png")
# plt.show()



pdf.image("plot.png",x = pdf.x , y = pdf.y, w = 100, h = 60, type = 'PNG', link = '')

print(pdf.y)
print(pdf.x)
pdf.cell(0, 5, '', 0,1,'C')
#Physical Observation

pdf.y = save_y_2
pdf.x = save_x_2

pdf.set_font('Arial', 'BUI', 18)
pdf.cell(0, 15, 'Physical Observation', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')





















pdf.output('Report_2.pdf', 'F')
webbrowser.open_new('Report_2.pdf')




















































