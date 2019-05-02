from collections import namedtuple
import unittest

# Named tuples assign meaning to each position in a tuple and allow for more readable,
# self-documenting code. They can be used wherever regular tuples are used, and they add
# the ability to access fields by name instead of position index.
# collections.namedtuple(typename, field_names[, verbose=False][, rename=False])

block = namedtuple('block', ['footprint', 'value'])

block_name1 = 'U1'
block_name2 = 'R3'
block_name3 = 'R1'
block_name4 = 'R2'
block_name5 = 'C1'
block_name6 = 'C2'
block_name7 = 'D1'
test_block1 = block('Package_DIP:DIP-4_W7.62mm', 'LM555')
test_block2 = block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '1k')
test_block3 = block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '4k7')
test_block4 = block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '10k')
test_block5 = block('Capacitor_SMD:CP_Elec_3x5.3', '100\u03BCF')
test_block6 = block('Capacitor_SMD:C_0201_0603Metric', '10n')
test_block7 = block('LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder', 'LED')


blocks = {block_name1: test_block1,
          block_name2: test_block2,
          block_name3: test_block3,
          block_name4: test_block4,
          block_name5: test_block5,
          block_name6: test_block6,
          block_name7: test_block7
          }


pin = namedtuple('pin', ['block_name', 'pin_name'])

net1 = 'Net-(R3-Pad1)'
pin1 = [pin('U1', '3'), pin('R3', '1')]
net2 = 'Net-(C1-Pad1)'
pin2 = [pin('U1', '2'), pin('U1', '5'), pin('U1', '6'), pin('R2', '2'), pin('C1', '1'), pin('C2', '1')]
net3 = 'Net-(R1-Pad2)'
pin3 = [pin('R2', '1'), pin('R1', '2'), pin('U1', '7')]
net4 = '+9V'
pin4 = [pin('R1', '1'), pin('U1', '4'), pin('U1', '8')]
net5 = 'GND'
pin5 = [pin('D1', '1'), pin('C2', '2'), pin('C1', '2'), pin('U1', '1')]
net6 = 'Net-(D1-Pad2)'
pin6 = [pin('D1', '2'), pin('R3', '2')]

nets = {net1: pin1,
        net2: pin2,
        net3: pin3,
        net4: pin4,
        net5: pin5,
        net6: pin6
        }

# Arguments:
# blocks: Dict[str, Block] (block_name to Block definition)
# nets: Dict[str, List[Pin]] (net name to list of connected pins)

def print_block_comp(block_name: str) -> str:
    return '(comp (ref {})'.format(block_name)

def print_block_value(block_value: str) -> str:
    return '(value {})'.format(block_value)

def print_block_footprint(block_footprint: str) -> str:
    return '(footprint {})'.format(block_footprint)

def print_block_tstamp(block_name: str) -> str:
    return '(tstamp {}))'.format(block_name)


def block_exp(dict: dict) -> str:
        """Given a dictionary of block_names (strings) as keys and Blocks (namedtuples) as corresponding values

        Example:
        (components
        (comp (ref U1)
        (value LM555)
        (footprint Package_DIP:DIP-4_W7.62mm)
        (tstamp U1))
        (comp (ref R3)
        (value 1k)
        (footprint OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical)
        (tstamp R3))

        """
        # assert len(dict) > 0, "Please pass in at least one block."

        # for name, b in dict.items():
        #         if not type(name) == type(""): 
        #                 raise TypeError("Please pass in a valid block name.")
        #         elif not type(b) == type(test_block1):
        #                 raise TypeError("Please pass in a valid block.")

        result = '(components ' 
        for (block_name, block) in dict.items():
            result += print_block_comp(block_name) + ' ' + print_block_value(block.value) + ' ' + print_block_footprint(block.footprint) + ' ' + print_block_tstamp(block_name) + ' '
        return result + ')'

        # for (block_name, block) in dict.items():  
                # print('(comp (ref {})'.format(block_name))
                # print('(value {})'.format(block.value))
                # print('(footprint {})'.format(block.footprint))
                # print('(tstamp {}))'.format(block_name))




def print_net_header(net_count: int, net_name: str) -> str:
    return '(net (code {}) (name "{}")'.format(net_count, net_name)

def print_net_pin(block_name: str, pin_name: str) -> str:
    return "(node (ref {}) (pin {})))".format(block_name, pin_name)

