import os
import itertools
from modules.utils.warpper import input_required
from modules.device import DeviceFactory


class LogicSimulator(object):
    def __init__(self):
        """ Init logic simulator.
        Attributes:
            name (str): The logic simulator name.
            __circuit (list): private variable, circuit device.
            __iPins (list): private variable, input pins.
            __oPins (list): private variable, output pins.
            has_input(bool): have input pins.
            __factory (DeviceFactory): private variable, create devices.
        """
        self.name = "Logic simulator"
        self.__circuit = []
        self.__iPins = []
        self.__oPins = []
        self.has_input = False
        self.__factory = DeviceFactory()

    @input_required
    def get_simulation_result(self, input_list: list) -> str:
        """ Get simulation result

        Args:
            input_list (list): list must have Boolean(s) with the same number of input pins.

        Returns:
            str: "input value | output value".

        Raises:
            ValueError: input_list length not equal to input pins length.
            Exception: Simulator has no output.
        """
        if len(input_list) != len(self.__iPins):
            raise ValueError("Input length not equal to simulator input length")

        result = ""

        for value, pin in zip(input_list, self.__iPins):
            pin.set_input(value)
            result += "1 " if value is True else "0 "

        if len(self.__oPins) < 1:
            raise Exception("Simulator has no output")

        result += "| "

        for pin in self.__oPins:
            result += "1 " if pin.get_output() is True else "0 "

        result = result.strip()
        result += "\n"

        return result

    @input_required
    def get_truth_table(self) -> str:
        """
        Get truth table from these circuits
        returns:
            str: truth table
                e.g:
                    i i i | o
                    1 2 3 | 1
                    ------+--
                    0 0 0 | 0
                    0 0 1 | 0
                    0 1 0 | 0
                    0 1 1 | 0
                    1 0 0 | 1
                    1 0 1 | 1
                    1 1 0 | 0
                    1 1 1 | 0
        """
        result = "Circuit Truth table:\n"
        i_len = len(self.__iPins)
        o_len = len(self.__oPins)

        result += "i " * i_len + "| " + "o" * (o_len - 1) + "o\n"

        for x in range(1, i_len + 1):
            result += "{} ".format(x)

        result += "| "

        for x in range(o_len):
            result += "{} ".format(x)
        result = result.strip()
        result += "\n" + "-" * (o_len + i_len) * 2 + "-" + "\n"

        conditions = list(itertools.product([False, True], repeat=i_len))

        for cond in conditions:
            result += self.get_simulation_result(cond)

        return result

    def reset(self):
        self.__circuit = []
        self.__iPins = []
        self.__oPins = []
        self.has_input = False

    def load(self, file_path: str) -> bool:
        """
        Load lcf file
        e.g:
            3               | 3 input pins
            3               | 3 gates
            1 -1 2.1 3.1 0  | 1 == AND gate, -1 == Input pin #1, 2.1, 3.1 == Output pin from 2, 3, 0 == end
            3 -2 0          | 3 == NOT gate
            2 2.1 -3 0      | 2 == OR gate
        """
        self.reset()

        if not os.path.exists(file_path):
            raise ValueError("file_path is not valid, make sure the file exists")

        lines = []
        with open(file_path, 'r', encoding='UTF-8') as f:
            for x in f.readlines():
                lines.append(x.strip().replace("\n", "").replace("\r", "").split(" "))

        try:
            input_pins = int(lines[0][0])
            is_output_pin = [True] * int(lines[1][0])

            for _ in range(input_pins):
                self.__iPins.append(self.__factory.create_iPin())

            for line in lines[2:]:
                self.__circuit.append(self.__factory.create_gate(int(line[0])))

            for i, line in enumerate(lines[2:]):
                for x in line[1:]:
                    val = int(float(x))  # "3.1" -> 3, "-1" -> -1
                    if val > 0:
                        self.__circuit[i].add_input_pin(self.__circuit[val - 1])
                        is_output_pin[val - 1] = False
                    elif val < 0:
                        self.__circuit[i].add_input_pin(self.__iPins[-val - 1])
                    else:
                        break
            for i, out in enumerate(is_output_pin):
                if out is True:
                    oPin = self.__factory.create_oPin()
                    oPin.add_input_pin(self.__circuit[i])
                    self.__oPins.append(oPin)

        except Exception as err:
            print(err)
            raise Exception("{} context not valid".format(file_path))

        self.has_input = True
