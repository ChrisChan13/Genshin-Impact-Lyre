import sys
import ctypes
import time
from threading import Thread
from pynput.keyboard import Listener, Key
from libs.midi import Midi
from libs.lyre import Lyre

def printSplitLine():
  print('\n' + '=' * 50 + '\n')

class PlayThread(Thread):
  midi = Midi()
  lyre = Lyre()
  # 是否退出程序
  shouldExit = False

  def __init__(self):
    Thread.__init__(self)

  def run(self):
    while not self.shouldExit:
      try:
        midiFiles = self.midi.getMidiFiles()
        midiSize = len(midiFiles)
        if midiSize == 0:
          raise Exception('MIDI 文件目录 {} 为空，请检查！'.format(self.midi.dir))
        print('选择要打开的 MIDI 文件：\n')
        print('\n'.join([str(i + 1) + '、' + midiFiles[i] for i in range(midiSize)]))
        index = int(input('\n请输入文件前数字序号（按 Enter 确定）：'))
        if not 1 <= index <= midiSize:
          printSplitLine()
          print('输入超出文件序号！')
          printSplitLine()
          continue
        midiFile = midiFiles[index - 1]
        print('\n准备演奏曲目：' + midiFile)
        print('\n请切换至《原神》游戏界面按下 Enter 开始演奏')
        print('演奏开始后可随时按下 Esc 中断演奏')
        # 延迟 input 回车触发监听器
        time.sleep(0.1)
        self.lyre.isWaitForSignal = True
        # 等待 Enter 进行演奏
        while self.lyre.isWaitForSignal:
          if self.lyre.shouldPlayBegin:
            break
        midiCtx = self.midi.getMidiCtx(midiFile)
        if self.lyre.isWaitForSignal:
          print('\n正在演奏..')
        for msg in midiCtx.play():
          # Esc 中断演奏
          if not self.lyre.isWaitForSignal: break
          if msg.type == 'note_on' or msg.type == 'note_off':
            noteList = self.lyre.getNote(msg.note)
            for note in noteList:
              # Esc 中断演奏
              if not self.lyre.isWaitForSignal: break
              if msg.type == 'note_on':
                self.lyre.playNote(note)
              if msg.type == 'note_off':
                self.lyre.offNote(note)
        self.lyre.reset()
        print('\n演奏结束！')
        printSplitLine()
      except Exception as error:
        errorMsg = str(error)
        printSplitLine()
        print('Error: ' + errorMsg)
        print('\n请按任意键退出！')
        printSplitLine()
        # 延迟 input 回车触发监听器
        time.sleep(0.1)
        self.shouldExit = True

# 是否管理员模式运行
def isAdmin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except RuntimeError:
    return False

def main():
  print('\n请切换至《原神》游戏界面并打开《风物之诗琴》做好演奏准备！\n')
  playingThread = PlayThread()
  playingThread.start()
  def onRelease(key):
    # Esc 中断演奏
    if playingThread.lyre.isWaitForSignal and key == Key.esc:
      playingThread.lyre.isWaitForSignal = False
      playingThread.lyre.shouldPlayBegin = False
    # Enter 开始演奏
    elif playingThread.lyre.isWaitForSignal and not playingThread.lyre.shouldPlayBegin and key == Key.enter:
      playingThread.lyre.shouldPlayBegin = True
    # 中断进程
    elif playingThread.shouldExit:
      return False
  with Listener(
    on_press = (),
    on_release = onRelease
  ) as listener:
    listener.join()

if __name__ == '__main__':
  if isAdmin():
    main()
  else:
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1)