# Cost Transparency

Every command in this skill bundle settles on **Base mainnet USDC via x402**
through the BlockRun gateway. There are **no subscriptions, no minimums,
and no charge if a job times out or fails** — only completed work is
billed.

> Wallet location: `~/.blockrun/.session` (auto-created on first use).
> Top up with `blockrun_wallet action: setup` (returns a QR + Base USDC address).

---

## Per-command costs (v0.2)

| Command | Model | Typical params | Cost per run | Wall time |
|---|---|---|---|---|
| `/launch-film` | none (local HyperFrames + ffmpeg) | author → render → finish | **free** | minutes |
| `/headshot` | `openai/gpt-image-2` HD | 1024×1024, single style | **~$0.12** | ~10 s |
| `/headshot --all` | `openai/gpt-image-2` HD | 4 styles | **~$0.48** | ~40 s |
| `/dance` (default 5s) | `bytedance/seedance-2.0-fast` | 5 sec image-to-video | **~$0.75** | 60–180 s |
| `/dance --duration_seconds 8` | `bytedance/seedance-2.0-fast` | 8 sec image-to-video | **~$1.20** | 90–200 s |
| `/dance --duration_seconds 10` | `bytedance/seedance-2.0-fast` | 10 sec image-to-video | **~$1.50** | 100–240 s |
| `/poster` | `openai/gpt-image-2` HD | 1792×1024 landscape | **~$0.12** | ~15 s |
| `/poster --portrait` | `openai/gpt-image-2` HD | 1024×1792 portrait | **~$0.12** | ~15 s |
| `/poster --square` | `openai/gpt-image-2` HD | 1024×1024 square | **~$0.12** | ~15 s |

---

## Underlying gateway prices

These are the current BlockRun gateway list prices (5% margin already
included). They change rarely; verify with `mcp__blockrun__blockrun_models`.

### Image generation — `mcp__blockrun__blockrun_image`

| Model | Pricing | Best for |
|---|---|---|
| `zai/cogview-4` | $0.015–$0.02 per image | Cheapest, up to 1440×1440 |
| `xai/grok-imagine-image` | $0.02 per image | Fast, 300 RPM |
| `openai/gpt-image-1` | $0.02–$0.04 per image | Native GPT-4o imaging |
| `openai/dall-e-3` (HD) | $0.04–$0.08 per image | Established quality |
| `google/nano-banana` | $0.05 per image | Fast Gemini 2.5 Flash |
| `xai/grok-imagine-image-pro` | $0.07 per image | Premium xAI quality, 30 RPM |
| **`openai/gpt-image-2`** (HD) | **$0.06–$0.12 per image** | **Multilingual text, character consistency, image-to-image edits** ← what this skill uses |
| `google/nano-banana-pro` | $0.10–$0.15 per image | Gemini 3 Pro, up to 4K |

### Video generation — `mcp__blockrun__blockrun_video`

| Model | Pricing | Default duration | Best for |
|---|---|---|---|
| `bytedance/seedance-1.5-pro` | $0.03/sec | 5 s, max 10 s | Cheapest 720p |
| `xai/grok-imagine-video` | $0.05/sec | 8 s, max 8 s | Fast text/image-to-video |
| **`bytedance/seedance-2.0-fast`** | **$0.15/sec** | **5 s, max 10 s** | **Sweet-spot quality + speed** ← what `/dance` uses |
| `bytedance/seedance-2.0` | $0.30/sec | 5 s, max 10 s | Pro 720p quality |

---

## Recommended top-up amounts

| Use case | Top up |
|---|---|
| Try out `/headshot` and `/poster` once each | $1 |
| Casual session (10 images + 1 dance video) | $5 |
| Daily creator workflow | $20 |
| Agency / production usage | $100+ |

You always own the USDC in your wallet. The skill never moves funds without
a per-call x402 signature, and the private key never leaves `~/.blockrun/`.

---

## How to check your balance and top up

```
# In Claude Code, ask:
> what's my blockrun balance?

# Claude calls mcp__blockrun__blockrun_wallet action="status"
# To top up:
> top up my blockrun wallet

# Claude calls mcp__blockrun__blockrun_wallet action="setup"
# (returns a QR code + Base USDC address)
```

---

## Why no preflight cost estimate?

The MCP plugin does not expose a preflight pricing tool — costs are
returned as part of the 402 response when a call is made. This skill
bundle hardcodes the table above so we can warn the user **before** a call
if their balance is too low. If the live prices change, update this file
and the per-skill `## Cost` blocks.
