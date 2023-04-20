metadata= {'protocolName': 'Pipette cleaning',
'author':'John Bryant <jbryant2@vt.edu>',
'description':'Pipette cleaning for DNA removal',
'apiLevel':'2.2'
}
from opentrons import protocol_api
from opentrons import simulate
#protocol = simulate.get_protocol_api('2.2')

import pandas
import numpy as np
import os
#import tkinter as tk

#from tkinter import * 
#window = Tk()
#window.geometry("400x100")
# window.title("Tip well count")

# entry = Entry(window)
# entry.pack()

# def confirm():
#     label = Label(window,text = entry.get())
#     label.pack()
#     global Wellcount
#     Wellcount = entry.get()

#     window.destroy()
# button = Button(window,text="Enter number of pipette boxes to clean, from 1 to 4",command = confirm)
# button.pack()
# window.mainloop()

# Wellcount = int(Wellcount)
Wellcount=1
id2well = {}
id2well[0] = 'A1'
id2well[1] = 'A2'
id2well[2] = 'A3'
id2well[3] = 'A4'
id2well[4] = 'A5'
id2well[5] = 'A6'
id2well[6] = 'A7'
id2well[7] = 'A8'
id2well[8] = 'A9'
# id2well[9] = 'A10'
# id2well[10] = 'A11'
# id2well[11] = 'A12'
id2well[9] = 'B1'
id2well[10] = 'B2'
id2well[11] = 'B3'
id2well[12] = 'B4'
id2well[13] = 'B5'
id2well[14] = 'B6'
id2well[15] = 'B7'
id2well[16] = 'B8'
id2well[17] = 'B9'
# id2well[21] = 'B10'
# id2well[22] = 'B11'
# id2well[23] = 'B12'
id2well[18] = 'C1'
id2well[19] = 'C2'
id2well[20] = 'C3'
id2well[21] = 'C4'
id2well[22] = 'C5'
id2well[23] = 'C6'
id2well[24] = 'C7'
id2well[25] = 'C8'
id2well[26] = 'C9'
# id2well[33] = 'C10'
# id2well[34] = 'C11'
# id2well[35] = 'C12'
id2well[27] = 'D1'
id2well[28] = 'D2'
id2well[29] = 'D3'
id2well[30] = 'D4'
id2well[31] = 'D5'
id2well[32] = 'D6'
id2well[33] = 'D7'
id2well[34] = 'D8'
id2well[35] = 'D9'
# id2well[45] = 'D10'
# id2well[46] = 'D11'
# id2well[47] = 'D12'
id2well[36] = 'E1'
id2well[37] = 'E2'
id2well[38] = 'E3'
id2well[39] = 'E4'
id2well[40] = 'E5'
id2well[41] = 'E6'
id2well[42] = 'E7'
id2well[43] = 'E8'
id2well[44] = 'E9'
# id2well[57] = 'E10'
# id2well[58] = 'E11'
# id2well[59] = 'E12'
id2well[45] = 'F1'
id2well[46] = 'F2'
id2well[47] = 'F3'
id2well[48] = 'F4'
id2well[49] = 'F5'
id2well[50] = 'F6'
id2well[51] = 'F7'
id2well[52] = 'F8'
id2well[53] = 'F9'
# id2well[69] = 'F10'
# id2well[70] = 'F11'
# id2well[71] = 'F12'
# id2well[72] = 'G1'
# id2well[73] = 'G2'
# id2well[74] = 'G3'
# id2well[75] = 'G4'
# id2well[76] = 'G5'
# id2well[77] = 'G6'
# id2well[78] = 'G7'
# id2well[79] = 'G8'
# id2well[80] = 'G9'
# id2well[81] = 'G10'
# id2well[82] = 'G11'
# id2well[83] = 'G12'
# id2well[84] = 'H1'
# id2well[85] = 'H2'
# id2well[86] = 'H3'
# id2well[87] = 'H4'
# id2well[88] = 'H5'
# id2well[89] = 'H6'
# id2well[90] = 'H7'
# id2well[91] = 'H8'
# id2well[92] = 'H9'
# id2well[93] = 'H10'
# id2well[94] = 'H11'
# id2well[95] = 'H12'


def run(protocol: protocol_api.ProtocolContext):

    #from opentrons import simulate
    #protocol= simulate.get_protocol_api('2.0')
    left_pipette = protocol.load_instrument('p10_single','left')
    solutionrack = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical',3)#verify location
    #reservoir = protocol.load_labware('nest_1_reservoir_195ml',6)#verify location
    if Wellcount > 0:
        tiprack1 = protocol.load_labware('opentrons_96_tiprack_10ul',2)#verify location
        tiprack2 = protocol.load_labware('opentrons_96_tiprack_10ul',5)#verify location
        r=0
        while r < 54:
            ####  CHANGES:
            ####  The pipette goes a little higher, and takes up a little more volume for the rinse than the clean steps
            ####  I added an extra clean step for DNA, but you can just do bleach, peroxide, and single rinse.
            
            left_pipette.pick_up_tip(tiprack1[id2well[r]])  
            left_pipette.mix(3,9,solutionrack['B3'].bottom(z=1)) #bleach
            left_pipette.move_to(solutionrack['B3'].top())
            
            
            left_pipette.mix(3,9.5,solutionrack['A3'].bottom(z=1)) #peroxide
            left_pipette.move_to(solutionrack['A3'].top())
            
            
            left_pipette.mix(3,9,solutionrack['B2'].bottom(z=1)) #citrajet
            left_pipette.move_to(solutionrack['B2'].top())
            protocol.delay(seconds=6)

            left_pipette.mix(3,9.5,solutionrack['A2'].bottom(z=1)) #baking soda
            left_pipette.move_to(solutionrack['A2'].top())
            protocol.delay(seconds=6)

            left_pipette.mix(4,10,solutionrack['B1'].bottom(z=16)) #water
            left_pipette.move_to(solutionrack['B1'].top())

            left_pipette.mix(5,10,solutionrack['A1'].bottom(z=16)) #water
            left_pipette.move_to(solutionrack['A1'].top())
            left_pipette.blow_out()
            left_pipette.drop_tip(tiprack2[id2well[r]])
            r += 1

   