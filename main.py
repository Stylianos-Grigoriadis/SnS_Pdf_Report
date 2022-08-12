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

def Muscle_labels(x_coordinate, y_coordinate, Muscle_name, Left_strength, Right_strength):
    pdf.set_font('Arial', '', 6)
    th = pdf.font_size
    print(pdf.font_size)
    print(th)
    print(pdf.y)
    pdf.x = x_coordinate
    pdf.y = y_coordinate
    Muscle_label_table = [str(Muscle_name),
                           'L = ' + str(Left_strength) + 'kg',
                           'R = ' + str(Right_strength) + 'kg'
                           ]
    for row in Muscle_label_table:
        pdf.ln(th)
        pdf.cell(width / 8, 21, str(row), border=0, align='L')

        pdf.x = x_coordinate


width = 210
height = 297

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 26)

pdf.set_x(10)
pdf.set_y(10)
#pdf.x = 1
#pdf.y = 101
print(pdf.y)
pdf.cell(0, 5, 'O', 0,1,'L')
print(pdf.y)
pdf.set_x(10)
pdf.set_y(50)
#pdf.x = 1
#pdf.y = 101
pdfx3 = pdf.x
pdfy3 = pdf.y
#print(pdf.x)
print(pdf.y)
#Hip extension
# HIP = 'Extension \n L = ' + str(df[2][12]) + 'kg \n' + 'R = ' + str(df[3][12]) + 'kg'
# pdf.cell(0, 0, HIP, 0,1,'L')

Muscle_labels(pdf.x + 10 ,pdf.y,'Extension',1,12)


















































































































pdf.output('Test.pdf', 'F')
webbrowser.open_new('Test.pdf')