def connections_exp(dict: dict) -> str:
        """Given a dictionary of net names (strings) as keys and a list of connected Pins (namedtuples) as corresponding values

        Example:
        (nets
            (net (code 1) (name "Net-(R1-Pad2)")
              (node (ref R2) (pin 1))
              (node (ref R1) (pin 2)))
            (net (code 3) (name GND)
              (node (ref C2) (pin 2))
              (node (ref C1) (pin 2))
              (node (ref R4) (pin 2)))
              
        """
        # assert len(dict) > 0, "Please pass in at least one block."

        # for name, pin_list in dict.items():
        #         if not type(name) == type(""):
        #                 raise TypeError("Please pass in a valid net name.")
        #         elif not type(pin_list) == type([]):
        #                 raise TypeError("Please pass in a valid list of pins.")
        #         else:
        #                 for p in pin_list:
        #                         if not type(p) == type(pin1[0]):
        #                                 raise TypeError("Please pass in a valid pin.")
        #                         assert len(p) > 0, "Please pass in at least one pin."
        
        result = '(nets '
        net_count = 1
        for (net_name, pin_list) in dict.items():
            result += print_net_header(net_count, net_name) + ' '
            net_count += 1
            for i in range(len(pin_list)):
                pin = pin_list[i]
                result += print_net_pin(pin.block_name, pin.pin_name) + ' '
        return result + ')'

        # print('(nets')
        # net_count = 1
        # for (net_name, pin_list) in dict.items():
        #         print('(net (code {}) (name "{}")'.format(net_count, net_name))
        #         net_count += 1
                
        #         for i in range(len(pin_list)):
        #                 pin = pin_list[i]
        #                 if i < len(pin_list) - 1:
        #                         print("(node (ref {}) (pin {}))".format(pin.block_name, pin.pin_name))
        #                 else:
        #                         print("(node (ref {}) (pin {})))".format(pin.block_name, pin.pin_name))
        # print(')')


block_exp(blocks)
connections_exp(nets)

#######################################################################################################################################################################################
###################### Unit Testing ###################################################################################################################################################
#######################################################################################################################################################################################

class TestNetlistExp(unittest.TestCase):
        def test_block_exp(self):
                dict1 = {'A': block('Capacitor', '10k'), 'B': block('LED', 'LED')}
                self.assertEqual(block_exp(dict1),
                        '(components (comp (ref A) (value 10k) (footprint Capacitor) (tstamp A)) (comp (ref B) (value LED) (footprint LED) (tstamp B)))')

                dict2 = {'C': 'Device', 'B': block('LED', 'LED')}
                with self.assertRaises(TypeError):
                    block_exp(dict2)

                dict3 = {}
                with self.assertRaises(AssertionError):
                    block_exp(dict3)

                dict4 = {'A': block('Capacitor', '10k'), 'B': pin('LED', 'LED')}
                with self.assertRaises(TypeError):
                    block_exp(dict4)

                dict5 = {1: block('Capacitor', '10k'), 2: block('LED', 'LED')}
                with self.assertRaises(TypeError):
                    block_exp(dict5)

                
        def test_connections_exp(self):
                dict1 = {'Net1': [pin('U1', '3'), pin('U2', '1')], 'Net2': [pin('R2', '4'), pin('R3', '1')], 'Net3': [pin('C1', '1'), pin('C3', '2')]}
                self.assertEqual(connections_exp(dict1),
                        '(nets (net (code 1) (name "Net1") (node (ref U1) (pin 3))) (node (ref U2) (pin 1))) (net (code 2) (name "Net2") (node (ref R2) (pin 4))) (node (ref R3) (pin 1))) (net (code 3) (name "Net3") (node (ref C1) (pin 1))) (node (ref C3) (pin 2))) )')
                
                dict2 = {'Net3': [], 'Net4': [pin('R2', '4'), pin('R3', '1')]}
                with self.assertRaises(AssertionError):
                    connections_exp(dict2)
                
                dict3 = {}
                with self.assertRaises(AssertionError):
                    connections_exp(dict3)

                dict4 = {'Net1': [pin('U1', '3'), pin('U2', '1')], 'Net2': [block('R2', '4'), pin('R3', '1')]}
                with self.assertRaises(TypeError):
                    connections_exp(dict4)

                dict5 = {1: [pin('U1', '3'), pin('U2', '1')], 2: [block('R2', '4'), pin('R3', '1')]}
                with self.assertRaises(TypeError):
                    connections_exp(dict5)


if __name__ == '__main__':
    unittest.main()