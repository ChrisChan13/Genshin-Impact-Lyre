# Genshin-Impact-Lyre

🎹《原神》 读取 MIDI 文件并 **自动演奏** 风物之诗琴/镜花之琴 脚本（仅支持 PC 非手柄）

> ⚠️警告：**任意性质**、**任意形式**、**任意内容** 的 **第三方工具**、**第三方脚本** 均有风险被原神官方判定为违规，从而进行 **账号安全限制** 甚至 **账号处罚**，使用前请知悉

## 介绍

原神 风物之诗琴/镜花之琴 仅支持弹奏 **C4~B6** 中的 **基本音级（白键）**，不支持弹奏 **变化音级（黑键）**。

处于 C4~B6 范围外的音级，将采用 **上升或下降** 若干八度直至给定音级范围内进行演奏。

所有 变化音级（黑键） 暂时跳过演奏，请尽量确保演奏的 MIDI 中 **不包含** 变化音级（黑键），以达到更好的演奏效果。

小调调性 中包含较多 变化音级（黑键），请尽量将演奏的 MIDI 调性 **上升或下降** 至 大调调性，以达到更好的演奏效果。

> MIDI 中各个演奏音节之间请尽量留有一小段间隔，特别是连续同一短音节快速演奏，可能会造成极短时间内脚本来不及释放原本被按下的键盘按键，从而被跳过演奏。将各个音节稍微缩短，在 **音节末端留白**，可避免触发此类问题

## 使用

1. 在 [Releases](https://github.com/ChrisChan13/Genshin-Impact-Lyre/releases) 中下载 ***Latest*** 版本 `Genshin-Impact-Lyre.exe` 以及 `midi.zip` 压缩包并解压
2. 将 `Genshin-Impact-Lyre.exe` 以及解压后的 `midi 文件夹` 放置于同一目录下
3. 双击 `Genshin-Impact-Lyre.exe` 以管理员身份运行
4. 在展示的 MIDI 列表中，输入将要演奏的 MIDI 文件序号并回车确认
5. 切换至原神游戏窗口，打开 风物之诗琴/镜花之琴
6. 按下 `Enter` 键开始演奏，按下 `Esc` 键可终止演奏
7. 循环 4~6 步骤，直至退出脚本

> PS：将自己制作的 MIDI 文件放入 `/midi` 文件夹下即可选择演奏自己制作的 MIDI 曲谱

<br>
<details>
  <summary><b>本地编译</b></summary>
  <br>

  1. 安装 Python3
  2. Clone 本项目
  3. 双击 `install.bat` 安装依赖
  4. 双击 `start.bat` 运行脚本
  5. 双击 `build.bat` 打包脚本（需要安装 `pyinstaller`）
  
  > PS：在项目源码中 `/midi` 目录下不包含 MIDI 文件，可在 [Releases](https://github.com/ChrisChan13/Genshin-Impact-Lyre/releases) 中下载 `midi.zip` 压缩包解压

</details>
<br>
<details>
  <summary><b>TODOs</b></summary>
  <br>

  1. 变化音级（黑键）的兼容演奏处理
  2. 小调的自动变调演奏处理

</details>
