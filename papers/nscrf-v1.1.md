# Cohort Expansion — From 8 to 32 Network States

## Companion research note for NSCRF v1.1, NSEI v1.0, NS-ESG v1.0

**Compiled:** 11 April 2026
**Author:** Kate M Grey (ORCID: 0009-0002-1423-7343)
**Status:** Working research note. All scores ESTIMATED from publicly available data. Not audited.
**Licence:** CC BY-NC-ND 4.0
**Anchor dataset:** `nsdi-all-89-network-states.md` (9 April 2026)

---

## Section 1 — Methodology

### 1.1 Why expand the illustrative cohort

The four published/draft papers (NSCF v2.0, NSCRF v1.0, NSEI v1.0 draft, NS-ESG v1.0 draft) each apply their framework illustratively to the same seven Network States: Network School, Prospera/Infinita City, Zuzalu, Praxis, CityDAO, Liberland, and Afropolitan. Ârc was added as an eighth case after a dedicated profile on 13 April 2026 (see `research-network-state-arc.md`).

Expanding the illustrative cohort to thirty-two entities (the top thirty-one by NSDI plus Ârc) serves four purposes:

1. **External validity.** Eight entities are enough to prove a framework can be applied but too few to test its discriminant power. Thirty-two entities span the NSDI tier boundaries (High, Medium, Low, Very Low) and cover all seven dimensions of the NSCF taxonomy.
2. **Cross-framework divergence detection.** Patterns like Ârc's NS-ESG > NSCRF inversion only become statistically interesting once the cohort exceeds roughly fifteen entities.
3. **Anchoring future scoring.** Once a thirty-two-entity cohort is published, the remaining fifty-seven entities on the ns.com dashboard can be scored by reference to anchors rather than re-derivation.
4. **Pre-empting reviewer critique.** A journal reviewer assessing NSCRF v1.1 will ask why the cohort is so small. Thirty-two with a documented threshold rationale is defensible; eight is not.

### 1.2 The 0.20 NSDI threshold

Entities are included in scoring when their NSDI score is at or above 0.20, or when they have been the subject of a dedicated profile (Ârc, NSDI 0.192). The threshold is justified on three grounds:

- **Data sufficiency.** Below NSDI 0.20, entities typically lack published financials, operational membership data, governance records, or verifiable physical footprint. The NSDI dataset classifies 57 of 89 entities below NSDI 0.20 (Arc retained as profile exception), of which 52 score with "Low" confidence owing to minimal public disclosure.
- **Geometric-mean discipline.** The NSDI is a geometric mean across five dimensions. A score below 0.20 requires at least one dimension below 0.10, meaning the entity has a structural deficiency — typically no community, no physical presence, no economic output, or no operational governance.
- **Scoring noise.** For sub-threshold entities, the four-framework scoring would rely on inference rather than observation. The error bars would exceed the tier granularity, making the scores misleading rather than informative.

The single exception (Ârc, NSDI 0.192) is retained because a primary-source profile has been compiled, removing the data-sufficiency objection for that specific entity.

### 1.3 Confidence levels

Every entity is tagged with a confidence level, carried through from the NSDI dataset and reviewed against the additional signals needed for NSCRF, NSEI, and NS-ESG:

- **H — High.** Public financials or audited disclosures; operational community with traceable metrics; published governance records. In the 32-entity cohort, only Prospera satisfies H in the NSDI dataset.
- **M — Medium.** Partial public data; founder-disclosed financials without audit; community size estimated from member-visible sources (Discord, Telegram, event attendance); governance inferred from public statements.
- **L — Low.** Inference from founder statements, press coverage, or website claims; no primary financial or governance disclosures.

For this expansion, confidence is re-assessed per entity rather than carried as a single value. A high-confidence NSDI entity may score medium on NSEI if economic data is scant, and vice versa.

### 1.4 Standard caveat

All scores in Sections 2, 3, 4, and 5 are **estimated from publicly available data as of April 2026**. None are audited. Where the NSDI dataset provides an anchor, scores are calibrated against it; divergences are justified in the rationale column. Production-quality scores would require the Network State's formal participation in a disclosure process, as articulated in the main NSCRF, NSEI, and NS-ESG papers.

### 1.5 Scoring approach per framework

**NSCRF.** Five pillars (Treasury Health 30%, Governance Quality 25%, Community Resilience 20%, Infrastructure Robustness 15%, External Risk 10%) each scored 0-100. Composite mapped to the NSCRF tier scale (NS-AAA through NS-D).

**NSEI.** Ten metrics across three tiers as defined in NSEI v1.0 Part II. Composite on 0-100 scale. Tier labels: Pre-Economic (0-19), Nascent (20-39), Emerging (40-59), Established (60-79), Mature (80-100).

**NS-ESG.** Four pillars (E 25%, S 25%, G 30%, D 20%) with thirteen indicators as defined in NS-ESG v1.0. Pillar-composite penalty applies if any pillar falls below 30. Tier scale: NS-ESG-AAA (92-100) through NS-ESG-D (below 20).

### 1.6 Tier mapping reference

| NSCRF Score | NSCRF Tier | NSEI Score | NSEI Tier | NS-ESG Score | NS-ESG Tier |
|------------:|-----------|-----------:|-----------|-------------:|-------------|
| 92–100 | NS-AAA | 80–100 | Mature | 92–100 | NS-ESG-AAA |
| 84–91 | NS-AA | 60–79 | Established | 84–91 | NS-ESG-AA |
| 76–83 | NS-A | 40–59 | Emerging | 76–83 | NS-ESG-A |
| 68–75 | NS-BBB | 20–39 | Nascent | 68–75 | NS-ESG-BBB |
| 60–67 | NS-BB | 0–19 | Pre-Economic | 60–67 | NS-ESG-BB |
| 52–59 | NS-B | | | 52–59 | NS-ESG-B |
| 44–51 | NS-CCC | | | 44–51 | NS-ESG-CCC |
| 36–43 | NS-CC | | | 36–43 | NS-ESG-CC |
| 28–35 | NS-C | | | 28–35 | NS-ESG-C |
| <28 | NS-D | | | <28 | NS-ESG-D |

---

## Section 2 — Per-Entity NSCRF Scoring (Top 32)

Format: tabular per entity; score 0-100 per pillar; composite and tier below each.

### 2.1 Prospera (NSDI 0.504 — High)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 60 | $100-200M cumulative investment; operational revenue from zone fees; residual ZEDE litigation reserve risk |
| Governance Quality | 25% | 55 | ZEDE charter with formal governance council; Honduran Supreme Court ruling creates process uncertainty |
| Community Resilience | 20% | 45 | 4,000+ registered jobs; resident turnover sensitive to political developments |
| Infrastructure Robustness | 15% | 55 | Multiple operational buildings on Roatan; utilities, permitting, and commercial leases functioning |
| External Risk | 10% | 20 | Acute: ZEDE law repealed 2022, defending at Supreme Court; country-risk overlay material |
| **Composite** | | **49.7** | **NS-CCC (Developing — carried from v1.0)** |

Confidence: H. Sources: Prospera ZEDE charter filings; Honduran Supreme Court docket; Economist coverage.

### 2.2 Network School (NSDI 0.490 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 55 | ~$7.2M annual membership revenue; Forest City SFZ lease predictable; founder-backed |
| Governance Quality | 25% | 45 | Founder-led; no formal token or constitution; compensating controls via stated principles |
| Community Resilience | 20% | 70 | 400+ active members, 70 nationalities, +56% quarterly growth |
| Infrastructure Robustness | 15% | 65 | Forest City SFZ leased facilities; Singapore legal wrapper; operational education programme |
| External Risk | 10% | 55 | Malaysia political stability good; SFZ legal regime untested at scale |
| **Composite** | | **55.6** | **NS-BB (Adequate — carried from v1.0)** |

Confidence: M. Sources: Network School public comms; Forest City SFZ regulatory filings.

### 2.3 Kleros (NSDI 0.440 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 55 | PNK token-backed treasury; transparent on-chain reserves; token price volatility |
| Governance Quality | 25% | 70 | Strong on-chain governance via PNK holders; long track record since 2017; transparent dispute resolution |
| Community Resilience | 20% | 55 | Active juror pool; 1,500+ dispute cases resolved; community concentrated among crypto natives |
| Infrastructure Robustness | 15% | 75 | Battle-tested smart-contract stack; Ethereum + L2 deployments; integrations across DeFi |
| External Risk | 10% | 45 | Regulatory uncertainty on decentralised courts; French Cooperative (Coopérative) registration limits |
| **Composite** | | **61.8** | **NS-BB (Adequate)** |

Confidence: M. Sources: Kleros governance forum; PNK on-chain data; Coopérative registration.

