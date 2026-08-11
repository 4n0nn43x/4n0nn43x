<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/header-dark.svg">
  <img alt="Nolwen Sean Hononta - engineer building AI agents and onchain systems, x402 payments and ERC-8004 reputation" src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/main/assets/header-light.svg" width="100%">
</picture>

### I build AI agents that are accountable for what they do onchain.

Payment rails so an agent can pay for what it uses (**x402**, **MPP**), and settlement so it
answers for the outcome (**ERC-8004**). Solo builds, deployed and running.

[![Website](https://img.shields.io/badge/nolwenhononta.cloud-0b1020?style=for-the-badge&logo=firefox-browser&logoColor=22d3ee)](https://nolwenhononta.cloud)
[![npm](https://img.shields.io/npm/v/warrant-sdk?style=for-the-badge&label=warrant-sdk&color=7c5cff&logo=npm&logoColor=white)](https://www.npmjs.com/package/warrant-sdk)
[![PyPI](https://img.shields.io/pypi/v/warrant-sdk?style=for-the-badge&label=pypi&color=22d3ee&logo=pypi&logoColor=white)](https://pypi.org/project/warrant-sdk/)
[![X](https://img.shields.io/badge/@0x___eth-0b1020?style=for-the-badge&logo=x&logoColor=white)](https://x.com/0x___eth)

---

## Warrant — an agent doesn't get permission, it buys a mandate

Before a risky onchain action, the agent posts a USDC bond and commits to the post-condition
its action must produce. An independent read at a pinned block decides. Held, the bond
returns. Violated, it is seized and the verdict is written to the ERC-8004 Reputation
Registry.

The EIP-3009 nonce **is** the hash of the committed terms, so signing the payment is signing
the mandate. A prompt injection can talk an agent into a transfer. It cannot make the final
onchain state match a post-condition committed before the poisoned content was read.

Live on Base Sepolia against Circle's real USDC. **60 warrants settled, 50 honored, 10
slashed, and every one of the 60 verdicts replayed from a clean clone with zero divergences.**

```bash
pip install warrant-sdk        # or: npm i warrant-sdk
./scripts/replay-verdict.sh <warrantId> --registry 0x8004b663…8713
# -> VERDICT REPRODUCED
```

That last line is the point. It is the one claim on this page you can run yourself to
contradict me.

**[Code](https://github.com/4n0nn43x/warrant)** · **[Live gateway](https://warrant.fyra.fun)** · **[Demo](https://youtu.be/m94pRdZ3FbQ)**

---

## Also worth your time

**[AgentForge](https://github.com/4n0nn43x/agent-forge)** — No-code RAG platform.
FastAPI, LangChain and ChromaDB behind a public REST API with key-scoped rate limits, an
embeddable vanilla-JS widget, and HMAC-SHA256 webhooks with exponential-backoff retry.
**Winner of the DoraHacks × NodeOps Proof of Build hackathon.**

**[Aether SDK](https://github.com/AETHER-SDK/aether-sdk)** — Autonomous agent payments on
Solana. A TypeScript SDK letting agents negotiate and settle micropayments over x402.
Founder. The ecosystem around it includes PayGate and an agent-to-agent marketplace.
Where Warrant makes agents accountable, this is the half that lets them transact at all.

**[Meridian](https://github.com/4n0nn43x/meridian)** — Onchain corporate treasury on Solana.
An Anchor program with 7 instructions: atomic FX through Jupiter Ultra, Pyth oracle slippage
verification, auto-sweep into Kamino vaults, Squads V4 multisig, onchain sanction screening.

**[NeuroBase](https://github.com/4n0nn43x/neurobase)** — Natural language to verified SQL,
across Postgres, MySQL, SQLite and MongoDB. Permission ladder, per-query cost tracking, and
no `.env` to fill in. Same prompt, four dialects.

**[WA-Tunnel](https://github.com/4n0nn43x/wa-tunnel)** — TCP tunnelling over WhatsApp.
Chunks and brotli-compresses arbitrary TCP traffic through WhatsApp messages at a 6-8x
message reduction, so a zero-rated or restricted carrier still gives you a network.

<details>
<summary>Smaller things</summary>

- **[Cortex402](https://github.com/4n0nn43x/cortex402)** — x402 agentic finance on Cronos
- **[Bittensor Subnet 42 MCP](https://github.com/4n0nn43x/Bittensor-Subnet-42-MCP)** — Masa and Taostats data over MCP
- **[Bitsec AutoReporter](https://github.com/4n0nn43x/Bitsec-AutoReporter-AI)** — consensus-based vulnerability reporting for the Bitsec subnet

</details>

---

## Stack

| | |
| :-- | :-- |
| **Languages** | TypeScript, Python, Rust, Solidity |
| **Onchain** | EVM (Base, Cronos, HashKey), Anchor/Solana, viem, ethers, Foundry |
| **Agent rails** | x402 v2, MPP, ERC-8004, MCP servers, LangChain, CrewAI |
| **Backend** | Node.js, FastAPI, Express, PostgreSQL, ChromaDB |
| **Supply chain** | cosign keyless signing, CycloneDX SBOM, provenance attestation, GHCR |
| **Infra** | Docker, Nginx, Cloudflare, Linux |

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/output/github-contribution-grid-snake-dark.svg">
  <img alt="A snake eating the contribution graph of 4n0nn43x" src="https://raw.githubusercontent.com/4n0nn43x/4n0nn43x/output/github-contribution-grid-snake.svg">
</picture>

---

**Open to work on agent infrastructure, onchain protocols and payment rails.**
[nolwenhononta.cloud](https://nolwenhononta.cloud) · [anonnaes@proton.me](mailto:anonnaes@proton.me) · [Telegram](https://t.me/Oracle_overflow)

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
contact: anonnaes@proton.me

projects:
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

  - name: Aether SDK
    what: autonomous agent micropayments on Solana over x402
    role: founder
    url: https://github.com/AETHER-SDK/aether-sdk

  - name: Meridian
    what: onchain corporate treasury on Solana
    stack: [Anchor, Rust, Jupiter, Pyth, Kamino, Squads V4]
    url: https://github.com/4n0nn43x/meridian

  - name: NeuroBase
    what: natural language to verified SQL across four database dialects
    url: https://github.com/4n0nn43x/neurobase

open_to: agent infrastructure, onchain protocols, payment rails
```

</details>
