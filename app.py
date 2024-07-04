import time
import random
import gradio as gr

def generate_music(song_name, description, genre):
    # Simulate a delay of 10 to 20 seconds
    delay = random.randint(10, 20)
    time.sleep(delay)
    # Return a fixed MP3 file
    return "ai_output.mp3"

# Add your Weibo link to the description
description = """
## 免费不限量的AI音乐生成器

如果觉得好用 **欢迎转发**微博分享给更多人体验

微博传送门:[阿尼亚是安妮亞](https://weibo.com/7402396589/OlOY4xNSy)
"""

# Detailed article about the AI music generator
article = """
### 欢迎使用Rhythmic Intelligent Composition Kit (R.I.C.K.)

**Rhythmic Intelligent Composition Kit**（简称R.I.C.K.）是一款尖端的AI音乐生成工具，专为音乐创作者和爱好者设计。我们利用最先进的机器学习和深度学习算法，结合大量音乐数据，为用户提供无与伦比的创作体验。

#### 功能特色：
1. **智能作曲**：R.I.C.K.能够根据用户提供的歌曲名称、描述和音乐风格，智能生成高质量的音乐作品。它不仅能够理解用户的意图，还能结合多种音乐元素，创作出令人惊叹的旋律。
2. **多种风格支持**：无论是流行、摇滚、古典还是电子音乐，R.I.C.K.都能轻松驾驭。用户只需输入想要的音乐风格，AI便会生成符合该风格的音乐作品。
3. **高效生成**：R.I.C.K.采用高效的算法和强大的计算资源，确保在短时间内生成音乐。用户无需等待太久，即可获得满意的音乐作品。
4. **用户友好界面**：我们提供简洁直观的用户界面，用户只需填写简单的表单，即可生成音乐。无论是专业音乐人还是初学者，都能轻松上手。
5. **定制化选项**：用户可以通过详细的音乐描述，进一步定制生成的音乐。R.I.C.K.会根据描述中的关键词和情感色彩，生成更符合用户期望的音乐作品。

#### 使用方法：
1. **输入歌曲名称**：为你的音乐作品命名。
2. **描述音乐**：提供一些关于音乐的描述，如情感、场景、主题等。
3. **选择音乐风格**：选择你想要的音乐风格，如流行、摇滚、古典或电子音乐。
4. **生成音乐**：点击生成按钮，R.I.C.K.会在短时间内生成你的音乐作品。

#### 关于我们：
R.I.C.K.由一群热爱音乐和人工智能的专家团队开发。我们致力于将AI技术应用于音乐创作，帮助更多人实现他们的音乐梦想。我们的目标是让每个人都能轻松创作出动人的音乐。

**了解更多**：请访问我的微博: [阿尼亚是安妮亞](https://weibo.com/u/7402396589)
"""

demo = gr.Interface(
    fn=generate_music,
    inputs=[
        gr.Textbox(label="Song Name"),
        gr.Textbox(label="Music Description"),
        gr.Textbox(label="Music Genre")
    ],
    outputs=gr.Audio(label="Generated Music"),
    title="Rhythmic Intelligent Composition Kit",
    description=description,
    article=article,
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()