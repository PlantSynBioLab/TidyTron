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
    solutiontrough2 = protocol.load_labware('nest_12_reservoir_15ml',6)#verify location
    solutiontrough3 = protocol.load_labware('nest_12_reservoir_15ml',1)#verify location
    solutiontrough4 = protocol.load_labware('nest_12_reservoir_15ml',2)#verify location
    trough = protocol.load_labware('agilent_1_reservoir_290ml',11)
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat',5)
    watertrough = protocol.load_labware('agilent_1_reservoir_290ml',9)
    watertrough2 = protocol.load_labware('agilent_1_reservoir_290ml',7)

    cleantiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',4)
    dirtyytiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',8)

    
    r = 0
   
    while r <= 11:

    # resuspend with 90uL bleach (leave the bleach in)
        right_pipette.pick_up_tip(cleantiprack1['A1'])
        
        if r < 6:
            right_pipette.aspirate (180, solutiontrough['A1']) #picking up bleach
        if  6 <= r <= 11:
            right_pipette.aspirate (180, solutiontrough['A6']) #picking up bleach

        right_pipette.dispense(190, plate[id2well1[r]])
        right_pipette.mix(5,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1'].top()) #get rid of it in waste trough.
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A1'])
        
       
        # Clean with 280 uL bleach (remove half)
        right_pipette.pick_up_tip(cleantiprack1['A2'])

        if r < 4:
            right_pipette.aspirate (280, solutiontrough['A9']) #picking up bleach
        if 4 <= r < 8:
            right_pipette.aspirate (280, solutiontrough['A10']) #picking up bleach
        if 8 <= r <= 11:
            right_pipette.aspirate (280, solutiontrough['A11']) #picking up bleach
        
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove half.
        right_pipette.dispense(300, trough['A1'].top()) #get rid of it in waste trough.
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A2'])


# Clean with 280 uL bleach (remove half)
        right_pipette.pick_up_tip(cleantiprack1['A3'])

        if r < 4:
            right_pipette.aspirate (280, solutiontrough3['A1']) #picking up bleach
        if 4 <= r < 8:
            right_pipette.aspirate (280, solutiontrough3['A2']) #picking up bleach
        if 8 <= r <= 11:
            right_pipette.aspirate (280, solutiontrough3['A3']) #picking up bleach
        
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove half.
        right_pipette.dispense(300, trough['A1'].top()) #get rid of it in waste trough.
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A3'])
       

# Rinse with H2O2 (remove everything)
        right_pipette.pick_up_tip(cleantiprack1['A4'])
        
        if r < 4:
            right_pipette.aspirate (280, solutiontrough['A2']) #picking up bleach
        if 4 <= r < 8:
            right_pipette.aspirate (280, solutiontrough['A7']) #picking up bleach
        if 8 <= r <= 11:
            right_pipette.aspirate (280, solutiontrough['A8']) #picking up bleach

        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1'].top()) #get rid of it in waste trough.
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A4'])

# Rinse with H2O2 (remove everything)
        right_pipette.pick_up_tip(cleantiprack1['A5'])
        
        if r < 4:
            right_pipette.aspirate (280, solutiontrough3['A4']) #picking up bleach
        if 4 <= r < 8:
            right_pipette.aspirate (280, solutiontrough3['A5']) #picking up bleach
        if 8 <= r <= 11:
            right_pipette.aspirate (280, solutiontrough3['A6']) #picking up bleach

        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(6,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]]) #remove everything.
        right_pipette.dispense(300, trough['A1'].top()) #get rid of it in waste trough.
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A5'])

        

# rinse with 280uL water (remove everything)
        right_pipette.pick_up_tip(cleantiprack1['A6'])
        right_pipette.aspirate (280, watertrough['A1']) #picking up water to rinse
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(5,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]])
        right_pipette.dispense(300, trough['A1'].top()) #get rid of used water in a waste tube
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A6'])
        
        
        
# Rinse with 280uL water
        right_pipette.pick_up_tip(cleantiprack1['A7'])
        right_pipette.aspirate (280, watertrough2['A1']) #picking up water to rinse
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(3,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]])
        right_pipette.dispense(300, trough['A1'].top()) #get rid of used water in a waste tube
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A7'])

