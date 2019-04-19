from modules.simulator import LogicSimulator


class TextUI(object):
    def __init__(self):
        """ Init TextUI.
        Attributes:
            __menu (list):                  Options for user select.
            __simulator (LogicSimulator):   Logic simulator instance.
            exit_flag (bool):               Exit flag, set to True to exit program.
        """
        self.__menu = ["Load logic circuit file", "Simulation", "Display truth table", "Exit"]
        self.__simulator = LogicSimulator()
        self.exit_flag = False

    def display_menu(self):
        """ Display menu
        Show menu to user.
        """
        for i, x in enumerate(self.__menu):
            print("{}. {}".format(i + 1, x))

        while not self.exit_flag:
            try:
                val = int(input("Command: ").replace("\n", "").replace("\r", ""))

                if 1 > val or val > 4:
                    raise ValueError()

                self.process_command(val)

            except Exception as err:
                print(err)
                print("Command must be integer, and in range 1 ~ 4")

    def process_command(self, value):
        """ Process command
        Args:
            value (int) : To process command
                1 : Load logic circuit file
                2 : Simulation
                3 : Display truth table
                4 : Exit
        """
        if value == 1:
            file_path = str(input("Please key in a file path: ").replace("\n", "").replace("\r", ""))
            try:
                self.__simulator.load(file_path)
                print("Load file successful")
            except Exception as err:
                print(err)

        elif value == 2:
            if not self.__simulator.has_input:
                print("Please load an lcf file, before using this operation.")
            else:
                input_list = []
                while len(input_list) != self.__simulator.input_length:
                    try:
                        val = int(
                            input("Please key in the value of input pin {}: ".format(len(input_list) + 1)
                                 ).replace("\n", "").replace("\r", "")
                        )
                        if val != 1 and val != 0:
                            raise ValueError()

                        input_list.append(True if val == 1 else False)

                    except Exception:
                        print("The value of input pin must be 0/1")

                try:
                    print(self.__simulator.get_simulation_result(input_list))

                except Exception as err:
                    print(err)

        elif value == 3:
            if not self.__simulator.has_input:
                print("Please load an lcf file, before using this operation.")
            else:
                try:
                    print(self.__simulator.get_truth_table())
                except Exception as err:
                    print(err)

        elif value == 4:
            self.exit_flag = True
