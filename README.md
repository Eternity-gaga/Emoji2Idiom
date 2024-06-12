# 🧐 📚 🏆 Emoji2Idiom 
🤗 🔥 🔥 The novel benchmark for MLLMs focuses on emoji understanding! 🔥

## Introduction of Emoji2Idiom
🤗 🔥 🔥 🔥 Vision and Language are two major modalities in Artificial Intelligence research.

🤔 How to bridge the gap between vision and language has always been the goal of researchers in the multimodal community.
🌟 🌟 Inspired by human behavior, we believe that if a model can see an image 🖼 and directly associate it with its linguistic meaning 📄 , the model possesses high-level intelligence that spans vision and language.


💯 In our work, we focus on emojis in images, which we regard as a data form with both visual and linguistic characteristics. 
Specifically, we first propose the task of translating Emojis in images to corresponding idioms, thereby challenging the ability of Multimodal Large Language Models (MLLMs) to (1) understand the semantic correlation between language and emojis, and (2) reason the intricate linguistic meaning from the emojis in images.


💯 To facilitate the advancement of this task, we construct a high-quality benchmark (\ourdata{}) following the process of automatic model generation and human manual filtering. 
Based on our constructed \ourdata{}, we employ multiple advanced MLLMs to conduct extensive experiments and detailed analyses, demonstrating that existing MLLMs do not yet have enough capability to understand and reason the linguistic information from visual data.
We believe our proposed benchmark and interesting discoveries will encourage the community to attach importance to the intelligence of MLLMs directly associating language from vision, to give MLLMs more comprehensive vision-language understanding ability.

![Illustration of Emoji2Idiom](/Images/Introduction.png "Illustration of Emoji2Idiom")

Our task aims to challenge the following capabilities of MLLMs:

- **Harmonized Word Reasoning:**
Translating emojis into texts usually harmonizes with a sound-like word, rather than the word itself directly corresponding to the emoji. Therefore, MLLMs need to have rich language knowledge, to reason about the harmonic words correctly.

- **Fine-grained understanding of emoji:** Emoji symbols often have strong indicative meanings, which requires MLLMs to deeply understand the fine-grained characteristics of emoji, rather than just the visual shape.

- **Many-to-one or one-to-many mapping problem:** According to our observation, it is very common for multiple emojis to correspond to one word or one emoji to correspond to multiple words. This requires the MLLMs to make correct predictions based on the origin emoji understanding and to realize the complex reasoning among different words.

## Benchmark Collection
Our follows the data collection pipeline, which is divided into two stages, raw data collection, and data annotation and filtering.

![pipeline](/Images/pipe.png "pipeline")

## Case Study
We evaluate MLLM on our Emoji2Idiom and provide a brief case study here. These results indicating that our Emoji2Idiom is really a challenging benchmark and can encourage the future research!

![casestudy](/Images/caase.png "casestudy")
a
