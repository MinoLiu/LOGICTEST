from modules.utils.warpper import input_required


class Device(object):
    def __init__(self):
        """
        Attributes:
            name (str):     The device name.
            _iPins (list):  protected variable, input pin from other instance.
            has_input:      Check if the instance has input.
        """
        self.has_input = False
        self._iPins = []
        self.name = "Device"

    def add_input_pin(self, pin):
        """
        Add input pin to _iPins
        Args:
            pin (Device): Inherit from Device object
        """
        self._iPins.append(pin)
        self.has_input = True

    def get_output(self):
        # please implement it
        pass

    def set_input(self, value):
        # only implement it in iPin
        pass


class oPin(Device):
    """
    Output pin
    """

    def __init__(self):
        super().__init__()
        self.name = "oPin"

    @input_required
    def get_output(self) -> bool:
        """
        Get the output from input.
        Returns:
            bool
        """
        return self._iPins[0].get_output()


class iPin(Device):
    """
    Input Pin
    """

    def __init__(self):
        super().__init__()
        self.name = "iPin"
        # Set inital value to False
        self.__input = False

    def add_input_pin(self, pin):
        """
        raises:
            Exception: Please use set_input, cause input pin don't need input pins.
        """
        raise Exception("Please use set_input, cause input pin don't need input pins.")

    def set_input(self, value: bool):
        """
        Set input value
        Args:
            value (bool): Set input boolean
        """
        self.__input = value
        self.has_input = True

    @input_required
    def get_output(self) -> bool:
        """
        Get the input value.
        Returns:
            bool
        """
        return self.__input


class gateNOT(Device):
    def __init__(self):
        super().__init__()
        self.name = "gateNOT"

    @input_required
    def get_output(self) -> bool:
        """
        Get NOT gate output
        Returns:
            bool
        """
        return not self._iPins[0].get_output()


class gateAND(Device):
    def __init__(self):
        super().__init__()
        self.name = "gateAND"

    @input_required
    def get_output(self) -> bool:
        """
        Get AND gate output
        Returns:
            bool
        """
        output = self._iPins[0].get_output()
        for pin in self._iPins[1:]:
            output = output and pin.get_output()

        return output


class gateOR(Device):
    def __init__(self):
        super().__init__()
        self.name = "gateOR"

    @input_required
    def get_output(self) -> bool:
        """
        Get OR gate output
        Returns:
            bool
        """
        output = self._iPins[0].get_output()
        for pin in self._iPins[1:]:
            output = output or pin.get_output()

        return output
