import pygame
import tkinter as tk
import sys

from assets import *

pygame.init()  # initializing pygame

# -----------------------------------------------------------
# Coordinarte system for tile placement
coords = {'A1': (25, 50), 'A2': (25, 100), 'A3': (25, 150), 'A4': (25, 200), 'A5': (25, 250), 'A6': (25, 300),
          'A7': (25, 350),
          'B1': (75, 50), 'B2': (75, 100), 'B3': (75, 150), 'B4': (75, 200), 'B5': (75, 250), 'B6': (75, 300),
          'B7': (75, 350),
          'C1': (125, 50), 'C2': (125, 100), 'C3': (125, 150), 'C4': (125, 200), 'C5': (125, 250), 'C6': (125, 300),
          'C7': (125, 350),
          'D1': (175, 50), 'D2': (175, 100), 'D3': (175, 150), 'D4': (175, 200), 'D5': (175, 250), 'D6': (175, 300),
          'D7': (175, 350),
          'E1': (225, 50), 'E2': (225, 100), 'E3': (225, 150), 'E4': (225, 200), 'E5': (225, 250), 'E6': (225, 300),
          'E7': (225, 350),
          'F1': (275, 50), 'F2': (275, 100), 'F3': (275, 150), 'F4': (275, 200), 'F5': (275, 250), 'F6': (275, 300),
          'F7': (275, 350),
          'G1': (325, 50), 'G2': (325, 100), 'G3': (325, 150), 'G4': (325, 200), 'G5': (325, 250), 'G6': (325, 300),
          'G7': (325, 350),
          'H1': (375, 50), 'H2': (375, 100), 'H3': (375, 150), 'H4': (375, 200), 'H5': (375, 250), 'H6': (375, 300),
          'H7': (375, 350),
          'I1': (425, 50), 'I2': (425, 100), 'I3': (425, 150), 'I4': (425, 200), 'I5': (425, 250), 'I6': (425, 300),
          'I7': (425, 350),
          'J1': (475, 50), 'J2': (475, 100), 'J3': (475, 150), 'J4': (475, 200), 'J5': (475, 250), 'J6': (475, 300),
          'J7': (475, 350),
          'K1': (525, 50), 'K2': (525, 100), 'K3': (525, 150), 'K4': (525, 200), 'K5': (525, 250), 'K6': (525, 300),
          'K7': (525, 350),
          'L1': (575, 50), 'L2': (575, 100), 'L3': (575, 150), 'L4': (575, 200), 'L5': (575, 250), 'L6': (575, 300),
          'L7': (575, 350),
          'M1': (625, 50), 'M2': (625, 100), 'M3': (625, 150), 'M4': (625, 200), 'M5': (625, 250), 'M6': (625, 300),
          'M7': (625, 350),
          'N1': (675, 50), 'N2': (675, 100), 'N3': (675, 150), 'N4': (675, 200), 'N5': (675, 250), 'N6': (675, 300),
          'N7': (675, 350)
          }
