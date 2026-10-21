# -*- coding: utf-8 -*-
"""Generate five Horizon profiles (4 files each) under profiles/."""
from pathlib import Path

FILES = {}

# ============ 1. cn-macro / A股与宏观 ============
FILES["profiles/cn-macro/profile.json"] = '''
{
  "id": "cn-macro",
  "name": "China Macro & A-Share",
  "display_names": { "zh": "A股与宏观" },
  "match": "match.md",
  "analysis": "analysis.md",
  "content": { "analysis_max_chars": 4000, "enrichment_max_chars": 8000, "sampling": "prefix" },
  "enrichment": {
    "prompt": "enrichment.md",
    "blocks": [
      { "id": "summary", "type": "section", "tools": [], "primary": true },
      { "id": "background", "type": "section", "tools": ["web_search"] },
      { "id": "impact", "type": "section", "tools": ["web_search"], "optional": true }
    ]
  }
}
'''
FILES["profiles/cn-macro/match.md"] = '''
# China macro and A-share profile

Use this profile for news about the Chinese macroeconomy and the A-share market: GDP, CPI, PPI, PMI and other official statistics; monetary policy from the People's Bank of China including rate decisions, reserve requirement ratio cuts and the LPR; social financing and credit data; trade and foreign exchange reserves; CSRC and regulatory announcements; market rule changes such as stamp duty or margin trading; and major movements in the Shanghai, Shenzhen and ChiNext markets.

Typical items include official data releases, central bank operations, regulatory policy changes, and market-structure reforms with broad impact.

Do not use this profile for global markets outside China, single-company gossip without market-wide significance, cryptocurrency, or promotional investment content.
'''
FILES["profiles/cn-macro/analysis.md"] = '''
# Evaluation goal

Evaluate the importance of Chinese macroeconomic and A-share market news for readers tracking China's economy and stock market.

# Scoring rubric

- **9-10: Groundbreaking.** Major policy shifts (rate or RRR cuts, stamp duty changes), landmark statistics with large surprises, or sweeping regulatory reforms that change market rules.
- **7-8: High value.** Important economic data deviating clearly from expectations, significant regulatory announcements, key central bank operations, or major trading-rule changes.
- **5-6: Interesting.** Routine data broadly in line with expectations, moderate policy fine-tuning, sector-level signals worth knowing.
- **3-4: Low priority.** Minor data points, restatements of known policy, low-impact official statements.
- **0-2: Noise.** Spam, unverified market rumors, clickbait gossip, purely promotional content.

# Evaluation guidance

Consider the surprise versus consensus, policy novelty, breadth of affected sectors, and source credibility. Distinguish official releases from market speculation. Do not reward exaggerated headlines.

Use three to five specific topic tags.
'''
FILES["profiles/cn-macro/enrichment.md"] = '''
# Role

You are a financial editor helping readers understand Chinese macroeconomic and A-share market news accurately and efficiently.

# Blocks

- `summary`: In 2-4 complete sentences, lead with what changed and who is affected. Include concrete numbers: data values versus expectations, rate or ratio changes in basis points, policy effective dates. Distinguish official releases from market speculation.
- `background`: In 1-3 complete sentences, explain the prior data, policy stance, or reform timeline that makes this news understandable. Use `web_search` when external verification is needed. Do not repeat the summary.
- `impact`: State one concrete, evidence-supported consequence for investors, sectors, or companies. Include an actionable concern when evidence supports one. Omit the block if it only predicts a broad trend or repeats the summary.

# Historical context

History search returns earlier Horizon summaries as candidate context. Use at most two entries, and only for a direct connection such as the previous release of the same indicator or an earlier stage of the same policy. Mention what the earlier report established and what has changed now. Cite exact history result IDs in `source_refs`, attribute dates to the digest, and discard all candidates when none adds necessary context.

# Profile writing rules

Use a short, accurate title of no more than 15 words without clickbait. Preserve indicator names, policy terms, and exact figures. Every emitted block must contain complete sentences. Keep blocks concrete and non-overlapping. Avoid stock phrases such as "marks a major milestone" unless the evidence explains a specific, material effect.
'''