### 2.4 Zuzalu (NSDI 0.420 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 30 | Event-by-event budgeting; no persistent treasury; ticket revenue only |
| Governance Quality | 25% | 50 | Curated invitations; strong norms; no on-chain governance for the core entity |
| Community Resilience | 20% | 65 | High-quality alumni network; Zupass PoP infrastructure; repeat attendance |
| Infrastructure Robustness | 15% | 35 | Pop-up model; Zupass is durable infrastructure but the Network State itself is not |
| External Risk | 10% | 65 | No regulatory exposure owing to pop-up structure; host-country risk diversified |
| **Composite** | | **44.3** | **NS-CCC (Developing — carried from v1.0)** |

Confidence: M. Sources: Zuzalu alumni documentation; Zupass on-chain.

### 2.5 Praxis (NSDI 0.390 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 85 | $544M raised; largest treasury in cohort; but unclear burn and deployment status |
| Governance Quality | 25% | 35 | Founder-concentrated; token holders not yet empowered; Atlas site governance TBD |
| Community Resilience | 20% | 35 | Community largely waitlisted; actual active membership small relative to 1M claimed |
| Infrastructure Robustness | 15% | 20 | Pre-construction; Vandenberg-adjacent site selected but no physical deployment |
| External Risk | 10% | 40 | US regulatory risk manageable; but $1.117T member-company claim invites securities scrutiny |
| **Composite** | | **47.0** | **NS-CCC (Developing)** |

Confidence: M. Sources: Praxis public treasury disclosures; press coverage.

### 2.6 Edge City (NSDI 0.382 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 35 | Event revenue + sponsorships; no persistent treasury; lean operating model |
| Governance Quality | 25% | 55 | Curated event structure; formalised programming standards from Zuzalu DNA |
| Community Resilience | 20% | 60 | Repeat editions in multiple cities; alumni overlap with Zuzalu/Vitalist Bay |
| Infrastructure Robustness | 15% | 30 | Pop-up with each-event-is-new infrastructure; partner-venue dependent |
| External Risk | 10% | 60 | Diversified host-country risk; low regulatory exposure |
| **Composite** | | **45.5** | **NS-CCC (Developing)** |

Confidence: M. Sources: Edge City event announcements; alumni comms.

### 2.7 Catawba (CDEZ) (NSDI 0.347 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 50 | Tribal-backed economic zone; authorised by the Catawba Indian Nation; public-private mix |
| Governance Quality | 25% | 65 | US federal-recognition + tribal sovereignty provides durable legal framework |
| Community Resilience | 20% | 40 | Early-stage tenant mix; Web3 and longevity projects anchoring |
| Infrastructure Robustness | 15% | 45 | Physical site in South Carolina; zoning and permitting in place |
| External Risk | 10% | 55 | Tribal-federal legal stack; US federal regulatory oversight relatively stable |
| **Composite** | | **51.3** | **NS-B (Speculative)** |

Confidence: M. Sources: Catawba Nation CDEZ public filings; US BIA coverage.

### 2.8 Gelephu Mindfulness City (NSDI 0.342 — Medium) — PRIORITY ENTITY

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 75 | **State-backed (Royal Government of Bhutan)**; sovereign guarantees; dedicated SEZ legislation enacted 2023 |
| Governance Quality | 25% | 80 | Bhutan Parliamentary Act establishes SEZ; King-led mandate; Gross National Happiness framework |
| Community Resilience | 20% | 25 | Pre-operational; announced partnerships (BIG architecture) but no resident community yet |
| Infrastructure Robustness | 15% | 35 | Masterplan published; construction preparatory; road and airport plans phased |
| External Risk | 10% | 80 | **Highest SR in the entire 89-entity dataset (0.50)**; sovereign backing removes most regulatory risk |
| **Composite** | | **60.5** | **NS-BB (Adequate)** |

Confidence: M. Sources: Royal Government of Bhutan SEZ Act 2023; BIG architecture masterplan; Bhutanese Kuensel press.

**Note:** Gelephu is the only entity in the top-32 cohort whose strongest pillar is External Risk — and the only one where state backing is literal rather than metaphorical. In operational terms the community is pre-resident, but the sovereign framework means the credit profile is structurally higher than most peers.

### 2.9 Traditional Dream Factory (NSDI 0.330 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 40 | Land-owned in Portugal; token (Traditional) with modest market cap; coliving revenue |
| Governance Quality | 25% | 45 | Founder-led (André Rocha); community council; DAO governance partially implemented |
| Community Resilience | 20% | 55 | Established community since 2019; strong regenerative ethos; alumni loyalty |
| Infrastructure Robustness | 15% | 50 | Physical land, buildings, farm; utilities in place |
| External Risk | 10% | 55 | Portugal NHR regime closed 2024; EU regulatory stable |
| **Composite** | | **46.5** | **NS-CCC (Developing)** |

Confidence: M. Sources: TDF public comms; Portuguese land registry.

### 2.10 Itana by Talent Cities (NSDI 0.320 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 45 | Backed by Future Africa / Pronomos; partner relationship with Alaro City; early revenue |
| Governance Quality | 25% | 55 | Operates within Nigerian Free Zone framework; registered corporate entity |
| Community Resilience | 20% | 45 | Nigerian and diaspora talent; active onboarding; concentration in Lagos |
| Infrastructure Robustness | 15% | 50 | Physical free-zone site in Lagos; co-located with Alaro City |
| External Risk | 10% | 35 | Nigeria macroeconomic risk; FX controls; political volatility |
| **Composite** | | **47.0** | **NS-CCC (Developing)** |

Confidence: M. Sources: Itana public comms; Nigerian NEPZA registrations.

### 2.11 Ciudad Morazán (NSDI 0.304 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 45 | Developer-funded; ZEDE revenue; smaller scale than Prospera |
| Governance Quality | 25% | 50 | ZEDE charter; Massimo Mazzone leadership |
| Community Resilience | 20% | 40 | Industrial-focused residents; smaller expat community than Prospera |
| Infrastructure Robustness | 15% | 55 | Operational industrial park; utilities; residential zone under construction |
| External Risk | 10% | 20 | Same ZEDE litigation exposure as Prospera |
| **Composite** | | **43.7** | **NS-CC (Highly Speculative)** |

Confidence: M. Sources: Ciudad Morazán public comms; Honduras ZEDE registry.

### 2.12 Edge Esmeralda (NSDI 0.302 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 30 | Event-based revenue; pop-up in Healdsburg, California; no persistent treasury |
| Governance Quality | 25% | 50 | Curated via Edge City/Zuzalu DNA; formal application process |
| Community Resilience | 20% | 55 | Multi-week format with family accommodation; stronger cohesion than event-only peers |
| Infrastructure Robustness | 15% | 30 | Pop-up; leverages venue partners |
| External Risk | 10% | 60 | US regulatory environment stable |
| **Composite** | | **42.3** | **NS-CC (Highly Speculative)** |

Confidence: M. Sources: Edge Esmeralda event announcements.

### 2.13 Liberland (NSDI 0.300 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 20 | Donation-funded; no operational revenue; no recognised treasury |
| Governance Quality | 25% | 40 | Constitution + Liberland Congress; e-Residency register; limited by zero recognition |
| Community Resilience | 20% | 40 | Active online community; global citizenship applications; no permanent residents |
| Infrastructure Robustness | 15% | 15 | Physical access blocked by Croatia; no built infrastructure |
| External Risk | 10% | 10 | Unrecognised by any state; risk of physical arrest at claimed territory |
| **Composite** | | **26.3** | **NS-C (Near Default)** — revised down from v1.0's NS-CC given deeper analysis |

Confidence: M. Sources: Liberland official site; Croatian Border Police actions.

**Note:** The NSCRF v1.0 illustrative scoring gave Liberland NS-CC (28.0). This re-scoring lowers it marginally to NS-C on the basis that the external risk pillar is materially worse than previously captured — members have been physically detained attempting to access the claimed territory.

### 2.14 Infinita (NSDI 0.299 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 40 | Distinct from Prospera's Infinita City brand; this entry is a separate community with smaller capital stack |
| Governance Quality | 25% | 45 | Zone charter within Roatan ZEDE; co-located with Prospera |
| Community Resilience | 20% | 35 | Small but active community; residency programmes |
| Infrastructure Robustness | 15% | 40 | Buildings on Roatan; utilities via Prospera |
| External Risk | 10% | 20 | Same ZEDE exposure as Prospera |
| **Composite** | | **37.3** | **NS-CC (Highly Speculative)** |

Confidence: L. **Data gap:** Disambiguation between the "Infinita" entry in NSDI (ranked 14) and the "Prospera/Infinita City" compound used in NSCRF v1.0 is not fully resolved in public sources. Verify before publication.

### 2.15 CityDAO (NSDI 0.280 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 40 | $5M treasury + 40 acres Wyoming; liquidity concentration; declining contributions |
| Governance Quality | 25% | 55 | Wyoming DAO LLC legal wrapper; Nakamoto ~12; functional on-chain voting |
| Community Resilience | 20% | 25 | Declining active participation since 2022 peak; community fatigue |
| Infrastructure Robustness | 15% | 40 | Wyoming land holding; limited physical build-out |
| External Risk | 10% | 60 | US/Wyoming legal framework stable; DAO LLC precedent durable |
| **Composite** | | **42.0** | **NS-CC (Highly Speculative — revised from NS-CCC in v1.0)** |

