# -*- coding: utf-8 -*-
# devices/relay.py
# 继电器控制模块

class Relay:
    def switch(self, state):
        print(f"Relay switched to {'ON' if state else 'OFF'}")