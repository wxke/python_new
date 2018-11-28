#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
RASE_DIR =os.path.dirname(os.path.dirname( os.path.abspath(__file__)))
sys.path.append(RASE_DIR)

from core import shop_main

shop_main.print_shop()
shop_main.shop_car_1(input())
shop_main.print_shop_cat()