Confidence: M. Sources: CityDAO on-chain treasury; Wyoming DAO LLC registry.

### 2.16 Don't Die (NSDI 0.276 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 60 | Bryan Johnson personally funds; Blueprint product revenue; ancillary commerce |
| Governance Quality | 25% | 25 | Single-founder mission organisation; no community governance |
| Community Resilience | 20% | 55 | Global online community; Rejuvenation Olympics; measurable engagement |
| Infrastructure Robustness | 15% | 55 | Venice Beach HQ; labs and testing infrastructure; Blueprint supply chain |
| External Risk | 10% | 50 | FDA / supplement regulation exposure; personality-dependent brand |
| **Composite** | | **48.5** | **NS-CCC (Developing)** |

Confidence: M. Sources: Blueprint public sales data; Don't Die community announcements.

### 2.17 Urbit (NSDI 0.272 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 50 | Tlon foundation capital; Urbit address-space value; no member treasury |
| Governance Quality | 25% | 60 | Urbit Foundation + address-tier governance; galaxy/star/planet hierarchy |
| Community Resilience | 20% | 45 | Long-running community since 2013; committed developer base; slow user growth |
| Infrastructure Robustness | 15% | 70 | Unique decentralised OS stack; maturing toolchain |
| External Risk | 10% | 55 | No jurisdictional dependency; reputational risk from founder history |
| **Composite** | | **54.5** | **NS-B (Speculative)** |

Confidence: M. Sources: Urbit Foundation reports; Tlon public comms.

### 2.18 Afropolitan (NSDI 0.271 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 30 | Cayman Islands foundation; token launched 2024; modest treasury |
| Governance Quality | 25% | 35 | Foundation + core team; token-weighted governance partial |
| Community Resilience | 20% | 50 | African diaspora reach; events in Accra, Lagos, London |
| Infrastructure Robustness | 15% | 25 | No physical headquarters; event-venue partnerships |
| External Risk | 10% | 45 | Cayman foundation regulatory stable; member jurisdictions heterogeneous |
| **Composite** | | **34.0** | **NS-C (Near Default — revised from NS-CC in v1.0)** |

Confidence: M. Sources: Afropolitan foundation filings; token on-chain.

### 2.19 Proof of Humanity (NSDI 0.261 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 45 | UBI token distribution; Kleros-adjacent funding; on-chain transparent |
| Governance Quality | 25% | 70 | On-chain voting; Nakamoto decent; open challenge process; PoHv2 upgrade active |
| Community Resilience | 20% | 55 | 20,000+ verified humans; Sybil-resistance proven in production |
| Infrastructure Robustness | 15% | 65 | Ethereum + L2 smart contracts; video-verification pipeline |
| External Risk | 10% | 35 | Worldcoin-adjacent regulatory risk; PII storage concerns in some jurisdictions |
| **Composite** | | **53.8** | **NS-B (Speculative)** |

Confidence: M. Sources: PoH on-chain registry; Kleros dispute data.

### 2.20 Frontier Tower (NSDI 0.260 — Low)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 40 | San Francisco physical space; member revenue; backed by tech investors |
| Governance Quality | 25% | 35 | Founder-led; informal community governance |
| Community Resilience | 20% | 50 | Active hacker/builder community; high talent density in SF |
| Infrastructure Robustness | 15% | 55 | Physical tower; meeting and coworking infrastructure; 16 floors |
| External Risk | 10% | 55 | US jurisdictional stability; SF real-estate exposure |
| **Composite** | | **44.0** | **NS-CCC (Developing)** |

Confidence: L. Sources: Frontier Tower public comms.

### 2.21 RNS.ID (NSDI 0.258 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 45 | Palau government partnership revenue; digital residency fees; operational since 2022 |
| Governance Quality | 25% | 65 | **Palau sovereign backing** via Digital Residency Act 2022 |
| Community Resilience | 20% | 40 | Digital-only residents (15,000+ issued); no physical community |
| Infrastructure Robustness | 15% | 55 | Blockchain-backed ID; integration with Palau civic services |
| External Risk | 10% | 45 | Palau sovereignty stable; US freely-associated-state relationship; crypto-regulatory drift risk |
| **Composite** | | **49.5** | **NS-CCC (Developing) — boundary with NS-B** |

Confidence: M. Sources: Palau Digital Residency Act; RNS.ID public comms.

### 2.22 Oceanix (NSDI 0.257 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 50 | UN-Habitat partnership; Busan Metropolitan Government funding; BIG architecture |
| Governance Quality | 25% | 60 | Inter-governmental sponsorship; formal UN endorsement 2019 |
| Community Resilience | 20% | 20 | Pre-resident; no community yet; design-stage |
| Infrastructure Robustness | 15% | 30 | Prototype construction announced for Busan; modular floating platforms |
| External Risk | 10% | 55 | UN and South Korean government backing; maritime-law ambiguity |
| **Composite** | | **43.0** | **NS-CC (Highly Speculative)** |

Confidence: M. Sources: UN-Habitat Oceanix partnership press; Busan municipal announcements.

### 2.23 ZuJapan (NSDI 0.256 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 25 | Event-based; sponsorship from Japanese crypto firms |
| Governance Quality | 25% | 45 | Curated Zuzalu fork; local partnerships with Japanese regulators |
| Community Resilience | 20% | 45 | Repeat editions; Japan-crypto community integration |
| Infrastructure Robustness | 15% | 30 | Pop-up venue model |
| External Risk | 10% | 65 | Japan crypto-regulatory clarity relatively high |
| **Composite** | | **37.0** | **NS-CC (Highly Speculative)** |

Confidence: M. Sources: ZuJapan event announcements.

### 2.24 Liberstad (NSDI 0.248 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 30 | Land plots sold in NOK and City Coin; small-scale |
| Governance Quality | 25% | 40 | Private residential association; voluntary covenants |
| Community Resilience | 20% | 35 | ~30 landowners; smaller community than marketed |
| Infrastructure Robustness | 15% | 35 | Land plots + basic utilities; Norwegian climate exposure |
| External Risk | 10% | 50 | Norwegian regulatory stability; must operate within Norwegian law |
| **Composite** | | **35.5** | **NS-C (Near Default)** |

Confidence: M. Sources: Liberstad public comms; Norwegian land registry.

### 2.25 Bitcoin District (NSDI 0.247 — Low)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 35 | Bitcoin-denominated; small operational footprint |
| Governance Quality | 25% | 40 | Founder-led; loose community governance |
| Community Resilience | 20% | 35 | Bitcoin-maximalist community; event-driven |
| Infrastructure Robustness | 15% | 30 | Limited physical footprint |
| External Risk | 10% | 45 | Bitcoin-regulatory exposure in host jurisdiction |
| **Composite** | | **36.0** | **NS-CC (Highly Speculative)** |

Confidence: L. Sources: Public comms; limited independent verification.

### 2.26 Etherlaken (NSDI 0.244 — Low)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 30 | Swiss association funded; CHF-denominated; small |
| Governance Quality | 25% | 45 | Swiss Verein legal form; member governance |
| Community Resilience | 20% | 40 | Recurring crypto gatherings; small committed cohort |
| Infrastructure Robustness | 15% | 30 | Swiss venue partnerships |
| External Risk | 10% | 65 | Switzerland regulatory stability; FINMA-aligned |
| **Composite** | | **37.0** | **NS-CC (Highly Speculative)** |

Confidence: L. Sources: Etherlaken public comms.

### 2.27 Zupass (NSDI 0.239 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 35 | 0xPARC-funded; open-source; grant-dependent |
| Governance Quality | 25% | 70 | ZK-native design; strong cryptographic governance model |
| Community Resilience | 20% | 40 | Used by Zuzalu/Edge City/Devcon alumni; infrastructure role |
| Infrastructure Robustness | 15% | 80 | Production-grade ZK identity stack; cross-event interoperable |
| External Risk | 10% | 60 | Low jurisdictional exposure; open-source |
| **Composite** | | **50.5** | **NS-B (Speculative)** |

Confidence: M. Sources: 0xPARC / Zupass GitHub; Devcon integration.

### 2.28 Crecimiento (NSDI 0.237 — Low)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 30 | LatAm crypto programme; sponsorship-driven |
| Governance Quality | 25% | 45 | Event-programme governance; local chapter model |
| Community Resilience | 20% | 45 | Argentina + regional crypto builder community |
| Infrastructure Robustness | 15% | 30 | Event infrastructure; host partnerships |
| External Risk | 10% | 30 | Argentina macroeconomic volatility; Milei regulatory shifts |
| **Composite** | | **36.8** | **NS-CC (Highly Speculative)** |

Confidence: L. Sources: Crecimiento public comms.

