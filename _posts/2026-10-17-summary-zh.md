---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 50 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [PS5 越狱运行大模型](#item-tech-news-1) ⭐️ 8.0/10
2. [Claude reveals ECDSA curve origins](#item-tech-news-2) ⭐️ 8.0/10
3. [90% of US working hours are spent on tasks not covered well by AI benchmarks](#item-tech-news-3) ⭐️ 8.0/10
4. [You could have invented transformers from memory](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenBSD 37 年内核漏洞&\#x27;Big Fish&\#x27;被利用](#item-tech-news-5) ⭐️ 7.0/10
6. [高通否认骁龙 8 Elite Gen 6 发热传闻，称正与厂商协同解决](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [PS5 越狱运行大模型](https://github.com/cobanov/PS5LM) ⭐️ 8.0/10

越狱后的 PS5 现在可以原生运行 Llama.cpp 框架，支持任何 GGUF 量化模型。该项目利用 PS5 的定制 AMD APU 硬件，为消费级游戏硬件上的 AI 应用开辟了新可能性。目前该项目已在 GitHub 上发布，但面临被索尼移除的风险。

hackernews · Anon84 · 10月16日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50122431)

**「技术背景」** Llama.cpp 是一个用 C/C++实现的开源项目，允许在不需要 Python 运行时的情况下运行大型语言模型，支持 CPU+GPU 混合推理以加速模型执行。GGUF\(GGML Universal Format\)是专门为本地推理设计的文件格式，将模型权重、配置和分词器数据打包成单个自描述文件，优化了在消费级硬件上的运行效率。PS5 越狱方面，2026 年 9 月发布的&quot;Relapse&quot;越狱适用于固件版本 7.00 至 13.60，允许用户在重启前获得系统访问权限，为在游戏主机上运行自定义软件创造了条件。

**「实际影响」** 用户可以将 PS5 用于需要持续 AI 处理的边缘计算任务，如监控服务器错误率、审查安全录像或植物生长监测。以每天约 0.7 美元的电费成本，PS5 每天可产生约 200 万个输出令牌，相当于价值约 3.5 美元的云服务。

**「社区讨论」** 社区对项目托管在 GitHub 表示担忧，认为索尼可能会随时移除该页面，建议使用更少企业管控的托管服务。同时，开发者们兴奋于将锁定设备转化为通用计算机的可能性，并探讨了在游戏中实现 AI 驱动 NPC 的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://sourceforge.net/projects/llama-cpp.mirror/">llama . cpp download | SourceForge.net</a></li>
<li><a href="https://www.ertas.ai/blog/gguf-format-explained">What Is GGUF ? The File Format for Local AI Models - Ertas AI</a></li>
<li><a href="https://psn.gg/news/ps5-relapse-jailbreak-public-firmware-13-60">PSN.GG · PS5 Relapse Jailbreak Is Public: Firmware 7.00-13.60</a></li>
<li><a href="https://videocardz.com/newz/ps5-13-60-jailbreak-released-almost-every-ps5-can-now-be-jailbroken">PS5 13.60 jailbreak released, almost every PS5 can now be ...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#edge computing`, `#gaming hardware`, `#jailbreaking`, `#LLM deployment`

---

<a id="item-tech-news-2"></a>
### [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Claude discovered that NIST elliptic curve cryptographic standards were generated using a simple C library random number function seeded with Unix timestamps.

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**标签**: `#cryptography`, `#security`, `#ai-research`, `#software-engineering`, `#standards`

---

<a id="item-tech-news-3"></a>
### [90% of US working hours are spent on tasks not covered well by AI benchmarks](https://www.mercor.com/research/labor-index/benchmark-map/) ⭐️ 8.0/10

Research shows AI benchmarks fail to cover most real-world work tasks, raising important questions about AI evaluation and development priorities.

hackernews · speckx · 10月16日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50121179)

**标签**: `#AI benchmarks`, `#Labor market`, `#AI evaluation`, `#Research analysis`, `#Work automation`

---

<a id="item-tech-news-4"></a>
### [You could have invented transformers from memory](https://alexwang.ai/posts/associative-memory/) ⭐️ 7.0/10

The article presents transformers through the lens of associative memory systems, offering a novel theoretical perspective on their architecture and capabilities.

hackernews · speckx · 10月16日 19:01 · [社区讨论](https://news.ycombinator.com/item?id=50122878)

**标签**: `#transformers`, `#machine-learning`, `#artificial-intelligence`, `#memory-systems`, `#theoretical-computer-science`

---

<a id="item-tech-news-5"></a>
### [OpenBSD 37 年内核漏洞&\#x27;Big Fish&\#x27;被利用](https://calif.io/research/big-fish) ⭐️ 7.0/10

研究人员发现并利用了 OpenBSD 中一个存在 37 年的内核漏洞&\#x27;Big Fish&\#x27;。该漏洞涉及映射 127 个 SysV 共享内存段，通过 munmap\(\)取消映射，然后分叉 259 个进程将共享内存附加计数包装为-32,643。这个漏洞突显了仅通过代码审查难以发现某些内核漏洞的挑战，尽管它存在于一个经过严格审计的代码库中。

hackernews · rs\_rs\_rs\_rs\_rs · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

**「OpenBSD 背景」** OpenBSD 是一个专注于安全的、免费的类 Unix 操作系统，基于伯克利软件分发\(BSD\)，由 Theo de Raadt 于 1995 年通过分叉 NetBSD 1.0 创建。该操作系统以其严格的安全审计和先进的缓解技术而闻名，包括 KARL 技术，该技术通过重新链接内核二进制文件来随机化函数和数据地址，尽管其内核内存分配器仍保持确定性特性。

**「安全影响」** 此次漏洞利用证明了即使在经过严格审计的代码库中，也可能存在长达数十年的安全隐患，攻击者可以通过组合多个漏洞实现本地权限提升获取 root 权限。OpenBSD 已在漏洞公开前修复了相关问题，但这一事件凸显了传统安全审计方法的局限性，以及对更深入代码审查和新型漏洞检测技术的迫切需求。

**「社区观点」** 社区讨论指出，这个漏洞在经过严格审计的代码库中存活 37 年令人震惊，引发了关于模糊测试或静态分析是否能发现此类漏洞，还是需要人类思考利用原语的讨论。有趣的是，该漏洞已在 NetBSD 于 1999 年的代码重写过程中被意外修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD">OpenBSD - Wikipedia</a></li>
<li><a href="https://calif.io/research/big-fish">Big Fish : Exploiting a 37-Year-Old Kernel Bug in OpenBSD | Calif</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD_security_features">OpenBSD security features - Wikipedia</a></li>
<li><a href="https://www.wikiwand.com/en/OpenBSD">OpenBSD - Wikiwand</a></li>
<li><a href="https://daily.dev/posts/big-fish-exploiting-a-37-year-old-kernel-bug-in-openbsd-u6hc8g4lt">Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD</a></li>
<li><a href="https://aicrier.com/post/got9bqqjbi3quvvti9pq">Big Fish Exploits 37-Year OpenBSD Bug — AICrier</a></li>
<li><a href="https://thedailytechfeed.com/37-year-old-kernel-bug-in-openbsd-finally-patched-after-root-exploit-poc/">37-Year-Old Kernel Bug in OpenBSD Finally Patched After Root ...</a></li>

</ul>
</details>

**标签**: `#security`, `#kernel`, `#open-source`, `#exploit`, `#operating-systems`

---

<a id="item-tech-news-6"></a>
### [高通否认骁龙 8 Elite Gen 6 发热传闻，称正与厂商协同解决](https://www.163.com/dy/article/L9EFR7ID051191D6.html) ⭐️ 7.0/10

Qualcomm denies overheating issues with Snapdragon 8 Elite Gen 6 while Samsung reportedly demands fixes before their flagship launch.

telegram · zaihuapd · 10月17日 04:12

**标签**: `#mobile processors`, `#chipset technology`, `#smartphone hardware`, `#industry competition`, `#thermal management`

---