from lib.serial import Serial
import machine

uart_id = 0x01
modbus_obj = Serial(uart_id, pins=('P0', 'P1'))

slave_addr = 0x0A
starting_address = 0x00
register_qty = 100
signed=True

register_value = modbus_obj.read_input_registers(slave_addr, starting_address, register_quantity, signed)
print('Input register value: ' + ' '.join('{:d}'.format(x) for x in register_value))
