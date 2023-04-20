metadata= {'protocolName': 'Pipette cleaning + plate cleaning',
'author':'Sriya Sridhar ',
'description':'Pipette cleaning for 1000ul tips',
'apiLevel':'2.2'
}

from opentrons import protocol_api
from opentrons import simulate

import pandas
import numpy as np
import os

#Dictionary for managing pipette tips
tiprackposition = {}
tiprackposition[0] = 'A1'
tiprackposition[1] = 'A2'
tiprackposition[2] = 'A3'
tiprackposition[3] = 'A4'
tiprackposition[4] = 'A5'
tiprackposition[5] = 'A6'
tiprackposition[6] = 'A7'
tiprackposition[7] = 'A8'
tiprackposition[8] = 'A9'
tiprackposition[9] = 'A10'
tiprackposition[10] = 'A11'
tiprackposition[11] = 'A12'
tiprackposition[12] = 'B1'
tiprackposition[13] = 'B2'
tiprackposition[14] = 'B3'
tiprackposition[15] = 'B4'
tiprackposition[16] = 'B5'
tiprackposition[17] = 'B6'
tiprackposition[18] = 'B7'
tiprackposition[19] = 'B8'
tiprackposition[20] = 'B9'
tiprackposition[21] = 'B10'
tiprackposition[22] = 'B11'
tiprackposition[23] = 'B12'
tiprackposition[24] = 'C1'
tiprackposition[25] = 'C2'
tiprackposition[26] = 'C3'
tiprackposition[27] = 'C4'
tiprackposition[28] = 'C5'
tiprackposition[29] = 'C6'
tiprackposition[30] = 'C7'
tiprackposition[31] = 'C8'
tiprackposition[32] = 'C9'
tiprackposition[33] = 'C10'
tiprackposition[34] = 'C11'
tiprackposition[35] = 'C12'
tiprackposition[36] = 'D1'
tiprackposition[37] = 'D2'
tiprackposition[38] = 'D3'
tiprackposition[39] = 'D4'
tiprackposition[40] = 'D5'
tiprackposition[41] = 'D6'
tiprackposition[42] = 'D7'
tiprackposition[43] = 'D8'
tiprackposition[44] = 'D9'
tiprackposition[45] = 'D10'
tiprackposition[46] = 'D11'
tiprackposition[47] = 'D12'
tiprackposition[48] = 'E1'
tiprackposition[49] = 'E2'
tiprackposition[50] = 'E3'
tiprackposition[51] = 'E4'
tiprackposition[52] = 'E5'
tiprackposition[53] = 'E6'
tiprackposition[54] = 'E7'
tiprackposition[55] = 'E8'
tiprackposition[56] = 'E9'
tiprackposition[57] = 'E10'
tiprackposition[58] = 'E11'
tiprackposition[59] = 'E12'
tiprackposition[60] = 'F1'
tiprackposition[61] = 'F2'
tiprackposition[62] = 'F3'
tiprackposition[63] = 'F4'
tiprackposition[64] = 'F5'
tiprackposition[65] = 'F6'
tiprackposition[66] = 'F7'
tiprackposition[67] = 'F8'
tiprackposition[68] = 'F9'
tiprackposition[69] = 'F10'
tiprackposition[70] = 'F11'
tiprackposition[71] = 'F12'
tiprackposition[72] = 'G1'
tiprackposition[73] = 'G2'
tiprackposition[74] = 'G3'
tiprackposition[75] = 'G4'
tiprackposition[76] = 'G5'
tiprackposition[77] = 'G6'
tiprackposition[78] = 'G7'
tiprackposition[79] = 'G8'
tiprackposition[80] = 'G9'
tiprackposition[81] = 'G10'
tiprackposition[82] = 'G11'
tiprackposition[83] = 'G12'
tiprackposition[84] = 'H1'
tiprackposition[85] = 'H2'
tiprackposition[86] = 'H3'
tiprackposition[87] = 'H4'
tiprackposition[88] = 'H5'
tiprackposition[89] = 'H6'
tiprackposition[90] = 'H7'
tiprackposition[91] = 'H8'
tiprackposition[92] = 'H9'
tiprackposition[93] = 'H10'
tiprackposition[94] = 'H11'
tiprackposition[95] = 'H12' 
# tiprackposition[96] = 'A1'
# tiprackposition[97] = 'A2'
# tiprackposition[98] = 'A3'
# tiprackposition[99] = 'A4'
# tiprackposition[100]= 'A5'
# tiprackposition[101] = 'A6'
# tiprackposition[102] = 'A7'
# tiprackposition[103] = 'A8'
# tiprackposition[104] = 'A9'
# tiprackposition[105] = 'A10'
# tiprackposition[106] = 'A11'
# tiprackposition[107] = 'A12'
# tiprackposition[108] = 'B1'
# tiprackposition[109] = 'B2'
# tiprackposition[110] = 'B3'
# tiprackposition[111] = 'B4'
# tiprackposition[112] = 'B5'
# tiprackposition[113] = 'B6'
# tiprackposition[114] = 'B7'
# tiprackposition[115] = 'B8'
# tiprackposition[116] = 'B9'
# tiprackposition[117] = 'B10'
# tiprackposition[118] = 'B11'
# tiprackposition[119] = 'B12'
# tiprackposition[120] = 'C1'
# tiprackposition[121] = 'C2'
# tiprackposition[122] = 'C3'
# tiprackposition[123] = 'C4'
# tiprackposition[124] = 'C5'
# tiprackposition[125] = 'C6'
# tiprackposition[126] = 'C7'
# tiprackposition[127] = 'C8'
# tiprackposition[128] = 'C9'
# tiprackposition[129] = 'C10'
# tiprackposition[130] = 'C11'
# tiprackposition[131] = 'C12'
# tiprackposition[132] = 'D1'
# tiprackposition[133] = 'D2'
# tiprackposition[134] = 'D3'
# tiprackposition[135] = 'D4'
# tiprackposition[136] = 'D5'
# tiprackposition[137] = 'D6'
# tiprackposition[138] = 'D7'
# tiprackposition[139] = 'D8'
# tiprackposition[140] = 'D9'
# tiprackposition[141] = 'D10'
# tiprackposition[142] = 'D11'
# tiprackposition[143] = 'D12'
# tiprackposition[144] = 'E1'
# tiprackposition[145] = 'E2'
# tiprackposition[146] = 'E3'
# tiprackposition[147] = 'E4'
# tiprackposition[148] = 'E5'
# tiprackposition[149] = 'E6'
# tiprackposition[150] = 'E7'
# tiprackposition[151] = 'E8'
# tiprackposition[152] = 'E9'
# tiprackposition[153] = 'E10'
# tiprackposition[154] = 'E11'
# tiprackposition[155] = 'E12'
# tiprackposition[156] = 'F1'
# tiprackposition[157] = 'F2'
# tiprackposition[158] = 'F3'
# tiprackposition[159] = 'F4'
# tiprackposition[160] = 'F5'
# tiprackposition[161] = 'F6'
# tiprackposition[162] = 'F7'
# tiprackposition[163] = 'F8'
# tiprackposition[164] = 'F9'
# tiprackposition[165] = 'F10'
# tiprackposition[166] = 'F11'
# tiprackposition[167] = 'F12'
# tiprackposition[168] = 'G1'
# tiprackposition[169] = 'G2'
# tiprackposition[170] = 'G3'
# tiprackposition[171] = 'G4'
# tiprackposition[172] = 'G5'
# tiprackposition[173] = 'G6'
# tiprackposition[174] = 'G7'
# tiprackposition[175] = 'G8'
# tiprackposition[176] = 'G9'
# tiprackposition[177] = 'G10'
# tiprackposition[178] = 'G11'
# tiprackposition[179] = 'G12'
# tiprackposition[180] = 'H1'
# tiprackposition[181] = 'H2'
# tiprackposition[182] = 'H3'
# tiprackposition[183] = 'H4'
# tiprackposition[184] = 'H5'
# tiprackposition[185] = 'H6'
# tiprackposition[186] = 'H7'
# tiprackposition[187] = 'H8'
# tiprackposition[188] = 'H9'
# tiprackposition[189] = 'H10'
# tiprackposition[190] = 'H11'
# tiprackposition[191] = 'H12'
# tiprackposition[192] = 'A1'
# tiprackposition[193] = 'A2'
# tiprackposition[194] = 'A3'
# tiprackposition[195] = 'A4'
# tiprackposition[196]= 'A5'
# tiprackposition[197] = 'A6'
# tiprackposition[198] = 'A7'
# tiprackposition[199] = 'A8'
# tiprackposition[200] = 'A9'
# tiprackposition[201] = 'A10'
# tiprackposition[202] = 'A11'
# tiprackposition[203] = 'A12'
# tiprackposition[204] = 'B1'
# tiprackposition[205] = 'B2'
# tiprackposition[206] = 'B3'
# tiprackposition[207] = 'B4'