# level setup for level 1
level1_pipes = {
    'A1': {straight_pipe, 180}, 'A2': {curve_pipe, 0}, 'A3': {curve_pipe, 270}, 'A4': {t_pipe, 90},
    'A5': {curve_pipe, 0}, 'A6': {straight_pipe, 90},
    'A7': {t_pipe, 180}, 'B1': {straight_pipe, 90}, 'B2': {straight_pipe, 0}, 'B3': {curve_pipe, 180},
    'B4': {straight_pipe, 90}, 'B5': {t_pipe, 270}, 'B6': {curve_pipe, 0},
    'B7': {straight_pipe, 0}, 'C1': {curve_pipe, 0}, 'C2': {curve_pipe, 180}, 'C3': {straight_pipe, 180},
    'C4': {straight_pipe, 0}, 'C5': {straight_pipe, 180}, 'C6': {curve_pipe, 270},
    'C7': {straight_pipe, 0}, 'D1': {t_pipe, 90}, 'D2': {straight_pipe, 0}, 'D3': {t_pipe, 180},
    'D4': {straight_pipe, 0}, 'D5': {curve_pipe, 180}, 'D6': {straight_pipe, 0},
    'D7': {straight_pipe, 270}, 'E1': {curve_pipe, 0}, 'E2': {straight_pipe, 270}, 'E3': {t_pipe, 0},
    'E4': {curve_pipe, 90}, 'E5': {straight_pipe, 180}, 'E6': {curve_pipe, 180},
    'E7': {straight_pipe, 270}, 'F1': {straight_pipe, 0}, 'F2': {curve_pipe, 270}, 'F3': {straight_pipe, 0},
    'F4': {straight_pipe, 90}, 'F5': {curve_pipe, 180}, 'F6': {t_pipe, 180},
    'F7': {t_pipe, 270}, 'G1': {curve_pipe, 0}, 'G2': {t_pipe, 0}, 'G3': {curve_pipe, 90}, 'G4': {curve_pipe, 90},
    'G5': {curve_pipe, 180}, 'G6': {straight_pipe, 900},
    'G7': {curve_pipe, 0}, 'H1': {straight_pipe, 0}, 'H2': {curve_pipe, 0}, 'H3': {t_pipe, 90}, 'H4': {curve_pipe, 90},
    'H5': {straight_pipe, 180}, 'H6': {curve_pipe, 90},
    'H7': {straight_pipe, 0}, 'I1': {curve_pipe, 90}, 'I2': {straight_pipe, 0}, 'I3': {t_pipe, 180},
    'I4': {straight_pipe, 90}, 'I5': {straight_pipe, 0}, 'I6': {t_pipe, 0},
    'I7': {curve_pipe, 0}, 'J1': {curve_pipe, 90}, 'J2': {straight_pipe, 0}, 'J3': {straight_pipe, 180},
    'J4': {straight_pipe, 180}, 'J5': {curve_pipe, 90}, 'J6': {straight_pipe, 0},
    'J7': {curve_pipe, 180}, 'K1': {curve_pipe, 0}, 'K2': {straight_pipe, 90}, 'K3': {straight_pipe, 0},
    'K4': {curve_pipe, 90}, 'K5': {curve_pipe, 180}, 'K6': {t_pipe, 180},
    'K7': {t_pipe, 0}, 'L1': {straight_pipe, 90}, 'L2': {curve_pipe, 0}, 'L3': {straight_pipe, 0},
    'L4': {straight_pipe, 0}, 'L5': {curve_pipe, 0}, 'L6': {straight_pipe, 180},
    'L7': {straight_pipe, 0}, 'M1': {t_pipe, 90}, 'M2': {t_pipe, 0}, 'M3': {curve_pipe, 0}, 'M4': {curve_pipe, 90},
    'M5': {straight_pipe, 0}, 'M6': {straight_pipe, 180},
    'M7': {curve_pipe, 0}, 'N1': {curve_pipe, 90}, 'N2': {straight_pipe, 0}, 'N3': {curve_pipe, 180},
    'N4': {straight_pipe, 90}, 'N5': {curve_pipe, 0}, 'N6': {t_pipe, 180},
    'N7': {straight_pipe, 0}

}
# Active pipes used in solution
level1_pipes_active_pipes = {
    'A1': 180, 'A2': 0, 'B2': 0, 'C2': 180, 'C3': 180, 'C4': 0, 'C5': 180, 'C6': 270,
    'D6': 0, 'E6': 180, 'E5': 180, 'E4': 90, 'F4': 90, 'G4': 90, 'G5': 180, 'H5': 180,
    'I5': 0, 'J5': 90, 'J4': 180, 'J3': 180, 'J2': 0, 'J1': 90, 'K1': 0, 'K2': 90,
    'K3': 0, 'K4': 90, 'L4': 0, 'M4': 90, 'M5': 0, 'M6': 180, 'M7': 0, 'N7': 0
}

# Correct soluion pipe values
level1_pipes_values_correct = {
    'A1': 0, 'A2': 180, 'B2': 270, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0,
    'D6': 270, 'E6': 90, 'E5': 180, 'E4': 90, 'F4': 90, 'G4': 180, 'G5': 180, 'H5': 270,
    'I5': 270, 'J5': 270, 'J4': 180, 'J3': 180, 'J2': 180, 'J1': 90, 'K1': 0, 'K2': 180,
    'K3': 0, 'K4': 0, 'L4': 270, 'M4': 180, 'M5': 0, 'M6': 0, 'M7': 180, 'N7': 270
}