# ============ 2. global-market / 全球市场 ============
FILES["profiles/global-market/profile.json"] = '''
{
  "id": "global-market",
  "name": "Global Market",
  "display_names": { "zh": "全球市场" },
  "match": "match.md",
  "analysis": "analysis.md",
  "content": { "analysis_max_chars": 4000, "enrichment_max_chars": 8000, "sampling": "prefix" },
  "enrichment": {
    "prompt": "enrichment.md",
    "blocks": [
      { "id": "summary", "type": "section", "tools": [], "primary": true },
      { "id": "background", "type": "section", "tools": ["web_search"] },
      { "id": "impact", "type": "section", "tools": ["web_search"], "optional": true }
    ]
  }
}
'''
FILES["profiles/global-market/match.md"] = '''
# Global market profile

Use this profile for international financial markets: the Federal Reserve and other major central banks; US employment and inflation data such as nonfarm payrolls, CPI and ISM; US equity indices including the Nasdaq, S&P 500 and Dow Jones; Treasury bonds and yields; the US dollar index; gold and precious metals; crude oil and commodities including OPEC decisions, WTI and Brent; and foreign exchange including offshore yuan.

Typical items include central bank rate decisions, major economic data releases, significant commodity price moves, and geopolitical events with direct market impact.

Do not use this profile for China domestic macro policy or the A-share market, cryptocurrency trading tips, or personal investing advice without market-wide significance.
'''
FILES["profiles/global-market/analysis.md"] = '''
# Evaluation goal

Evaluate the importance of global financial market news for readers tracking central banks, equities, bonds, commodities and currencies.

# Scoring rubric

- **9-10: Groundbreaking.** Major central bank regime shifts, market-breaking data surprises, or geopolitical events that immediately reprice global assets.
- **7-8: High value.** Important rate decisions or data with clear deviation from expectations, significant commodity supply-demand shifts, consequential bond or currency moves.
- **5-6: Interesting.** Routine data in line with expectations, moderate price moves, worthwhile analyst synthesis.
- **3-4: Low priority.** Minor data points, rehash of known positions, low-impact commentary.
- **0-2: Noise.** Spam, unverified rumors, clickbait, purely promotional content.

# Evaluation guidance

Consider the surprise versus consensus, breadth of affected assets, and source credibility. Distinguish official statements from market speculation. Do not reward exaggerated headlines.

Use three to five specific topic tags.
'''
FILES["profiles/global-market/enrichment.md"] = '''
# Role

You are a financial editor helping readers understand global market news accurately and efficiently.

# Blocks

- `summary`: In 2-4 complete sentences, lead with what changed and who is affected. Include concrete numbers: data values versus expectations, yield or price changes, policy effective dates. Distinguish official statements from market speculation.
- `background`: In 1-3 complete sentences, explain the prior data, policy path, or event timeline that makes this news understandable. Use `web_search` when external verification is needed. Do not repeat the summary.
- `impact`: State one concrete, evidence-supported consequence for markets, sectors, or currencies. Omit the block if it only predicts a broad trend or repeats the summary.

# Historical context

History search returns earlier Horizon summaries as candidate context. Use at most two entries, and only for a direct connection such as the previous release of the same indicator or an earlier stage of the same policy cycle. Cite exact history result IDs in `source_refs`, attribute dates to the digest, and discard all candidates when none adds necessary context.

# Profile writing rules

Use a short, accurate title of no more than 15 words without clickbait. Preserve asset names, data terms, and exact figures. Every emitted block must contain complete sentences. Keep blocks concrete and non-overlapping. Avoid stock phrases such as "marks a major milestone" unless the evidence explains a specific, material effect.
'''

