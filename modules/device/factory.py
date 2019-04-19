from .base import gateAND, gateNOT, gateOR, iPin, oPin


class DeviceFactory(object):
    def create_gate(self, number: int):
        """
        Factory for create logic gate

        Args:
            number (int): 1 -> AND
                          2 -> OR
                          3 -> NOT

        Returns:
            gateAND
            gateOR
            gateNOT
        """
        if number == 1:
            return gateAND()
        elif number == 2:
            return gateOR()
        elif number == 3:
            return gateNOT()

    def create_iPin(self):
        """
        Factory for create input pin
        Returns:
            iPin
        """
        return iPin()

    def create_oPin(self):
        """
        Factory for create output pin
        Returns:
            oPin
        """
        return oPin()
