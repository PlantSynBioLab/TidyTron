metadata= {'protocolName': 'Pipette cleaning',
'author':'Cameron Longmire <camel94@vt.edu> and John Bryant <jbryant2@vt.edu>',
'description':'Tip cleaning for E. coli',
'apiLevel':'2.2'
}
from opentrons import protocol_api


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



def run(protocol: protocol_api.ProtocolContext):

    left_pipette = protocol.load_instrument('p300_multi_gen2','right')
    washtrough = protocol.load_labware('usascientific_12_reservoir_22ml', 3)

    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',2) #dirty
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul',5) #clean
    
    r=0
    while r <= 11:
        left_pipette.pick_up_tip(tiprack1[id2well[r]])  
        
        left_pipette.mix(1,300,washtrough['A1'].bottom(z=2))

        left_pipette.mix(2,300,washtrough['A2'].bottom(z=2))
        
        left_pipette.mix(1,300,washtrough['A3'].bottom(z=2))

        left_pipette.move_to(washtrough['A3'].top())
        left_pipette.blow_out()
        left_pipette.drop_tip(tiprack2[id2well[r]])
        r += 1