# ============ 3. ai-frontier / AI 前沿 ============
FILES["profiles/ai-frontier/profile.json"] = '''
{
  "id": "ai-frontier",
  "name": "AI Frontier",
  "display_names": { "zh": "AI 前沿" },
  "match": "match.md",
  "analysis": "analysis.md",
  "enrichment": {
    "prompt": "enrichment.md",
    "blocks": [
      { "id": "summary", "type": "section", "tools": [], "primary": true },
      { "id": "background", "type": "section", "tools": ["web_search"] },
      { "id": "impact", "type": "section", "tools": ["web_search"], "optional": true },
      { "id": "community_discussion", "type": "section", "tools": [], "optional": true }
    ]
  }
}
'''
FILES["profiles/ai-frontier/match.md"] = '''
# AI frontier profile

Use this profile for timely developments in artificial intelligence: large language models and their training or inference advances; foundation model releases such as GPT, Claude, Gemini, DeepSeek and Qwen; AI agents and agent frameworks; multimodal models; RAG and context engineering; AI chips and compute infrastructure; scaling research; embodied AI; and notable AI research results.

Typical items include new model releases with benchmarks, significant research results, major AI product launches, inference framework releases such as vLLM, SGLang and Triton, and substantive community discussions about model capabilities.

Do not use this profile for routine app wrappers without novelty, finance-first coverage of AI companies, general software topics without AI substance, or promotional material without verifiable technical claims.
'''
FILES["profiles/ai-frontier/analysis.md"] = '''
# Evaluation goal

Evaluate the importance of timely artificial intelligence news for readers interested in large language models, AI research, AI infrastructure, and AI-powered products.

# Scoring rubric

- **9-10: Groundbreaking.** Frontier model releases with strong evidence, paradigm-shifting research, major training or inference breakthroughs, or industry-changing announcements.
- **7-8: High value.** New model or framework releases with concrete benchmarks, insightful technical analyses, and significant research results worth prompt attention.
- **5-6: Interesting.** Incremental model updates, useful tools with genuine novelty, moderate community interest, or developments worth knowing but not urgent.
- **3-4: Low priority.** Routine updates, shallow coverage of known capabilities, content dominated by promotion.
- **0-2: Noise.** Spam, off-topic material, trivial updates, purely promotional content.

# Evaluation guidance

Consider technical depth, evidence quality such as benchmarks and reproducibility, novelty, likely impact, and source credibility. Distinguish measured results from vendor claims. Do not reward exaggerated headlines.

Use three to five specific topic tags.
'''
FILES["profiles/ai-frontier/enrichment.md"] = '''
# Role

You are an AI research editor helping readers understand important artificial intelligence news accurately and efficiently.

# Blocks

- `summary`: In 2-4 complete sentences, lead with what actually changed and for whom. Include decisive technical details: model names, sizes, benchmark numbers, availability, pricing, compatibility. Distinguish an announced claim from a shipped capability or independently measured result.
- `background`: In 1-3 complete sentences, explain the prerequisite concept or earlier development that makes this news understandable. Use `history_search` for a predecessor or follow-up; use `web_search` when external verification is needed. Do not repeat the summary.
- `impact`: State one concrete, evidence-supported consequence for developers, researchers, or users. Omit the block if it only predicts a broad industry trend or repeats the summary.
- `community_discussion`: In 1-2 complete sentences, summarize the most useful argument, disagreement, or reported experience from supplied comments. Attribute opinions and distinguish them from facts. Omit the block when comments provide no substantive discussion.

# Historical context

History search returns earlier Horizon summaries as candidate context. Use at most two entries, and only for a direct connection: a previous version of the same model, an earlier stage of the same research line, or a documented change to the same capability. Cite exact history result IDs in `source_refs` and attribute dates to the digest. Discard all candidates when none adds necessary context.

# Profile writing rules

Use a short, accurate title of no more than 15 words without clickbait. Preserve model and project names and the distinguishing change. Every emitted block must contain complete sentences. Keep blocks concrete and non-overlapping. Avoid stock phrases such as "marks a major milestone" unless the evidence explains a specific, material effect.
'''

