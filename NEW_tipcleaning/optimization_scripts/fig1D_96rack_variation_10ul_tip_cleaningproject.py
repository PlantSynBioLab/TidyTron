metadata= {'protocolName': 'Pipette cleaning',
'author':'Cameron Longmire <camel94@vt.edu>',
'description':'Pipette cleaning for 1000ul tips',
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
Wellcount=2
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
id2well[9] = 'A10'
id2well[10] = 'A11'
id2well[11] = 'A12'
id2well[12] = 'B1'
id2well[13] = 'B2'
id2well[14] = 'B3'
id2well[15] = 'B4'
id2well[16] = 'B5'
id2well[17] = 'B6'
id2well[18] = 'B7'
id2well[19] = 'B8'
id2well[20] = 'B9'
id2well[21] = 'B10'
id2well[22] = 'B11'
id2well[23] = 'B12'
id2well[24] = 'C1'
id2well[25] = 'C2'
id2well[26] = 'C3'
id2well[27] = 'C4'
id2well[28] = 'C5'
id2well[29] = 'C6'
id2well[30] = 'C7'
id2well[31] = 'C8'
id2well[32] = 'C9'
id2well[33] = 'C10'
id2well[34] = 'C11'
id2well[35] = 'C12'
id2well[36] = 'D1'
id2well[37] = 'D2'
id2well[38] = 'D3'
id2well[39] = 'D4'
id2well[40] = 'D5'
id2well[41] = 'D6'
id2well[42] = 'D7'
id2well[43] = 'D8'
id2well[44] = 'D9'
id2well[45] = 'D10'
id2well[46] = 'D11'
id2well[47] = 'D12'
id2well[48] = 'E1'
id2well[49] = 'E2'
id2well[50] = 'E3'
id2well[51] = 'E4'
id2well[52] = 'E5'
id2well[53] = 'E6'
id2well[54] = 'E7'
id2well[55] = 'E8'
id2well[56] = 'E9'
id2well[57] = 'E10'
id2well[58] = 'E11'
id2well[59] = 'E12'
id2well[60] = 'F1'
id2well[61] = 'F2'
id2well[62] = 'F3'
id2well[63] = 'F4'
id2well[64] = 'F5'
id2well[65] = 'F6'
id2well[66] = 'F7'
id2well[67] = 'F8'
id2well[68] = 'F9'
id2well[69] = 'F10'
id2well[70] = 'F11'
id2well[71] = 'F12'
id2well[72] = 'G1'
id2well[73] = 'G2'
id2well[74] = 'G3'
id2well[75] = 'G4'
id2well[76] = 'G5'
id2well[77] = 'G6'
id2well[78] = 'G7'
id2well[79] = 'G8'
id2well[80] = 'G9'
id2well[81] = 'G10'
id2well[82] = 'G11'
id2well[83] = 'G12'
id2well[84] = 'H1'
id2well[85] = 'H2'
id2well[86] = 'H3'
id2well[87] = 'H4'
id2well[88] = 'H5'
id2well[89] = 'H6'
id2well[90] = 'H7'
id2well[91] = 'H8'
id2well[92] = 'H9'
id2well[93] = 'H10'
id2well[94] = 'H11'
id2well[95] = 'H12'
id2well[96] = 'A1'
id2well[97] = 'A2'
id2well[98] = 'A3'
id2well[99] = 'A4'
id2well[100] = 'A5'
id2well[101] = 'A6'
id2well[102] = 'A7'
id2well[103] = 'A8'
id2well[104] = 'A9'
id2well[105] = 'A10'
id2well[106] = 'A11'
id2well[107] = 'A12'
id2well[108] = 'B1'
id2well[109] = 'B2'
id2well[110] = 'B3'
id2well[111] = 'B4'
id2well[112] = 'B5'
id2well[113] = 'B6'
id2well[114] = 'B7'
id2well[115] = 'B8'
id2well[116] = 'B9'
id2well[117] = 'B10'
id2well[118] = 'B11'
id2well[119] = 'B12'
id2well[120] = 'C1'
id2well[121] = 'C2'
id2well[122] = 'C3'
id2well[123] = 'C4'
id2well[124] = 'C5'
id2well[125] = 'C6'
id2well[126] = 'C7'
id2well[127] = 'C8'
id2well[128] = 'C9'
id2well[129] = 'C10'
id2well[130] = 'C11'
id2well[131] = 'C12'
id2well[132] = 'D1'
id2well[133] = 'D2'
id2well[134] = 'D3'
id2well[135] = 'D4'
id2well[136] = 'D5'
id2well[137] = 'D6'
id2well[138] = 'D7'
id2well[139] = 'D8'
id2well[140] = 'D9'
id2well[141] = 'D10'
id2well[142] = 'D11'
id2well[143] = 'D12'
id2well[144] = 'E1'
id2well[145] = 'E2'
id2well[146] = 'E3'
id2well[147] = 'E4'
id2well[148] = 'E5'
id2well[149] = 'E6'
id2well[150] = 'E7'
id2well[151] = 'E8'
id2well[152] = 'E9'
id2well[153] = 'E10'
id2well[154] = 'E11'
id2well[155] = 'E12'
id2well[156] = 'F1'
id2well[157] = 'F2'
id2well[158] = 'F3'
id2well[159] = 'F4'
id2well[160] = 'F5'
id2well[161] = 'F6'
id2well[162] = 'F7'
id2well[163] = 'F8'
id2well[164] = 'F9'
id2well[165] = 'F10'
id2well[166] = 'F11'
id2well[167] = 'F12'
id2well[168] = 'G1'
id2well[169] = 'G2'
id2well[170] = 'G3'
id2well[171] = 'G4'
id2well[172] = 'G5'
id2well[173] = 'G6'
id2well[174] = 'G7'
id2well[175] = 'G8'
id2well[176] = 'G9'
id2well[177] = 'G10'
id2well[178] = 'G11'
id2well[179] = 'G12'
id2well[180] = 'H1'
id2well[181] = 'H2'
id2well[182] = 'H3'
id2well[183] = 'H4'
id2well[184] = 'H5'
id2well[185] = 'H6'
id2well[186] = 'H7'
id2well[187] = 'H8'
id2well[188] = 'H9'
id2well[189] = 'H10'
id2well[190] = 'H11'
id2well[191] = 'H12'

id2plate = {}
id2plate[1] = 'A1'
id2plate[3] = 'A2'
id2plate[5] = 'A3'
id2plate[7] = 'A4'
id2plate[9] = 'A5'
id2plate[11] = 'A6'
id2plate[13] = 'A7'
id2plate[15] = 'A8'
id2plate[17] = 'A9'
id2plate[19] = 'A10'
id2plate[21] = 'A11'
id2plate[23] = 'A12'
id2plate[25] = 'B1'
id2plate[27] = 'B2'
id2plate[29] = 'B3'
id2plate[31] = 'B4'
id2plate[33] = 'B5'
id2plate[35] = 'B6'
id2plate[37] = 'B7'
id2plate[39] = 'B8'
id2plate[41] = 'B9'
id2plate[43] = 'B10'
id2plate[45] = 'B11'
id2plate[47] = 'B12'
id2plate[49] = 'C1'
id2plate[51] = 'C2'
id2plate[53] = 'C3'
id2plate[55] = 'C4'
id2plate[57] = 'C5'
id2plate[59] = 'C6'
id2plate[61] = 'C7'
id2plate[63] = 'C8'
id2plate[65] = 'C9'
id2plate[67] = 'C10'
id2plate[69] = 'C11'
id2plate[71] = 'C12'
id2plate[73] = 'D1'
id2plate[75] = 'D2'
id2plate[77] = 'D3'
id2plate[79] = 'D4'
id2plate[81] = 'D5'
id2plate[83] = 'D6'
id2plate[85] = 'D7'
id2plate[87] = 'D8'
id2plate[89] = 'D9'
id2plate[91] = 'D10'
id2plate[93] = 'D11'
id2plate[95] = 'D12'
id2plate[97] = 'E1'
id2plate[99] = 'E2'
id2plate[101] = 'E3'
id2plate[103] = 'E4'
id2plate[105] = 'E5'
id2plate[107] = 'E6'
id2plate[109] = 'E7'
id2plate[111] = 'E8'
id2plate[113] = 'E9'
id2plate[115] = 'E10'
id2plate[117] = 'E11'
id2plate[119] = 'E12'
id2plate[121] = 'F1'
id2plate[123] = 'F2'
id2plate[125] = 'F3'
id2plate[127] = 'F4'
id2plate[129] = 'F5'
id2plate[131] = 'F6'
id2plate[133] = 'F7'
id2plate[135] = 'F8'
id2plate[137] = 'F9'
id2plate[139] = 'F10'
id2plate[141] = 'F11'
id2plate[143] = 'F12'
id2plate[145] = 'G1'
id2plate[147] = 'G2'
id2plate[149] = 'G3'
id2plate[151] = 'G4'
id2plate[153] = 'G5'
id2plate[155] = 'G6'
id2plate[157] = 'G7'
id2plate[159] = 'G8'
id2plate[161] = 'G9'
id2plate[163] = 'G10'
id2plate[165] = 'G11'
id2plate[167] = 'G12'
id2plate[169] = 'H1'
id2plate[171] = 'H2'
id2plate[173] = 'H3'
id2plate[175] = 'H4'
id2plate[177] = 'H5'
id2plate[179] = 'H6'
id2plate[181] = 'H7'
id2plate[183] = 'H8'
id2plate[185] = 'H9'
id2plate[187] = 'H10'
id2plate[189] = 'H11'
id2plate[191] = 'H12'


def run(protocol: protocol_api.ProtocolContext):
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_10ul',2)#dirty
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_10ul',6)#verify location
    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul',5) #clean
    #from opentrons import simulate
    #protocol= simulate.get_protocol_api('2.0')
    left_pipette = protocol.load_instrument('p10_single','left')
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1])
    solutionrack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical',3)#verify location
    #reservoir = protocol.load_labware('nest_1_reservoir_195ml',6)#verify location
    #plate = protocol.load_labware('nest_96_wellplate_200ul_flat',1) #culture plate
    if Wellcount > 0:
        
        r=0
        while r <= 95:
            if r <= 95:
                left_pipette.pick_up_tip(tiprack1[id2well[r]])
            # if r >95:
            #     left_pipette.pick_up_tip(tiprack2[id2well[r]]) 

            left_pipette.mix(1,10,solutionrack['B4']) #bleach
            left_pipette.mix(2,10,solutionrack['A4']) #peroxide
            left_pipette.mix(1,10,solutionrack['B3']) #water
            
            
            #left_pipette.aspirate(10,solutionrack['A1'])
 
            #if r == 0:
                #left_pipette.dispense(10,plate[id2plate[r]])
                #left_pipette.mix(3,10,plate[id2plate[r]])
                #left_pipette.drop_tip()
            if r % 2 == 0:
                # if r % 6 ==0:
                #     left_pipette.drop_tip()
                #     right_pipette.pick_up_tip() ##possible error
                #     right_pipette.mix(3,300,solutionrack['A1'])
                #     right_pipette.drop_tip()
                # else:
                left_pipette.drop_tip(tiprack3[id2well[r]])

            else:
                # left_pipette.dispense(10,plate[id2plate[r]])
                # left_pipette.mix(3,10,plate[id2plate[r]])
                # left_pipette.drop_tip()
                left_pipette.drop_tip()
                
            
            
            #left_pipette.move_to(solutionrack['B4'].top()) 
            #left_pipette.blow_out()
            #left_pipette.mix(1,10,solutionrack['A4'].bottom(z=2))
            #left_pipette.mix(1,10,solutionrack['A3'].bottom(z=16))
            #left_pipette.move_to(solutionrack['A4'].top())
            #left_pipette.blow_out()
            #left_pipette.mix(1,10,reservoir['A1'].bottom(z=5))
            #left_pipette.move_to(reservoir['A1'].top())
            #left_pipette.move_to(solutionrack['A3'].top())
            #left_pipette.blow_out()
            #left_pipette.drop_tip(tiprack2[id2well[r]])
            r += 1

    
    
    
    
    
    
    

    