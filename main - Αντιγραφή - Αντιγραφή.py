from fpdf import FPDF
import webbrowser
pdf = FPDF()
pdf.set_font("Helvetica", "B", 24)
pdf.set_line_width(1.5)
pdf.add_page()

with pdf.local_context(fill_opacity=0.25):
    # Insert an image:
    pdf.image("D:\Stavros & Stylian Corporation\Report\plot_Ankle_after_resizing.png", x = 10, y = 100, h = 50 )


# Print some text with full opacity:

# Produce the resulting PDF:
pdf.output("transparency.pdf")
webbrowser.open_new('transparency.pdf')