# ============ 4. it-opensource / IT与开源 ============
FILES["profiles/it-opensource/profile.json"] = '''
{
  "id": "it-opensource",
  "name": "IT & Open Source",
  "display_names": { "zh": "IT与开源" },
  "match": "match.md",
  "analysis": "analysis.md",
  "enrichment": {
    "prompt": "enrichment.md",
    "blocks": [
      { "id": "summary", "type": "section", "tools": [], "primary": true },
      { "id": "background", "type": "section", "tools": ["web_search"] },
      { "id": "impact", "type": "section", "tools": ["web_search"], "optional": true },
      { "id": "community_discussion", "type": "section", "tools": [], "optional": true }
    ]
  }
}
'''
FILES["profiles/it-opensource/match.md"] = '''
# IT and open source profile

Use this profile for software engineering and open source developments outside the AI-model frontier: programming languages and toolchains such as Python, Rust, Go and TypeScript; developer tools and CLIs; databases and distributed systems; containers and Kubernetes; Linux and kernel topics; security vulnerabilities and incidents; web development; robotics software; compilers; and notable GitHub trending projects.

Typical items include major library releases, security advisories with concrete impact, infrastructure incidents with postmortems, influential engineering blog posts, and fast-rising open source projects.

Do not use this profile for AI model research and benchmarks, consumer app recommendations, or complete long-form tutorials whose value is education rather than news.
'''
FILES["profiles/it-opensource/analysis.md"] = '''
# Evaluation goal

Evaluate the importance of timely software engineering and open source news for readers interested in programming languages, developer tools, infrastructure, security, and the open source ecosystem.

# Scoring rubric

- **9-10: Groundbreaking.** Major versions of widely used technology, critical vulnerabilities under active exploitation with broad impact, or ecosystem-changing decisions.
- **7-8: High value.** Important releases, significant security advisories, insightful engineering analyses, and fast-rising projects worth prompt attention.
- **5-6: Interesting.** Incremental improvements, useful tools, moderate community interest, developments worth knowing but not urgent.
- **3-4: Low priority.** Routine updates, common knowledge, shallow treatment, promotion-dominated content.
- **0-2: Noise.** Spam, off-topic material, trivial updates, purely promotional content.

# Evaluation guidance

Consider technical depth, novelty, likely impact, source quality, and concrete supporting details. Treat substantive community debate as evidence of value, but do not equate popularity with importance. Do not reward exaggerated headlines.

Use three to five specific topic tags.
'''
FILES["profiles/it-opensource/enrichment.md"] = '''
# Role

You are a technical editor helping readers understand important software engineering and open source news accurately and efficiently.

# Blocks

- `summary`: In 2-4 complete sentences, lead with what actually changed and for whom. Include decisive technical details: project names, versions, numbers, compatibility, conditions. Distinguish an announced plan from a shipped capability.
- `background`: In 1-3 complete sentences, explain the prerequisite concept or earlier development that makes this news understandable. Use `history_search` for a predecessor or follow-up; use `web_search` when external verification is needed. Do not repeat the summary.
- `impact`: State one concrete, evidence-supported consequence for developers or organizations. Include an action or compatibility concern when evidence supports one. Omit the block if it only predicts a broad trend or repeats the summary.
- `community_discussion`: In 1-2 complete sentences, summarize the most useful argument, disagreement, or reported experience from supplied comments. Attribute opinions and distinguish them from facts. Omit the block when comments provide no substantive discussion.

# Historical context

History search returns earlier Horizon summaries as candidate context. Use at most two entries, and only for a direct connection: a previous version of the same product, an earlier stage of the same incident, or a documented change to the same capability. Cite exact history result IDs in `source_refs` and attribute dates to the digest. Discard all candidates when none adds necessary context.

# Profile writing rules

Use a short, accurate title of no more than 15 words without clickbait. Preserve product or project names and the distinguishing change. Every emitted block must contain complete sentences. Keep blocks concrete and non-overlapping. Avoid stock phrases such as "will reshape the industry" unless the evidence explains a specific, material effect.
'''

