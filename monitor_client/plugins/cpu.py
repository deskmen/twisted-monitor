#!/usr/bin/env python

import commands


def monitor():
    shell_command = "sar 1 3| grep 'Average:'"
    status,result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {"status":status}
    else:
        value_dic = {}
        user,nice,system,iowait,steal,idle = result.split()[2:]
        value_dic = {
            'user':user,
            'nice':nice,
            'system':system,
            'iowait':iowait,
            'steal':steal,
            'idle':idle,
            'status':status
        }
    return value_dic
