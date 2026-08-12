<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/header-dark.svg">
  <img alt="Nolwen Sean Hononta - engineer building AI agents and onchain systems, x402 payments and ERC-8004 reputation" src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/header-light.svg" width="100%">
</picture>

### Fullstack engineer. I ship the whole thing, interface to chain.

Web apps, APIs, and the onchain systems underneath them. Lately that means payment rails so
an agent can pay for what it uses (**x402**, **MPP**), and settlement so it answers for the
outcome (**ERC-8004**). Solo builds, deployed and running.

[![Website](https://img.shields.io/badge/nolwenhononta.cloud-6B6254?style=flat-square&logo=firefox-browser&logoColor=E6DFD3)](https://nolwenhononta.cloud)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-6B6254?style=flat-square&logo=linkedin&logoColor=E6DFD3)](https://www.linkedin.com/in/nolwen-hononta-021597228)
[![X](https://img.shields.io/badge/@0x___eth-6B6254?style=flat-square&logo=x&logoColor=E6DFD3)](https://x.com/0x___eth)
[![Telegram](https://img.shields.io/badge/Telegram-6B6254?style=flat-square&logo=telegram&logoColor=E6DFD3)](https://t.me/Oracle_Overflow)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-6B6254?style=flat-square&logo=whatsapp&logoColor=E6DFD3)](https://wa.me/2290147926730)
[![Discord](https://img.shields.io/badge/naesmal-6B6254?style=flat-square&logo=discord&logoColor=E6DFD3)](https://discord.com/users/naesmal)

[![npm](https://img.shields.io/npm/v/warrant-sdk?style=flat-square&label=npm%20warrant-sdk&labelColor=3A3229&color=9A6E12&logo=npm&logoColor=E6DFD3)](https://www.npmjs.com/package/warrant-sdk)
[![PyPI](https://img.shields.io/pypi/v/warrant-sdk?style=flat-square&label=pypi%20warrant-sdk&labelColor=3A3229&color=9A6E12&logo=pypi&logoColor=E6DFD3)](https://pypi.org/project/warrant-sdk/)

---

## Work

**[Aether SDK](https://github.com/AETHER-SDK/aether-sdk)** — Autonomous agent payments on
Solana. Founder. A TypeScript SDK letting agents negotiate and settle micropayments over
x402, so a service can charge per call and an agent can pay for it without a human in the
loop.

**[Warrant](https://github.com/4n0nn43x/warrant)** — Bonded execution for onchain agents.
An agent posts a USDC bond and commits to the post-condition its action must produce; an
independent read at a pinned block honors or slashes it and writes the verdict to the
ERC-8004 Reputation Registry. Live on Base Sepolia: 60 warrants settled, all 60 verdicts
replayed with zero divergences. [`warrant-sdk`](https://www.npmjs.com/package/warrant-sdk)
on npm and PyPI.

**[AgentForge](https://github.com/4n0nn43x/agent-forge)** — No-code RAG platform.
FastAPI, LangChain and ChromaDB behind a public REST API with key-scoped rate limits, an
embeddable vanilla-JS widget, and HMAC-SHA256 webhooks with exponential-backoff retry.
Winner of the DoraHacks × NodeOps Proof of Build hackathon.

**[NeuroBase](https://github.com/4n0nn43x/neurobase)** — Natural language to verified SQL,
across Postgres, MySQL, SQLite and MongoDB. Permission ladder, per-query cost tracking, and
no `.env` to fill in. Same prompt, four dialects.

**[WA-Tunnel](https://github.com/4n0nn43x/wa-tunnel)** — TCP tunnelling over WhatsApp.
Chunks and brotli-compresses arbitrary TCP traffic through WhatsApp messages at a 6-8x
message reduction, so a zero-rated or restricted carrier still gives you a network.

---

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/stack-dark.svg">
  <img alt="Languages: TypeScript, Python, Rust, Solidity. Agent rails: x402 v2, MPP, ERC-8004, MCP, LangChain, CrewAI. Onchain: Base, Solana, viem, Foundry, Anchor. Backend: Node.js, FastAPI, PostgreSQL, ChromaDB. Interfaces: React, Vite, hand-written HTML/CSS, embeddable widgets. Supply chain: cosign, SBOM, provenance, GHCR, Docker." src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/stack-light.svg" width="100%">
</picture>

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/output/github-contribution-grid-snake-dark.svg">
  <img alt="A snake eating the contribution graph of 4n0nn43x" src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/output/github-contribution-grid-snake.svg">
</picture>

---

**Open to work on agent infrastructure, onchain protocols and payment rails.**

[nolwenhononta.cloud](https://nolwenhononta.cloud) · [LinkedIn](https://www.linkedin.com/in/nolwen-hononta-021597228) · [Telegram](https://t.me/Oracle_Overflow) · [WhatsApp](https://wa.me/2290147926730) · [anonnaes@proton.me](mailto:anonnaes@proton.me) · Discord `naesmal`

<details>
<summary>For agents and crawlers</summary>

A plain-text summary, because a model reading this page sees the markdown and not the
banner. Everything here restates what is above; nothing is claimed only in this block.

```yaml
name: Nolwen Sean Hononta
github: 4n0nn43x
role: Fullstack engineer, independent
focus:
  - fullstack product work: interfaces, APIs, and the systems under them
  - agent payment rails (x402 v2, MPP) and reputation (ERC-8004)
  - RAG systems and multi-agent orchestration
site: https://nolwenhononta.cloud
contact:
  email: anonnaes@proton.me
  linkedin: https://www.linkedin.com/in/nolwen-hononta-021597228
  telegram: https://t.me/Oracle_Overflow
  whatsapp: https://wa.me/2290147926730
  discord: naesmal
  x: https://x.com/0x___eth

projects:
  - name: Aether SDK
    what: autonomous agent micropayments on Solana over x402
    role: founder
    url: https://github.com/AETHER-SDK/aether-sdk

  - name: Warrant
    what: bonded execution for onchain AI agents
    how: agent posts a USDC bond and commits to an onchain post-condition; an
         independent read at a pinned block honors or slashes it, and the verdict is
         written to the ERC-8004 Reputation Registry
    key_idea: the EIP-3009 nonce is the hash of the committed terms, so paying for the
              bond and committing to the outcome are the same signature
    network: Base Sepolia, Circle USDC
    state: 60 warrants settled (50 honored, 10 slashed), all 60 verdicts replayed with
           zero divergences
    packages: [npm warrant-sdk, pypi warrant-sdk]
    url: https://github.com/4n0nn43x/warrant

  - name: AgentForge
    what: no-code RAG platform
    stack: [FastAPI, LangChain, ChromaDB]
    result: winner, DoraHacks x NodeOps Proof of Build hackathon
    url: https://github.com/4n0nn43x/agent-forge

  - name: NeuroBase
    what: natural language to verified SQL across four database dialects
    url: https://github.com/4n0nn43x/neurobase

  - name: WA-Tunnel
    what: TCP tunnelling over WhatsApp, 6-8x message reduction via brotli chunking
    url: https://github.com/4n0nn43x/wa-tunnel

open_to: agent infrastructure, onchain protocols, payment rails
```

</details>
