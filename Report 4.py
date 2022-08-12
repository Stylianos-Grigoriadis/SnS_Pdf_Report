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
    print(pdf.y)
    pdf.x = x_coordinate
    pdf.y = y_coordinate
    Muscle_label_table = [str(Muscle_name),
                           'L = ' + str(Left_strength) + 'kg',
                           'R = ' + str(Right_strength) + 'kg'
                           ]
    for row in Muscle_label_table:
        pdf.cell(width / 8, 1.5 * 14, str(row), border=0, align='L')
        #for datum in row:
            # Enter data in colums
            # Notice the use of the function str to coerce any input to the
            # string type. This is needed
            # since pyFPDF expects a string, not a number.
            #pdf.cell(width / 8, 1.5 * 14, str(datum), border=0, align='L')
            # print(pdf.x)
        pdf.ln(th)
        pdf.x = x_coordinate


# Insert the excel with all the info

df = pd.read_excel(r'D:\Stavros & Stylian Corporation\Μετρησείς\Mylonas_Vasilis.xlsx')

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

#Start the writting of Force
pdf.set_font('Arial', 'BUI', 18)
pdf.cell(0, 15, 'Force Tests', 0,1,'L')

#Call Spider_plot for the hip
# R/L = [δεξια, πανω, αριστερα, κατω ]
# R/L = [Hip Abd, Hip Ex, Hip Add, Hip Fl]
R = [df[3][15], df[3][13], df[3][16],df[3][14]]
L = [df[2][15], df[2][13], df[2][16],df[2][14]]

R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Hip')

save_x = pdf.x
save_y = pdf.y

pdf.image("plot_Hip_after_resizing.png",x = pdf.x , y = pdf.y,  w = 55, h = 62.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)

#Call Spider_plot for the knee
#R/L = [Knee Ex, Knee Fl, Knee Fl/ Knee Ex]
R = [round(df[3][12],2), df[3][10], df[3][11]]
L = [round(df[2][12],2), df[2][10], df[2][11]]

R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,3,'Knee')

pdf.y = save_y
pdf.x = save_x + 80

pdf.image("plot_Knee_after_resizing.png",x = pdf.x -13, y = pdf.y,  w = 55, h = 62.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)

#Call Spider_plot for the ankle
#R/L = [Ankle P, Ankle D, Ankle In, Ankle Ev]
R = [df[3][20], df[3][18], df[3][19], df[3][17]]
L = [df[2][20], df[2][18], df[2][19], df[2][17]]

R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Ankle')

pdf.x = save_x + 160
pdf.y = save_y
pdf.image("plot_Ankle_after_resizing.png",x = pdf.x -25, y = pdf.y , w = 55, h = 62.5, type = 'PNG', link = '')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 5, '', 0,1,'C')
#Write spider plots labels
#Muscle_labels(x_coordinate,y_coordinate,Muscle_name,Left_strength,Right_strength)
#Hip Labels
pdf.x = 1
pdf.y = 101

pdfx3 = pdf.x
pdfy3 = pdf.y

#Hip Extension
pdf.x = pdfx3
pdf.y = pdfy3
Muscle_labels(pdf.x + 30 ,pdf.y - 12,'Extension',df[2][13],df[3][13])
#Hip Flexion
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 30,pdf.y + 43,'Flexion',df[2][14],df[3][14])
#Hip Adduction
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x,pdf.y + 15,'Adduction',df[2][16],df[3][16])

#Hip Abduction
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 62,pdf.y + 15,'Abduction',df[2][15],df[3][15])
#Knee Extension
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 83,pdf.y - 10,'Extension',df[2][10],df[3][10])
#Knee Flexion
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 83,pdf.y + 40 ,'Flexion',df[2][11],df[3][11])

#Knee Fl/Ex
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 128,pdf.y + 8 ,'Fl/Ex',round(df[2][12],2),round(df[3][12],2))

#Ankle Plantar Fl
pdf.x = pdfx3
pdf.y = pdfy3
Muscle_labels(pdf.x + 165 ,pdf.y - 12,'Plantar Fl',df[2][18],df[3][18])

#Ankle Dorsi Fl
pdf.x = pdfx3
pdf.y = pdfy3
Muscle_labels(pdf.x + 165 ,pdf.y + 43,'Dorsi Fl',df[2][17],df[3][17])

#Ankle Inversion
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 135,pdf.y + 17 ,'Inversion',df[2][19],df[3][19])

#Ankle Eversion
pdf.y = pdfy3
pdf.x = pdfx3
Muscle_labels(pdf.x + 196,pdf.y + 15,'Eversion',df[2][20],df[3][20])


#Start writing the Jumps and YoYo Test
pdf.x = save_x
pdf.y = save_y + 65

pdf.set_font('Arial', 'BUI', 18)
pdf.cell(0, 15, 'Jumps and YoYo test', 0,1,'L')
pdf.cell(0, 5, '', 0,1,'C')

pdf.set_font('Arial', '', 16)
#Elastic_index = ((CMJ - SJ)/SJ)*100
#Use_of_arms_index = ((CMJ_with_hands - CMJ)/CMJ)*100
#Reflective_power_index = ((TF - TC)/TC)*100
Elastic_index = round(((df[2][22] - df[2][21])/df[2][21])*100,2)
Use_of_arms_index = round(((df[2][23] - df[2][22])/df[2][22])*100,2)
Reflective_power_index = round(((df[2][25] - df[2][26])/df[2][26])*100,2)
Jumps_table = [['Elastic index','',':\t\t\t\t\t\t' + str(Elastic_index)],
        ['', '','','', ''],
        ['Use of arms','',':\t\t\t\t\t\t' + str(Use_of_arms_index)],
        ['', '', ''],
        ['Reflective Power index','',':\t\t\t\t\t\t' + str(Reflective_power_index)],
        ['', '', ''],
        ['YoYo test score', '',':\t\t\t\t\t\t' + str(df[2][27])]
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

data = {'Squat Jump': df[2][21], 'Counter-Movement\nJump        ': df[2][22], 'Counter-Movement\nJump with Hands': df[2][23],
        'Drop Jump': df[2][24]}
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
pdf.set_line_width(1.5)
with pdf.local_context(fill_opacity=0.25):
    # Insert an image:
    pdf.image("D:\Stavros & Stylian Corporation\Report\photos\ootballpitch2.png", x=0, y=0, w=width, h=height)





























pdf.output('Report_5.pdf', 'F')
webbrowser.open_new('Report_5.pdf')
