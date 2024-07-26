##########################################################################
#
#  THIS FILE IS GENERATED FROM TEMPLATE. DON'T MODIFY IT
#
#  uniee_values.py
#
#  Created on: Jan 14, 2022
#      Author: Miroslav Ondra <ondra@faster.cz>
# 


class Product:
	def __init__(self, id, name, **kwargs):
		self.id = id
		self.name = name
		self.vars = kwargs

class Board:
	def __init__(self, id, name, slots, **kwargs):
		self.id = id
		self.name = name
		self.slots = slots
		self.vars = kwargs

class Slot:
	def __init__(self, slot, **kwargs):
		self.slot = slot
		self.vars = kwargs

products = {
  '271': Product(271, 'IRISx1', dt='unipi_irisx1' ),
  '527': Product(527, 'IRISx2', dt='unipi_irisx2' ),
  '783': Product(783, 'IRISx5', dt='unipi_irisx5' ),
  '1039': Product(1039, 'IRISx7', dt='unipi_irisx7' ),
  '1295': Product(1295, 'IRISx21', dt='unipi_irisx21' ),
  '1551': Product(1551, 'IRISx71', dt='unipi_irisx71' ),
}

boards = {
  '100': Board(100, 'IC_DiS4_0',{
             '11': Slot(11, dt=['060f_ic0064_slot11', 'ic0064_slot11'] , udev=['060f_ic0064_slot11', 'ic0064_slot11'] ),
             '12': Slot(12, dt=['060f_ic0064_slot12', 'ic0064_slot12'] , udev=['060f_ic0064_slot12', 'ic0064_slot12'] ),
             '21': Slot(21, dt=['060f_ic0064_slot21', 'ic0064_slot21'] , udev=['060f_ic0064_slot21', 'ic0064_slot21'] ),
             '22': Slot(22, dt=['060f_ic0064_slot22', 'ic0064_slot22'] , udev=['060f_ic0064_slot22', 'ic0064_slot22'] ),
             '32': Slot(32, dt=['060f_ic0064_slot32', 'ic0064_slot32'] , udev=['060f_ic0064_slot32', 'ic0064_slot32'] ),
             '42': Slot(42, dt=['060f_ic0064_slot42', 'ic0064_slot42'] , udev=['060f_ic0064_slot42', 'ic0064_slot42'] ),
             '52': Slot(52, dt=['060f_ic0064_slot52', 'ic0064_slot52'] , udev=['060f_ic0064_slot52', 'ic0064_slot52'] ),
             '62': Slot(62, dt=['060f_ic0064_slot62', 'ic0064_slot62'] , udev=['060f_ic0064_slot62', 'ic0064_slot62'] ),
             '72': Slot(72, dt=['060f_ic0064_slot72', 'ic0064_slot72'] , udev=['060f_ic0064_slot72', 'ic0064_slot72'] ),
    }),
  '101': Board(101, 'IC_LoRaNode_1',{
             '11': Slot(11, dt=['060f_ic0065_slot11', 'ic0065_slot11'] , udev=['060f_ic0065_slot11', 'ic0065_slot11'] ),
             '12': Slot(12, dt=['060f_ic0065_slot12', 'ic0065_slot12'] , udev=['060f_ic0065_slot12', 'ic0065_slot12'] ),
             '21': Slot(21, dt=['060f_ic0065_slot21', 'ic0065_slot21'] , udev=['060f_ic0065_slot21', 'ic0065_slot21'] ),
             '22': Slot(22, dt=['060f_ic0065_slot22', 'ic0065_slot22'] , udev=['060f_ic0065_slot22', 'ic0065_slot22'] ),
             '62': Slot(62, dt=['060f_ic0065_slot62', 'ic0065_slot62'] , udev=['060f_ic0065_slot62', 'ic0065_slot62'] ),
             '72': Slot(72, dt=['060f_ic0065_slot72', 'ic0065_slot72'] , udev=['060f_ic0065_slot72', 'ic0065_slot72'] ),
    }),
  '103': Board(103, 'IC_Light1P80_1',{
             '11': Slot(11, dt=['060f_ic0067_slot11', 'ic0067_slot11'] , udev=['060f_ic0067_slot11', 'ic0067_slot11'] ),
             '12': Slot(12, dt=['060f_ic0067_slot12', 'ic0067_slot12'] , udev=['060f_ic0067_slot12', 'ic0067_slot12'] ),
             '21': Slot(21, dt=['060f_ic0067_slot21', 'ic0067_slot21'] , udev=['060f_ic0067_slot21', 'ic0067_slot21'] ),
             '22': Slot(22, dt=['060f_ic0067_slot22', 'ic0067_slot22'] , udev=['060f_ic0067_slot22', 'ic0067_slot22'] ),
             '32': Slot(32, dt=['060f_ic0067_slot32', 'ic0067_slot32'] , udev=['060f_ic0067_slot32', 'ic0067_slot32'] ),
             '42': Slot(42, dt=['060f_ic0067_slot42', 'ic0067_slot42'] , udev=['060f_ic0067_slot42', 'ic0067_slot42'] ),
             '52': Slot(52, dt=['060f_ic0067_slot52', 'ic0067_slot52'] , udev=['060f_ic0067_slot52', 'ic0067_slot52'] ),
             '62': Slot(62, dt=['060f_ic0067_slot62', 'ic0067_slot62'] , udev=['060f_ic0067_slot62', 'ic0067_slot62'] ),
             '72': Slot(72, dt=['060f_ic0067_slot72', 'ic0067_slot72'] , udev=['060f_ic0067_slot72', 'ic0067_slot72'] ),
    }),
  '105': Board(105, 'IC_DiS2Do2_1',{
             '11': Slot(11, dt=['060f_ic0069_slot11', 'ic0069_slot11'] , udev=['060f_ic0069_slot11', 'ic0069_slot11'] ),
             '12': Slot(12, dt=['060f_ic0069_slot12', 'ic0069_slot12'] , udev=['060f_ic0069_slot12', 'ic0069_slot12'] ),
             '21': Slot(21, dt=['060f_ic0069_slot21', 'ic0069_slot21'] , udev=['060f_ic0069_slot21', 'ic0069_slot21'] ),
             '22': Slot(22, dt=['060f_ic0069_slot22', 'ic0069_slot22'] , udev=['060f_ic0069_slot22', 'ic0069_slot22'] ),
             '32': Slot(32, dt=['060f_ic0069_slot32', 'ic0069_slot32'] , udev=['060f_ic0069_slot32', 'ic0069_slot32'] ),
             '42': Slot(42, dt=['060f_ic0069_slot42', 'ic0069_slot42'] , udev=['060f_ic0069_slot42', 'ic0069_slot42'] ),
             '52': Slot(52, dt=['060f_ic0069_slot52', 'ic0069_slot52'] , udev=['060f_ic0069_slot52', 'ic0069_slot52'] ),
             '62': Slot(62, dt=['060f_ic0069_slot62', 'ic0069_slot62'] , udev=['060f_ic0069_slot62', 'ic0069_slot62'] ),
             '72': Slot(72, dt=['060f_ic0069_slot72', 'ic0069_slot72'] , udev=['060f_ic0069_slot72', 'ic0069_slot72'] ),
    }),
  '106': Board(106, 'IC_R485R485422_1',{
             '11': Slot(11, dt=['060f_ic006a_slot11', 'ic006a_slot11'] , udev=['060f_ic006a_slot11', 'ic006a_slot11'] ),
             '12': Slot(12, dt=['060f_ic006a_slot12', 'ic006a_slot12'] , udev=['060f_ic006a_slot12', 'ic006a_slot12'] ),
             '21': Slot(21, dt=['060f_ic006a_slot21', 'ic006a_slot21'] , udev=['060f_ic006a_slot21', 'ic006a_slot21'] ),
             '22': Slot(22, dt=['060f_ic006a_slot22', 'ic006a_slot22'] , udev=['060f_ic006a_slot22', 'ic006a_slot22'] ),
             '62': Slot(62, dt=['060f_ic006a_slot62', 'ic006a_slot62'] , udev=['060f_ic006a_slot62', 'ic006a_slot62'] ),
             '72': Slot(72, dt=['060f_ic006a_slot72', 'ic006a_slot72'] , udev=['060f_ic006a_slot72', 'ic006a_slot72'] ),
    }),
  '107': Board(107, 'IC_AoU4_1',{
             '11': Slot(11, dt=['060f_ic006b_slot11', 'ic006b_slot11'] , udev=['060f_ic006b_slot11', 'ic006b_slot11'] ),
             '12': Slot(12, dt=['060f_ic006b_slot12', 'ic006b_slot12'] , udev=['060f_ic006b_slot12', 'ic006b_slot12'] ),
             '21': Slot(21, dt=['060f_ic006b_slot21', 'ic006b_slot21'] , udev=['060f_ic006b_slot21', 'ic006b_slot21'] ),
             '22': Slot(22, dt=['060f_ic006b_slot22', 'ic006b_slot22'] , udev=['060f_ic006b_slot22', 'ic006b_slot22'] ),
             '32': Slot(32, dt=['060f_ic006b_slot32', 'ic006b_slot32'] , udev=['060f_ic006b_slot32', 'ic006b_slot32'] ),
             '42': Slot(42, dt=['060f_ic006b_slot42', 'ic006b_slot42'] , udev=['060f_ic006b_slot42', 'ic006b_slot42'] ),
             '52': Slot(52, dt=['060f_ic006b_slot52', 'ic006b_slot52'] , udev=['060f_ic006b_slot52', 'ic006b_slot52'] ),
             '62': Slot(62, dt=['060f_ic006b_slot62', 'ic006b_slot62'] , udev=['060f_ic006b_slot62', 'ic006b_slot62'] ),
             '72': Slot(72, dt=['060f_ic006b_slot72', 'ic006b_slot72'] , udev=['060f_ic006b_slot72', 'ic006b_slot72'] ),
    }),
  '108': Board(108, 'ID_AiUC8_1',{
             '12': Slot(12, dt=['060f_id006c_slot12', 'id006c_slot12'] , udev=['060f_id006c_slot12', 'id006c_slot12'] ),
             '22': Slot(22, dt=['060f_id006c_slot22', 'id006c_slot22'] , udev=['060f_id006c_slot22', 'id006c_slot22'] ),
             '32': Slot(32, dt=['060f_id006c_slot32', 'id006c_slot32'] , udev=['060f_id006c_slot32', 'id006c_slot32'] ),
             '42': Slot(42, dt=['060f_id006c_slot42', 'id006c_slot42'] , udev=['060f_id006c_slot42', 'id006c_slot42'] ),
             '52': Slot(52, dt=['060f_id006c_slot52', 'id006c_slot52'] , udev=['060f_id006c_slot52', 'id006c_slot52'] ),
             '62': Slot(62, dt=['060f_id006c_slot62', 'id006c_slot62'] , udev=['060f_id006c_slot62', 'id006c_slot62'] ),
             '72': Slot(72, dt=['060f_id006c_slot72', 'id006c_slot72'] , udev=['060f_id006c_slot72', 'id006c_slot72'] ),
    }),
  '109': Board(109, 'ID_AiRTD8_1',{
             '12': Slot(12, dt=['060f_id006d_slot12', 'id006d_slot12'] , udev=['060f_id006d_slot12', 'id006d_slot12'] ),
             '22': Slot(22, dt=['060f_id006d_slot22', 'id006d_slot22'] , udev=['060f_id006d_slot22', 'id006d_slot22'] ),
             '32': Slot(32, dt=['060f_id006d_slot32', 'id006d_slot32'] , udev=['060f_id006d_slot32', 'id006d_slot32'] ),
             '42': Slot(42, dt=['060f_id006d_slot42', 'id006d_slot42'] , udev=['060f_id006d_slot42', 'id006d_slot42'] ),
             '52': Slot(52, dt=['060f_id006d_slot52', 'id006d_slot52'] , udev=['060f_id006d_slot52', 'id006d_slot52'] ),
             '62': Slot(62, dt=['060f_id006d_slot62', 'id006d_slot62'] , udev=['060f_id006d_slot62', 'id006d_slot62'] ),
             '72': Slot(72, dt=['060f_id006d_slot72', 'id006d_slot72'] , udev=['060f_id006d_slot72', 'id006d_slot72'] ),
    }),
  '111': Board(111, 'ID_Do8_1',{
             '12': Slot(12, dt=['060f_id006f_slot12', 'id006f_slot12'] , udev=['060f_id006f_slot12', 'id006f_slot12'] ),
             '22': Slot(22, dt=['060f_id006f_slot22', 'id006f_slot22'] , udev=['060f_id006f_slot22', 'id006f_slot22'] ),
             '32': Slot(32, dt=['060f_id006f_slot32', 'id006f_slot32'] , udev=['060f_id006f_slot32', 'id006f_slot32'] ),
             '42': Slot(42, dt=['060f_id006f_slot42', 'id006f_slot42'] , udev=['060f_id006f_slot42', 'id006f_slot42'] ),
             '52': Slot(52, dt=['060f_id006f_slot52', 'id006f_slot52'] , udev=['060f_id006f_slot52', 'id006f_slot52'] ),
             '62': Slot(62, dt=['060f_id006f_slot62', 'id006f_slot62'] , udev=['060f_id006f_slot62', 'id006f_slot62'] ),
             '72': Slot(72, dt=['060f_id006f_slot72', 'id006f_slot72'] , udev=['060f_id006f_slot72', 'id006f_slot72'] ),
    }),
  '112': Board(112, 'IC_CANFD_1',{
             '11': Slot(11, dt=['060f_ic0070_slot11', 'ic0070_slot11'] ),
             '12': Slot(12, dt=['060f_ic0070_slot12', 'ic0070_slot12'] ),
             '21': Slot(21, dt=['060f_ic0070_slot21', 'ic0070_slot21'] ),
             '22': Slot(22, dt=['060f_ic0070_slot22', 'ic0070_slot22'] ),
             '32': Slot(32, dt=['060f_ic0070_slot32', 'ic0070_slot32'] ),
             '42': Slot(42, dt=['060f_ic0070_slot42', 'ic0070_slot42'] ),
             '52': Slot(52, dt=['060f_ic0070_slot52', 'ic0070_slot52'] ),
             '62': Slot(62, dt=['060f_ic0070_slot62', 'ic0070_slot62'] ),
             '72': Slot(72, dt=['060f_ic0070_slot72', 'ic0070_slot72'] ),
    }),
  '113': Board(113, 'IC_Eth100_1',{
             '11': Slot(11, udev=['060f_ic0071_slot11', 'ic0071_slot11'] ),
             '12': Slot(12, udev=['060f_ic0071_slot12', 'ic0071_slot12'] ),
             '21': Slot(21, udev=['060f_ic0071_slot21', 'ic0071_slot21'] ),
             '22': Slot(22, udev=['060f_ic0071_slot22', 'ic0071_slot22'] ),
             '32': Slot(32, udev=['060f_ic0071_slot32', 'ic0071_slot32'] ),
             '42': Slot(42, udev=['060f_ic0071_slot42', 'ic0071_slot42'] ),
             '52': Slot(52, udev=['060f_ic0071_slot52', 'ic0071_slot52'] ),
             '62': Slot(62, udev=['060f_ic0071_slot62', 'ic0071_slot62'] ),
             '72': Slot(72, udev=['060f_ic0071_slot72', 'ic0071_slot72'] ),
    }),
  '114': Board(114, 'IC_R232_1',{
             '11': Slot(11, dt=['060f_ic0072_slot11', 'ic0072_slot11'] , udev=['060f_ic0072_slot11', 'ic0072_slot11'] ),
             '12': Slot(12, dt=['060f_ic0072_slot12', 'ic0072_slot12'] , udev=['060f_ic0072_slot12', 'ic0072_slot12'] ),
             '21': Slot(21, dt=['060f_ic0072_slot21', 'ic0072_slot21'] , udev=['060f_ic0072_slot21', 'ic0072_slot21'] ),
             '22': Slot(22, dt=['060f_ic0072_slot22', 'ic0072_slot22'] , udev=['060f_ic0072_slot22', 'ic0072_slot22'] ),
             '62': Slot(62, dt=['060f_ic0072_slot62', 'ic0072_slot62'] , udev=['060f_ic0072_slot62', 'ic0072_slot62'] ),
             '72': Slot(72, dt=['060f_ic0072_slot72', 'ic0072_slot72'] , udev=['060f_ic0072_slot72', 'ic0072_slot72'] ),
    }),
  '115': Board(115, 'ID_SATA_1',{
             '12': Slot(12, udev=['050f_id0073_slot12', '060f_id0073_slot12', 'id0073_slot12'] ),
             '22': Slot(22, udev=['060f_id0073_slot22', 'id0073_slot22'] ),
             '32': Slot(32, udev=['060f_id0073_slot32', 'id0073_slot32'] ),
             '42': Slot(42, udev=['060f_id0073_slot42', 'id0073_slot42'] ),
    }),
  '116': Board(116, 'ID_LTE_1',{
             '12': Slot(12, dt=['060f_id0074_slot12', 'id0074_slot12'] , udev=['050f_id0074_slot12', '060f_id0074_slot12', 'id0074_slot12'] , has_lte=['1'] ),
             '22': Slot(22, dt=['060f_id0074_slot22', 'id0074_slot22'] , udev=['060f_id0074_slot22', 'id0074_slot22'] , has_lte=['1'] ),
             '32': Slot(32, dt=['060f_id0074_slot32', 'id0074_slot32'] , udev=['060f_id0074_slot32', 'id0074_slot32'] , has_lte=['1'] ),
             '42': Slot(42, dt=['060f_id0074_slot42', 'id0074_slot42'] , udev=['060f_id0074_slot42', 'id0074_slot42'] , has_lte=['1'] ),
    }),
  '117': Board(117, 'IC_GPS_1',{
             '11': Slot(11, dt=['060f_ic0075_slot11', 'ic0075_slot11'] , udev=['060f_ic0075_slot11', 'ic0075_slot11'] ),
             '12': Slot(12, dt=['060f_ic0075_slot12', 'ic0075_slot12'] , udev=['060f_ic0075_slot12', 'ic0075_slot12'] ),
             '21': Slot(21, dt=['060f_ic0075_slot21', 'ic0075_slot21'] , udev=['060f_ic0075_slot21', 'ic0075_slot21'] ),
             '22': Slot(22, dt=['060f_ic0075_slot22', 'ic0075_slot22'] , udev=['060f_ic0075_slot22', 'ic0075_slot22'] ),
             '62': Slot(62, dt=['060f_ic0075_slot62', 'ic0075_slot62'] , udev=['060f_ic0075_slot62', 'ic0075_slot62'] ),
             '72': Slot(72, dt=['060f_ic0075_slot72', 'ic0075_slot72'] , udev=['060f_ic0075_slot72', 'ic0075_slot72'] ),
    }),
  '118': Board(118, 'IC_AccGyro_1',{
             '11': Slot(11, dt=['060f_ic0076_slot11', 'ic0076_slot11'] , udev=['060f_ic0076_slot11', 'ic0076_slot11'] ),
             '12': Slot(12, dt=['060f_ic0076_slot12', 'ic0076_slot12'] , udev=['060f_ic0076_slot12', 'ic0076_slot12'] ),
             '21': Slot(21, dt=['060f_ic0076_slot21', 'ic0076_slot21'] , udev=['060f_ic0076_slot21', 'ic0076_slot21'] ),
             '22': Slot(22, dt=['060f_ic0076_slot22', 'ic0076_slot22'] , udev=['060f_ic0076_slot22', 'ic0076_slot22'] ),
             '32': Slot(32, dt=['060f_ic0076_slot32', 'ic0076_slot32'] , udev=['060f_ic0076_slot32', 'ic0076_slot32'] ),
             '42': Slot(42, dt=['060f_ic0076_slot42', 'ic0076_slot42'] , udev=['060f_ic0076_slot42', 'ic0076_slot42'] ),
             '52': Slot(52, dt=['060f_ic0076_slot52', 'ic0076_slot52'] , udev=['060f_ic0076_slot52', 'ic0076_slot52'] ),
             '62': Slot(62, dt=['060f_ic0076_slot62', 'ic0076_slot62'] , udev=['060f_ic0076_slot62', 'ic0076_slot62'] ),
             '72': Slot(72, dt=['060f_ic0076_slot72', 'ic0076_slot72'] , udev=['060f_ic0076_slot72', 'ic0076_slot72'] ),
    }),
  '119': Board(119, 'IC_Di1Ro2_1',{
             '11': Slot(11, dt=['060f_ic0077_slot11', 'ic0077_slot11'] , udev=['060f_ic0077_slot11', 'ic0077_slot11'] ),
             '12': Slot(12, dt=['060f_ic0077_slot12', 'ic0077_slot12'] , udev=['060f_ic0077_slot12', 'ic0077_slot12'] ),
             '21': Slot(21, dt=['060f_ic0077_slot21', 'ic0077_slot21'] , udev=['060f_ic0077_slot21', 'ic0077_slot21'] ),
             '22': Slot(22, dt=['060f_ic0077_slot22', 'ic0077_slot22'] , udev=['060f_ic0077_slot22', 'ic0077_slot22'] ),
             '32': Slot(32, dt=['060f_ic0077_slot32', 'ic0077_slot32'] , udev=['060f_ic0077_slot32', 'ic0077_slot32'] ),
             '42': Slot(42, dt=['060f_ic0077_slot42', 'ic0077_slot42'] , udev=['060f_ic0077_slot42', 'ic0077_slot42'] ),
             '52': Slot(52, dt=['060f_ic0077_slot52', 'ic0077_slot52'] , udev=['060f_ic0077_slot52', 'ic0077_slot52'] ),
             '62': Slot(62, dt=['060f_ic0077_slot62', 'ic0077_slot62'] , udev=['060f_ic0077_slot62', 'ic0077_slot62'] ),
             '72': Slot(72, dt=['060f_ic0077_slot72', 'ic0077_slot72'] , udev=['060f_ic0077_slot72', 'ic0077_slot72'] ),
    }),
  '120': Board(120, 'ID_DiS16_1',{
             '12': Slot(12, dt=['060f_id0078_slot12', 'id0078_slot12'] , udev=['060f_id0078_slot12', 'id0078_slot12'] ),
             '22': Slot(22, dt=['060f_id0078_slot22', 'id0078_slot22'] , udev=['060f_id0078_slot22', 'id0078_slot22'] ),
             '32': Slot(32, dt=['060f_id0078_slot32', 'id0078_slot32'] , udev=['060f_id0078_slot32', 'id0078_slot32'] ),
             '42': Slot(42, dt=['060f_id0078_slot42', 'id0078_slot42'] , udev=['060f_id0078_slot42', 'id0078_slot42'] ),
             '52': Slot(52, dt=['060f_id0078_slot52', 'id0078_slot52'] , udev=['060f_id0078_slot52', 'id0078_slot52'] ),
             '62': Slot(62, dt=['060f_id0078_slot62', 'id0078_slot62'] , udev=['060f_id0078_slot62', 'id0078_slot62'] ),
             '72': Slot(72, dt=['060f_id0078_slot72', 'id0078_slot72'] , udev=['060f_id0078_slot72', 'id0078_slot72'] ),
    }),
  '121': Board(121, 'ID_Do16_1',{
             '12': Slot(12, dt=['060f_id0079_slot12', 'id0079_slot12'] , udev=['060f_id0079_slot12', 'id0079_slot12'] ),
             '22': Slot(22, dt=['060f_id0079_slot22', 'id0079_slot22'] , udev=['060f_id0079_slot22', 'id0079_slot22'] ),
             '32': Slot(32, dt=['060f_id0079_slot32', 'id0079_slot32'] , udev=['060f_id0079_slot32', 'id0079_slot32'] ),
             '42': Slot(42, dt=['060f_id0079_slot42', 'id0079_slot42'] , udev=['060f_id0079_slot42', 'id0079_slot42'] ),
             '52': Slot(52, dt=['060f_id0079_slot52', 'id0079_slot52'] , udev=['060f_id0079_slot52', 'id0079_slot52'] ),
             '62': Slot(62, dt=['060f_id0079_slot62', 'id0079_slot62'] , udev=['060f_id0079_slot62', 'id0079_slot62'] ),
             '72': Slot(72, dt=['060f_id0079_slot72', 'id0079_slot72'] , udev=['060f_id0079_slot72', 'id0079_slot72'] ),
    }),
  '122': Board(122, 'ID_R232x4_1',{
             '12': Slot(12, udev=['050f_id007a_slot12', '060f_id007a_slot12', 'id007a_slot12'] ),
             '22': Slot(22, udev=['060f_id007a_slot22', 'id007a_slot22'] ),
             '32': Slot(32, udev=['060f_id007a_slot32', 'id007a_slot32'] ),
             '42': Slot(42, udev=['060f_id007a_slot42', 'id007a_slot42'] ),
    }),
  '123': Board(123, 'ID_AiUC8_2',{
             '12': Slot(12, dt=['060f_id007b_slot12', 'id007b_slot12'] , udev=['060f_id007b_slot12', 'id007b_slot12'] ),
             '22': Slot(22, dt=['060f_id007b_slot22', 'id007b_slot22'] , udev=['060f_id007b_slot22', 'id007b_slot22'] ),
             '32': Slot(32, dt=['060f_id007b_slot32', 'id007b_slot32'] , udev=['060f_id007b_slot32', 'id007b_slot32'] ),
             '42': Slot(42, dt=['060f_id007b_slot42', 'id007b_slot42'] , udev=['060f_id007b_slot42', 'id007b_slot42'] ),
             '52': Slot(52, dt=['060f_id007b_slot52', 'id007b_slot52'] , udev=['060f_id007b_slot52', 'id007b_slot52'] ),
             '62': Slot(62, dt=['060f_id007b_slot62', 'id007b_slot62'] , udev=['060f_id007b_slot62', 'id007b_slot62'] ),
             '72': Slot(72, dt=['060f_id007b_slot72', 'id007b_slot72'] , udev=['060f_id007b_slot72', 'id007b_slot72'] ),
    }),
  '124': Board(124, 'IC_DiS4_1',{
             '11': Slot(11, dt=['060f_ic007c_slot11', 'ic007c_slot11'] , udev=['060f_ic007c_slot11', 'ic007c_slot11'] ),
             '12': Slot(12, dt=['060f_ic007c_slot12', 'ic007c_slot12'] , udev=['060f_ic007c_slot12', 'ic007c_slot12'] ),
             '21': Slot(21, dt=['060f_ic007c_slot21', 'ic007c_slot21'] , udev=['060f_ic007c_slot21', 'ic007c_slot21'] ),
             '22': Slot(22, dt=['060f_ic007c_slot22', 'ic007c_slot22'] , udev=['060f_ic007c_slot22', 'ic007c_slot22'] ),
             '32': Slot(32, dt=['060f_ic007c_slot32', 'ic007c_slot32'] , udev=['060f_ic007c_slot32', 'ic007c_slot32'] ),
             '42': Slot(42, dt=['060f_ic007c_slot42', 'ic007c_slot42'] , udev=['060f_ic007c_slot42', 'ic007c_slot42'] ),
             '52': Slot(52, dt=['060f_ic007c_slot52', 'ic007c_slot52'] , udev=['060f_ic007c_slot52', 'ic007c_slot52'] ),
             '62': Slot(62, dt=['060f_ic007c_slot62', 'ic007c_slot62'] , udev=['060f_ic007c_slot62', 'ic007c_slot62'] ),
             '72': Slot(72, dt=['060f_ic007c_slot72', 'ic007c_slot72'] , udev=['060f_ic007c_slot72', 'ic007c_slot72'] ),
    }),
  '125': Board(125, 'IC_Ai2Ao1_1',{
             '11': Slot(11, dt=['060f_ic007d_slot11', 'ic007d_slot11'] , udev=['060f_ic007d_slot11', 'ic007d_slot11'] ),
             '12': Slot(12, dt=['060f_ic007d_slot12', 'ic007d_slot12'] , udev=['060f_ic007d_slot12', 'ic007d_slot12'] ),
             '21': Slot(21, dt=['060f_ic007d_slot21', 'ic007d_slot21'] , udev=['060f_ic007d_slot21', 'ic007d_slot21'] ),
             '22': Slot(22, dt=['060f_ic007d_slot22', 'ic007d_slot22'] , udev=['060f_ic007d_slot22', 'ic007d_slot22'] ),
             '32': Slot(32, dt=['060f_ic007d_slot32', 'ic007d_slot32'] , udev=['060f_ic007d_slot32', 'ic007d_slot32'] ),
             '42': Slot(42, dt=['060f_ic007d_slot42', 'ic007d_slot42'] , udev=['060f_ic007d_slot42', 'ic007d_slot42'] ),
             '52': Slot(52, dt=['060f_ic007d_slot52', 'ic007d_slot52'] , udev=['060f_ic007d_slot52', 'ic007d_slot52'] ),
             '62': Slot(62, dt=['060f_ic007d_slot62', 'ic007d_slot62'] , udev=['060f_ic007d_slot62', 'ic007d_slot62'] ),
             '72': Slot(72, dt=['060f_ic007d_slot72', 'ic007d_slot72'] , udev=['060f_ic007d_slot72', 'ic007d_slot72'] ),
    }),
  '126': Board(126, 'ID_Em3f_1',{
             '12': Slot(12, dt=['060f_id007e_slot12', 'id007e_slot12'] ),
             '22': Slot(22, dt=['060f_id007e_slot22', 'id007e_slot22'] ),
             '32': Slot(32, dt=['060f_id007e_slot32', 'id007e_slot32'] ),
             '42': Slot(42, dt=['060f_id007e_slot42', 'id007e_slot42'] ),
             '52': Slot(52, dt=['060f_id007e_slot52', 'id007e_slot52'] ),
             '62': Slot(62, dt=['060f_id007e_slot62', 'id007e_slot62'] ),
             '72': Slot(72, dt=['060f_id007e_slot72', 'id007e_slot72'] ),
    }),
  '127': Board(127, 'IC_LoRaNode_2',{
             '11': Slot(11, dt=['060f_ic007f_slot11', 'ic007f_slot11'] , udev=['060f_ic007f_slot11', 'ic007f_slot11'] ),
             '12': Slot(12, dt=['060f_ic007f_slot12', 'ic007f_slot12'] , udev=['060f_ic007f_slot12', 'ic007f_slot12'] ),
             '21': Slot(21, dt=['060f_ic007f_slot21', 'ic007f_slot21'] , udev=['060f_ic007f_slot21', 'ic007f_slot21'] ),
             '22': Slot(22, dt=['060f_ic007f_slot22', 'ic007f_slot22'] , udev=['060f_ic007f_slot22', 'ic007f_slot22'] ),
             '62': Slot(62, dt=['060f_ic007f_slot62', 'ic007f_slot62'] , udev=['060f_ic007f_slot62', 'ic007f_slot62'] ),
             '72': Slot(72, dt=['060f_ic007f_slot72', 'ic007f_slot72'] , udev=['060f_ic007f_slot72', 'ic007f_slot72'] ),
    }),
  '128': Board(128, 'IC_Zigbee_1',{
             '11': Slot(11, dt=['060f_ic0080_slot11', 'ic0080_slot11'] , udev=['060f_ic0080_slot11', 'ic0080_slot11'] ),
             '12': Slot(12, dt=['060f_ic0080_slot12', 'ic0080_slot12'] , udev=['060f_ic0080_slot12', 'ic0080_slot12'] ),
             '21': Slot(21, dt=['060f_ic0080_slot21', 'ic0080_slot21'] , udev=['060f_ic0080_slot21', 'ic0080_slot21'] ),
             '22': Slot(22, dt=['060f_ic0080_slot22', 'ic0080_slot22'] , udev=['060f_ic0080_slot22', 'ic0080_slot22'] ),
             '62': Slot(62, dt=['060f_ic0080_slot62', 'ic0080_slot62'] , udev=['060f_ic0080_slot62', 'ic0080_slot62'] ),
             '72': Slot(72, dt=['060f_ic0080_slot72', 'ic0080_slot72'] , udev=['060f_ic0080_slot72', 'ic0080_slot72'] ),
    }),
  '1000': Board(1000, 'IC_IQRF_1',{
             '11': Slot(11, dt=['060f_ic03e8_slot11', 'ic03e8_slot11'] , udev=['060f_ic03e8_slot11', 'ic03e8_slot11'] ),
             '12': Slot(12, dt=['060f_ic03e8_slot12', 'ic03e8_slot12'] , udev=['060f_ic03e8_slot12', 'ic03e8_slot12'] ),
             '21': Slot(21, dt=['060f_ic03e8_slot21', 'ic03e8_slot21'] , udev=['060f_ic03e8_slot21', 'ic03e8_slot21'] ),
             '22': Slot(22, dt=['060f_ic03e8_slot22', 'ic03e8_slot22'] , udev=['060f_ic03e8_slot22', 'ic03e8_slot22'] ),
             '62': Slot(62, dt=['060f_ic03e8_slot62', 'ic03e8_slot62'] , udev=['060f_ic03e8_slot62', 'ic03e8_slot62'] ),
             '72': Slot(72, dt=['060f_ic03e8_slot72', 'ic03e8_slot72'] , udev=['060f_ic03e8_slot72', 'ic03e8_slot72'] ),
    }),
  '1001': Board(1001, 'ID_Eth100Di1WiFi_1',{
             '12': Slot(12, dt=['060f_id03e9_slot12', 'id03e9_slot12'] , udev=['060f_id03e9_slot12', 'id03e9_slot12'] ),
             '22': Slot(22, dt=['060f_id03e9_slot22', 'id03e9_slot22'] , udev=['060f_id03e9_slot22', 'id03e9_slot22'] ),
             '62': Slot(62, dt=['060f_id03e9_slot62', 'id03e9_slot62'] , udev=['060f_id03e9_slot62', 'id03e9_slot62'] ),
             '72': Slot(72, dt=['060f_id03e9_slot72', 'id03e9_slot72'] , udev=['060f_id03e9_slot72', 'id03e9_slot72'] ),
    }),
}

# Family names
family = {
  '1': 'UNIPI1',
  '2': 'G1XX',
  '3': 'NEURON',
  '5': 'AXON',
  '6': 'CM40',
  '7': 'PATRON',
  '15': 'IRIS',
  '16': 'OEM',
}

def unipi_product_info(product_id, version=None):
	''' return product_info or none '''
	return products.get(str(product_id), None)

def unipi_product_info_by_name(product_name, version=None):
	''' return product_info or none '''
	for k,v in products.items():
		if v.name.lower() == product_name.lower(): 
			return v
	return None

def unipi_board_info(board_id, slot=None, version=None):
	''' return board_info or None '''
	board_info = boards.get(str(board_id), None)
	if slot == None or board_info == None:
		return board_info
	if board_info.slots is None:
		return None
	return board_info.slots.get(str(slot), None)


def unipi_family_name(product_id):
	''' return family name or none '''
	return family.get(str(product_id & 0xff), None)
