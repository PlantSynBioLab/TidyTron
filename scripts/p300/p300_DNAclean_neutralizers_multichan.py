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

    multi_pipette = protocol.load_instrument('p300_multi_gen2','right')
    washtrough = protocol.load_labware('usascientific_12_reservoir_22ml', 3)

    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul',2) #dirty
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul',5) #clean
        
    r=0
    while r <= 11:


        multi_pipette.pick_up_tip(tiprack1[id2well[r]])  
        multi_pipette.mix(3,290,washtrough['A1']) #bleach
        multi_pipette.move_to(washtrough['A1'].top())
        
        
        multi_pipette.mix(3,295,washtrough['A2']) #peroxide
        multi_pipette.move_to(washtrough['A2'].top())
        
        
        multi_pipette.mix(3,290,washtrough['A3']) #citrajet
        multi_pipette.move_to(washtrough['A3'].top())
        protocol.delay(seconds=6)

        multi_pipette.mix(3,295,washtrough['A4']) #baking soda
        multi_pipette.move_to(washtrough['A4'].top())
        protocol.delay(seconds=6)

        multi_pipette.mix(5,300,washtrough['A5']) #water
        multi_pipette.move_to(washtrough['A5'].top())

        multi_pipette.mix(6,300,washtrough['A6']) #water
        multi_pipette.move_to(washtrough['A6'].top())
        multi_pipette.blow_out()
        
        multi_pipette.drop_tip(tiprack2[id2well[r]])
        r += 1