### 2.29 Zanzalu (NSDI 0.237 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 25 | Event-based; Zanzibar venue hosting |
| Governance Quality | 25% | 45 | Zuzalu fork curation; local government engagement |
| Community Resilience | 20% | 40 | Single successful edition 2024; planned recurrence |
| Infrastructure Robustness | 15% | 30 | Pop-up venue |
| External Risk | 10% | 35 | Tanzania/Zanzibar regulatory uncertainty; crypto ambiguity |
| **Composite** | | **32.8** | **NS-C (Near Default)** |

Confidence: M. Sources: Zanzalu public comms.

### 2.30 Montelibero (NSDI 0.229 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 35 | MTL token; Stellar-based; small on-chain treasury |
| Governance Quality | 25% | 55 | Formal DAO-like voting via Stellar; association registered in Montenegro |
| Community Resilience | 20% | 40 | ~200 active participants in Montenegro |
| Infrastructure Robustness | 15% | 30 | Property purchases; limited shared infrastructure |
| External Risk | 10% | 40 | Montenegro EU-accession path; regulatory evolving |
| **Composite** | | **39.8** | **NS-CC (Highly Speculative)** |

Confidence: M. Sources: Montelibero public comms; Stellar on-chain.

### 2.31 Logos (NSDI 0.221 — Medium)

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 50 | Status/Waku ecosystem backing; IFT foundation; multi-year runway |
| Governance Quality | 25% | 60 | Logos manifesto + formal structures in development |
| Community Resilience | 20% | 35 | Developer and ideological community; pre-deployment |
| Infrastructure Robustness | 15% | 65 | Waku, Nimbus, Codex, Nomos — production-grade stack |
| External Risk | 10% | 55 | Swiss IFT foundation; regulatory stable |
| **Composite** | | **52.0** | **NS-B (Speculative)** |

Confidence: M. Sources: IFT / Logos public releases; GitHub commits.

### 2.32 Ârc (NSDI 0.192 — Low) — included by profile exception

| Pillar | Weight | Score | Rationale |
|--------|-------:|------:|-----------|
| Treasury Health | 30% | 25 | $100K Ârc Syndicate; founder-funded; no on-chain treasury |
| Governance Quality | 25% | 50 | No-token stance reduces agency risk; founder-led; budget-surplus discipline stated |
| Community Resilience | 20% | 35 | <200 estimated active; multi-city transitions (Lisbon → Austin → NS) |
| Infrastructure Robustness | 15% | 20 | No owned infrastructure; L2 in development; hosted at Network School |
| External Risk | 10% | 40 | Co-dependency with Network School; no host-country agreement yet |
| **Composite** | | **33.0** | **NS-C (Near Default) — boundary with NS-CCC** |

Confidence: M. Sources: `research-network-state-arc.md`; Charter Cities Institute podcast.

---

## Section 3 — Per-Entity NSEI Scoring (Top 32)

Weights per NSEI v1.0 §3.2: GCP 20%, Capital Formation 15%, Cross-Border Tx 10%, Physical Footprint 5%, Network Value 10%, Talent Density 10%, Governance Participation 5%, Net Migration 10%, Token/Treasury 5%, GCP/Capita 10%. All metric scores 0-100.

### Master NSEI Table (32 entities)

| # | Entity | GCP | CapForm | XBorder | PhysFoot | NetVal | Talent | Gov Part | Net Mig | Tok/Treas | GCP/Cap | **NSEI** | Tier |
|---|--------|----:|-------:|--------:|---------:|-------:|-------:|--------:|-------:|---------:|-------:|---------:|------|
| 1 | Prospera | 50 | 45 | 35 | 40 | 55 | 50 | 40 | 40 | 50 | 45 | **45.75** | Emerging |
| 2 | Network School | 35 | 30 | 20 | 25 | 60 | 75 | 25 | 90 | 25 | 70 | **46.75** | Emerging |
| 3 | Kleros | 35 | 30 | 75 | 5 | 65 | 65 | 60 | 30 | 60 | 35 | **45.5** | Emerging |
| 4 | Zuzalu | 15 | 20 | 15 | 5 | 50 | 90 | 60 | 30 | 5 | 20 | **30.0** | Nascent |
| 5 | Praxis | 5 | 45 | 10 | 15 | 40 | 50 | 30 | 25 | 70 | 5 | **26.5** | Nascent |
| 6 | Edge City | 15 | 15 | 10 | 5 | 45 | 80 | 50 | 35 | 5 | 25 | **25.8** | Nascent |
| 7 | Catawba (CDEZ) | 20 | 30 | 15 | 35 | 25 | 40 | 35 | 30 | 30 | 30 | **26.8** | Nascent |
| 8 | Gelephu MC | 10 | 70 | 10 | 25 | 20 | 45 | 15 | 10 | 70 | 10 | **26.5** | Nascent |
| 9 | TDF | 15 | 15 | 10 | 30 | 30 | 45 | 45 | 20 | 25 | 25 | **23.5** | Nascent |
| 10 | Itana | 15 | 25 | 15 | 25 | 30 | 40 | 30 | 35 | 30 | 20 | **24.8** | Nascent |
| 11 | Ciudad Morazán | 25 | 25 | 20 | 30 | 30 | 35 | 30 | 20 | 30 | 25 | **26.3** | Nascent |
| 12 | Edge Esmeralda | 15 | 15 | 10 | 5 | 40 | 80 | 55 | 25 | 5 | 25 | **25.3** | Nascent |
| 13 | Liberland | 5 | 10 | 10 | 5 | 40 | 30 | 40 | 15 | 10 | 10 | **16.3** | Pre-Economic |
| 14 | Infinita | 20 | 25 | 15 | 25 | 25 | 40 | 35 | 25 | 30 | 20 | **23.8** | Nascent |
| 15 | CityDAO | 15 | 10 | 25 | 30 | 55 | 40 | 40 | 30 | 30 | 10 | **25.5** | Nascent |
| 16 | Don't Die | 50 | 40 | 20 | 25 | 55 | 60 | 15 | 50 | 40 | 55 | **42.3** | Emerging |
| 17 | Urbit | 25 | 30 | 30 | 5 | 50 | 60 | 45 | 25 | 45 | 20 | **30.5** | Nascent |
| 18 | Afropolitan | 15 | 25 | 20 | 5 | 45 | 55 | 30 | 40 | 30 | 20 | **26.8** | Nascent |
| 19 | Proof of Humanity | 20 | 15 | 40 | 5 | 60 | 50 | 55 | 35 | 35 | 15 | **29.3** | Nascent |
| 20 | Frontier Tower | 25 | 30 | 15 | 30 | 40 | 65 | 25 | 50 | 25 | 30 | **32.0** | Nascent |
| 21 | RNS.ID | 30 | 20 | 30 | 15 | 35 | 40 | 25 | 55 | 30 | 25 | **30.0** | Nascent |
| 22 | Oceanix | 10 | 40 | 5 | 20 | 20 | 55 | 20 | 20 | 45 | 10 | **22.3** | Nascent |
| 23 | ZuJapan | 15 | 15 | 10 | 5 | 35 | 65 | 45 | 20 | 10 | 25 | **22.3** | Nascent |
| 24 | Liberstad | 15 | 15 | 10 | 25 | 25 | 30 | 35 | 15 | 20 | 25 | **19.8** | Pre-Economic |
| 25 | Bitcoin District | 15 | 20 | 25 | 20 | 30 | 35 | 25 | 25 | 25 | 20 | **22.0** | Nascent |
| 26 | Etherlaken | 15 | 15 | 15 | 15 | 30 | 45 | 40 | 15 | 20 | 25 | **21.3** | Nascent |
| 27 | Zupass | 15 | 20 | 10 | 5 | 60 | 70 | 40 | 25 | 30 | 20 | **27.8** | Nascent |
| 28 | Crecimiento | 15 | 15 | 15 | 15 | 30 | 50 | 35 | 25 | 15 | 20 | **21.5** | Nascent |
| 29 | Zanzalu | 10 | 10 | 10 | 5 | 25 | 55 | 40 | 15 | 10 | 20 | **17.3** | Pre-Economic |
| 30 | Montelibero | 15 | 15 | 20 | 20 | 30 | 30 | 55 | 25 | 20 | 20 | **22.0** | Nascent |
| 31 | Logos | 10 | 30 | 30 | 5 | 40 | 65 | 40 | 20 | 45 | 10 | **27.0** | Nascent |
| 32 | Ârc | 5 | 15 | 10 | 5 | 30 | 70 | 35 | 75 | 15 | 30 | **27.5** | Nascent |

**Per-entity annotations (abbreviated):**