# Rinse with 280uL water
        right_pipette.pick_up_tip(cleantiprack1['A8'])
        right_pipette.aspirate (280, watertrough2['A1']) #picking up water to rinse
        right_pipette.dispense(290, plate[id2well1[r]])
        right_pipette.mix(3,270,plate[id2well1[r]])
        right_pipette.aspirate(300, plate[id2well1[r]])
        right_pipette.dispense(300, trough['A1'].top()) #get rid of used water in a waste tube
        right_pipette.blow_out()
        right_pipette.drop_tip(dirtyytiprack1['A8'])

        
        r += 1

        #from opentrons import simulate
        #protocol= simulate.get_protocol_api('2.0')
        


        # col 1
        right_pipette.pick_up_tip(dirtyytiprack1['A1'])
        right_pipette.mix(3,295,solutiontrough['A3']) #bleach
        right_pipette.move_to(solutiontrough['A3'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough['A4']) #H2O2
        right_pipette.move_to(solutiontrough['A4'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough['A5']) #DI rinse
        right_pipette.move_to(solutiontrough['A5'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A1'])

        # col 2
        right_pipette.pick_up_tip(dirtyytiprack1['A2'])
        right_pipette.mix(3,295,solutiontrough2['A1']) #bleach
        right_pipette.move_to(solutiontrough2['A1'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A2']) #H2O2
        right_pipette.move_to(solutiontrough2['A2'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A3']) #DI rinse
        right_pipette.move_to(solutiontrough2['A3'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A2'])

        # col 3
        right_pipette.pick_up_tip(dirtyytiprack1['A3'])
        right_pipette.mix(3,295,solutiontrough3['A7']) #bleach
        right_pipette.move_to(solutiontrough3['A7'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough3['A8']) #H2O2
        right_pipette.move_to(solutiontrough3['A8'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough3['A9']) #DI rinse
        right_pipette.move_to(solutiontrough3['A9'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A3'])

        # col 4
        right_pipette.pick_up_tip(dirtyytiprack1['A4'])
        right_pipette.mix(3,295,solutiontrough2['A4']) #H2O2
        right_pipette.move_to(solutiontrough2['A4'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A5']) #H2O2
        right_pipette.move_to(solutiontrough2['A5'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A6']) #DI rinse
        right_pipette.move_to(solutiontrough2['A6'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A4'])

        # col 5
        right_pipette.pick_up_tip(dirtyytiprack1['A5'])
        right_pipette.mix(3,295,solutiontrough3['A10']) #H2O2
        right_pipette.move_to(solutiontrough3['A10'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough3['A11']) #H2O2
        right_pipette.move_to(solutiontrough3['A11'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough3['A12']) #DI rinse
        right_pipette.move_to(solutiontrough3['A12'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A5'])

        # col 6
        right_pipette.pick_up_tip(dirtyytiprack1['A6'])
        right_pipette.mix(3,295,solutiontrough2['A7']) #DI rinse
        right_pipette.move_to(solutiontrough2['A7'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A8']) #DI rinse
        right_pipette.move_to(solutiontrough2['A8'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A9']) #DI rinse
        right_pipette.move_to(solutiontrough2['A9'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A6'])

        # col 7
        right_pipette.pick_up_tip(dirtyytiprack1['A7'])
        right_pipette.mix(3,295,solutiontrough2['A10']) #DI rinse
        right_pipette.move_to(solutiontrough2['A10'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A11']) #DI rinse
        right_pipette.move_to(solutiontrough2['A11'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough2['A12']) #DI rinse
        right_pipette.move_to(solutiontrough2['A12'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A7'])

        # col 8
        right_pipette.pick_up_tip(dirtyytiprack1['A8'])
        right_pipette.mix(3,295,solutiontrough4['A1']) #DI rinse
        right_pipette.move_to(solutiontrough4['A1'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough4['A2']) #DI rinse
        right_pipette.move_to(solutiontrough4['A2'].top())
        right_pipette.blow_out()
        right_pipette.mix(3,300,solutiontrough4['A3']) #DI rinse
        right_pipette.move_to(solutiontrough4['A3'].top())
        right_pipette.blow_out()
        right_pipette.drop_tip(cleantiprack1['A8'])