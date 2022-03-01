import ctypes

# 键盘 Hex 码
keysHexCode = {
  'z': 0x2c, 'x': 0x2d, 'c': 0x2e, 'v': 0x2f, 'b': 0x30, 'n': 0x31, 'm': 0x32, # C4~B4
  'a': 0x1e, 's': 0x1f, 'd': 0x20, 'f': 0x21, 'g': 0x22, 'h': 0x23, 'j': 0x24, # C5~B5 (中央)
  'q': 0x10, 'w': 0x11, 'e': 0x12, 'r': 0x13, 't': 0x14, 'y': 0x15, 'u': 0x16, # C6~B6
}

POINTER = ctypes.POINTER(ctypes.c_ulong)
SendInput = ctypes.windll.user32.SendInput

class KeyBoardInput(ctypes.Structure):
  _fields_ = [
    ('wVK', ctypes.c_ushort),
    ('wScan', ctypes.c_ushort),
    ('dwFlags', ctypes.c_ulong),
    ('time', ctypes.c_ulong),
    ('dwExtraInfo', POINTER)
  ]

class HardwareInput(ctypes.Structure):
  _fields_ = [
    ('uMsg', ctypes.c_ulong),
    ('wParamL', ctypes.c_short),
    ('wParamH', ctypes.c_ushort)
  ]

class MouseInput(ctypes.Structure):
  _fields_ = [
    ('dx', ctypes.c_ulong),
    ('dy', ctypes.c_ulong),
    ('mouseData', ctypes.c_ulong),
    ('dwFlags', ctypes.c_ulong),
    ('time', ctypes.c_ulong),
    ('dwExtraInfo', POINTER)
  ]

class InputInterface(ctypes.Union):
  _fields_ = [
    ('ki', KeyBoardInput),
    ('hi', HardwareInput),
    ('mi', MouseInput)
  ]

class Input(ctypes.Structure):
  _fields_ = [
    ('type', ctypes.c_ulong),
    ('ii', InputInterface)
  ]

class KeyBoard():

  # 按下按键
  def pressKey(self, keyCode):
    hexKeyCode = keysHexCode[keyCode]
    inputInst = InputInterface()
    inputInst.ki = KeyBoardInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(ctypes.c_ulong(0)))
    pointer = Input(ctypes.c_ulong(1), inputInst)
    SendInput(1, ctypes.pointer(pointer), ctypes.sizeof(pointer))

  # 松开按键
  def releaseKey(self, keyCode):
    hexKeyCode = keysHexCode[keyCode]
    inputInst = InputInterface()
    inputInst.ki = KeyBoardInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(ctypes.c_ulong(0)))
    pointer = Input(ctypes.c_ulong(1), inputInst)
    SendInput(1, ctypes.pointer(pointer), ctypes.sizeof(pointer))