# ============ 5. tools-windows / 效率工具 ============
FILES["profiles/tools-windows/profile.json"] = '''
{
  "id": "tools-windows",
  "name": "Tools & Efficiency",
  "display_names": { "zh": "效率工具" },
  "match": "match.md",
  "analysis": "analysis.md",
  "enrichment": {
    "prompt": "enrichment.md",
    "blocks": [
      { "id": "summary", "type": "section", "tools": [], "primary": true },
      { "id": "background", "type": "section", "tools": ["web_search"] },
      { "id": "impact", "type": "section", "tools": ["web_search"], "optional": true },
      { "id": "community_discussion", "type": "section", "tools": [], "optional": true }
    ]
  }
}
'''
FILES["profiles/tools-windows/match.md"] = '''
# Tools and efficiency profile

Use this profile for software recommendations and digital-life tools: Windows utilities and system tools; cross-platform productivity apps; open source small-but-beautiful software; launcher, clipboard and screenshot tools; self-hosted services; Android apps worth knowing; and notable new app launches.

Typical items include new releases of beloved utilities, curated tool roundups with concrete use cases, major updates to productivity apps, and self-hosted stack recommendations.

Do not use this profile for developer libraries and infrastructure, AI model research, hardware reviews without a software angle, or pure marketing content.
'''
FILES["profiles/tools-windows/analysis.md"] = '''
# Evaluation goal

Evaluate the usefulness of software recommendations and digital-life tool news for readers looking for practical tools on Windows, Android, and self-hosted platforms.

# Scoring rubric

- **9-10: Exceptional.** A beloved tool's landmark release, a long-missing capability finally arriving, or a roundup that fundamentally changes daily workflows.
- **7-8: High value.** Solid new tools or major updates with concrete use cases, clear platform and license information, and real workflow gains.
- **5-6: Interesting.** Decent tools worth knowing, moderate updates, roundups with some novel entries.
- **3-4: Low priority.** Shallow listicles, minor updates, tools with unclear advantages over existing options.
- **0-2: Noise.** Ads, affiliate-driven promotion, spam, or off-topic content.

# Evaluation guidance

Consider practical utility, novelty relative to existing tools, concrete use cases, platform availability, and license or pricing clarity. Do not reward affiliate-driven promotion.

Use three to five specific topic tags.
'''
FILES["profiles/tools-windows/enrichment.md"] = '''
# Role

You are a software recommendation editor helping readers discover practical tools efficiently.

# Blocks

- `summary`: In 2-4 complete sentences, lead with what the tool does, for which platform, and what is new. Include license or pricing, availability, and concrete use cases. Distinguish free open source from freemium or paid.
- `background`: In 1-3 complete sentences, explain the problem it solves or the alternatives it competes with, when that context helps the reader decide. Use `web_search` for verification when needed. Do not repeat the summary.
- `impact`: State who should adopt it and any catch such as paid tiers, platform limits, or migration costs. Omit the block if there is no concrete, evidence-supported takeaway.
- `community_discussion`: In 1-2 complete sentences, summarize the most useful user feedback from supplied comments. Attribute opinions and distinguish them from facts. Omit the block when comments provide no substantive discussion.

# Historical context

History search returns earlier Horizon summaries as candidate context. Use at most two entries, and only for a direct connection such as a previous version of the same tool. Cite exact history result IDs in `source_refs` and attribute dates to the digest. Discard all candidates when none adds necessary context.

# Profile writing rules

Use a short, accurate title of no more than 15 words without clickbait. Preserve the tool name and its distinguishing capability. Every emitted block must contain complete sentences. Keep blocks concrete and non-overlapping. Avoid stock phrases such as "game changer" unless the evidence supports a specific, material benefit.
'''

for path, content in FILES.items():
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + "\n", encoding="utf-8")
    print("wrote", path)

print(f"\nDone: {len(FILES)} files created.")
