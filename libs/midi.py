import os
import mido

class Midi():
  # midi 文件目录
  dir = 'midi/'

  # 获取 midi 文件列表
  def getMidiFiles(self):
    if os.path.exists(self.dir):
      files = os.listdir(self.dir)
      midiFiles = []
      for file in files:
        if file.endswith('.mid'):
          midiFiles.append(file)
      return midiFiles
    else:
      raise Exception('MIDI 文件目录 {} 不存在，请检查！'.format(self.dir))

  # 获取 midi 上下文对象
  def getMidiCtx(self, filePath):
    midiCtx = mido.MidiFile(self.dir + filePath)
    return midiCtx