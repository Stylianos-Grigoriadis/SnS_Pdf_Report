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
import pandas as pd

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
    ax.set_title(Joint + "\n"+ "\n", fontsize = 30, fontweight='bold')
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
    plt.tight_layout()
    plt.savefig("plot_" + Joint + ".png")

    # Resizing image

    image_hip = Image.open(r"plot_" + Joint + ".png")
    width, height = image_hip.size

    # Setting the points for cropped image
    left = 162
    top = 1
    right = 738
    bottom = height

    im1 = image_hip.crop((left, top, right, bottom))

    #im1.show()
    # plt.show()
    im1.save("plot_" + Joint + "_after_resizing.png")
def Muscle_labels(x_coordinate, y_coordinate, Muscle_name, Left_strength, Right_strength):
    pdf.set_font('Arial', '', 6)
    th = pdf.font_size
    pdf.x = pdf.x + x_coordinate
    pdf.y = pdf.y + y_coordinate
    Muscle_label_table = [[str(Muscle_name)],
                           ['L = ' + str(Left_strength) + 'kg'],
                           ['R = ' + str(Right_strength) + 'kg']
                           ]
    for row in Muscle_label_table:
        for datum in row:
            # Enter data in colums
            # Notice the use of the function str to coerce any input to the
            # string type. This is needed
            # since pyFPDF expects a string, not a number.
            pdf.cell(width / 8, 1.5 * 14, str(datum), border=0, align='L')
            print(pdf.x)
        pdf.ln(th)
        pdf.x = pdf.x + x_coordinate


# Insert the excel with all the info

df = pd.read_excel(r'C:\Stavros & Stylian Corporation\Μετρησείς\Mylonas_Vasilis.xlsx')

width = 210
height = 297

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 15, 'Athletic Repsort', 1,1,'C')
pdf.cell(0, 5, '', 0,1,'C')

pdf.set_font('Arial', '', 16)

Charactiristics_table = [['Name', ':', str(df[2][0]), '', 'Age', ':', str(df[2][5])],
                ['Surname', ':', str(df[2][1]), '', 'Athletic Age', ':', str(df[2][6])],
                ['Date', ':', date.today(), '', 'Sport', ':', str(df[2][7])],
                ['Height', ':', str(df[2][3]), '', 'Injury', '=>', ''],
                ['Weight', ':', str(df[2][4]), '', str(df[2][8]), '', '']
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
pdf.cell(0, 15, 'Force Test', 0,1,'L')

#Call Spider_plot for the hip

# R/L = Hip Ex, Hip Fl, Hip Abd, Hip Add]
R = [df[3][12], df[3][13], df[3][14], df[3][15]]
L = [df[2][12], df[2][13], df[2][14], df[2][15]]
#R = [20, 30, 12, 14]
#L = [22, 27, 14, 14]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Hip')


#print(pdf.x)
#print(pdf.y)
#save the y, x so that you can use it after to place the other diagrams
save_x = pdf.x
save_y = pdf.y
# #Resizing image
#
# image_hip = Image.open(r"plot_Hip.png")
# width, height = image_hip.size
#
# # Setting the points for cropped image
# left = 88
# top = 1
# right = 800
# bottom = height
#
# im1 = image_hip.crop((left, top, right, bottom))
#
# im1.show()

pdf.image("plot_Hip_after_resizing.png",x = pdf.x , y = pdf.y,  w = 55, h = 62.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)

#Call Spider_plot for the knee
#R/L = [Knee Ex, Knee Fl, Knee Fl/ Knee Ex]
R = [df[3][10], df[3][11], df[3][11]/df[3][10]]
L = [df[2][10], df[2][11], df[2][11]/df[2][10]]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,3,'Knee')

pdf.y = save_y
#print(pdf.y)
pdf.x = save_x + 80

pdf.image("plot_Knee_after_resizing.png",x = pdf.x -13, y = pdf.y,  w = 55, h = 62.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)

#Call Spider_plot for the ankle
#R/L = [Ankle D, Ankle P, Ankle In, Ankle Ev]
R = [df[3][16], df[3][17], df[3][18], df[3][19]]
L = [df[2][16], df[2][17], df[2][18], df[2][19]]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Ankle')

pdf.x = save_x + 160
pdf.y = save_y
pdf.image("plot_Ankle_after_resizing.png",x = pdf.x -25, y = pdf.y , w = 55, h = 62.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)

pdf.x = save_x
pdf.y = save_y + 65

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
th = pdf.font_size

for row in Jumps_table:
    for datu in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(width/7,th, str(datu), border=0)
    pdf.ln(1.5*th)

save_y_2 = pdf.y
pdf.y = save_y
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

pdf.cell(0, 5, '', 0,1,'C')

#Physical Observation

pdf.y = save_y_2
pdf.x = save_x_2

pdf.set_font('Arial', 'BUI', 18)
pdf.cell(0, 15, 'Physical Observation', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')

pdfy3 = pdf.y
pdfx3 = pdf.x
#Muscle_labels(x_coordinate,y_coordinate,Muscle_name,Left_strength,Right_strength)
Muscle_labels(12,-166,'Extension',df[2][12],df[3][12])
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(75,-165,'Extension',df[2][10],df[3][10])




























pdf.output('Report_3.pdf', 'F')
webbrowser.open_new('Report_3.pdf')
