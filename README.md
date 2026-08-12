<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/header-dark.svg">
  <img alt="Nolwen Sean Hononta - engineer building AI agents and onchain systems, x402 payments and ERC-8004 reputation" src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/header-light.svg" width="100%">
</picture>

### I build the infrastructure autonomous agents need to transact onchain.

Payment rails so an agent can pay for what it uses (**x402**, **MPP**), and settlement so it
answers for the outcome (**ERC-8004**). Solo builds, deployed and running.

[![Website](https://img.shields.io/badge/nolwenhononta.cloud-0b1020?style=for-the-badge&logo=firefox-browser&logoColor=22d3ee)](https://nolwenhononta.cloud)
[![npm](https://img.shields.io/npm/v/warrant-sdk?style=for-the-badge&label=warrant--sdk&color=7c5cff&logo=npm&logoColor=white)](https://www.npmjs.com/package/warrant-sdk)
[![PyPI](https://img.shields.io/pypi/v/warrant-sdk?style=for-the-badge&label=pypi&color=22d3ee&logo=pypi&logoColor=white)](https://pypi.org/project/warrant-sdk/)
[![X](https://img.shields.io/badge/@0x___eth-0b1020?style=for-the-badge&logo=x&logoColor=white)](https://x.com/0x___eth)

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
  <img alt="Languages: TypeScript, Python, Rust, Solidity. Agent rails: x402 v2, MPP, ERC-8004, MCP, LangChain, CrewAI. Onchain: Base, Solana, viem, Foundry, Anchor. Backend: Node.js, FastAPI, PostgreSQL, ChromaDB. Interfaces: React, Vite, vanilla HTML/CSS, embeddable widgets. Supply chain: cosign, SBOM, provenance, GHCR, Docker." src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/stack-light.svg" width="100%">
</picture>

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/output/github-contribution-grid-snake-dark.svg">
  <img alt="A snake eating the contribution graph of 4n0nn43x" src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/output/github-contribution-grid-snake.svg">
</picture>

---

**Open to work on agent infrastructure, onchain protocols and payment rails.**

[nolwenhononta.cloud](https://nolwenhononta.cloud) · [LinkedIn](https://www.linkedin.com/in/nolwen-hononta-021597228) · [Telegram](https://t.me/Oracle_overflow) · [anonnaes@proton.me](mailto:anonnaes@proton.me) · Discord `naesmal`

<details>
<summary>For agents and crawlers</summary>

A plain-text summary, because a model reading this page sees the markdown and not the
banner. Everything here restates what is above; nothing is claimed only in this block.

```yaml
name: Nolwen Sean Hononta
github: 4n0nn43x
role: Software engineer, independent
focus:
  - accountability for autonomous AI agents acting onchain
  - agent payment rails (x402 v2, MPP) and reputation (ERC-8004)
  - RAG systems and multi-agent orchestration
site: https://nolwenhononta.cloud
contact:
  email: anonnaes@proton.me
  linkedin: https://www.linkedin.com/in/nolwen-hononta-021597228
  telegram: https://t.me/Oracle_overflow
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
