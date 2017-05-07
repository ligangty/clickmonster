#!/usr/bin/env python
from execution import repeater
import os

global i
i = 0


def print_num_plus():
  global i
  os.system('clear')
  print(i)
  i = i + 1


repeater.Repeat.repeat(100, 0.01, print_num_plus)