#for rinsing
id2well1 = {}
id2well1[0] = 'A1'
id2well1[1] = 'A2'
id2well1[2] = 'A3'
id2well1[3] = 'A4'
id2well1[4] = 'A5'
id2well1[5] = 'A6'
id2well1[6] = 'A7'
id2well1[7] = 'A8'
id2well1[8] = 'A9'
id2well1[9] = 'A10'
id2well1[10] = 'A11'
id2well1[11] = 'A12'
id2well1[12] = 'B1'
id2well1[13] = 'B2'
id2well1[14] = 'B3'
id2well1[15] = 'B4'
id2well1[16] = 'B5'
id2well1[17] = 'B6'
id2well1[18] = 'B7'
id2well1[19] = 'B8'
id2well1[20] = 'B9'
id2well1[21] = 'B10'
id2well1[22] = 'B11'
id2well1[23] = 'B12'
id2well1[24] = 'C1'
id2well1[25] = 'C2'
id2well1[26] = 'C3'
id2well1[27] = 'C4'
id2well1[28] = 'C5'
id2well1[29] = 'C6'
id2well1[30] = 'C7'
id2well1[31] = 'C8'
id2well1[32] = 'C9'
id2well1[33] = 'C10'
id2well1[34] = 'C11'
id2well1[35] = 'C12'
id2well1[36] = 'D1'
id2well1[37] = 'D2'
id2well1[38] = 'D3'
id2well1[39] = 'D4'
id2well1[40] = 'D5'
id2well1[41] = 'D6'
id2well1[42] = 'D7'
id2well1[43] = 'D8'
id2well1[44] = 'D9'
id2well1[45] = 'D10'
id2well1[46] = 'D11'
id2well1[47] = 'D12'
id2well1[48] = 'E1'
id2well1[49] = 'E2'
id2well1[50] = 'E3'
id2well1[51] = 'E4'
id2well1[52] = 'E5'
id2well1[53] = 'E6'
id2well1[54] = 'E7'
id2well1[55] = 'E8'
id2well1[56] = 'E9'
id2well1[57] = 'E10'
id2well1[58] = 'E11'
id2well1[59] = 'E12'
id2well1[60] = 'F1'
id2well1[61] = 'F2'
id2well1[62] = 'F3'
id2well1[63] = 'F4'
id2well1[64] = 'F5'
id2well1[65] = 'F6'
id2well1[66] = 'F7'
id2well1[67] = 'F8'
id2well1[68] = 'F9'
id2well1[69] = 'F10'
id2well1[70] = 'F11'
id2well1[71] = 'F12'
id2well1[72] = 'G1'
id2well1[73] = 'G2'
id2well1[74] = 'G3'
id2well1[75] = 'G4'
id2well1[76] = 'G5'
id2well1[77] = 'G6'
id2well1[78] = 'G7'
id2well1[79] = 'G8'
id2well1[80] = 'G9'
id2well1[81] = 'G10'
id2well1[82] = 'G11'
id2well1[83] = 'G12'
id2well1[84] = 'H1'
id2well1[85] = 'H2'
id2well1[86] = 'H3'
id2well1[87] = 'H4'
id2well1[88] = 'H5'
id2well1[89] = 'H6'
id2well1[90] = 'H7'
id2well1[91] = 'H8'
id2well1[92] = 'H9'
id2well1[93] = 'H10'
id2well1[94] = 'H11'
id2well1[95] = 'H12'

