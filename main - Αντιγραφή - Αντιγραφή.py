import matplotlib.pyplot as plt
import math
from datetime import date



def Spider_plot(dataL, dataR, DaL,DaR, Number_of_Variables_PLotted, Joint):
    # ANGLESL = np.linspace(0.05, 2 * np.pi - 0.05, 4, endpoint=False)
    # ANGLESR = np.linspace(0.05,  np.pi - 0.05, 4, endpoint=False)

    ANGLESL = [i * math.radians(360/Number_of_Variables_PLotted) - 0.25 for i in range(Number_of_Variables_PLotted)]
    ANGLESR = [i * math.radians(360/Number_of_Variables_PLotted) + 0.25 for i in range(Number_of_Variables_PLotted)]

    # ANGLESL = np.linspace(0.05, 2 * np.pi + 0.5, 4, endpoint=False)
    # ANGLESR = np.linspace(0.05, 2 * np.pi - 0.5, 4, endpoint=False)
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

    # XTICKS = ax.xaxis.get_major_ticks()
    # for tick in XTICKS:
    #     tick.set_pad(10)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_title(Joint + "\n", fontsize = 30, fontweight='bold')
    #ax.set_title('2022-6-30')
    # ax.set_theta_offset(1.2 * np.pi / 2)
    # ax.set_ylim(-1500, 3500)
    xTicks_names = ['Glutes\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[0], 1), R=round(DaR[0], 1), c='Kg'),
                    'Iliopsoas\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[1], 1), R=round(DaR[1], 1), c='Kg'),
                    'Abductors\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[2], 1), R=round(DaR[2], 1), c='Kg'),
                    'Adductors\nL:{L}{c}\nR:{R}{c}'.format(L=round(DaL[3], 1), R=round(DaR[3], 1), c='Kg')]
    xTicks = [i * math.radians(360/Number_of_Variables_PLotted) for i in range(4)]
    plt.xticks(ticks=xTicks, labels=xTicks_names)
    ax.bar(ANGLESR, dataR, color="#6C5B7B", alpha=0.9, width=0.45, zorder=10, label='Right')
    ax.bar(ANGLESL, dataL, color="#F8B195", alpha=0.9, width=0.45, zorder=10, label='Left')
    plt.legend(loc='upper left', bbox_to_anchor=(0.8, 1.10),
          ncol=1, fancybox=True, shadow=True, prop={'size': 14})
    # plt.tight_layout()
    plt.show()

R = [20, 30, 12, 14]
L = [22, 27, 14, 14]
R_perc = [r/(l+r)*100 for r,l in zip(R,L)]
L_perc = [l/(l+r)*100 for r,l in zip(R,L)]
Data_to_annotate_L= L
Data_to_annotate_R= R
Spider_plot(L_perc,R_perc,Data_to_annotate_L,Data_to_annotate_R,4,'Hip')


