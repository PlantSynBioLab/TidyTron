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


clean = {}
clean[0] = 'A1'
clean[1] = 'A2'
clean[2] = 'A3'
clean[3] = 'A4'
clean[4] = 'A5'




def run(protocol: protocol_api.ProtocolContext):

    #from opentrons import simulate
    #protocol= simulate.get_protocol_api('2.0')
    right_pipette = protocol.load_instrument('p300_multi','right')
    #right_pipette = protocol.load_instrument('p10_single','right')

    solutiontrough = protocol.load_labware('nest_12_reservoir_15ml',3)#verify location
    trough = protocol.load_labware('agilent_1_reservoir_290ml',11)
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat',2)
    watertrough = protocol.load_labware('agilent_1_reservoir_290ml',9)
    

    cleantiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',1)
    dirtyytiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',5)

    
    r = 0
    t = 0
    while r <= 11:

    # resuspend with 90uL bleach (leave the bleach in)
        if t<=11:
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])

        else:
            t=0 
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])
        
        if r < 3:
            right_pipette.aspirate (180, solutiontrough['A1']) #picking up bleach
        if 3 <= r < 6:
            right_pipette.aspirate (180, solutiontrough['A6']) #picking up bleach
        if 6 <= r < 9:
            right_pipette.aspirate (180, solutiontrough['A8']) #picking up bleach
        if 9 <= r <= 11:
            right_pipette.aspirate (180, solutiontrough['A11']) #picking up bleach

        right_pipette.dispense(190, plate[id2well1[r]])
        right_pipette.mix(5,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1']) #get rid of it in waste trough.
        right_pipette.drop_tip(dirtyytiprack1['A1'])
        
        s=t
        t += 1

        # Clean with 280 uL bleach (remove half)
        if t<=11: 
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]]) 

        else: 
            t=0
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]]) 

        if r < 3:
            right_pipette.aspirate (280, solutiontrough['A1']) #picking up bleach
        if 3 <= r < 6:
            right_pipette.aspirate (280, solutiontrough['A6']) #picking up bleach
        if 6 <= r < 9:
            right_pipette.aspirate (280, solutiontrough['A8']) #picking up bleach
        if 9 <= r <= 11:
            right_pipette.aspirate (280, solutiontrough['A11']) #picking up bleach

        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove half.
        right_pipette.dispense(300, trough['A1']) #get rid of it in waste trough.
        right_pipette.drop_tip(dirtyytiprack1['A2'])

        t+=1

# Rinse with H2O2 (remove everything)
        if t<=11: 
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])

        else: 
            t=0
            right_pipette.pick_up_tip(cleantiprack1[tiprackposition[t]])

        if r < 4:
            right_pipette.aspirate (280, solutiontrough['A2']) #picking up bleach
        if 4 <= r < 8:
            right_pipette.aspirate (280, solutiontrough['A7']) #picking up bleach
        if 8 <= r < 11:
            right_pipette.aspirate (280, solutiontrough['A9']) #picking up bleach

        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1']) #get rid of it in waste trough.
        right_pipette.drop_tip(dirtyytiprack1['A3'])

        t += 1

# rinse with 280uL water (remove everything)

        if t<=11:   
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

        if t<=11:
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
            if s<=11:
                right_pipette.pick_up_tip(dirtyytiprack1[clean[cl]])
            else:
                s=0 
                right_pipette.pick_up_tip(dirtyytiprack1[clean[cl]]) 

            right_pipette.mix(3,295,solutiontrough['A3']) #bleach
            right_pipette.move_to(solutiontrough['A3'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,300,solutiontrough['A4']) #H2O2
            right_pipette.move_to(solutiontrough['A4'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,300,solutiontrough['A5']) #DI rinse
            right_pipette.move_to(solutiontrough['A5'].top())
            right_pipette.blow_out()
            right_pipette.drop_tip(cleantiprack1[id2well1[s]])
            cl+=1
            s+=1





