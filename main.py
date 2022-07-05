import re

import pymem


class WallHack:
    def __init__(self, switch: bool = True):
        self.switch = switch
        self.process = pymem.Pymem('csgo.exe')

    def get_addr(self):
        byte = rb'\x83\xF8.\x8B\x45\x08\x0F'

        client = pymem.process.module_from_name(
            self.process.process_handle,
            'client.dll'
        )

        lp_base_dll = client.lpBaseOfDll
        module = self.process.read_bytes(lp_base_dll, client.SizeOfImage)

        addr_info = lp_base_dll + re.search(byte, module).start() + 2 # type: ignore

        return addr_info


    def write_bytes_and_close_process(self, address: int = None):
        if address:
            self.process.write_uchar(address, 2 if address == 1 else 1 if self.switch else 0)
            self.process.close_process()

        return None

    def start(self):
        bool_reverse = {
            True: 'enabled',
            False: 'disabled'
        }

        if self.switch:
            self.write_bytes_and_close_process(self.get_addr())

        return f'WH now {bool_reverse[self.switch]}'