clean = {}
clean[0] = 'A1'
clean[1] = 'A2'
clean[2] = 'A3'
clean[3] = 'A4'
clean[4] = 'A5'




def run(protocol: protocol_api.ProtocolContext):

    #from opentrons import simulate
    #protocol= simulate.get_protocol_api('2.0')
    right_pipette = protocol.load_instrument('p300_single','right')
    left_pipette = protocol.load_instrument('p10_single','left')

    solutionrack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical',3)#verify location
    trough = protocol.load_labware('agilent_1_reservoir_290ml',11)
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat',2)
    watertrough = protocol.load_labware('agilent_1_reservoir_290ml',9)
    

    cleantiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',1)
    dirtyytiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',5)

    
    r = 0
    t = 0
    while r <= 96:

    # resuspend with 90uL bleach (leave the bleach in)
        if t<96:
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])

        else:
            t=0 
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])
        
        right_pipette.aspirate (180, solutionrack['B4']) #picking up bleach
        right_pipette.dispense(190, plate[id2well1[r]])
        right_pipette.mix(5,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1']) #get rid of it in waste trough.
        right_pipette.drop_tip(dirtyytiprack1['A1'])
        
        s=t
        t += 1

        # Clean with 280 uL bleach (remove half)
        if t<96: 
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]]) 

        else: 
            t=0
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]]) 

        right_pipette.aspirate (280, solutionrack['B4']) #grab bleach
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove half.
        right_pipette.dispense(300, trough['A1']) #get rid of it in waste trough.
        right_pipette.drop_tip(dirtyytiprack1['A2'])

        t+=1

