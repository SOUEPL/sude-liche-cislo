import builtins

input_values = []
print_values = []


def simulated_input(entry):
    global input_values, print_values

    print_values.append(entry)
    return input_values.pop(0)


def simulated_io_start(input_values, print_values):

    input_values = []
    print_values = []

    builtins.input = simulated_input
    builtins.print = lambda output: print_values.append(output)

    return (input_values, print_values)


def get_display_output():
    global print_values

    return print_values


def set_keyboard_input(simulated_inputs):
    global input_values, print_values

    input_values, print_values = simulated_io_start(input_values, print_values)
    input_values = simulated_inputs
