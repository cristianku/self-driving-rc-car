import smbus
import time

import scipy.integrate as integrate

class accelerometr():

    def __init__(self):
      self.velocity_ms = 0
      self.velocity = 0
      self.lastdisplay = time.time()

      self.xAccl_array = [0,0,0]

      self.yAccl_array = []
      self.g = 0

    def read_acc(self):
            # Get I2C bus
            bus = smbus.SMBus(1)

            # LSM303DLHC Accl address, 0x19(25)
            # Select control register1, 0x20(32)
            #		0x27(39)	Acceleration data rate = 10Hz, Power ON, X, Y, Z axis enabled
            bus.write_byte_data(0x19, 0x20, 0x27)
            # LSM303DLHC Accl address, 0x19(25)
            # Select control register4, 0x23(35)
            #		0x00(00)	Continuos update, Full scale selection = +/-2g,
            bus.write_byte_data(0x19, 0x23, 0x00)

            time.sleep(0.01)

            # LSM303DLHC Accl address, 0x19(25)
            # Read data back from 0x28(40), 2 bytes
            # X-Axis Accl LSB, X-Axis Accl MSB
            self.curr_time = time.time()
            data0 = bus.read_byte_data(0x19, 0x28)
            data1 = bus.read_byte_data(0x19, 0x29)
            self.after_time = time.time()

            # Convert the data
            xAccl = data1 * 256 + data0
            if xAccl > 32767:
                xAccl -= 65536

                # LSM303DLHC Accl address, 0x19(25)
                # Read data back from 0x2A(42), 2 bytes
                # Y-Axis Accl LSB, Y-Axis Accl MSB
                data0 = bus.read_byte_data(0x19, 0x2A)
                data1 = bus.read_byte_data(0x19, 0x2B)
                after_time = time.time()
                # Convert the data
                yAccl = data1 * 256 + data0
                if yAccl > 32767:
                    yAccl -= 65536

            # LSM303DLHC Accl address, 0x19(25)
            # Read data back from 0x2A(42), 2 bytes
            # Y-Axis Accl LSB, Y-Axis Accl MSB
            data0 = bus.read_byte_data(0x19, 0x2A)
            data1 = bus.read_byte_data(0x19, 0x2B)
            after_time = time.time()
            # Convert the data
            yAccl = data1 * 256 + data0
            if yAccl > 32767:
                yAccl -= 65536

            # LSM303DLHC Accl address, 0x19(25)
            # Read data back from 0x2C(44), 2 bytes
            # Z-Axis Accl LSB, Z-Axis Accl MSB
            data0 = bus.read_byte_data(0x19, 0x2C)
            data1 = bus.read_byte_data(0x19, 0x2D)

            # Convert the data
            zAccl = data1 * 256 + data0
            if zAccl > 32767:
                zAccl -= 65536


            self.dt = self.after_time -self.curr_time

            Accl_array = []
            Accl_array.append(xAccl)
            Accl_array.append(yAccl)
            Accl_array.append(zAccl)


            # print " integrating  self.xAccl_array ", self.xAccl_array, "self.dt  ", self.dt
            # print "              self.yAccl_array ", self.yAccl_array, "self.dt  ", self.dt

            self.velocity_ms = integrate.simps(Accl_array , dx=self.dt)
            self.velocity = self.velocity_ms * 18 / 360
            # Output data to screen
            if time.time() - self.lastdisplay > 1:
                self.lastdisplay = time.time()
                print time.asctime(), " -  velocity km/h    ", self.velocity
                # print time.asctime(), " -  acceleration m/s ", xAccl #self.acceleration_cleaned
            # print "Acceleration in Y-Axis : %d" % yAccl
            # print "Acceleration in Z-Axis : %d" % zAccl
            # print "Magnetic field in X-Axis : %d" %xMag
            # print "Magnetic field in Y-Axis : %d" %yMag
            # print "Magnetic field in Z-Axis : %d" %zMag

    def main(self):
        while True:
            self.read_acc()