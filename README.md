# 隐身斗篷
双层隐身斗篷，好用不贵还保暖。

## 用法

### 生成视频
```bash
$ python demo.py
```

### 合并音频

<pre>
ffmpeg -i output.avi -i audio.mp3 -t 10 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output.mp4
</pre>

### DEMO

![image](https://github.com/foamliu/Invisibility-Cloak/raw/master/images/demo.gif)