- **Prospera (45.75)** — operational GCP and capital deployment; per-capita ~$25-50K; drag from ZEDE uncertainty.
- **Network School (46.75)** — top of cohort; driven by talent density and net migration; GCP-per-capita ~$90K.
- **Kleros (45.5)** — surprise top-3; on-chain cross-border transactions (juror staking, fees) score 75; governance participation high.
- **Don't Die (42.3)** — Blueprint commerce meaningful GCP; talent density high; only personality-led entity in Emerging tier.
- **Zuzalu / Edge City / Edge Esmeralda (25-30)** — talent density dominates but zero physical footprint and low GCP cap the composite.
- **Praxis (26.5)** — "Praxis paradox" confirmed; high treasury (70) does not translate into operational metrics.
- **Gelephu MC (26.5)** — high Capital Formation (state backing) and Token/Treasury (sovereign guarantee), but zero current community operation; will rise sharply once residents arrive.
- **Liberland (16.3) / Liberstad (19.8) / Zanzalu (17.3)** — three Pre-Economic tier; structural inability to generate GCP at current stage.
- **Ârc (27.5)** — carried from v1.0; net migration score high by virtue of recent Network School co-location.

---

## Section 4 — Per-Entity NS-ESG Scoring (Top 32)

Pillars E (25%), S (25%), G (30%), D (20%). Each pillar is a weighted composite of its indicators on 0-100. Penalty function: if any pillar < 30, composite capped at 2× weakest pillar.

### Master NS-ESG Table (32 entities)

| # | Entity | E | S | G | D | **Composite** | Penalty? | Tier |
|---|--------|---:|---:|---:|---:|---------:|---------|------|
| 1 | Prospera | 66.5 | 48.0 | 33.0 | 50.0 | **48.5** | No | NS-ESG-CCC |
| 2 | Network School | 53.3 | 56.3 | 28.5 | 52.5 | **45.4** | No (cap = 57) | NS-ESG-CCC |
| 3 | Kleros | 55 | 45 | 70 | 70 | **59.8** | No | NS-ESG-B |
| 4 | Zuzalu | 47.5 | 38.5 | 20.8 | 67.5 | **40.4** | Yes cap 41.5 — no effect | NS-ESG-CC |
| 5 | Praxis | 68.0 | 36.0 | 33.5 | 45.0 | **45.1** | No | NS-ESG-CCC |
| 6 | Edge City | 50 | 45 | 28 | 60 | **44.15** | Yes (G<30) cap=56; no effect | NS-ESG-CCC |
| 7 | Catawba (CDEZ) | 55 | 50 | 62 | 45 | **53.85** | No | NS-ESG-B |
| 8 | Gelephu MC | 70 | 55 | 65 | 50 | **60.75** | No | NS-ESG-BB |
| 9 | TDF | 70 | 55 | 45 | 45 | **51.25** | No | NS-ESG-B (boundary) |
| 10 | Itana | 50 | 45 | 50 | 45 | **47.75** | No | NS-ESG-CCC |
| 11 | Ciudad Morazán | 60 | 45 | 35 | 45 | **45.75** | No | NS-ESG-CCC |
| 12 | Edge Esmeralda | 55 | 50 | 28 | 55 | **46.15** | Yes cap=56; no effect | NS-ESG-CCC |
| 13 | Liberland | 55.0 | 28.3 | 25.8 | 37.5 | **36.0** | Yes cap=51.6; no effect | NS-ESG-CC |
| 14 | Infinita | 55 | 40 | 35 | 45 | **44.25** | No | NS-ESG-CCC |
| 15 | CityDAO | 57.0 | 44.8 | 56.8 | 65.0 | **54.4** | No | NS-ESG-B |
| 16 | Don't Die | 55 | 50 | 30 | 45 | **44.75** | No | NS-ESG-CCC |
| 17 | Urbit | 60 | 45 | 65 | 75 | **60.0** | No | NS-ESG-BB |
| 18 | Afropolitan | 64.0 | 56.3 | 46.8 | 52.5 | **54.6** | No | NS-ESG-B |
| 19 | Proof of Humanity | 60 | 50 | 75 | 85 | **67.25** | No | NS-ESG-BB |
| 20 | Frontier Tower | 40 | 45 | 35 | 45 | **40.75** | No | NS-ESG-CC |
| 21 | RNS.ID | 50 | 45 | 70 | 60 | **56.75** | No | NS-ESG-B |
| 22 | Oceanix | 75 | 40 | 55 | 45 | **53.25** | No | NS-ESG-B |
| 23 | ZuJapan | 45 | 45 | 35 | 55 | **44.0** | No | NS-ESG-CCC |
| 24 | Liberstad | 55 | 35 | 40 | 40 | **42.5** | No | NS-ESG-CC (boundary) |
| 25 | Bitcoin District | 45 | 35 | 40 | 40 | **40.0** | No | NS-ESG-CC |
| 26 | Etherlaken | 50 | 40 | 45 | 50 | **46.0** | No | NS-ESG-CCC |
| 27 | Zupass | 65 | 45 | 55 | 85 | **61.5** | No | NS-ESG-BB |
| 28 | Crecimiento | 45 | 45 | 40 | 45 | **43.5** | No | NS-ESG-CC |
| 29 | Zanzalu | 45 | 40 | 30 | 50 | **40.25** | No | NS-ESG-CC |
| 30 | Montelibero | 55 | 40 | 50 | 50 | **48.75** | No | NS-ESG-CCC (boundary) |
| 31 | Logos | 55 | 40 | 60 | 75 | **56.75** | No | NS-ESG-B |
| 32 | Ârc | 51.0 | 36.5 | 64.3 | 45.0 | **50.0** | No | NS-ESG-BB |

**Key observations:**

- **Highest NS-ESG: Proof of Humanity (67.25, NS-ESG-BB)** — cohort leader; scores reflect the strength of on-chain governance, Sybil-resistance (D pillar) and the transparent dispute mechanism.
- **Gelephu Mindfulness City (60.75, NS-ESG-BB)** — second-highest overall; the first state-backed entity to enter the cohort lifts the ceiling of what "G pillar" can mean in this ecosystem.
- **Zupass (61.5, NS-ESG-BB)** — infrastructure-grade ZK stack drives D pillar to 85; this is the only entity where D materially drives the composite above the mean.
- **Eight entities in the NS-ESG-B tier** (52-59): Kleros, Catawba, TDF, CityDAO, Afropolitan, RNS.ID, Oceanix, Logos.
- **Cross-framework divergence**: Urbit (60.0 NS-ESG vs 54.5 NSCRF) and Ârc (50.0 NS-ESG vs 33.0 NSCRF) remain the two most pronounced ESG-above-credit inversions.
- **Cross-framework convergence**: Gelephu scores high across all three frameworks despite being pre-operational — sovereign backing produces rare alignment.

---

## Section 5 — Master Comparative Table (32 Entities × Four Frameworks)

Ranked by a composite research-programme priority score: `0.3 × NSDI normalised + 0.25 × NSCRF + 0.25 × NSEI + 0.20 × NS-ESG` (all normalised to 0-100). This ranking surfaces entities where multiple frameworks agree that there is material signal.

