#!/usr/bin/env python

import cpu,load


def get_cpu_status():
    return cpu.monitor()
def get_load_status():
    return load.monitor()


