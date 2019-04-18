from .base import gateAND, gateNOT, gateOR, iPin, oPin

class DeviceFactory(object):
    def create_gate(self, number : int):
        """
        @param int
            1 -> AND
            2 -> OR
            3 -> NOT
        """
        if number == 1:
            return gateAND()
        elif number == 2:
            return gateOR()
        elif number == 3:
            return gateNOT()

    def create_iPin(self):
        return iPin()

    def create_oPin(self):
        return oPin()