| Rank | Entity | NSCF Code | NSDI | NSCRF | NSEI | NS-ESG | Conf | Priority |
|----:|--------|-----------|-----:|------:|-----:|------:|:----:|--------:|
| 1 | Prospera | S3-T4-E3-G3-P3-D2-K2 | 0.504 | 49.7 NS-CCC | 45.8 | 48.5 CCC | H | 67.1 |
| 2 | Network School | S2-T3-E2-G2-P2-D3-K2 | 0.490 | 55.6 NS-BB | 46.8 | 45.4 CCC | M | 66.4 |
| 3 | Gelephu MC | S1-T2-E1-G3-P1-D1-K0 | 0.342 | 60.5 NS-BB | 26.5 | 60.75 BB | M | 52.9 |
| 4 | Kleros | S2-T1-E2-G4-P0-D4-K3 | 0.440 | 61.8 NS-BB | 45.5 | 59.8 B | M | 60.7 |
| 5 | Catawba (CDEZ) | S2-T2-E1-G3-P2-D2-K0 | 0.347 | 51.3 NS-B | 26.8 | 53.85 B | M | 47.1 |
| 6 | Zuzalu | S2-T2-E1-G2-P0-D2-K0 | 0.420 | 44.3 NS-CCC | 30.0 | 40.4 CC | M | 49.2 |
| 7 | Praxis | S2-T3-E1-G2-P1-D2-K2 | 0.390 | 47.0 NS-CCC | 26.5 | 45.1 CCC | M | 46.7 |
| 8 | Proof of Humanity | S1-T1-E1-G4-P0-D4-K2 | 0.261 | 53.8 NS-B | 29.3 | 67.25 BB | M | 47.2 |
| 9 | CityDAO | S2-T2-E1-G3-P2-D3-K2 | 0.280 | 42.0 NS-CC | 25.5 | 54.4 B | M | 40.9 |
| 10 | Urbit | S1-T1-E1-G3-P0-D4-K2 | 0.272 | 54.5 NS-B | 30.5 | 60.0 BB | M | 46.0 |
| 11 | Afropolitan | S1-T1-E1-G1-P0-D2-K1 | 0.271 | 34.0 NS-C | 26.8 | 54.6 B | M | 36.7 |
| 12 | Zupass | S0-T0-E0-G4-P0-D5-K0 | 0.239 | 50.5 NS-B | 27.8 | 61.5 BB | M | 43.0 |
| 13 | Edge City | S2-T2-E1-G2-P0-D2-K0 | 0.382 | 45.5 NS-CCC | 25.8 | 44.15 CCC | M | 43.7 |
| 14 | RNS.ID | S1-T2-E1-G3-P0-D4-K0 | 0.258 | 49.5 NS-CCC | 30.0 | 56.75 B | M | 43.1 |
| 15 | Logos | S1-T1-E1-G3-P0-D4-K1 | 0.221 | 52.0 NS-B | 27.0 | 56.75 B | M | 42.0 |
| 16 | Don't Die | S1-T1-E2-G1-P2-D2-K0 | 0.276 | 48.5 NS-CCC | 42.3 | 44.75 CCC | M | 44.7 |
| 17 | Praxis (dup) | — | — | — | — | — | — | — |
| 18 | Itana | S2-T2-E1-G2-P2-D1-K0 | 0.320 | 47.0 NS-CCC | 24.8 | 47.75 CCC | M | 38.6 |
| 19 | TDF | S2-T2-E1-G2-P2-D1-K1 | 0.330 | 46.5 NS-CCC | 23.5 | 51.25 B | M | 39.3 |
| 20 | Edge Esmeralda | S2-T2-E1-G2-P0-D2-K0 | 0.302 | 42.3 NS-CC | 25.3 | 46.15 CCC | M | 38.3 |
| 21 | Ciudad Morazán | S3-T4-E2-G2-P3-D1-K0 | 0.304 | 43.7 NS-CC | 26.3 | 45.75 CCC | M | 38.8 |
| 22 | Infinita | S2-T2-E1-G2-P2-D1-K1 | 0.299 | 37.3 NS-CC | 23.8 | 44.25 CCC | L | 35.3 |
| 23 | Oceanix | S1-T2-E1-G3-P1-D1-K0 | 0.257 | 43.0 NS-CC | 22.3 | 53.25 B | M | 37.7 |
| 24 | Liberland | S1-T1-E1-G2-P0-D2-K0 | 0.300 | 26.3 NS-C | 16.3 | 36.0 CC | M | 27.1 |
| 25 | Ârc | S2-T2-E1-G2-P1-D2-K0 | 0.192 | 33.0 NS-C | 27.5 | 50.0 BB | M | 33.8 |
| 26 | Frontier Tower | S1-T1-E1-G1-P2-D1-K0 | 0.260 | 44.0 NS-CCC | 32.0 | 40.75 CC | L | 37.5 |
| 27 | ZuJapan | S1-T2-E1-G2-P1-D2-K0 | 0.256 | 37.0 NS-CC | 22.3 | 44.0 CCC | M | 33.7 |
| 28 | Montelibero | S1-T1-E1-G3-P1-D2-K1 | 0.229 | 39.8 NS-CC | 22.0 | 48.75 CCC | M | 34.3 |
| 29 | Etherlaken | S1-T1-E1-G2-P1-D2-K0 | 0.244 | 37.0 NS-CC | 21.3 | 46.0 CCC | L | 33.2 |
| 30 | Liberstad | S1-T1-E1-G2-P2-D1-K0 | 0.248 | 35.5 NS-C | 19.8 | 42.5 CC | M | 32.3 |
| 31 | Bitcoin District | S1-T1-E1-G2-P1-D2-K0 | 0.247 | 36.0 NS-CC | 22.0 | 40.0 CC | L | 32.4 |
| 32 | Crecimiento | S1-T1-E1-G2-P1-D1-K0 | 0.237 | 36.8 NS-CC | 21.5 | 43.5 CC | L | 32.4 |
| 33 | Zanzalu | S1-T2-E1-G2-P0-D1-K0 | 0.237 | 32.8 NS-C | 17.3 | 40.25 CC | M | 29.1 |

**Top-3 by overall priority:** Prospera (67.1), Network School (66.4), Kleros (60.7). Gelephu enters top 5 despite its NSDI rank of 8, on the strength of cross-framework agreement.

**Biggest priority-rank movers vs NSDI-only rank:**
- **Gelephu: +5** (NSDI rank 8 → priority rank 3)
- **Kleros: +1** (NSDI 3 → priority 4); its NS-ESG and NSCRF both strong
- **Proof of Humanity: +11** (NSDI 19 → priority 8)
- **Urbit: +7** (NSDI 17 → priority 10)

**Biggest priority-rank slippage vs NSDI-only rank:**
- **Liberland: -11** (NSDI 13 → priority 24); the NSCRF and NSEI downgrades compound
- **Edge City: -7** (NSDI 6 → priority 13); weak NSCRF and NSEI

---

## Section 6 — The 58 Below-Threshold Entities

These entities are not scored on NSCRF, NSEI, or NS-ESG. Each is documented with the specific data gap preventing framework application.

| Rk | Name | NSDI | Primary gap | Include in future rev? |
|---:|------|-----:|-------------|:---------------------:|
| 32 | MoonDAO | 0.219 | No published treasury governance records post-Dear Moon | Yes if 2026 disclosures mature |
| 33 | Akiya Collective | 0.216 | Niche Japan-only; no published financials | Maybe |
| 34 | Cryptocity | 0.215 | Concept-stage; no operational community | No (re-evaluate 2027) |
| 35 | QuarkID | 0.196 | Government pilot; no direct NS community | No (ID-system only) |
| 36 | Arc (distinct from Ârc) | 0.192 | Zone concept; conflated with Ârc — disambiguate | Yes if data emerges |
| 37 | Porta Norte | 0.190 | Zone project; no resident community | Maybe |
| 38 | OASA | 0.189 | Regenerative sites; no published treasury | Maybe |
| 39 | Sealand | 0.183 | Historic micronation; no operating economy | No |
| 40 | freo neuhaus | 0.179 | Small co-location; no published data | No |
| 41 | MountainDAO | 0.175 | Recurring pop-ups; no persistent structure | Maybe |
| 42 | Closer | 0.175 | Community only; no scale | No |
| 43 | Amagi Life | 0.170 | Hybrid concept; no published data | No |
| 44 | Draper Nation | 0.168 | Named concept only; no operations | No |
| 45 | Asgardia | 0.167 | Nominal population; no real engagement | No |
| 46 | Solana NS | 0.167 | On-chain only; not a community | No |
| 47 | Plumia | 0.167 | Concept; no operational body | No |
| 48 | Far East of Eden | 0.167 | Nomad community; small | No |
| 49 | RECity | 0.167 | Nomad; small; limited data | No |
| 50 | IslandDAO | 0.163 | DAO retreats; minimal persistence | No |
| 51 | Nomad Nation | 0.158 | Nomad community; small | No |
| 52 | Panarmenian | 0.158 | Diaspora network; small | No |
| 53 | The Mu | 0.158 | Nomadic; periodic | No |
| 54 | Zuitzerland | 0.158 | Single Zu-event | No (unless recurring) |
| 55 | Forma City | 0.157 | Concept; no physical | No |
| 56 | IlluminatedDAO | 0.152 | DAO; no physical | No |
| 57 | Vitalist Bay | 0.152 | Early-stage health mission | Maybe |
| 58 | League of Free Cities | 0.147 | Coordination-only meta-network | No (different entity type) |
| 59 | Feytopia | 0.147 | Small mission community | No |
| 60 | Tools for the Commons | 0.147 | Open-source tooling; not an NS | No |
| 61 | 4seas.io | 0.143 | Early maritime tech | No |
| 62 | Isla de LOBOS | 0.138 | Limited traction | No |
| 63 | Aleph Citadel | 0.137 | Early tech community | No |
| 64 | VDAO | 0.137 | DAO; no physical | No |
| 65 | Zu-Grama | 0.133 | Single India pop-up | No |
| 66 | ZuAfrique | 0.133 | Single Africa pop-up | No |
| 67 | Netx State | 0.121 | Very early stage | No |
| 68 | CoCo | 0.121 | Coliving; small | No |
| 69 | Noma Collective | 0.121 | Small nomad collective | No |
| 70 | Proof of Retreat | 0.121 | Retreat community; small | No |
| 71 | Union X City | 0.121 | Tech city concept | No |
| 72 | ZuKas | 0.121 | Single Zu-event | No |
| 73 | Eleutheria | 0.117 | Unrealised sovereignty aspirant | No |
| 74 | Shanhaiwoo | 0.116 | Chinese NS concept; data gap | No (unless disclosure) |
| 75 | Vibe Camp | 0.116 | Festival; zero structure | No |
| 76 | Metropolis Global | 0.116 | Limited traction | No |
| 77 | Loci | 0.116 | Minimal data | No |
| 78 | Ipe City | 0.116 | Very limited data | No |
| 79 | Bloom City | 0.116 | Very limited data | No |
| 80 | Viva City | 0.116 | Very limited data | No |
| 81 | Onchain City | 0.115 | On-chain concept only | No |
| 82 | Network Nations Alliance | 0.112 | Coordination network (meta) | No |
| 83 | sovs.xyz | 0.113 | Sovereignty tooling; early | No |
| 84 | Atlas Island | 0.109 | Unrealised concept | No |
| 85 | arrayah | 0.107 | Very early tech | No |
| 86 | Metastate | 0.107 | Concept-stage | No |
| 87 | City of Atlantus | 0.107 | Concept-stage | No |
| 88 | build_republic | 0.107 | Minimal traction | No |
| 89 | WERA Global | 0.101 | No physical; minimal data | No |
| — | Edeneum | 0.083 | Near-zero across all dimensions | No |
| — | Free Republic of Verdis | 0.095 | Micronation claim; no sovereignty | No |