# Rinse with H2O2 (remove everything)
        if t<96: 
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])

        else: 
            t=0
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])

        right_pipette.aspirate (280, solutionrack['B3']) #grab H2O2
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1']) #get rid of it in waste trough.
        right_pipette.drop_tip(dirtyytiprack1['A3'])

        t += 1

# rinse with 280uL water (remove everything)

        if t<96:   
             right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])  

        else:
            t=0
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])


        right_pipette.aspirate (280, watertrough['A1']) #picking up water to rinse
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(5,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]])
        right_pipette.dispense(300, trough['A1']) #get rid of used water in a waste tube
        right_pipette.drop_tip(dirtyytiprack1['A4'])
        
        t += 1
        
# Rinse with 280uL water

        if t<96:
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])  

        else:
            t=0
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])


        right_pipette.aspirate (280, watertrough['A1']) #picking up water to rinse
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(3,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]])
        right_pipette.dispense(300, trough['A1']) #get rid of used water in a waste tube
        right_pipette.drop_tip(dirtyytiprack1['A5'])

        t += 1
        r += 1

        #from opentrons import simulate
        #protocol= simulate.get_protocol_api('2.0')
        

        cl = 0
        while cl < 5:
            right_pipette.pick_up_tip(dirtyytiprack1[clean[cl]])  
            right_pipette.mix(3,10,solutionrack['B4']) #bleach
            #right_pipette.move_to(solutionrack['B4'].top())
            #right_pipette.blow_out()
            right_pipette.mix(3,10,solutionrack['A4']) #H2O2
            right_pipette.move_to(solutionrack['A4'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,10,solutionrack['B3']) #DI rinse
            right_pipette.move_to(solutionrack['B3'].top())
            right_pipette.blow_out()
            right_pipette.drop_tip(cleantiprack1[id2well[s]])
            cl+=1
            s+=1







 ######TODO:
 #complete rinse while loop, explain difference b/w tiprack and 
 #id2well dictionaries. 

 #tell sriya that we had to stop setting t=0 in the if else statements to make it keep taking tips from the second rack.

 #might need to add a thirt final rinse for plate. and bring down mix number to 2

 #1% h2o2

