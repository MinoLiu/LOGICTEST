from modules.utils.warpper import input_required
import itertools

class LogicSimulator(object):
    def __init__(self):
        self.name = "Logic simulator"
        self.__circuit = []
        self.__iPins = []
        self.__oPins = []
    
    @input_required
    def get_simulation_result(self, input_list : list) -> str:
        if len(input_list) != len(self.__iPins):
            raise Exception("Input length not equal to simulator input length")
                
        result = ""

        for value,pin in zip(input_list, self.__iPins):
            pin.set_input(value)
            result += "1 " if value is True else "0 "
        
        if len(self.__oPins) < 1:
            raise Exception("Simulator has no output")

        result += "| "

        for pin in range(self.__oPins):
            result += "1 " if pin.get_output() is True else "0 "
        result += "\n"

        return result

    @input_required
    def get_truth_table(self) -> str:
        result = "Circuit Truth table:\n"
        i_len = len(self.__iPins)
        o_len = len(self.__oPins)

        result += "i "*i_len + "| " + "o "*o_len
        for x in range(1, i_len + 1):
            result += "{} ".format(x)
        
        result += "| "

        for x in range(o_len):
            result += "{} ".format(x)

        result += "\n" + "-"*(o_len+i_len) + "-"
        
        conditions = list(itertools.product([False, True], repeat=len(i_len)))
        
        for cond in conditions:
            result += self.get_simulation_result(cond)
        
        return result

    
    def load(self, file_path : str) -> bool:
        pass