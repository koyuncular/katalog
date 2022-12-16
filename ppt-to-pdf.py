import comtypes.client
import os

def ppt_to_pdf(input_path, output_path):
    # Open the PowerPoint file
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    presentation = powerpoint.Presentations.Open(input_path)
    
    # Save the PowerPoint file as a PDF
    presentation.SaveAs(output_path, 32)
    
    # Close the PowerPoint file and quit the application
    presentation.Close()
    powerpoint.Quit()

# Convert the PowerPoint file to a PDF
input_path = r"C:\Users\user\Desktop\DENEME\input.pptx"
output_path = r"C:\Users\user\Desktop\DENEME\output.pdf"
ppt_to_pdf(input_path, output_path)