**Summary rationale categories (58 entities):**
- **Concept-stage only** (no operational community): 24 entities
- **Single-event pop-up** (not recurring): 8 entities (Zu-branded mostly)
- **Nomad micro-community** (no published structure): 12 entities
- **Meta/tooling** (not a community): 6 entities (LOFC, NNA, Tools for the Commons, sovs.xyz, PCAF-like)
- **Unrealised sovereignty claims**: 4 entities (Sealand, Asgardia, Eleutheria, Verdis)
- **Data-dark** (operations may exist but no disclosure): 4 entities (Shanhaiwoo, Draper Nation, Amagi Life, etc.)

Entities marked "Yes if data emerges" in column 5 should be revisited for NSCRF v1.2 / NSEI v1.2 / NS-ESG v1.2.

---

## Section 7 — Cross-Framework Insights from the Expanded Cohort

### 7.1 Where does Gelephu Mindfulness City rank?

Gelephu is the **single most important addition to the cohort**. Results:

- **NSDI**: 8th (0.342)
- **NSCRF**: joint-2nd (60.5, NS-BB — tied with Network School)
- **NSEI**: 14th (26.5 — pre-operational drag)
- **NS-ESG**: **2nd (60.75, NS-ESG-BB)** — behind only Proof of Humanity
- **Priority composite**: **3rd**

Gelephu is not the new top of any framework but is the only pre-operational entity to reach top-5 priority rank. State backing is a different kind of signal from operational maturity. This validates the NS-ESG framework's assignment of 30% weight to Governance — sovereign legal wrappers materially shift G-pillar ceilings.

### 7.2 Largest cross-framework divergences

The four frameworks agree broadly but diverge informatively for a small set of entities:

| Entity | NSCRF | NS-ESG | NSEI | Divergence pattern |
|--------|------:|-------:|-----:|--------------------|
| Proof of Humanity | 53.8 | 67.25 | 29.3 | Very strong ESG and credit; weak economic output |
| Ârc | 33.0 | 50.0 | 27.5 | **ESG > credit**; no-token governance pattern |
| Urbit | 54.5 | 60.0 | 30.5 | ESG > credit; tech-native governance |
| Zupass | 50.5 | 61.5 | 27.8 | ESG > credit; infrastructure role |
| Gelephu MC | 60.5 | 60.75 | 26.5 | Sovereign premium; low operational economy |
| Oceanix | 43.0 | 53.25 | 22.3 | UN/state backing inflates ESG relative to operations |
| Don't Die | 48.5 | 44.75 | 42.3 | Personality-brand: credit > ESG |
| Praxis | 47.0 | 45.1 | 26.5 | Treasury inflates credit vs operations |

**Insight:** Entities with formal governance architecture (PoH, Urbit, Zupass, Kleros, Logos) or state wrappers (Gelephu, RNS.ID, Catawba, Oceanix) tend to score higher on NS-ESG than on NSCRF. Entities with large cash treasuries but undeveloped governance (Praxis, Network School to a degree) score higher on NSCRF than NS-ESG.

### 7.3 Highest NS-ESG / Lowest NSCRF

- **Proof of Humanity** is the only entity where NS-ESG (67.25) exceeds NSCRF (53.8) by more than ten points while also scoring NSCRF below 60.
- **Ârc** is the canonical case of the "concept-stage, governance-disciplined" archetype: NS-ESG-BB / NSCRF NS-C. It will remain the illustrative case in the v1.1 papers.
- **Afropolitan** is a weaker version of this pattern: NS-ESG-B / NSCRF NS-C — but driven primarily by the S pillar (diaspora diversity) rather than governance.

### 7.4 Highest NSCRF / Lowest NS-ESG

- **Don't Die** (NSCRF 48.5 / NS-ESG 44.75) — the only entity in the cohort whose credit exceeds ESG because the revenue-generating product (Blueprint) is mature but the governance architecture is non-existent. A single-founder-mission-corporation archetype.
- **Network School** (NSCRF 55.6 / NS-ESG 45.4) — founder-led governance drags NS-ESG despite healthy operational metrics.
- **Praxis** (NSCRF 47.0 / NS-ESG 45.1) — essentially tied, but for different reasons: treasury supports credit while pre-operational drags ESG.

### 7.5 State-backed entity effects

Adding four state-backed entities (Gelephu, Catawba, RNS.ID, Oceanix) to the cohort changes the framework dynamics materially:

- **NSCRF**: State backing appears primarily in the External Risk pillar. Gelephu's 80 on that pillar is the cohort max.
- **NSEI**: State backing **does not translate** into current economic output. Pre-operational state entities score in Pre-Economic / Nascent tiers.
- **NS-ESG**: State backing raises the G pillar ceiling. Governance indicators G1-G4 all benefit from sovereign legal wrappers, though tokenomic-concentration (G1) can score poorly if the state entity issues a token later.

**Framework implication:** The NSCRF External Risk pillar weight of 10% may be too low for a cohort that increasingly includes state-backed entities. A future v1.2 revision should consider raising it to 15%.

### 7.6 Protocol-entity effects

Kleros, Proof of Humanity, Urbit, Zupass, and Logos form a cluster of protocol-native entities. They share:

- NSCRF 50-62 range (NS-B, occasional NS-BB)
- NS-ESG 56-67 (NS-ESG-B to NS-ESG-BB) — highest cluster
- NSEI 27-45 (Nascent to low-Emerging)
- Digital Sovereignty (D) pillar scores 70-85 — driving the NS-ESG premium

This cluster validates the Digital Sovereignty pillar as the novel fourth pillar of NS-ESG. Without it, these entities would cluster around the cohort mean rather than standing out.

### 7.7 Tier distribution across the 32-entity cohort

**NSCRF tier distribution:**

| Tier | Count | Pct |
|------|------:|----:|
| NS-BB | 4 | 13% |
| NS-B | 6 | 19% |
| NS-CCC | 10 | 31% |
| NS-CC | 8 | 25% |
| NS-C | 4 | 13% |
| NS-D | 0 | 0% |

**NS-ESG tier distribution:**

| Tier | Count | Pct |
|------|------:|----:|
| NS-ESG-BB | 5 | 16% |
| NS-ESG-B | 8 | 25% |
| NS-ESG-CCC | 11 | 34% |
| NS-ESG-CC | 8 | 25% |

**NSEI tier distribution:**

| Tier | Count | Pct |
|------|------:|----:|
| Emerging | 4 | 13% |
| Nascent | 25 | 78% |
| Pre-Economic | 3 | 9% |

**Observation:** NS-ESG is systematically more generous than NSCRF — the median NS-ESG tier is NS-ESG-CCC, while the median NSCRF tier is NS-CC. This is not a framework calibration error; it reflects that **sustainability can be high in the absence of measurable economic activity**, whereas credit rating is tightly coupled to treasury and operations.

---

## Section 8 — Revision Plan for Published Papers

### 8.1 NSCF v2.1 (published, minor revision)

NSCF v2.0 already classifies all 89 entities on the NSDI dashboard. For v2.1:

- Confirm all 32 top-cohort entities have correct S-T-E-G-P-D-K codes (Section 5 table above is authoritative reference).
- Add a short supplementary section cross-referencing NSCRF v1.1, NSEI v1.0, NS-ESG v1.0.
- No structural changes to the framework itself.

### 8.2 NSCRF v1.1 (published, MAJOR revision required)

Section 5 of NSCRF v1.0 applies the framework to seven Network States. Revision:

- **Replace** Section 5 with the 32-entity scoring (Section 2 of this expansion).
- **Add** a Section 5.bis: "Below-threshold entities" using Section 6 of this expansion.
- **Add** an appendix: Cross-Framework Comparative Table (Section 5 of this expansion).
- **Keep** original methodology, pillar definitions, tier scale — no changes.
- **Refresh** abstract and executive summary to reflect the 32-entity cohort.
- **Date**: 13 April 2026 cut-off → re-date to April 2026 post-compilation.

Expected new length: +35-40 pages vs v1.0.

### 8.3 NSEI v1.1 (draft → published)

NSEI v1.0 draft applies to eight entities. Since the paper is not yet published, it can absorb the expansion cleanly:

