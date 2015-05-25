import untangle
import serial

def get_data(port='/dev/ttyUSB1', verbose=False):
	"""Gets temperature and power usage data from an attached CurrentCost meter.

	Parameters:
	 - port: the port that the CurrentCost meter is attached to. Somthing like /dev/ttyUSB0 or COM1

	Returns:
	(temperature, usage), with temperature in degrees C, and usage in Watts
	"""
	ser = serial.Serial(port, 57600)
	xmldata = ser.readline()
        if verbose:
                print(xmldata)
        ser.close()
	p = untangle.parse(xmldata)
	temperature = float(p.msg.tmpr.cdata)
	watts = int(p.msg.ch1.watts.cdata)
	return (watts, temperature)

