from modules.utils.warpper import input_required

class Device(object):
    def __init__(self):
        self.has_input = False
        self._iPins = []
        self.name = "Device"
    

    def add_input_pin(self, pin : Device):
        self._iPins.append(pin)
        self.has_input = True
    
    def get_output(self):
        # please implement it
        pass

    def set_input(self, value):
        # only implement it in iPin
        pass

class oPin(Device):
    def __init__(self):
        super().__init__()
        self.name = "oPin"
        self._input = False

    @input_required
    def get_output(self):
        return self._iPins[0].get_output()


class iPin(Device):
    def __init__(self):
        super().__init__()
        self.name = "iPin"
        self._input = False
    
    def add_input_pin(self, pin):
        raise Exception("Please use set_input, cause input pin has no input pins.")

    def set_input(self, value : bool):
        self._input = value
        self.has_input = True

    @input_required
    def get_output(self):
        return self._input

class gateNOT(Device):
    def __init__(self):
        super().__init__()
        self.name = "gateNOT"

    @input_required
    def get_output(self):
            return not self._iPins[0].get_output()


class gateAND(Device):
    def __init__(self):
        super().__init__()
        self.name = "gateAND"

    @input_required
    def get_output(self):
        output = self._iPins[0].get_output()
        for pin in self._iPins[1:]:
            output = output and pin.get_output()
        
        return output

class gateOR(Device):
    def __init__(self):
        super().__init__()
        self.name = "gateOR"

    @input_required
    def get_output(self):
        output = self._iPins[0].get_output()
        for pin in self._iPins[1:]:
            output = output or pin.get_output()
        
        return output