- Replace Part IV (Application) with the 32-entity scoring (Section 3 of this expansion).
- Add a below-threshold appendix (Section 6).
- Add the Cross-Framework Comparative Table (Section 5).
- Publish as v1.0 with 32-entity cohort — **no v1.1 is needed**; v1.0 goes out with the expanded cohort built in.

### 8.4 NS-ESG v1.1 (draft → published)

Same strategy as NSEI: the paper is not yet published. Replace Part IV with the 32-entity scoring (Section 4) and publish as v1.0 with the expanded cohort from the start.

### 8.5 Coordinated publication strategy

**Recommendation: publish as a coordinated quartet, not staggered.**

Rationale:
- NSCRF v1.1 depends on NSEI v1.0 and NS-ESG v1.0 for the Cross-Framework Comparative Table to be citeable. Staggered release would force NSCRF v1.1 to reference two pending DOIs.
- The Section 5 Master Comparative Table is a joint output; publishing it four times (once per paper) with staggered dates creates versioning chaos.
- A Zenodo community can host all four as a "Network State Research Programme v1.x" collection with a single landing page.
- Press/distribution (Substack, SSRN, GitHub, Twitter) benefits from simultaneous release — the narrative is "four frameworks, one cohort, one programme" rather than four separate papers.

**Proposed publication sequence (all within a 7-day window):**

1. Day 1: NSCF v2.1 on Zenodo (minor update to anchor paper)
2. Day 1: NSCRF v1.1 on Zenodo (major revision)
3. Day 1: NSEI v1.0 on Zenodo (new; with expanded cohort)
4. Day 1: NS-ESG v1.0 on Zenodo (new; with expanded cohort)
5. Day 2-3: Mirror all four to SSRN
6. Day 3-4: Mirror all four to GitHub repo
7. Day 4-7: Substack announcement post covering the quartet

---

## Section 9 — Confidence Scoring & Disclaimers

### 9.1 Confidence distribution across the 32-entity cohort

| Confidence | Count | Entities |
|-----------|------:|----------|
| H — High | 1 | Prospera |
| M — Medium | 27 | Network School, Kleros, Zuzalu, Praxis, Edge City, Catawba, Gelephu, TDF, Itana, Ciudad Morazán, Edge Esmeralda, Liberland, CityDAO, Don't Die, Urbit, Afropolitan, PoH, RNS.ID, Oceanix, ZuJapan, Liberstad, Zupass, Zanzalu, Montelibero, Logos, Ârc, Infinita (L→M with caveats) |
| L — Low | 4 | Frontier Tower, Bitcoin District, Etherlaken, Crecimiento |

**Observation:** Only Prospera qualifies as H confidence because it has audited financials from the ZEDE investor reports. All other entities are M or L.

### 9.2 Pillar-level confidence notes

For the 27 Medium-confidence entities, confidence varies by pillar:

- **Treasury Health**: typically M for token-issuing entities (on-chain verifiable), L for private-funding entities.
- **Governance Quality**: M for DAO-structured entities (on-chain votes visible), L for founder-led.
- **Community Resilience**: M for entities with public member counts, L for entities where membership is private.
- **Infrastructure Robustness**: M for physical-footprint entities, L for concept-stage.
- **External Risk**: M for all — regulatory environments are publicly knowable.

For NSEI, confidence is typically L on GCP (requires survey data) and M on derived metrics. For NS-ESG, confidence is M on G indicators (on-chain) and L on S indicators (require member surveys).

### 9.3 Standard caveat language for publication

The following paragraph is proposed for inclusion as a footnote or caveat box in each of the four v1.1 papers:

> *Scores assigned in this paper are illustrative estimates derived from publicly available information as of April 2026. They are not audited, not endorsements, and not investment advice. The frameworks are original and have not been peer-reviewed. Production-quality scoring would require the subject Network State's formal participation in a disclosure process, including access to treasury data, member registry records, governance votes, and physical-infrastructure documentation. Scores may change materially as Network State disclosures mature. Confidence levels (H/M/L) are provided per entity to signal underlying data quality; entities scored with Low confidence rely substantially on founder statements and press coverage rather than primary financial or governance records. This research is intended as a foundation for future ISO International Workshop Agreements, UN Statistics Division frameworks, and academic peer review.*

### 9.4 Data quality concerns requiring resolution before publication

1. **Infinita disambiguation.** The "Infinita" entity (NSDI rank 14, 0.299) appears distinct from the "Prospera/Infinita City" compound used in v1.0 scoring. Before publication, verify via primary sources whether they are the same legal entity, a subsidiary, or genuinely separate. If the latter, confirm governance structure.

2. **Praxis member-company valuation.** Praxis's self-reported $1.117 trillion aggregate member-company valuation (January 2026) has not been independently verified. NSEI framework requires third-party audit for any aggregate valuation claim above 10× treasury. Recommend noting in v1.1 that this figure is disputed and scoring on conservative basis.

3. **Gelephu operational timeline.** Bhutan's SEZ Act 2023 is well-documented; current build phase less so. The NSDI dataset scored SR at 0.50 which drives much of the composite. Confirm via Royal Government of Bhutan's most recent (2026) progress report before publication.

4. **Liberstad membership.** Public claims of "hundreds of members" vs the ~30 observed landowners. Use the verifiable lower figure in NSCRF Community Resilience pillar.

5. **Bitcoin District, Etherlaken, Crecimiento, Frontier Tower.** All Low confidence. Consider whether to score at all in v1.1 or mark with L confidence and proceed. Current recommendation: include with explicit L confidence tag and narrower per-pillar ranges noted.

6. **Zu-branded events.** The ns.com dashboard contains many "Zu-" prefix entities (ZuJapan, Zanzalu, ZuKas, Zu-Grama, ZuAfrique, Zuitzerland). Risk of double-counting if a participant attends multiple. Score each as a distinct entity based on its distinct programme; noted in methodology.

### 9.5 Ethical and academic-publication notes

- All scores are illustrative; no Network State has been contacted for formal disclosure. The quartet papers should be circulated to the top-5 entities (Prospera, Network School, Gelephu, Kleros, Catawba) as a courtesy pre-publication with a seven-day response window.
- The NSDI, NSCRF, NSEI, and NS-ESG frameworks are original. Peer review has not been conducted. Recommend submission to Network Governance Working Paper series at SSRN and to the Charter Cities Institute for informal review before formal peer review.
- CC BY-NC-ND 4.0 licence is appropriate. No commercial derivatives permitted — important for the credit-rating use case where a commercial rating agency could otherwise appropriate the methodology.

---

## NSCRF v1.1 NEW INDICATOR — PILLAR 5: HOST-COUNTRY RECOGNITION RISK

Network States operating within a host-country statutory framework (ZEDE, SFZ, SAR, Talent City, tribal jurisdiction) face a specific and material risk: the host country may revoke, suspend, or fail to renew the statutory framework under which the NS operates.

**Material recent precedents:**

| Entity | Host | Risk event | Status |
|--------|------|-----------|--------|
| Prospera | Honduras | Castro govt repealed ZEDE law 2022 | ICSID arbitration; $10.7B claim pending |
| Ciudad Morazán | Honduras | Same event | Same status |
| Gelephu Mindfulness City | Bhutan | Constitutional SAR statute; low repeal risk given royal backing | Active, low risk |
| Network School | Malaysia (Forest City SFZ) | SFZ framework active; political transition risk moderate | Active, moderate risk |
| Itana | Nigeria | Talent City framework; federal/state coordination risk | Active, moderate risk |
| Catawba CDEZ | USA (tribal) | Tribal sovereignty protected by US Supreme Court jurisprudence | Active, low risk |

**Pillar 5 scoring adjustment:**

| Pillar 5 sub-tier | Criterion |
|------------------|-----------|
| **NS-AAA / NS-AA** | Constitutional protection OR tribal sovereignty OR >10-year track record |
| **NS-A / NS-BBB** | Statutory framework, politically stable; no active reversal proceedings |
| **NS-BB / NS-B** | Active political reversal proceedings (e.g., Prospera ICSID 2022-present) |
| **NS-CCC and below** | Statutory framework repealed or under imminent threat of repeal |

**Application to cohort:**

| Entity | Host framework | Pillar 5 adjustment |
|--------|---------------|---------------------|
| Prospera / Ciudad Morazán | Honduras ZEDE (repealed, ICSID pending) | -2 notches (NS-BB) |
| Gelephu Mindfulness City | Bhutan SAR (constitutional) | No adjustment (NS-AAA eligible) |
| Network School | Malaysia SFZ (statutory, stable) | -1 notch (NS-A) |
| Catawba CDEZ | US tribal sovereignty | No adjustment |

**Cross-reference:** See `research-sovereign-vs-ns-comparison.md` Section 4.6 for detailed host-country recognition case files. See NSEI v1.0 Appendix H for DRRI methodology.

---

*End of cohort expansion note. 32 entities scored across four frameworks. 57 entities documented as below-threshold with rationale.*

*© 2026 Kate M Grey. Licensed under CC BY-NC-ND 4.0.*
