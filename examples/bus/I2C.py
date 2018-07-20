"""
NI ELVIS III Inter-Integrated Circuit (I2C) Example
This example illustrates how to write data to or read data from an I2C slave
device through the I2C channels. The program first defines the configuration
for the I2C communication, then writes to and reads from the I2C device in a
loop. Each time the write is called a list of hexadecimal data is written to
the I2C device; each time the read is called a list of data is returned from
the I2C device.

The I2C configuration consists of two parameters: bank and mode. There are two
identical banks of I2C port (A and B). There are two speeds of I2C
communication (standard and fast).

To read data from and write data to the I2C slave device, you must specify an
address in 7 bits. The NI ELVIS III helper library (academicIO) will left
shift the address and insert the read/write bit based on the function been
called to match the I2C standard. After that, it will become a 8 bits address.
The first 7 bits represent the device address and the last bit represents the
mode operation (read mode or write mode).

See https://www.nxp.com/docs/en/user-guide/UM10204.pdf for more details about
I2C.

This example illustrates how to set the ADXL345 device to measure mode by
setting the power control register (0x2D).

See http://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf
for more details about ADXL345. See page 25 for more details about power
control register.

This example uses:
    1. Bank A, I2C.SCL.
    2. Bank A, I2C.SDA.

Hardware setup:
    1. Connect an I2C.SCL of a slave device to I2C.SCL (DIO14) on bank A.
    2. Connect an I2C.SDA of a slave device to I2C.SDA (DIO15) on bank A.

Result:
    The program sets the I2C device to measure mode and reads back the value
    from the same register of the I2C slave device for validation. The
    returned value should be 8 in decimal.
"""
import time
import sys
sys.path.append('source/nielvisiii')
import academicIO
from enums import Bank, I2CSpeedMode

# specify the bank
bank = Bank.A
# specify the mode of operation that this program uses to communicate with the
# I2C slave device
speed = I2CSpeedMode.STANDARD

# open an I2C session
with academicIO.I2C(bank, speed) as I2C:
    # specify the 7-bit address, in hexadecimal
    # we use the chip ADXL345 for this example and its slave device address is
    # 0x53. You might need to change the slave device address depends on the
    # device you have.
    slave_device_address = 0x53

    # specify the bytes to write to the I2C slave device
    # the first parameter of the write function is 0x2D which represents to
    # the power control register of ADXL345, and the second parameter of the
    # write function is the value to write to the register. 0x08 sets the
    # bit 3 of the power control register to high which sets the device to
    # measure mode.
    data_to_write = [0x2D, 0x08]
    # write data to the I2C slave device
    I2C.write(slave_device_address, data_to_write)

    # specify the number of bytes to read from the I2C slave device
    number_bytes_to_read = 1
    # read data from the I2C slave device
    return_value = I2C.read(slave_device_address, number_bytes_to_read)
    # print the data
    print return_value