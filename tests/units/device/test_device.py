def test_device_init(test_device):
    assert test_device.name == 'Device'


def test_add_input_pin(test_device, test_iPin):
    test_device.add_input_pin(test_iPin)
    assert test_device._iPins[0] == test_iPin


def test_get_output(test_device):
    test_device.get_output()


def test_set_input(test_device):
    test_device.set_input(True)