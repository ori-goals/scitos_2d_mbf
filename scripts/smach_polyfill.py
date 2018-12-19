# Copied from uos / ceres_robot / ceres_navigation om 19/12/2018

from smach import CBInterface as SmachCBInterface
from smach import cb_interface as smach_cb_interface


class CBInterface(SmachCBInterface):
    def __init__(self, cb, outcomes=[], input_keys=[], output_keys=[],
                 io_keys=[], _instance=None):
        SmachCBInterface.__init__(self, cb, outcomes, input_keys, output_keys, io_keys)
        self._instance = _instance

    def __get__(self, obj, type=None):
        return CBInterface(self._cb, outcomes=self._outcomes, input_keys=self._input_keys, output_keys=self._output_keys, _instance=obj)

    def __call__(self, *args, **kwargs):
        if self._instance is not None:
            return self._cb(self._instance, *args, **kwargs)
        else:
            return self._cb(*args, **kwargs)

class cb_interface(smach_cb_interface):
    def __init__(self, *args, **kwargs):
        smach_cb_interface.__init__(self, *args, **kwargs)

    def __call__(self, cb):
        return CBInterface(cb, self._outcomes, self._input_keys, self._output_keys)