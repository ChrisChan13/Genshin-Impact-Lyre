from libs.keyboard import KeyBoard

# 键盘表
keys = [
  'z', 'x', 'c', 'v', 'b', 'n', 'm', # C4~B4
  'a', 's', 'd', 'f', 'g', 'h', 'j', # C5~B5 (中央)
  'q', 'w', 'e', 'r', 't', 'y', 'u', # C6~B6
]

# 音节表
notes = [
  48, 50, 52, 53, 55, 57, 59, # C4~B4
  60, 62, 64, 65, 67, 69, 71, # C5~B5 (中央)
  72, 74, 76, 77, 79, 81, 83, # C6~B6
]

# 键盘-音节 匹配
keysNotes = {}
for i in range(len(notes)):
  keysNotes[notes[i]] = keys[i]

class Lyre():
  # 是否等待 Enter 演奏状态
  isWaitForSignal = False
  # 是否开始演奏状态
  shouldPlayBegin = False
  # 当前正在演奏音节
  playingNotes = set()

  keyBoard = KeyBoard()

  # 演奏音节
  def playNote(self, note):
    # 长音 等及时释放
    if note in self.playingNotes:
      self.offNote(note)
    self.playingNotes.add(note)
    self.keyBoard.pressKey(keysNotes[note])

  # 释放音节
  def offNote(self, note):
    self.playingNotes.discard(note)
    self.keyBoard.releaseKey(keysNotes[note])

  # 获取音节
  def getNote(self, note):
    noteList = []
    # 低于最低八度，升高至最低八度
    while note < notes[0]:
      note += 12
    # 高于最高八度，降低至最高八度
    while note > notes[-1]:
      note -= 12

    # TODO: 半音兼容
    # C4~B4 黑键
    # if notes[0] <= note <= notes[6] and note not in notes:
    # C5~B5 黑键
    # if notes[7] <= note <= notes[13] and note not in notes:
    # C6~B6 黑键
    # if notes[14] <= note <= notes[20] and note not in notes:

    if note in notes:
      noteList.append(note)
    return noteList
  
  # TODO: 自动调音
  # def autoTune(self) -> None:
  #   pass

  # 重置
  def reset(self):
    playingNotes = self.playingNotes.copy()
    # 清空未释放按键
    for note in playingNotes:
      self.offNote(note)
    self.isWaitForSignal = False
    self.shouldPlayBegin = False
    self.playingNotes = set()