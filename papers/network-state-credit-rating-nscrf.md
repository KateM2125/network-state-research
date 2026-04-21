# Network State Credit Rating Framework (NSCRF)
## A First-Principles Methodology for Assessing Creditworthiness of Network States
### Research Brief for Academic Paper Series
### Compiled: 5 April 2026

---

## EXECUTIVE SUMMARY

No credit rating methodology exists for Network States. The three major credit rating agencies -- Moody's Investors Service, S&P Global Ratings, and Fitch Ratings -- collectively rate approximately 140 sovereign governments and tens of thousands of corporations. Their methodologies assume territorial tax bases, involuntary populations, central banks, audited financial statements, and bond markets. Network States possess none of these characteristics.

Yet Network States are increasingly handling significant capital. Praxis has raised $544 million. Total DAO treasury assets globally exceed $24.5 billion. The ns.com dashboard tracks 117 startup societies. As these entities mature, investors, members, host countries, and counterparties will need a standardized way to assess their creditworthiness -- their ability to meet financial obligations, sustain operations, and protect stakeholder value.

This paper constructs the **Network State Credit Rating Framework (NSCRF)** from first principles. It surveys how sovereign and corporate credit ratings work today, identifies why those methodologies fail for Network States, and proposes a five-pillar rating methodology with explicit weightings, scoring criteria, and rating scales. It applies the methodology to seven Network States using publicly available data, and assesses the commercial viability of a Network State credit rating agency.

The NSCRF is designed to be the third leg of a comprehensive analytical framework:
- **NSCF** (Network State Classification Framework) -- classifies what a Network State is
- **NSEI** (Network State Economic Index) -- measures what a Network State produces
- **NSCRF** (Network State Credit Rating Framework) -- assesses how creditworthy a Network State is

Together, these frameworks provide the analytical infrastructure for Network States to be assessed with the same rigor applied to traditional sovereign and corporate entities.

---

## PART I: HOW SOVEREIGN CREDIT RATINGS WORK TODAY

### 1.1 Overview of Sovereign Credit Ratings

A sovereign credit rating represents a rating agency's opinion of a government's ability and willingness to service its debt obligations in full and on time. Sovereign ratings serve as a ceiling for most domestic issuers and are the foundation of a country's cost of capital.

**Key facts:**
- Moody's rates approximately 145 sovereign issuers
- S&P rates approximately 135 sovereign issuers
- Fitch rates approximately 120 sovereign issuers
- Approximately 100+ countries have ratings from all three agencies

Source: https://www.moodys.com/researchandratings/ratings-list/sovereign/
Source: https://disclosure.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/2961552
Source: https://www.fitchratings.com/research/sovereigns

### 1.2 Moody's Sovereign Rating Methodology

Moody's published its comprehensive sovereign rating methodology in November 2024 ("Sovereign and Supranational Methodology"). The methodology assesses four broad factors:

**Factor 1: Economic Strength (Weight: ~25%)**
- GDP growth rate and growth volatility
- GDP per capita (nominal and PPP)
- Economic diversification
- Credit-to-GDP ratio
- Scale of the economy (nominal GDP)

**Factor 2: Institutional and Governance Strength (Weight: ~25%)**
- Quality of institutions (rule of law, control of corruption, regulatory quality)
- Policy effectiveness and credibility
- Government effectiveness (World Bank Worldwide Governance Indicators)
- Transparency and track record

**Factor 3: Fiscal Strength (Weight: ~25%)**
- Government debt burden (debt/GDP, debt/revenue)
- Debt affordability (interest payments/revenue, interest/GDP)
- Debt trajectory and fiscal balance
- Government revenue base
- Government financial asset position

**Factor 4: Susceptibility to Event Risk (Weight: ~25%)**
- Political risk (regime stability, geopolitical risk)
- Government liquidity risk (refinancing profile, access to funding)
- Banking sector risk (size relative to GDP, asset quality, concentration)
- External vulnerability risk (current account, reserves, external debt)

**The Moody's process:**
1. Score each sub-factor on a scale
2. Combine sub-factor scores into factor scores
3. Combine factor scores into an initial "scorecard-indicated outcome"
4. Apply qualitative adjustments for factors not captured in the scorecard
5. Assign the final rating

**Key principle:** Moody's uses a weighted average approach but the factors interact. A country with strong fiscal metrics but weak institutions will not receive a high rating because institutional weakness undermines fiscal sustainability.

Source: Moody's, "Rating Methodology: Sovereigns," November 2024
URL: https://ratings.moodys.com/api/rmc-documents/430057

### 1.3 S&P Global Ratings Sovereign Methodology

S&P's sovereign methodology, last updated in December 2017 ("Sovereign Rating Methodology"), uses five key rating factors:

**Factor 1: Institutional Assessment (Qualitative)**
- Institutional and governance effectiveness and stability
- Policy predictability and transparency
- Debt repayment culture
- Security risks

**Factor 2: Economic Assessment**
- Income levels (GDP per capita)
- Growth prospects
- Economic diversity and volatility

**Factor 3: External Assessment**
- External liquidity position
- Status of currency in international transactions
- External debt (narrow net external debt/CAR)

**Factor 4: Fiscal Assessment -- Flexibility and Performance**
- Fiscal balance trajectory
- Revenue and expenditure levels and trends
- Debt burden and debt structure
- Contingent liabilities
- Long-term fiscal trends

**Factor 5: Fiscal Assessment -- Debt Burden**
- Net general government debt/GDP
- General government interest expenditure/general government revenue
- Gross general government debt/GDP

**Factor 6: Monetary Assessment**
- Exchange rate regime
- Monetary policy credibility
- Price stability record
- Depth of local capital markets

**The S&P process:**
1. Combine Institutional + Economic assessments to get "Institutional and Economic Profile"
2. Combine External + Fiscal + Monetary assessments to get "Flexibility and Performance Profile"
3. Map the two profiles to a matrix to obtain an "indicative rating level"
4. Apply supplemental adjustments (exceptional events, peer comparison)
5. Determine foreign currency and local currency ratings (may differ)

**Key distinction from Moody's:** S&P's framework more explicitly separates "willingness to pay" (institutional/political factors) from "ability to pay" (economic/fiscal/external factors). S&P also places greater emphasis on monetary policy assessment as a standalone factor.

Source: S&P Global Ratings, "Sovereign Rating Methodology," December 2017
URL: https://disclosure.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/2961552

### 1.4 Fitch Ratings Sovereign Methodology

Fitch's sovereign rating model ("Sovereign Rating Model -- SRM") uses 18 variables grouped into four pillars:

**Pillar 1: Structural Features**
- GDP per capita (PPP)
- Governance indicators (composite of World Bank WGI)
- Share of global FX reserves held in the sovereign's currency
- Years since last default

**Pillar 2: Macroeconomic Performance, Policies, and Prospects**
- Real GDP growth (5-year average and forecast)
- Consumer price inflation
- Fiscal balance/GDP
- Current account balance + FDI/GDP

**Pillar 3: Public Finances**
- General government gross debt/GDP
- General government interest payments/revenue
- Government debt dynamics (change in debt/GDP ratio)
- Gross financing needs

**Pillar 4: External Finances**
- External debt/GDP
- Commodity dependence
- Reserve coverage (reserves/external payments)
- Current account balance

**The Fitch process:**
1. Run the quantitative Sovereign Rating Model (SRM) using 18 variables to produce an initial model output
2. Apply a Qualitative Overlay (QO) of up to +/- 3 notches for factors not captured in the model
3. Key qualitative factors: political stability, banking sector health, macro prudential risk, structural reform trajectory
4. Publish the final rating

**Key distinction:** Fitch is the most explicitly quantitative of the three agencies, with its SRM producing a model-indicated rating before qualitative adjustments. This makes it the most transparent and reproducible methodology.

Source: Fitch Ratings, "Sovereign Rating Criteria," April 2023
URL: https://www.fitchratings.com/research/sovereigns/sovereign-rating-criteria-03-04-2023

### 1.5 Common Dimensions Across All Three Agencies

| Dimension | Moody's | S&P | Fitch |
|---|---|---|---|
| **Economic strength** | GDP growth, GDP/capita, diversification, credit-to-GDP | GDP/capita, growth prospects, diversity, volatility | GDP/capita (PPP), real GDP growth |
| **Institutional quality** | Governance indicators, policy effectiveness, transparency | Institutional effectiveness, governance stability, rule of law | Governance composite (WGI) |
| **Fiscal strength** | Debt/GDP, debt/revenue, interest burden, fiscal balance | Fiscal balance, debt burden, contingent liabilities | Debt/GDP, interest/revenue, fiscal balance, gross financing needs |
| **External vulnerability** | Current account, reserves, external debt, banking sector | External liquidity, currency status, external debt | External debt/GDP, reserves, commodity dependence |
| **Monetary policy** | Embedded in institutional assessment | Standalone factor: exchange rate, price stability, capital markets | Embedded in macro performance pillar |
| **Political risk** | Event risk factor | Institutional assessment | Qualitative overlay |

**The universal equation:**
> Creditworthiness = f(Economic Strength, Institutional Quality, Fiscal Capacity, External Resilience, Political Stability)

This is the foundation from which the NSCRF is built.

### 1.6 Rating Scales

| Quality | Moody's | S&P | Fitch | Meaning |
|---|---|---|---|---|
| **Highest quality** | Aaa | AAA | AAA | Minimal credit risk |
| **High quality** | Aa1, Aa2, Aa3 | AA+, AA, AA- | AA+, AA, AA- | Very low credit risk |
| **Upper medium** | A1, A2, A3 | A+, A, A- | A+, A, A- | Low credit risk |
| **Medium** | Baa1, Baa2, Baa3 | BBB+, BBB, BBB- | BBB+, BBB, BBB- | Moderate credit risk |
| **Speculative** | Ba1, Ba2, Ba3 | BB+, BB, BB- | BB+, BB, BB- | Substantial credit risk |
| **Highly speculative** | B1, B2, B3 | B+, B, B- | B+, B, B- | High credit risk |
| **Substantial risks** | Caa1, Caa2, Caa3 | CCC+, CCC, CCC- | CCC+, CCC, CCC- | Very high credit risk |
| **Extremely speculative** | Ca | CC | CC | Near default |
| **Default** | C | SD/D | D | In default |

**Investment grade:** Baa3/BBB- and above
**Speculative grade ("junk"):** Ba1/BB+ and below

**Global distribution (approximate, 2025):**
- AAA/Aaa: 10-12 sovereigns (Australia, Canada, Denmark, Germany, Luxembourg, Netherlands, Norway, Singapore, Sweden, Switzerland, and a few others)
- AA: ~15-20 sovereigns
- A: ~20-25 sovereigns
- BBB (investment grade floor): ~25-30 sovereigns
- Below investment grade: ~50-60 sovereigns
- Default: Variable (currently ~5-8 in some form of distress)

Source: S&P Global Ratings definitions: https://www.spglobal.com/ratings/en/about/understanding-credit-ratings
Source: Moody's rating scale: https://www.moodys.com/sites/products/productattachments/ap075378_1_1408_ki.pdf

### 1.7 Data Inputs Required for Sovereign Ratings

Sovereign credit ratings require access to:

| Category | Specific Data | Source |
|---|---|---|
| Macroeconomic | GDP (nominal, real, PPP), GDP growth, inflation, unemployment | IMF WEO, World Bank WDI, national statistics office |
| Fiscal | Government revenue, expenditure, budget balance, public debt stock, debt composition, interest payments | Ministry of Finance, IMF Article IV, debt management office |
| External | Balance of payments, current account, FDI, portfolio flows, external debt, reserves | Central bank, IMF BOP statistics |
| Monetary | Interest rates, money supply, exchange rate, inflation targeting framework | Central bank |
| Institutional | Governance indicators, corruption perception, rule of law, regulatory quality | World Bank WGI, Transparency International CPI |
| Banking | Bank assets/GDP, NPL ratios, capital adequacy, concentration | Central bank, banking supervisor |
| Political | Regime type, political stability, geopolitical risk | Qualitative assessment, EIU, PRS Group |

**Critical observation for Network States:** Of these seven data categories, Network States can provide direct analogues for at most two (fiscal and limited institutional). They cannot provide national accounts data, central bank statistics, banking sector data, or formal political/institutional indicators. The NSCRF must find proxies for each.

---

## PART II: HOW CORPORATE CREDIT RATINGS WORK

### 2.1 Key Differences from Sovereign Ratings

Corporate credit ratings assess a company's ability to meet its financial obligations. Unlike sovereigns, companies:
- Can default and be liquidated (sovereigns cannot cease to exist)
- Have audited financial statements (annual, quarterly)
- Generate revenue from identifiable products/services
- Operate under a legal jurisdiction's bankruptcy framework
- Have identifiable owners and governance structures

### 2.2 S&P Corporate Rating Framework

S&P's corporate methodology evaluates:

**Business Risk Profile:**
- Industry risk (cyclicality, competitive dynamics, barriers to entry)
- Country risk (where operations are located)
- Competitive position (scale, diversity, efficiency, profitability)

**Financial Risk Profile:**
- Cash flow adequacy (FFO/debt, FOCF/debt)
- Capital structure (debt/capital, debt/EBITDA)
- Liquidity (coverage of near-term obligations)
- Financial policy (management strategy toward leverage)

**Modifiers:**
- Diversification/portfolio effect
- Capital structure complexity
- Financial policy aggressiveness
- Management and governance assessment
- Comparable ratings analysis

Source: S&P Global Ratings, "Corporate Methodology," November 2013 (updated periodically)
URL: https://disclosure.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/2891327

### 2.3 Moody's Corporate Rating Framework

Moody's corporate ratings focus on:

**Industry and Business Profile:**
- Industry-specific rating factors (Moody's publishes sector-specific methodologies)
- Scale, diversification, market position
- Operating efficiency and cost structure

**Financial Profile:**
- Leverage (Debt/EBITDA)
- Coverage (EBITDA/Interest)
- Cash flow generation and free cash flow
- Liquidity and financial flexibility

**Governance and Management:**
- Board structure and independence
- Financial policy and risk appetite
- Track record and management quality
- Related party transactions

Source: Moody's corporate methodologies by industry sector
URL: https://www.moodys.com/research-and-ratings/ratings/rating-methodologies

### 2.4 Why Corporate Ratings Matter for Network States

Network States sit in a structural gap between sovereigns and corporations:

| Characteristic | Sovereign | Corporation | Network State |
|---|---|---|---|
| Revenue source | Tax base (involuntary) | Product/service sales | Membership fees, services, token sales (voluntary) |
| Governance | Constitutional/legislative | Board of directors | Founder-led, DAO, council, or constitutional |
| Population/stakeholders | Citizens (can't easily leave) | Shareholders, employees | Members (can exit instantly) |
| Territory | Sovereign territory | Offices, facilities | Distributed nodes, leased spaces |
| Debt issuance | Sovereign bonds | Corporate bonds, loans | Crypto bonds, DeFi lending, token issuance |
| Financial reporting | National accounts (GDP, BOP) | GAAP/IFRS audited financials | On-chain data + self-reporting (unaudited) |
| Failure mode | Debt restructuring, never ceases to exist | Bankruptcy, liquidation | Community dissolution, treasury drain, fork |
| Monetary policy | Central bank, currency issuance | None (uses sovereign currency) | May have integrated token (not sovereign currency) |

**Conclusion:** The NSCRF must borrow from both sovereign and corporate rating methodologies -- using the sovereign framework's attention to institutional quality and external vulnerability, and the corporate framework's attention to cash flow analysis, leverage, governance, and liquidity.

---

## PART III: WHY EXISTING METHODOLOGIES FAIL FOR NETWORK STATES

### 3.1 Nine Structural Gaps

**1. No territorial tax base.**
Sovereign ratings assume a government can tax a captive population within defined borders. Network State "tax" (membership fees) is voluntary. Members who disagree with fee levels leave. There is no coercive revenue capacity.

**2. No sovereign debt issuance.**
Sovereign ratings exist primarily to assess sovereign bonds. Network States have not issued traditional bonds. Some may issue tokens or borrow from DeFi protocols, but there is no sovereign bond market to price credit risk.

**3. Voluntary membership (population exit risk).**
Sovereign ratings assume citizens cannot easily emigrate en masse. Network State members can leave with a cancellation email. Population can collapse in weeks. This is more similar to a subscription business than a sovereign -- but with political/community dimensions subscription models do not capture.

**4. Distributed geography (no single jurisdiction).**
Sovereign ratings assume a country operates under one legal framework. Network States span multiple jurisdictions. Prospera operates under Honduran law (disputed). Network School operates under Malaysian law. Praxis will operate under US and possibly other jurisdictions. Regulatory risk is multiplicative, not singular.

**5. Treasury may be in cryptocurrency.**
Sovereign ratings assume reserves are held in foreign exchange and gold, denominated in stable fiat currencies. Network State treasuries may hold BTC, ETH, governance tokens, stablecoins, NFTs, or other volatile digital assets. Treasury value can drop 50% in a quarter.

**6. Governance is code-based or founder-led.**
Sovereign ratings assess institutional quality using World Bank Governance Indicators (rule of law, control of corruption, etc.) built for nation-states. Network State governance may be a multisig wallet controlled by three founders, a token-weighted DAO vote, or a social smart contract. Existing governance indicators are not designed for these structures.

**7. No audited financial statements.**
Corporate ratings require GAAP/IFRS-audited financials. Most Network States have no audited financials. Some have on-chain treasury data that is publicly verifiable, which is arguably more transparent than annual audited statements -- but the format and standards are entirely different.

**8. No central bank or monetary policy.**
Sovereign ratings assess monetary policy credibility, exchange rate regime, and price stability. Network States may have integrated tokens but lack central banks, monetary policy committees, or inflation targeting frameworks. Token price is set by market forces, not policy.

**9. No military or enforcement capability.**
Sovereign ratings implicitly account for a state's ability to enforce its will -- collect taxes, maintain order, defend territory. Network States rely on social consensus, smart contracts, and host country legal frameworks for enforcement. If a member violates community rules, the worst penalty is expulsion. If a host country changes policy, the Network State has no recourse except relocation.

### 3.2 What Can Be Salvaged from Existing Methodologies

Despite these gaps, the fundamental logic of credit analysis -- assessing ability to meet obligations -- transfers. The question changes from "Can this government service its sovereign debt?" to "Can this community sustain its operations, protect its treasury, and deliver value to members and counterparties?"

| Sovereign Concept | Network State Analogue | Measurable? |
|---|---|---|
| GDP and economic output | Gross Community Product (GCP) | Estimated; partially on-chain |
| Government revenue | Membership fees + service revenue + token revenue | Yes (treasury inflows) |
| Government debt | DeFi borrowings + token obligations + contractual commitments | Partially on-chain |
| Fiscal balance | Treasury inflows minus outflows (burn rate) | Yes (on-chain + accounting) |
| Reserves | Treasury holdings (stablecoins, crypto, fiat) | Yes (on-chain for crypto) |
| Institutional quality | Governance model maturity + transparency + participation | Assessable via framework |
| External vulnerability | Regulatory risk + crypto market correlation + concentration risk | Assessable via analysis |
| Population stability | Member retention rate + net migration | Yes (membership data) |
| Monetary policy credibility | Token design + treasury management policy | Assessable |

---

## PART IV: THE NETWORK STATE CREDIT RATING FRAMEWORK (NSCRF)

### 4.1 Design Principles

1. **Built from both sovereign and corporate rating logic** -- borrows institutional assessment from sovereign methodology and cash flow analysis from corporate methodology
2. **Every criterion is measurable** -- either directly observable (on-chain data, membership records) or assessable through standardized evaluation
3. **Weights are explicit and auditable** -- unlike rating agencies that often use opaque "committee judgment"
4. **Adapted for Network State realities** -- voluntary membership, crypto treasuries, distributed geography, code-based governance
5. **Forward-looking** -- credit ratings are opinions about the future, not descriptions of the past
6. **Compatible with NSCF and NSEI** -- draws on the same data infrastructure as the classification and economic frameworks

### 4.2 Five Rating Pillars

The NSCRF assesses Network States across five pillars. Each pillar receives a score from 0 to 100. Pillar scores are combined using the specified weights to produce a composite credit score from 0 to 100, which maps to a rating grade.

---

### PILLAR 1: TREASURY HEALTH (Weight: 30%)
*Analogous to: Moody's Fiscal Strength + S&P Fiscal Assessment*

This is the most heavily weighted pillar because, unlike sovereigns, Network States cannot print currency or compel tax payment. Treasury is their lifeline.

#### 1.1 Treasury Size and Per-Member Adequacy (Sub-weight: 20% of pillar)

| Score | Treasury Size (USD equivalent) | Treasury Per Active Member |
|---|---|---|
| 90-100 | > $100M | > $10,000 |
| 70-89 | $10M - $100M | $5,000 - $10,000 |
| 50-69 | $1M - $10M | $1,000 - $5,000 |
| 30-49 | $100K - $1M | $100 - $1,000 |
| 10-29 | $10K - $100K | $10 - $100 |
| 0-9 | < $10K | < $10 |

#### 1.2 Treasury Composition Quality (Sub-weight: 20% of pillar)

Treasury composition directly affects credit quality because volatile assets can evaporate.

| Score | Composition |
|---|---|
| 90-100 | > 70% in stablecoins (USDC, USDT) or fiat; < 10% in volatile crypto; remaining in diversified assets |
| 70-89 | 50-70% stablecoins/fiat; 10-30% volatile crypto; modest diversification |
| 50-69 | 30-50% stablecoins/fiat; 30-50% volatile crypto; some diversification |
| 30-49 | 10-30% stablecoins/fiat; 50-70% volatile crypto; concentrated |
| 10-29 | < 10% stablecoins/fiat; > 70% volatile crypto; highly concentrated in 1-2 tokens |
| 0-9 | 100% in single volatile asset or treasury composition unknown |

**Rationale:** A $10M treasury that is 90% in USDC is far more creditworthy than a $10M treasury that is 90% in a governance token. In the March 2025 crypto correction, BTC fell 45% from its all-time high. A treasury holding 90% BTC would have lost $4.5M of a $10M treasury in months.

#### 1.3 Burn Rate and Runway (Sub-weight: 25% of pillar)

The single most important treasury metric: how long can the Network State operate at current spending if all revenue stops?

| Score | Runway (months at current burn rate) |
|---|---|
| 90-100 | > 36 months |
| 70-89 | 18 - 36 months |
| 50-69 | 12 - 18 months |
| 30-49 | 6 - 12 months |
| 10-29 | 3 - 6 months |
| 0-9 | < 3 months or unknown |

**Benchmark:** Y Combinator advises startups to maintain 18-24 months of runway. For Network States, which have community obligations beyond mere business survival, 18+ months should be the minimum for investment-grade consideration.

#### 1.4 Revenue Diversity and Stability (Sub-weight: 20% of pillar)

| Score | Revenue Profile |
|---|---|
| 90-100 | 4+ distinct revenue streams; no single source > 30% of revenue; recurring revenue > 70% of total; 3-year positive growth trend |
| 70-89 | 3-4 revenue streams; no single source > 40%; recurring > 60%; growing |
| 50-69 | 2-3 revenue streams; no single source > 50%; recurring > 40%; stable |
| 30-49 | 1-2 revenue streams; single source > 50%; recurring < 40%; volatile |
| 10-29 | Single revenue source; entirely dependent on one stream; declining |
| 0-9 | No identifiable revenue; dependent on grants or token sales only |

**Revenue source classification:**
- **Recurring:** Membership fees, subscription services, property income
- **Variable but repeatable:** Service fees, event tickets, consulting
- **One-time/speculative:** Token launches, NFT sales, grants, donations
- **Market-dependent:** Trading revenue, yield farming, staking rewards

#### 1.5 Revenue Growth Rate (Sub-weight: 15% of pillar)

| Score | Trailing 12-Month Revenue Growth |
|---|---|
| 90-100 | > 50% YoY growth with increasing margins |
| 70-89 | 25-50% YoY growth, stable margins |
| 50-69 | 10-25% YoY growth |
| 30-49 | 0-10% YoY growth or flat |
| 10-29 | Declining 0-25% YoY |
| 0-9 | Declining > 25% YoY or no data |

---

### PILLAR 2: GOVERNANCE QUALITY (Weight: 25%)
*Analogous to: Moody's Institutional & Governance Strength + S&P Institutional Assessment*

Governance quality determines whether treasury resources will be deployed effectively and whether the community can adapt to challenges. For Network States, where membership is voluntary and exit is costless, governance quality is existential -- poor governance causes member flight, which collapses the community.

#### 2.1 Governance Model Maturity (Sub-weight: 25% of pillar)

A progression scale from least to most institutionally mature:

| Score | Governance Stage | Description |
|---|---|---|
| 90-100 | **Constitutional with checks and balances** | Written constitution; separation of powers; independent judiciary or arbitration; amendment process requiring supermajority; term limits for leadership |
| 70-89 | **Elected council with formal charter** | Leadership elected by members; written charter; regular elections; transparent decision process; recall mechanism |
| 50-69 | **Structured DAO or multi-stakeholder body** | Token-weighted or quadratic voting; formal proposal process; quorum requirements; treasury multisig with 3+ signers |
| 30-49 | **Council or advisory board (appointed)** | Founder appoints council; advisory input on decisions; some formal process; limited accountability |
| 10-29 | **Founder-led with informal input** | Single founder/small team makes all decisions; community input is informal and non-binding |
| 0-9 | **No identifiable governance** | No clear decision-making process; no accountability mechanism; opaque |

**Note on founder-led governance:** Founder-led governance (30-49) is not inherently bad -- early-stage entities often need decisive leadership. But it creates key-person risk, which is penalized in Pillar 5 (External Risk). A mature founder-led entity that has published a governance roadmap toward decentralization would receive a higher score than one with no succession plan.

#### 2.2 Governance Participation and Engagement (Sub-weight: 20% of pillar)

| Score | Participation Level |
|---|---|
| 90-100 | > 60% of eligible members participate in governance; high proposal volume; active deliberation |
| 70-89 | 40-60% participation; regular proposals; engaged community |
| 50-69 | 20-40% participation; periodic proposals; moderate engagement |
| 30-49 | 10-20% participation; infrequent proposals; passive community |
| 10-29 | < 10% participation; rare proposals; disengaged |
| 0-9 | No governance participation mechanism or 0% participation |

**Benchmark:** Average DAO voter participation is 17% (2025). Network States, with physical colocation and shared mission, should achieve 30%+ to be considered healthy.

Source: https://patentpc.com/blog/dao-growth-stats-treasury-sizes-governance-votes-activity

#### 2.3 Transparency and Reporting (Sub-weight: 20% of pillar)

| Score | Transparency Level |
|---|---|
| 90-100 | Audited financial statements (external auditor); real-time on-chain treasury dashboard; quarterly reporting to members; governance decisions publicly documented; smart contracts audited |
| 70-89 | Unaudited but regular financial reporting; on-chain treasury visible; governance decisions documented; annual or semi-annual member report |
| 50-69 | Periodic financial disclosures; some on-chain visibility; governance decisions partially documented |
| 30-49 | Irregular financial disclosure; limited on-chain data; governance decisions not consistently documented |
| 10-29 | Minimal disclosure; no on-chain visibility; opaque decision-making |
| 0-9 | No financial disclosure; no transparency mechanism |

#### 2.4 Governance Attack Surface (Sub-weight: 20% of pillar)

This measures vulnerability to governance manipulation -- a risk unique to crypto-native organizations.

| Score | Governance Security |
|---|---|
| 90-100 | Identity-verified voting (1-person-1-vote or quadratic); multisig requires 5+ signers with geographic distribution; governance contracts audited; timelocks on major decisions; no single entity controls > 5% of votes |
| 70-89 | Multi-sig with 3-4 signers; token distribution reasonably decentralized (no entity > 15%); governance contracts audited; timelock on treasury withdrawals |
| 50-69 | Multi-sig with 3 signers; moderate token concentration (top entity 15-30%); basic security measures |
| 30-49 | 2-of-3 multisig; high token concentration (top entity 30-50%); limited security measures |
| 10-29 | Single signer controls treasury or governance token; extreme concentration |
| 0-9 | No security measures; single point of failure; no multisig |

#### 2.5 Key Person Dependency (Sub-weight: 15% of pillar)

| Score | Dependency Level |
|---|---|
| 90-100 | No single person is critical; distributed leadership; formal succession plan; leadership transitions have occurred successfully |
| 70-89 | 2-3 key leaders; succession plan documented; deputies or successors identified |
| 50-69 | Clear founder influence but operational team could continue without founder; no formal succession plan |
| 30-49 | Founder is highly identified with entity but has operational team; departure would cause significant disruption |
| 10-29 | Entirely dependent on single founder; no succession plan; no operational depth |
| 0-9 | Single founder with no team; departure would end the entity |

---

### PILLAR 3: COMMUNITY RESILIENCE (Weight: 20%)
*Analogous to: Moody's Economic Strength + S&P Economic Assessment*

Community resilience is the Network State equivalent of economic strength. A country with a large, diversified, growing economy is more creditworthy. A Network State with a large, diversified, growing, and loyal membership base is more creditworthy.

#### 3.1 Member Retention Rate (Sub-weight: 30% of pillar)

The most important community metric. In a voluntary-membership entity, retention is the ultimate vote of confidence.

| Score | 12-Month Retention Rate |
|---|---|
| 90-100 | > 85% annual retention |
| 70-89 | 70-85% retention |
| 50-69 | 55-70% retention |
| 30-49 | 40-55% retention |
| 10-29 | 25-40% retention |
| 0-9 | < 25% retention or no data |

**Benchmark:** SaaS industry average annual churn is 5-7% (93-95% retention). Premium communities like Soho House report 80-90% retention. Network States should target 70%+ for investment-grade consideration.

#### 3.2 Net Migration and Growth Trajectory (Sub-weight: 25% of pillar)

| Score | Net Growth |
|---|---|
| 90-100 | > 30% net annual growth with waitlist; demand exceeds capacity |
| 70-89 | 15-30% net annual growth; strong inbound demand |
| 50-69 | 5-15% net annual growth; stable demand |
| 30-49 | 0-5% net annual growth; flat demand |
| 10-29 | Declining membership 0-15% YoY |
| 0-9 | Declining > 15% YoY or mass exodus event |

#### 3.3 Member Economic Quality (Sub-weight: 20% of pillar)

| Score | Member Economic Profile |
|---|---|
| 90-100 | GCP per member > $90,000; high concentration of founders, investors, researchers; proven capital formation track record |
| 70-89 | GCP per member $50,000-90,000; strong professional community; some capital formation |
| 50-69 | GCP per member $20,000-50,000; mixed professional levels; modest capital formation |
| 30-49 | GCP per member $5,000-20,000; primarily early-career or lower-income members |
| 10-29 | GCP per member $1,000-5,000; limited economic activity |
| 0-9 | GCP per member < $1,000 or unknown |

#### 3.4 Diversity and Distribution (Sub-weight: 15% of pillar)

| Score | Diversity Profile |
|---|---|
| 90-100 | Members from 30+ countries; 5+ professional sectors well-represented; no single nationality > 30% |
| 70-89 | 15-30 countries; 3-5 professional sectors; no single nationality > 40% |
| 50-69 | 10-15 countries; 2-3 sectors; some nationality concentration |
| 30-49 | 5-10 countries; 1-2 dominant sectors; significant nationality concentration |
| 10-29 | < 5 countries; single professional sector; one nationality > 60% |
| 0-9 | Essentially mono-national or single-profession; no diversity |

#### 3.5 Cultural Cohesion (Sub-weight: 10% of pillar)

| Score | Cohesion Indicators |
|---|---|
| 90-100 | Strong shared identity; high event attendance; active internal social life; low conflict; members self-identify with community |
| 70-89 | Good shared identity; regular events well-attended; moderate social engagement |
| 50-69 | Emerging identity; some events; mixed engagement levels |
| 30-49 | Weak shared identity; low event attendance; significant internal disagreements |
| 10-29 | Fragmented community; internal conflicts; factions |
| 0-9 | No meaningful community identity; purely transactional relationship |

---

### PILLAR 4: INFRASTRUCTURE ROBUSTNESS (Weight: 15%)
*Analogous to: Fitch External Finances + S&P External Assessment*

Infrastructure determines whether the Network State can sustain operations through adverse conditions. It encompasses both digital and physical infrastructure, plus the legal structures that protect the entity's existence.

#### 4.1 Digital Infrastructure (Sub-weight: 25% of pillar)

| Score | Digital Capability |
|---|---|
| 90-100 | Self-hosted or multi-cloud infrastructure; 99.9%+ uptime; dedicated security team; bug bounty program; regular penetration testing; encrypted member data; no single vendor dependency |
| 70-89 | Reliable third-party infrastructure; 99.5%+ uptime; security audits; encrypted data; 2+ backup systems |
| 50-69 | Standard cloud infrastructure; 99%+ uptime; basic security; some redundancy |
| 30-49 | Single-platform dependency (e.g., Discord + Google Workspace); occasional outages; limited security |
| 10-29 | Minimal digital infrastructure; frequent issues; no security measures |
| 0-9 | No meaningful digital infrastructure or entirely dependent on free social media platforms |

#### 4.2 Physical Infrastructure Quality (Sub-weight: 20% of pillar)

| Score | Physical Assets |
|---|---|
| 90-100 | Owned real estate in 3+ locations; purpose-built facilities; long-term leases; high build quality; complete amenities |
| 70-89 | Owned or long-term leased in 1-2 locations; good facilities; most amenities |
| 50-69 | Medium-term leases (1-3 years); adequate facilities; basic amenities |
| 30-49 | Short-term leases (< 1 year); basic facilities; limited amenities |
| 10-29 | Pop-up/temporary spaces only; event-based physical presence |
| 0-9 | No physical infrastructure (virtual only) |

#### 4.3 Legal Structure Robustness (Sub-weight: 25% of pillar)

| Score | Legal Position |
|---|---|
| 90-100 | Incorporated in multiple jurisdictions with clear legal identity; registered foundation/trust for treasury; formal agreements with host countries; legal counsel retained; IP protected; regulatory compliance program |
| 70-89 | Incorporated in 1-2 jurisdictions; foundation or company structure; formal host country agreement; legal counsel |
| 50-69 | Single jurisdiction incorporation; basic legal structure; informal host country relationship; occasional legal advice |
| 30-49 | Minimal legal structure; unclear entity status; no formal host country relationship |
| 10-29 | No legal entity; operates informally; legally vulnerable |
| 0-9 | No legal structure and operating in ways that create active legal risk |

#### 4.4 Smart Contract and Protocol Security (Sub-weight: 15% of pillar)

| Score | Security Status |
|---|---|
| 90-100 | All smart contracts audited by 2+ reputable firms; formal verification where applicable; bug bounty with substantial rewards; insurance coverage; incident response plan |
| 70-89 | Primary contracts audited by 1 reputable firm; bug bounty; incident response plan |
| 50-69 | Some contracts audited; basic security review; no bug bounty |
| 30-49 | Self-reviewed code; no external audit; limited security |
| 10-29 | Unaudited smart contracts handling member funds |
| 0-9 | No smart contracts or unaudited contracts with critical vulnerabilities |

#### 4.5 Host Country Relationship Stability (Sub-weight: 15% of pillar)

| Score | Relationship Quality |
|---|---|
| 90-100 | Formal long-term agreement (10+ years) with host government; tax treaty protection; multiple host countries providing redundancy; host government is supportive and stable |
| 70-89 | Formal agreement (5-10 years); good relationship; host government stable; 2+ host countries |
| 50-69 | Formal agreement (1-5 years) or informal good relationship; single host country; host government stable |
| 30-49 | Short-term or informal arrangement; host government relationship uncertain; some regulatory tension |
| 10-29 | No formal agreement; hostile or deteriorating host country relationship; regulatory threat |
| 0-9 | Active legal dispute with host country; imminent regulatory action; forced relocation risk |

---

### PILLAR 5: EXTERNAL RISK (Weight: 10%)
*Analogous to: Moody's Susceptibility to Event Risk*

External risk captures threats beyond the Network State's control that could cause sudden deterioration in creditworthiness.

#### 5.1 Crypto Market Correlation (Sub-weight: 25% of pillar)

| Score | Crypto Sensitivity |
|---|---|
| 90-100 | Treasury < 10% correlated with BTC/ETH prices; revenue entirely in fiat or stablecoins; no token dependency |
| 70-89 | Treasury 10-25% correlated; mixed revenue sources; token exists but not critical |
| 50-69 | Treasury 25-50% correlated; moderate crypto revenue; token has meaningful governance role |
| 30-49 | Treasury 50-75% correlated; significant crypto revenue; token is core to economic model |
| 10-29 | Treasury > 75% correlated; entirely crypto-dependent revenue; token is the economy |
| 0-9 | 100% single-token treasury; total dependence on one crypto asset price |

#### 5.2 Regulatory Risk (Sub-weight: 25% of pillar)

| Score | Regulatory Exposure |
|---|---|
| 90-100 | Operations in regulatory-stable jurisdictions; proactive compliance; no current regulatory inquiries; legal structure withstands foreseeable regulatory changes |
| 70-89 | Mostly stable jurisdictions; compliance program exists; manageable regulatory risk |
| 50-69 | Some regulatory uncertainty; limited compliance program; regulatory changes could require adaptation |
| 30-49 | Significant regulatory uncertainty; operating in grey areas; potential for adverse regulatory action |
| 10-29 | Active regulatory scrutiny; operating in hostile regulatory environment; material legal risk |
| 0-9 | Under investigation or enforcement action; operating illegally in key jurisdictions |

#### 5.3 Concentration Risk (Sub-weight: 25% of pillar)

| Score | Concentration Level |
|---|---|
| 90-100 | Diversified across: 3+ host countries, 3+ blockchain networks (if applicable), distributed leadership, multiple revenue streams, multiple infrastructure providers |
| 70-89 | Moderate diversification: 2-3 host countries, 2+ chains, some leadership distribution |
| 50-69 | Limited diversification: 1-2 host countries, 1-2 chains, concentrated leadership |
| 30-49 | High concentration: single host country, single chain, single leader, dominant revenue source |
| 10-29 | Extreme concentration: single point of failure in host country, chain, leader, and revenue |
| 0-9 | Total dependence on single factor in all dimensions |

#### 5.4 Reputational and Competitive Risk (Sub-weight: 15% of pillar)

| Score | Risk Level |
|---|---|
| 90-100 | Strong positive reputation; media coverage mostly favorable; differentiated position; no direct competitors threatening member base; founder has strong public credibility |
| 70-89 | Good reputation; manageable competitive environment; some differentiation |
| 50-69 | Mixed reputation; moderate competitive pressure; unclear differentiation |
| 30-49 | Reputational concerns (past controversies, governance disputes); high competitive pressure |
| 10-29 | Significant reputational damage; losing members to competitors; negative media cycle |
| 0-9 | Severe reputational crisis; mass departures; fraud allegations |

#### 5.5 Black Swan Vulnerability (Sub-weight: 10% of pillar)

| Score | Resilience to Extreme Events |
|---|---|
| 90-100 | Multiple redundancies; geographic distribution; diversified treasury; can survive loss of any single component; disaster recovery plan tested |
| 70-89 | Some redundancy; 2+ locations; treasury partially diversified; basic continuity plan |
| 50-69 | Limited redundancy; could survive moderate shocks; no formal continuity plan |
| 30-49 | Fragile to shocks; single location; concentrated treasury; founder departure would be critical |
| 10-29 | Highly vulnerable; single point of failure in multiple dimensions |
| 0-9 | No resilience capacity; any significant shock would end the entity |

---

### 4.3 Composite Score Calculation

**Step 1:** Calculate each pillar score (0-100) by combining sub-factor scores using their sub-weights.

**Step 2:** Calculate the Composite Credit Score (CCS):

> CCS = (Treasury Health x 0.30) + (Governance Quality x 0.25) + (Community Resilience x 0.20) + (Infrastructure Robustness x 0.15) + (External Risk x 0.10)

**Step 3:** Map the CCS to a rating grade using the scale in Section 4.4.

**Weight rationale:**
- **Treasury Health (30%):** In a voluntary-membership entity without taxing power, financial sustainability is the dominant credit factor. A Network State that runs out of money ceases to exist.
- **Governance Quality (25%):** Governance determines whether treasury is managed well and whether the community can navigate crises. It is the "institutional strength" equivalent.
- **Community Resilience (20%):** The membership base is the "economy." Without members, there is no revenue, no governance participation, no community. Retention is the ultimate leading indicator.
- **Infrastructure Robustness (15%):** Physical and digital infrastructure create persistence. A well-structured entity is harder to destroy than a loosely organized one.
- **External Risk (10%):** External factors matter but are less controllable. The weight is lower because the other pillars capture the entity's capacity to withstand external shocks.

---

### 4.4 Network State Credit Rating Scale

The NSCRF uses a scale inspired by the major rating agencies but adapted for Network States. The scale acknowledges that even the most advanced Network States today would not qualify for the highest traditional sovereign ratings (which assume centuries of institutional track record).

| Grade | CCS Range | Interpretation | Moody's Equivalent | S&P/Fitch Equivalent |
|---|---|---|---|---|
| **NS-AAA** | 90-100 | Exceptional. Strongest fundamentals across all pillars. Self-sustaining with massive treasury, mature governance, loyal community, robust infrastructure. No Network State currently qualifies. | Aaa | AAA |
| **NS-AA** | 80-89 | Excellent. Very strong across most pillars. Minor vulnerabilities only. Sustainable operations with strong growth trajectory. | Aa1-Aa3 | AA+/AA/AA- |
| **NS-A** | 70-79 | Strong. Good fundamentals with some notable weaknesses in 1-2 pillars. Sustainable medium-term but needs improvement for long-term resilience. | A1-A3 | A+/A/A- |
| **NS-BBB** | 60-69 | Adequate. Meets minimum standards across most pillars. Adequate treasury and governance but vulnerabilities exist. Lowest investment-grade rating. | Baa1-Baa3 | BBB+/BBB/BBB- |
| **NS-BB** | 50-59 | Speculative. Meaningful credit weaknesses. May have strong treasury but weak governance, or strong community but weak treasury. Near-term viability likely but medium-term uncertain. | Ba1-Ba3 | BB+/BB/BB- |
| **NS-B** | 40-49 | Highly speculative. Significant weaknesses in multiple pillars. Viability depends on favorable conditions continuing. Adverse event could trigger rapid deterioration. | B1-B3 | B+/B/B- |
| **NS-CCC** | 30-39 | Substantial risk. Dependent on favorable conditions for continued operation. Treasury may be inadequate. Governance may be dysfunctional. Community may be fragmenting. | Caa1-Caa3 | CCC+/CCC/CCC- |
| **NS-CC** | 20-29 | Near distress. Very high risk of operational failure. Treasury depleting. Members departing. Governance in crisis. | Ca | CC |
| **NS-C** | 10-19 | Imminent failure. Treasury nearly exhausted. Community has largely departed. Operations minimal. | C | C |
| **NS-D** | 0-9 | Defunct/Default. Entity has ceased operations, defaulted on obligations, or community has dissolved. | C | D |

**Investment grade floor:** NS-BBB (CCS >= 60)
**Speculative grade:** NS-BB and below (CCS < 60)

### 4.5 Developmental Scale for Early-Stage Network States

The standard scale above is designed for established Network States (NSCF Stage S2+). For Stage S1 entities (Startup Societies), a simplified **Developmental Rating** is more appropriate, because many scoring criteria require data that pre-revenue, pre-governance entities simply do not have.

| Dev Rating | Description | Criteria |
|---|---|---|
| **NS-D1 (Promising)** | Early-stage entity with credible team, clear vision, initial funding, and growing community. Data insufficient for full rating. | Identifiable founder(s) with track record; > 100 members; treasury > $50K; clear roadmap |
| **NS-D2 (Emerging)** | Entity demonstrating traction but pre-institutional. Some data available. | > 500 members; treasury > $500K; governance mechanism exists; some revenue; 6+ months operating history |
| **NS-D3 (Pre-Investment Grade)** | Entity approaching institutional maturity. Enough data for partial rating. Transitioning from Developmental to Standard scale. | > 1,000 members; treasury > $1M; formal governance; 12+ months operating; retention data available |
| **NR (Not Rated)** | Insufficient data for even developmental rating. | Does not meet NS-D1 criteria; no public data |

**Graduation:** An entity moves from the Developmental scale to the Standard scale when it has 12+ months of operating data across all five pillars. This is analogous to how credit rating agencies assign provisional ratings to newly formed entities.

---

### 4.6 What "NS-AAA" Looks Like

An NS-AAA Network State would exhibit:

**Treasury:** $100M+ treasury, 70%+ in stablecoins/fiat, 36+ months runway, 4+ diversified revenue streams all growing, no single source > 30% of revenue.

**Governance:** Constitutional governance with checks and balances, 60%+ participation, regular public reporting, externally audited financials, distributed multisig (5+ signers), no single entity controls > 5% of votes, formal succession plan, leadership transitions have occurred successfully.

**Community:** 85%+ annual retention, 30%+ net growth with waitlist, GCP per member > $90,000, 30+ nationalities, 5+ professional sectors, strong cultural cohesion.

**Infrastructure:** Owned real estate in 3+ locations, self-hosted digital infrastructure with 99.9% uptime, incorporated in multiple jurisdictions, formal long-term agreements with host governments, all smart contracts audited, comprehensive legal structure.

**External Risk:** < 10% crypto correlation, operating in regulatory-stable jurisdictions with proactive compliance, diversified across 3+ host countries and chains, strong positive reputation, formal disaster recovery plan.

**Assessment:** No Network State in 2026 meets these criteria. The most advanced entities (Network School, Prospera) are in the NS-BB to NS-B range. NS-AAA represents a target state for a mature, decade-old Network State with multiple location nodes and institutional-grade infrastructure.

### 4.7 What "Junk" (NS-CCC and Below) Looks Like

An NS-CCC Network State would exhibit:

**Treasury:** < $100K or rapidly depleting; 90%+ in single volatile token; < 3 months runway; single revenue source declining.

**Governance:** Founder-led with no succession plan; < 10% participation; no financial reporting; single-signer treasury; no audits.

**Community:** < 40% annual retention; declining membership; low GCP per member; limited diversity; internal conflicts.

**Infrastructure:** No physical presence; dependent on free platforms; no legal entity; no host country relationship; unaudited smart contracts.

**External Risk:** 100% correlated with single crypto asset; operating in hostile regulatory environment; single point of failure across all dimensions; active reputational crisis.

---

## PART V: ILLUSTRATIVE RATINGS

### Methodology Note

The following ratings are illustrative, based on publicly available information as of April 2026. All scores involve significant estimation and assumption. A formal rating would require direct data access and management engagement. Data limitations are noted for each entity.

### 5.1 Network School

**NSCF Code:** NS-S2.T4/T2.E5.G1.P1.D3
**NSDI:** 0.49 (Medium Network Development)

| Pillar | Sub-factor | Score | Notes |
|---|---|---|---|
| **Treasury Health (30%)** | | | |
| | Treasury size/per-member | 55 | Estimated $7.2M annual revenue ($1,500 x 400 x 12); treasury size not publicly disclosed; per-member adequate |
| | Composition quality | 65 | Assumed majority fiat (membership fees collected in USD); some crypto exposure likely |
| | Burn rate/runway | 60 | Revenue appears to cover costs; SaaS-like model with high occupancy suggests 12-18 month implied runway |
| | Revenue diversity | 55 | Primary revenue is membership fees; some sponsorships, events, partnerships; dominated by single stream |
| | Revenue growth | 80 | Membership grew from 128 to 400+ in ~12 months; strong growth trajectory |
| | **Pillar 1 Score** | **62** | |
| **Governance Quality (25%)** | | | |
| | Model maturity | 25 | Founder-led (Balaji Srinivasan); no formal governance charter; no elected council |
| | Participation | 50 | High informal engagement (daily community activity); no formal governance voting |
| | Transparency | 40 | Some public communication; no published financials; no on-chain treasury |
| | Governance security | 35 | Founder-controlled; no multisig governance; no governance token |
| | Key person dependency | 15 | Extremely high Balaji dependency; brand = founder; no public succession plan |
| | **Pillar 2 Score** | **33** | |
| **Community Resilience (20%)** | | | |
| | Retention rate | 60 | Estimated 55-70%; cohort model means some natural churn; growth suggests good retention |
| | Net migration | 85 | Strong growth from 128 to 400+ ; expansion plans to multiple cities |
| | Member economic quality | 85 | Very high talent density; founders, investors, researchers from top institutions; GCP ~$90K/member |
| | Diversity | 90 | 70+ countries; multiple professional sectors; strong diversity |
| | Cultural cohesion | 75 | Strong shared identity; active in-person community; daily events and lectures |
| | **Pillar 3 Score** | **77** | |
| **Infrastructure Robustness (15%)** | | | |
| | Digital infrastructure | 45 | Standard platforms (assumed); no proprietary infrastructure; basic member tools |
| | Physical infrastructure | 50 | Leased facilities in Forest City; single location; adequate but not owned |
| | Legal structure | 55 | Incorporated entity (assumed); operates within Forest City SFZ; single jurisdiction |
| | Smart contract security | N/A | No significant smart contract exposure; scored as 50 (neutral) |
| | Host country relationship | 65 | Forest City SFZ is government-supported; IRDA relationship; but single host country |
| | **Pillar 4 Score** | **53** | |
| **External Risk (10%)** | | | |
| | Crypto market correlation | 65 | Revenue in fiat (membership fees); some crypto-adjacent risk from member base |
| | Regulatory risk | 70 | Malaysia is relatively stable; Forest City SFZ has government support; JS-SEZ framework |
| | Concentration risk | 30 | Single location, single founder, membership fees dominant revenue; high concentration |
| | Reputational risk | 70 | Strong positive reputation; Balaji's brand; some controversy around NS concept but manageable |
| | Black swan vulnerability | 35 | Single location + single founder = dual single points of failure |
| | **Pillar 5 Score** | **54** | |

**Composite Credit Score:**
> CCS = (62 x 0.30) + (33 x 0.25) + (77 x 0.20) + (53 x 0.15) + (54 x 0.10)
> CCS = 18.6 + 8.25 + 15.4 + 7.95 + 5.4
> **CCS = 55.6**

**Rating: NS-BB (Speculative)**

**Key strengths:** Exceptional community quality (talent density, diversity, growth); strong revenue model (subscription-based, recession-resistant for committed members); unique positioning in Forest City SFZ.

**Key weaknesses:** Extreme founder dependency (Balaji Srinivasan is the brand, the strategy, and the decision-maker); lack of formal governance; single physical location; no public financial reporting.

**Upgrade triggers:** Formal governance structure implemented; second physical location established; financial reporting initiated; succession planning.

**Downgrade triggers:** Balaji Srinivasan departure or disengagement; Malaysia regulatory change affecting Forest City SFZ; membership decline below 300; revenue shortfall requiring treasury draw-down.

**Data limitations:** Treasury size, composition, and runway are estimated. Retention data is inferred from growth patterns. Revenue data is estimated from public membership fee information.

---

### 5.2 Prospera / Infinita City

**NSCF Code:** NS-S3.T1/T3.E3.G5.P4.D3
**NSDI:** 0.50 (Medium Network Development)

| Pillar | Sub-factor | Score | Notes |
|---|---|---|---|
| **Treasury Health (30%)** | | | |
| | Treasury size | 65 | $100-200M total investment; actual treasury unclear; significant capital deployed |
| | Composition | 50 | BTC legal tender in zone; likely mixed crypto/fiat; composition uncertain |
| | Burn rate/runway | 50 | Operating businesses generate revenue; but legal dispute costs unclear |
| | Revenue diversity | 60 | Business registrations, residency fees, tax revenue (1% business, 5% personal), events |
| | Revenue growth | 45 | Legal uncertainty (ZEDE constitutionality dispute) creates headwinds |
| | **Pillar 1 Score** | **54** | |
| **Governance Quality (25%)** | | | |
| | Model maturity | 70 | ZEDE charter provides constitutional framework; formal governance structure; dispute resolution |
| | Participation | 50 | Business community engaged; governance mechanisms formal but participation data limited |
| | Transparency | 55 | Published charter and legal framework; some business transparency; limited financial disclosure |
| | Governance security | 60 | Formal legal framework; multi-stakeholder governance; but dependent on Honduran state recognition |
| | Key person dependency | 45 | Multiple leaders (Erick Brimen, Niklas Anzinger); less dependent on single founder than NS |
| | **Pillar 2 Score** | **56** | |
| **Community Resilience (20%)** | | | |
| | Retention | 55 | Businesses appear to be staying despite legal uncertainty; residential community stable |
| | Net migration | 40 | Growth slowed by legal dispute; some businesses waiting for clarity |
| | Economic quality | 65 | 200+ businesses; mix of biotech, software, tourism; moderate GCP per capita |
| | Diversity | 50 | International businesses but geographically concentrated; limited nationality diversity data |
| | Cultural cohesion | 50 | Longevity/biotech mission provides cohesion; but political uncertainty creates anxiety |
| | **Pillar 3 Score** | **52** | |
| **Infrastructure Robustness (15%)** | | | |
| | Digital | 50 | Basic digital infrastructure; not a tech-native community |
| | Physical | 70 | Real buildings, operating businesses, residential units on Roatan; physical territory is real |
| | Legal structure | 30 | ZEDE constitutionality disputed; Supreme Court ruled against ZEDEs Sep 2024; status in limbo |
| | Smart contract security | 45 | Bitcoin accepted; some DeFi activity; limited audit information |
| | Host country relationship | 20 | Active constitutional dispute with Honduras; new president may revive but uncertain |
| | **Pillar 4 Score** | **42** | |
| **External Risk (10%)** | | | |
| | Crypto correlation | 45 | BTC as legal tender creates direct correlation; treasury mix uncertain |
| | Regulatory risk | 15 | Active Supreme Court ruling against ZEDE framework; highest possible regulatory risk |
| | Concentration risk | 20 | Single host country (Honduras); single island (Roatan); single legal framework (ZEDE) |
| | Reputational risk | 40 | Controversial; criticized by Honduran civil society; "libertarian enclave" narrative |
| | Black swan vulnerability | 20 | Legal dissolution is an active risk, not a theoretical one |
| | **Pillar 5 Score** | **28** | |

**Composite Credit Score:**
> CCS = (54 x 0.30) + (56 x 0.25) + (52 x 0.20) + (42 x 0.15) + (28 x 0.10)
> CCS = 16.2 + 14.0 + 10.4 + 6.3 + 2.8
> **CCS = 49.7**

**Rating: NS-B (Highly Speculative)**

**Key strengths:** Most advanced physical infrastructure of any Network State; formal constitutional governance framework (ZEDE charter); real operating businesses generating real revenue; diverse economic activity.

**Key weaknesses:** Active constitutional dispute with Honduras is an existential threat; extreme geographic and legal concentration (single island, single country, single legal framework); regulatory risk is the highest of any rated entity.

**Upgrade triggers:** Favorable resolution of ZEDE constitutional dispute; expansion to second jurisdiction; stable revenue growth for 12+ months.

**Downgrade triggers:** Adverse court ruling forcing closure; mass business departures; treasury depletion from legal costs.

**Data limitations:** Treasury data is not publicly available. Revenue data is estimated from tax rates and business count. Retention and governance participation data are inferred.

---

### 5.3 Praxis

**NSCF Code:** NS-S2.T5/T2.E2.G6.P0.D3
**NSDI:** 0.39 (Low Network Development)

| Pillar | Sub-factor | Score | Notes |
|---|---|---|---|
| **Treasury Health (30%)** | | | |
| | Treasury size | 85 | $544M raised; largest war chest in the Network State ecosystem |
| | Composition | 50 | Crypto-heavy (VC investment in crypto context); composition details not public |
| | Burn rate/runway | 60 | Massive capital base; but city construction is extraordinarily capital-intensive; runway depends on deployment rate |
| | Revenue diversity | 20 | Essentially zero operating revenue; entirely dependent on invested capital; no recurring revenue yet |
| | Revenue growth | 15 | No operating revenue to grow; pre-revenue entity |
| | **Pillar 1 Score** | **47** | |
| **Governance Quality (25%)** | | | |
| | Model maturity | 35 | Dryden Brown founder-led; community engagement through online platforms; no formal governance charter |
| | Participation | 30 | Large claimed community (151K) but active participation unclear; online forums vs. real governance |
| | Transparency | 35 | Some public communication; major announcements public; but financial detail limited |
| | Governance security | 30 | No on-chain governance; investor structure unclear; decision-making centralized |
| | Key person dependency | 25 | Dryden Brown is highly identified with project; multiple investors provide some counterweight |
| | **Pillar 2 Score** | **31** | |
| **Community Resilience (20%)** | | | |
| | Retention | 35 | 151K "citizens" claimed; actual engaged community likely far smaller; no retention data |
| | Net migration | 50 | Waitlist of 50,000 suggests demand; but virtual sign-ups vs actual committed members unclear |
| | Economic quality | 40 | Claims $1.117 trillion aggregate valuation of member companies; self-reported and unverifiable |
| | Diversity | 55 | 80 countries claimed; tech-heavy but international |
| | Cultural cohesion | 30 | Primarily online community; limited in-person interaction pre-construction; cohesion untested |
| | **Pillar 3 Score** | **40** | |
| **Infrastructure Robustness (15%)** | | | |
| | Digital | 50 | Active web presence; online community platforms; crypto-native infrastructure |
| | Physical | 15 | Atlas site selected (Vandenberg, CA) but construction not complete; no operational physical space |
| | Legal structure | 50 | US-incorporated; formal legal entity; investor agreements provide some structure |
| | Smart contract security | 40 | Some crypto infrastructure; audit status unknown |
| | Host country relationship | 45 | US is stable but crypto-regulatory environment is evolving; Vandenberg site secured |
| | **Pillar 4 Score** | **39** | |
| **External Risk (10%)** | | | |
| | Crypto correlation | 35 | Crypto-native funding and community; high correlation with crypto market sentiment |
| | Regulatory risk | 55 | US regulatory environment is uncertain for crypto but rule of law is strong |
| | Concentration risk | 30 | Single planned location; single founder; single funding base (crypto VC) |
| | Reputational risk | 50 | Mixed: high-profile but also polarizing; "build a city" pitch draws skepticism |
| | Black swan vulnerability | 30 | Pre-construction; if market turns, capital deployment may stall |
| | **Pillar 5 Score** | **40** | |

**Composite Credit Score:**
> CCS = (47 x 0.30) + (31 x 0.25) + (40 x 0.20) + (39 x 0.15) + (40 x 0.10)
> CCS = 14.1 + 7.75 + 8.0 + 5.85 + 4.0
> **CCS = 39.7**

**Rating: NS-CCC (Substantial Risk)**

**Key observation:** Despite having the largest treasury ($544M) of any Network State, Praxis receives a low rating because:
1. No operating revenue (zero recurring income)
2. No physical community yet (construction phase)
3. Governance is immature (founder-led, online-only)
4. 151K "citizens" is an unverifiable vanity metric (likely < 10K active)
5. City construction is the most capital-intensive possible deployment (high burn risk)

This demonstrates the framework's critical insight: **capital is not creditworthiness.** A sovereign nation with massive oil reserves but no institutions, no rule of law, and no functioning economy would similarly receive a low rating from Moody's/S&P despite financial resources.

**Upgrade triggers:** Successful construction completion and community move-in; establishment of recurring revenue; formal governance implementation; retention data proving community commitment.

**Downgrade triggers:** Significant cost overruns; failure to begin construction; major investor withdrawal; crypto market collapse reducing treasury value.

---

### 5.4 Zuzalu

**NSCF Code:** NS-S2.T4/T2.E3.G6.P2.D2

| Pillar | Score | Key Rationale |
|---|---|---|
| Treasury Health | 35 | No permanent treasury; event-funded model; Gitcoin grants; low financial sustainability |
| Governance Quality | 45 | Community-driven; Vitalik Buterin influence but not sole leader; informal governance; high community engagement |
| Community Resilience | 65 | Strong community identity; high-quality members; 20+ derivative events; global distribution; but pop-up model means no retention data |
| Infrastructure Robustness | 25 | No permanent infrastructure; pop-up events are temporary; no legal entity; no host country agreements |
| External Risk | 40 | Low crypto correlation (event-funded); but regulatory risk from operating in many countries; Vitalik dependency |

**CCS = (35 x 0.30) + (45 x 0.25) + (65 x 0.20) + (25 x 0.15) + (40 x 0.10) = 10.5 + 11.25 + 13.0 + 3.75 + 4.0 = 42.5**

**Rating: NS-B (Highly Speculative)**

**Key observation:** Zuzalu's pop-up model is brilliantly adaptive but structurally weak for credit assessment. No permanent treasury, no permanent location, no formal governance. Its strength is community quality and cultural impact, which are hard to capitalize.

---

### 5.5 CityDAO

**NSCF Code:** NS-S1.T2.E1.G3.P1.D3

| Pillar | Score | Key Rationale |
|---|---|---|
| Treasury Health | 40 | $5M treasury; on-chain (transparent); but limited revenue generation beyond initial token sales |
| Governance Quality | 50 | On-chain DAO governance; token-weighted voting; transparent; but low participation and internal disputes |
| Community Resilience | 25 | 7,000 token holders but minimal active community; limited physical presence; Wyoming land largely unused |
| Infrastructure Robustness | 35 | 40 acres in Wyoming (real); on-chain governance (real); but minimal physical development; DAO LLC in Wyoming |
| External Risk | 45 | Low crypto correlation relative to peers; US-based; but single asset (land) and governance disputes |

**CCS = (40 x 0.30) + (50 x 0.25) + (25 x 0.20) + (35 x 0.15) + (45 x 0.10) = 12.0 + 12.5 + 5.0 + 5.25 + 4.5 = 39.25**

**Rating: NS-CCC (Substantial Risk)**

**Key observation:** CityDAO is a governance experiment that has not evolved into a functioning community. The $5M treasury provides some buffer, but the disconnect between 7,000 token holders and near-zero active community activity signals fundamental viability risk.

---

### 5.6 Liberland

**NSCF Code:** NS-S2.T5.E1.G4.P1.D3

| Pillar | Score | Key Rationale |
|---|---|---|
| Treasury Health | 25 | Treasury details opaque; LLM token exists but unclear value; limited identifiable revenue |
| Governance Quality | 40 | Written constitution; formal governance framework; Vit Jedlicka as president; some democratic mechanisms; but actual participation data unavailable |
| Community Resilience | 30 | Claims 700,000+ registered citizens; actual active community likely < 1,000; some in-person gatherings |
| Infrastructure Robustness | 20 | Claimed territory (Gornja Siga, Croatia-Serbia border) is not controlled in practice; no buildings; no host country recognition; Croatia actively blocks access |
| External Risk | 15 | Claimed territory is actively disputed; Croatia does not recognize; no international recognition; extremely concentrated risk |

**CCS = (25 x 0.30) + (40 x 0.25) + (30 x 0.20) + (20 x 0.15) + (15 x 0.10) = 7.5 + 10.0 + 6.0 + 3.0 + 1.5 = 28.0**

**Rating: NS-CC (Near Distress)**

**Key observation:** Liberland has the most ambitious sovereignty claim of any Network State but the weakest foundation to support it. The territorial claim is unrecognized and physically inaccessible. The gap between rhetorical ambition (sovereign nation) and operational reality (online community with no territory) is the largest of any rated entity.

---

### 5.7 Afropolitan

**NSCF Code:** NS-S1.T3.E1.G1.P0.D2

| Pillar | Score | Key Rationale |
|---|---|---|
| Treasury Health | 20 | $2.1M seed funding (2022); unclear how much remains; revenue from events, dating service ($49/mo), mentoring; limited scale |
| Governance Quality | 15 | Founder-led; no governance mechanism for community; corporate structure, not community governance; opaque |
| Community Resilience | 25 | Networking events attract participants; but "digital nation" framing does not match operational reality; primarily SF Bay Area |
| Infrastructure Robustness | 15 | No physical territory; event-based; standard corporate legal structure; no host country relationship as "nation" |
| External Risk | 30 | Low crypto exposure (primarily events/services company); but gap between rhetoric and reality creates reputational risk |

**CCS = (20 x 0.30) + (15 x 0.25) + (25 x 0.20) + (15 x 0.15) + (30 x 0.10) = 6.0 + 3.75 + 5.0 + 2.25 + 3.0 = 20.0**

**Rating: NS-CC (Near Distress)**

**Key observation:** Afropolitan is assessed as a Network State because it claims to be building one. By that standard, it has the widest credibility gap of any rated entity. It is operationally a small networking and events company ($2.1M seed, dating app, event tickets) marketing itself as a "digital nation for the African diaspora." Until it develops actual community governance, treasury, physical presence, or member-state infrastructure, the credit rating reflects the entity's reality, not its aspiration.

Source: https://africasacountry.com/2025/05/afropolitans-and-the-fantasy-of-a-digital-nation

---

### 5.8 Rating Summary Table

| Entity | CCS | Rating | Rating Outlook | Primary Strength | Primary Weakness |
|---|---|---|---|---|---|
| **Network School** | 55.6 | NS-BB | Positive | Community quality; revenue model | Founder dependency; single location |
| **Prospera / Infinita** | 49.7 | NS-B | Negative | Physical infrastructure; governance charter | Constitutional dispute with Honduras |
| **Praxis** | 39.7 | NS-CCC | Developing | Treasury size ($544M) | Pre-revenue; pre-construction; governance immaturity |
| **Zuzalu** | 42.5 | NS-B | Stable | Community quality; cultural impact | No permanent treasury, infrastructure, or legal entity |
| **CityDAO** | 39.3 | NS-CCC | Stable | On-chain governance; treasury transparency | Minimal active community; governance disputes |
| **Liberland** | 28.0 | NS-CC | Negative | Sovereignty ambition; constitutional framework | No actual territory control; no recognition |
| **Afropolitan** | 20.0 | NS-CC | Negative | Mission resonance (African diaspora) | Extreme gap between rhetoric and reality |

---

## PART VI: DATA REQUIREMENTS

### 6.1 Complete Data Requirements for a Full Rating

| Category | Data Required | Source | Frequency |
|---|---|---|---|
| **Treasury** | | | |
| | Total treasury value (USD equivalent) | On-chain wallets + bank accounts | Quarterly |
| | Treasury composition breakdown (% stablecoins, % volatile crypto, % fiat, % other) | On-chain analysis + self-report | Quarterly |
| | Monthly inflows and outflows (last 12 months) | On-chain + accounting records | Monthly |
| | Current monthly burn rate | Accounting records | Monthly |
| | Revenue by source (membership fees, services, token sales, grants, other) | Financial statements | Quarterly |
| | Top 5 expense categories | Financial statements | Quarterly |
| | Outstanding liabilities (DeFi loans, contractual obligations, pending payments) | On-chain + legal review | Quarterly |
| **Governance** | | | |
| | Governance model documentation (constitution, charter, bylaws) | Public documents | Annual |
| | List of governance decision-makers (council members, multisig signers) | Public + self-report | Annual |
| | Governance participation data (proposals submitted, votes cast, participation rates) | On-chain + platform analytics | Quarterly |
| | Multisig configuration (N-of-M, signer identities, geographic distribution) | On-chain | Annual |
| | Token distribution (top 10 holders, Gini coefficient, founder allocation) | On-chain | Quarterly |
| | Governance audit or assessment (if any) | Third-party report | Annual |
| | Succession plan documentation | Self-report | Annual |
| **Community** | | | |
| | Total active members (defined as logged in + participated in last 30 days) | Platform analytics | Monthly |
| | Retention cohort data (monthly and annual) | Platform analytics | Quarterly |
| | New member applications and acceptances | Membership system | Monthly |
| | Member departures and reasons (if collected) | Exit surveys | Quarterly |
| | Member demographic profile (nationality distribution, professional sectors, education) | Membership database | Annual |
| | GCP per member estimate | Economic survey + on-chain | Annual |
| | Net Promoter Score or satisfaction survey | Member survey | Semi-annual |
| **Infrastructure** | | | |
| | Digital platform uptime and incident log | Platform monitoring | Monthly |
| | Physical asset inventory (owned vs. leased, location, lease terms) | Legal/property records | Annual |
| | Security audit reports (smart contract, infrastructure) | Third-party auditor | Annual |
| | Legal entity documentation (incorporation, licenses, registrations) | Legal counsel | Annual |
| | Host country agreement documentation | Legal counsel | Annual |
| | Insurance coverage (if any) | Insurance records | Annual |
| **External** | | | |
| | Host country regulatory status and recent policy changes | Legal counsel + public records | Quarterly |
| | Crypto market exposure analysis (correlation of treasury value to BTC/ETH) | Quantitative analysis | Quarterly |
| | Competitive landscape assessment | Market research | Annual |
| | Media sentiment analysis | Media monitoring | Quarterly |
| | Pending or active legal proceedings | Legal counsel | Quarterly |

### 6.2 On-Chain vs Self-Reported Data

| Data Element | On-Chain Observable | Self-Reported Required |
|---|---|---|
| Treasury value (crypto portion) | Yes | No |
| Treasury value (fiat portion) | No | Yes |
| Treasury composition (crypto) | Yes | No |
| Token distribution | Yes | No |
| Multisig configuration | Yes | No |
| Governance votes (on-chain DAOs) | Yes | No |
| Governance decisions (off-chain) | No | Yes |
| Smart contract code | Yes | No |
| Member count | No (unless on-chain census) | Yes |
| Retention data | No | Yes |
| Revenue data (crypto) | Partially (inflows to known wallets) | Partially |
| Revenue data (fiat) | No | Yes |
| Physical asset data | No | Yes |
| Legal entity data | No | Yes |
| Host country relationship | No | Yes |

**Key insight:** Approximately 30-40% of the data needed for a full NSCRF rating is observable on-chain without the entity's cooperation. The remaining 60-70% requires self-reporting. This is better than sovereign ratings (which are almost entirely dependent on government self-reporting through national statistics offices) but worse than public company ratings (which have mandatory audited disclosure).

### 6.3 Minimum Data for a Preliminary Rating

A preliminary ("shadow") rating can be assigned with:

| Minimum Data | Source | Why Required |
|---|---|---|
| Identifiable treasury wallet addresses (crypto) | Public blockchain | Treasury size and composition assessment |
| Public membership count | Website/public reporting | Community scale |
| Governance model description | Website/whitepaper | Governance assessment |
| Operating history (months since launch) | Public records | Track record |
| Physical location(s) | Public information | Infrastructure assessment |
| Founder/leadership identification | Public information | Key person risk |
| Publicly stated mission and structure | Website/whitepaper | Framework classification |

With this minimum data, a preliminary rating in the NS-D1 to NS-D3 (Developmental) range can be assigned. A full Standard scale rating requires the complete dataset in Section 6.1.

### 6.4 Rating Review Frequency

| Review Type | Frequency | Trigger |
|---|---|---|
| **Full annual review** | Every 12 months | Comprehensive reassessment using full data submission |
| **Interim review** | Every 6 months | Abbreviated assessment focusing on material changes |
| **Event-driven review** | Ad hoc | Triggered by: treasury decline > 30%, host country regulatory change, founder departure, governance crisis, member exodus > 20%, security breach, legal action |
| **Rating watch** | As needed | Entity placed on "watch" (positive, negative, or developing) when a material event occurs but the full impact is not yet clear |

**Rationale:** The crypto ecosystem moves faster than traditional markets. Annual reviews (standard for sovereign ratings) are insufficient. Semi-annual interim reviews capture meaningful changes. Event-driven reviews provide responsiveness to the volatile nature of Network State operations.

---

## PART VII: COMPARISON WITH EXISTING FRAMEWORKS

### 7.1 NSCRF vs Moody's Sovereign Methodology

| Dimension | Moody's Sovereign | NSCRF | Adaptation |
|---|---|---|---|
| **Economic Strength** | GDP growth, GDP/capita, diversification | GCP per member, member economic quality, talent density | GDP replaced with GCP; national economy replaced with community economy |
| **Institutional Strength** | WB Governance Indicators, policy effectiveness | Governance model maturity, participation, transparency, key person risk | WGI indicators replaced with bespoke governance assessment; key person risk added (not relevant for sovereigns) |
| **Fiscal Strength** | Debt/GDP, interest/revenue, fiscal balance | Treasury size, composition, burn rate, revenue diversity | Government debt replaced with treasury management; tax base replaced with voluntary revenue |
| **Event Risk** | Political risk, banking, external, liquidity | Crypto correlation, regulatory, concentration, reputation, black swan | Banking sector risk replaced with crypto market risk; political risk adapted for host country relationship |
| **Weighting** | ~25% each (four factors) | 30/25/20/15/10 (five pillars) | Treasury overweighted because NS cannot tax or print money; external risk underweighted because internal factors are more determinative |

**What is borrowed from Moody's:** The four-factor structure; the concept of combining quantitative scorecards with qualitative overlays; the rating scale logic; the distinction between "ability to pay" and "willingness to pay."

**What is novel:** Treasury composition analysis (crypto-specific); key person dependency assessment; voluntary membership dynamics (retention as a credit factor); on-chain data integration; governance attack surface assessment.

### 7.2 NSCRF vs S&P Corporate Methodology

| Dimension | S&P Corporate | NSCRF | Adaptation |
|---|---|---|---|
| **Business Risk** | Industry risk, competitive position, country risk | Community resilience, cultural cohesion, competitive risk | "Industry" replaced with "community type"; competitive position replaced with retention and growth |
| **Financial Risk** | Cash flow, leverage, liquidity | Treasury health (burn rate, runway, revenue diversity) | FFO/debt replaced with runway months; leverage metrics adapted for entities without traditional debt |
| **Governance** | Management & governance modifier | Full pillar (Governance Quality, 25% weight) | Elevated from modifier to core pillar; governance is existential for voluntary-membership entities |
| **Financial Policy** | Aggressiveness of leverage/M&A | Treasury composition, revenue concentration | Risk appetite assessment adapted from corporate leverage to crypto treasury management |

**What is borrowed from S&P Corporate:** Cash flow analysis; burn rate/runway concept; governance as a rating factor; the business risk / financial risk dual assessment.

**What is novel:** Voluntary membership dynamics; crypto treasury composition analysis; governance attack surface; community cohesion as a credit factor.

### 7.3 NSCRF vs DeFi Protocol Risk Frameworks

Several organizations provide risk ratings for DeFi protocols. The most relevant comparisons:

**DeFi Safety (defisafety.com)**
- Rates DeFi protocols on a 0-100 scale based on process quality
- Focus areas: documentation quality, testing, audit status, admin key management, oracles
- Purely technical/operational assessment; no community or economic factors
- NSCRF adapts: smart contract audit status, infrastructure security

**Exponential DeFi (exponential.fi)**
- Provides risk ratings for DeFi pools and strategies
- Assesses: asset risk, platform risk, complexity risk
- Focus on smart contract and economic exploit risk
- NSCRF adapts: treasury composition risk analysis, governance attack surface

**Gauntlet / Chaos Labs**
- Quantitative risk assessment for DeFi protocols
- Focus on economic simulation, liquidation risk, oracle risk
- NSCRF adapts: quantitative treasury stress testing concept (how does treasury value change under crypto drawdown scenarios)

**Blue Chip DeFi Score (by various analysts)**
- Combines TVL, audit status, team identity, governance decentralization, longevity
- Most similar to NSCRF in combining multiple dimensions
- NSCRF adapts: multi-dimensional scoring concept; longevity (operating history) as a factor

| Feature | DeFi Safety | Exponential | NSCRF |
|---|---|---|---|
| Scope | Protocol code quality | Pool/strategy risk | Entire Network State |
| Community assessment | No | No | Yes (20% weight) |
| Governance assessment | Minimal (admin keys) | No | Yes (25% weight) |
| Treasury/financial | No | Limited (asset risk) | Yes (30% weight) |
| Physical infrastructure | No | No | Yes (15% weight) |
| External risk | No | Limited | Yes (10% weight) |
| Forward-looking | No (point-in-time) | No | Yes (outlook assignments) |
| Rating scale | 0-100 score | Risk grade | NS-AAA to NS-D scale |

**What is borrowed from DeFi frameworks:** Smart contract audit importance; on-chain data verification; governance attack surface concept; quantitative scoring methodology.

**What is novel in NSCRF:** Community resilience as a credit factor; physical infrastructure assessment; host country relationship; voluntary membership dynamics; forward-looking outlook; rating scale with investment-grade / speculative-grade distinction.

### 7.4 Summary: What is Borrowed vs What is Novel

| Element | Origin | Adaptation for Network States |
|---|---|---|
| Multi-pillar scoring framework | All three CRAs | Pillars redesigned for NS realities |
| Quantitative scorecard + qualitative overlay | Moody's, Fitch | Applied to NS data sources (on-chain + self-report) |
| Cash flow / runway analysis | Corporate credit (S&P) | Adapted for crypto treasury and voluntary revenue |
| Governance as institutional quality | Sovereign credit (all CRAs) | Expanded to full pillar; governance attack surface added |
| Rating scale (AAA to D) | All three CRAs | "NS-" prefix; same scale logic; developmental scale added |
| Investment grade / speculative grade distinction | All three CRAs | NS-BBB threshold at CCS >= 60 |
| Event-driven review triggers | All three CRAs | Adapted for crypto-specific events |
| **Treasury composition quality scoring** | **Novel** | No CRA rates asset composition this granularly; specific to crypto treasury risk |
| **Voluntary membership retention as credit factor** | **Novel** | Sovereigns have captive populations; retention is the NS substitute |
| **Key person dependency scoring** | **Novel** | CRAs assess management quality but not single-founder existential risk at this level |
| **Governance attack surface** | **Novel (adapted from DeFi)** | Multisig, token concentration, timelocks -- crypto-native governance security |
| **Developmental rating scale** | **Novel** | Recognizes that most NS are pre-institutional; provides framework for early-stage assessment |
| **Host country relationship as credit factor** | **Novel** | Sovereigns do not depend on other sovereigns for territorial existence; NS do |
| **On-chain data verification** | **Adapted from DeFi** | Unique advantage: partial independent verification without entity cooperation |

---

## PART VIII: COMMERCIAL POTENTIAL

### 8.1 Could This Become a Business?

Yes. The Network State credit rating agency is a viable business concept. The market conditions are analogous to the early days of DeFi risk ratings (2020-2021), which have since become established services.

**Market size estimate:**
- 117 tracked startup societies (ns.com dashboard, April 2026)
- Growing at roughly 30-50% per year
- Combined capital under management / treasury exceeds $1 billion
- Total DAO ecosystem treasury: ~$24.5 billion
- If 10% of entities seek ratings within 3 years: ~35-50 rated entities by 2029

**Revenue model:**

| Revenue Stream | Payer | Annual Fee (Estimated) | Rationale |
|---|---|---|---|
| **Issuer-pays rating** | Network State entity | $5,000 - $50,000 per annual rating | Analogous to corporate rating fees (which range from $25K-$500K); NS fees at lower end due to entity size |
| **Investor-pays subscription** | VCs, LPs, family offices, DAOs investing in NS ecosystem | $1,000 - $10,000/year per subscriber | Access to full rating reports, methodology, and rating changes |
| **Host country advisory** | Governments (SEZ authorities, IRDA, DIFC, etc.) | $10,000 - $100,000 per engagement | Advisory on NS creditworthiness for zones considering NS tenants |
| **Member-facing reports** | Individual NS members or prospective members | Free or $50/report | Builds credibility; lead generation for paid services |
| **Research and consulting** | Academic institutions, think tanks, multilateral bodies | $5,000 - $50,000 per project | Custom research, methodology licensing, conference presentations |

**Conservative Year 1-3 projection:**
- Year 1: 5-10 rated entities, 20-50 investor subscribers = $75K-$250K revenue
- Year 2: 15-25 rated entities, 50-100 subscribers = $200K-$600K revenue
- Year 3: 30-50 rated entities, 100-200 subscribers = $500K-$1.5M revenue

### 8.2 Who Would Pay?

**Investors:**
- Crypto VCs evaluating Network State investments (Paradigm, Coinbase Ventures, a16z crypto)
- Traditional VCs entering the space
- Family offices and HNWIs considering NS membership or investment
- DAOs allocating treasury to NS-related projects
- LP (limited partners) conducting due diligence on funds investing in NS ecosystem

**Network State entities themselves:**
- Seeking credibility for fundraising (a rated entity signals maturity)
- Attracting members (members want to know the entity they're joining is financially sound)
- Negotiating with host countries (a credit rating strengthens the entity's position)
- Benchmark against peers (competitive intelligence)

**Host countries and zone authorities:**
- IRDA (Malaysia) evaluating NS tenants for Forest City SFZ
- DIFC/ADGM (UAE) assessing NS applicants
- Any SEZ authority considering hosting Network States
- UNCTAD, World Bank, or other multilateral bodies tracking the phenomenon

**Insurance providers:**
- If NS ever seek insurance (property, directors' liability, cyber), insurers need risk assessment tools

### 8.3 Precedents

**DeFi Safety** (defisafety.com): Founded ~2020. Rates 100+ DeFi protocols. Revenue from protocol fees and data subscriptions. Proves the market for crypto-native risk rating services.

**Exponential DeFi** (exponential.fi): Risk ratings for DeFi yield strategies. YC-backed. Revenue from user subscriptions and protocol partnerships.

**DeepDAO** (deepdao.io): DAO analytics platform tracking 2,400+ DAOs. Provides governance metrics, treasury data, and organizational analysis. Subscription-based revenue.

**Chainanalysis / Elliptic / TRM Labs**: Blockchain analytics firms valued in billions. Different scope (compliance/AML) but proves that blockchain data analysis is a viable business.

**CoinGecko / CoinMarketCap**: Free crypto data with premium features. Built large businesses on crypto data aggregation.

All of these demonstrate that structured, analytical services for crypto-native entities can generate revenue. NSCRF would be the first to apply this to Network States as political/community entities rather than just protocols or tokens.

### 8.4 Fit with Frontier Zones Capital Fund Thesis

The NSCRF directly supports a Frontier Zones Capital fund thesis:

1. **Due diligence infrastructure:** A fund investing in Network States needs a systematic way to evaluate creditworthiness. NSCRF provides that framework. The rating agency and the fund are complementary businesses.

2. **Deal flow generation:** Rating Network States creates visibility into the ecosystem. The rating process requires deep engagement with each entity, generating proprietary insights and relationships that feed deal flow.

3. **LP confidence:** LPs investing in a frontier fund want evidence of rigorous risk assessment. "We rate every entity in our portfolio using NSCRF" is a powerful differentiator.

4. **Exit multiple:** A functioning credit rating agency with 30-50 rated entities and growing subscriber base is a valuable standalone business. If the fund is structured to incubate the rating agency, the agency itself becomes a portfolio asset.

5. **First-mover IP advantage:** The first published, rigorous credit rating methodology for Network States has significant intellectual property value. It sets the standard that others must respond to.

6. **Academic credibility:** Published in an academic journal, the NSCRF provides the fund's principals with thought leadership positioning in a field where credibility matters enormously.

---

## PART IX: ACADEMIC REFERENCES

### 9.1 Rating Agency Published Methodologies

| Source | Title | Year | URL |
|---|---|---|---|
| Moody's | Rating Methodology: Sovereigns | 2024 | https://ratings.moodys.com/api/rmc-documents/430057 |
| Moody's | Sovereign Rating List | Current | https://www.moodys.com/researchandratings/ratings-list/sovereign/ |
| S&P Global Ratings | Sovereign Rating Methodology | 2017 | https://disclosure.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/2961552 |
| S&P Global Ratings | Understanding Credit Ratings | Current | https://www.spglobal.com/ratings/en/about/understanding-credit-ratings |
| S&P Global Ratings | Corporate Methodology | 2013+ | https://disclosure.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/2891327 |
| Fitch Ratings | Sovereign Rating Criteria | 2023 | https://www.fitchratings.com/research/sovereigns/sovereign-rating-criteria-03-04-2023 |
| Fitch Ratings | Sovereign Ratings | Current | https://www.fitchratings.com/research/sovereigns |

### 9.2 Basel Committee and Regulatory Standards

| Source | Title | Year | URL |
|---|---|---|---|
| Basel Committee (BCBS) | Basel II: International Convergence of Capital Measurement and Capital Standards | 2006 | https://www.bis.org/publ/bcbs128.htm |
| Basel Committee (BCBS) | Basel III: Finalising Post-Crisis Reforms | 2017 | https://www.bis.org/bcbs/publ/d424.htm |
| Basel Committee (BCBS) | The Standardised Approach for Credit Risk | 2006 | https://www.bis.org/publ/bcbs128.htm (Part 2, Section II) |
| IOSCO | Code of Conduct Fundamentals for Credit Rating Agencies | 2015 | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD482.pdf |
| EU Regulation | Regulation (EC) No 1060/2009 on Credit Rating Agencies | 2009 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009R1060 |

### 9.3 DeFi and DAO Risk Assessment

| Source | Title | Year | URL |
|---|---|---|---|
| DeFi Safety | Process Quality Reviews | Ongoing | https://defisafety.com |
| Exponential DeFi | Risk Ratings Methodology | Ongoing | https://exponential.fi |
| DeepDAO | DAO Analytics | Ongoing | https://deepdao.io |
| Gauntlet | DeFi Risk Modeling | Ongoing | https://gauntlet.network |
| Chaos Labs | Risk Management for DeFi | Ongoing | https://chaoslabs.xyz |
| Messari | Governor: DAO Governance Analytics | Ongoing | https://messari.io/governor/overview |

### 9.4 Academic Literature on Credit Risk and Non-State Entities

| Author(s) | Title | Journal/Source | Year | Relevance |
|---|---|---|---|---|
| Cantor, R. & Packer, F. | "Determinants and Impact of Sovereign Credit Ratings" | FRBNY Economic Policy Review | 1996 | Foundational study of sovereign credit rating determinants |
| Afonso, A., Gomes, P., & Rother, P. | "Short- and Long-Run Determinants of Sovereign Debt Credit Ratings" | International Journal of Finance & Economics | 2011 | Empirical analysis of what drives sovereign ratings |
| Mellios, C. & Paget-Blanc, E. | "Which Factors Determine Sovereign Credit Ratings?" | European Journal of Finance | 2006 | Quantitative analysis of CRA methodology factors |
| El-Shagi, M. & von Schweinitz, G. | "The Dilemma of European Financial Sector Regulation" | Journal of Financial Stability | 2018 | Critique of CRA methodology and regulatory implications |
| Srinivasan, B. | *The Network State: How to Start a New Country* | Self-published | 2022 | Foundational text defining Network States |
| World Economic Forum | "Decentralized Autonomous Organization Toolkit" | WEF White Paper | 2023 | Framework for assessing DAO governance |
| World Economic Forum | "Decentralized Autonomous Organizations: Beyond the Hype" | WEF/Wharton | 2022 | DAO classification and analysis |
| Barbereau, T. et al. | "Decentralised Finance's Unregulated Governance: Minority Rule in the Digital Wild West" | Journal of Industrial and Business Economics | 2023 | DAO governance analysis and critique |
| De Filippi, P. & Wright, A. | *Blockchain and the Law: The Rule of Code* | Harvard University Press | 2018 | Legal frameworks for blockchain-based organizations |
| Reijers, W. et al. | "Now the Code Runs Itself: On-chain and Off-chain Governance of Blockchain Technologies" | Topoi | 2021 | Governance models for blockchain communities |
| Atzori, M. | "Blockchain Technology and Decentralized Governance" | SSRN Working Paper | 2015 | Early analysis of blockchain for governance |
| Schneider, N. | "Admins, Mods, and Benevolent Dictators for Life: The Implicit Feudalism of Online Communities" | New Media & Society | 2022 | Power dynamics in digital communities -- relevant to governance assessment |

### 9.5 Network State and Charter City Literature

| Source | Title | Year | URL |
|---|---|---|---|
| Srinivasan, B. | The Network State (full text) | 2022 | https://thenetworkstate.com |
| Charter Cities Institute | Research publications | Ongoing | https://chartercitiesinstitute.org/research |
| Free Cities Foundation | Network State research | Ongoing | https://freecitiesfoundation.org |
| Romer, P. | "Technologies, Rules, and Progress: The Case for Charter Cities" | Center for Global Development | 2010 | Foundational charter city economics paper |
| Mason, P. | "The Governance of Startup Societies" | SSRN | 2024 | Governance models for new communities |

### 9.6 Additional Referenced Sources

| Source | URL |
|---|---|
| ns.com Network State Dashboard | https://ns.com/dashboard |
| DAO statistics (PatentPC) | https://patentpc.com/blog/dao-growth-stats-treasury-sizes-governance-votes-activity |
| DAO statistics (CoinLaw) | https://coinlaw.io/decentralized-autonomous-organizations-statistics/ |
| a16z: 16 Ways to Measure Network Effects | https://a16z.com/16-ways-to-measure-network-effects/ |
| Afropolitan assessment | https://africasacountry.com/2025/05/afropolitans-and-the-fantasy-of-a-digital-nation |
| Moody's Rating Scale | https://www.moodys.com/sites/products/productattachments/ap075378_1_1408_ki.pdf |
| World Bank Worldwide Governance Indicators | https://info.worldbank.org/governance/wgi/ |
| Transparency International CPI | https://www.transparency.org/en/cpi |

---

## PART X: METHODOLOGY LIMITATIONS AND FUTURE WORK

### 10.1 Limitations

1. **Data quality:** The illustrative ratings in Part V rely heavily on publicly available data, which is incomplete and often self-reported. A commercial rating service would require direct data access and management engagement.

2. **Calibration:** The scoring criteria (0-100 scales for each sub-factor) are proposed based on professional judgment and industry benchmarking. They require empirical calibration once a critical mass of entities is rated (minimum 20-30 for statistical significance).

3. **Weight sensitivity:** The pillar weights (30/25/20/15/10) are proposed based on first-principles analysis of what matters most for Network State creditworthiness. Alternative weighting schemes could produce materially different ratings. Sensitivity analysis should be conducted.

4. **Survivorship bias:** Only currently operating entities are assessed. Failed or dissolved Network States (Vitalia, various dissolved DAOs) are not in the sample. A complete methodology would study failure cases to validate that the framework assigns low scores to entities that subsequently fail.

5. **Cultural bias:** The methodology is designed primarily based on Western-origin, crypto-native Network States. Network State-like communities emerging from non-Western contexts (e.g., African diaspora communities, Southeast Asian cooperative networks) may require adapted criteria.

6. **Temporal limitations:** Network States evolve rapidly. A rating assigned today may be obsolete in months. The event-driven review mechanism partially addresses this but cannot eliminate the challenge.

7. **Moral hazard:** If Network States know the rating criteria, they may optimize for scores rather than substance (Goodhart's Law). Rating agencies must assess substance, not just metrics.

8. **Comparability with traditional ratings:** The NS-AAA to NS-D scale uses familiar labels but represents a fundamentally different asset class. An NS-BBB Network State is not equivalent to a BBB sovereign or corporation. Users must understand this distinction.

### 10.2 Future Work

1. **Empirical validation:** Apply the methodology to all 117 tracked startup societies to create a baseline distribution and validate scoring criteria.

2. **Backtesting:** Apply the methodology retrospectively to entities that have failed (Vitalia, various dissolved DAOs) to test whether the framework assigns appropriately low scores pre-failure.

3. **Sensitivity analysis:** Test how rating outcomes change under different weighting schemes to identify which pillars are most determinative.

4. **Correlation analysis:** Study the correlation between NSCRF scores and actual outcomes (member retention, treasury growth, fundraising success, operational stability) to validate predictive power.

5. **Peer review:** Submit the methodology for review by credit rating professionals, DAO governance researchers, and Network State founders.

6. **Integration with NSCF and NSEI:** Formalize the relationship between classification (NSCF), economic output (NSEI), and creditworthiness (NSCRF) into a unified analytical framework.

7. **Regulatory engagement:** Present the methodology to financial regulators (IOSCO, ESMA, SEC) to begin the conversation about whether Network State credit ratings should be subject to the same regulatory framework as traditional credit ratings.

8. **On-chain implementation:** Explore whether NSCRF ratings can be partially automated through on-chain data feeds, reducing the cost and increasing the frequency of ratings.

---

## APPENDIX A: PILLAR WEIGHT SENSITIVITY ANALYSIS

To demonstrate the impact of pillar weight choices, here are Network School's ratings under three alternative weighting schemes:

| Weighting Scheme | Treasury | Governance | Community | Infrastructure | External | CCS | Rating |
|---|---|---|---|---|---|---|---|
| **Base case** | 30% | 25% | 20% | 15% | 10% | 55.6 | NS-BB |
| **Community-weighted** | 20% | 20% | 30% | 15% | 15% | 58.6 | NS-BB |
| **Governance-weighted** | 25% | 30% | 20% | 15% | 10% | 53.1 | NS-BB |
| **Equal weight** | 20% | 20% | 20% | 20% | 20% | 51.8 | NS-BB |

Network School's rating is robust to weighting changes (remains NS-BB across all scenarios) because its weakness (governance) and strength (community) offset each other. An entity with more extreme variance across pillars would show greater rating sensitivity to weight changes.

---

## APPENDIX B: NSCRF SCORING WORKSHEET

**For use in rating a Network State. Complete each sub-factor, calculate pillar scores, then composite score.**

### Pillar 1: Treasury Health (Weight: 30%)

| Sub-factor | Sub-weight | Score (0-100) | Weighted Score |
|---|---|---|---|
| 1.1 Treasury size & per-member adequacy | 20% | _____ | _____ |
| 1.2 Treasury composition quality | 20% | _____ | _____ |
| 1.3 Burn rate & runway | 25% | _____ | _____ |
| 1.4 Revenue diversity & stability | 20% | _____ | _____ |
| 1.5 Revenue growth rate | 15% | _____ | _____ |
| **Pillar 1 Total** | **100%** | | **_____** |

### Pillar 2: Governance Quality (Weight: 25%)

| Sub-factor | Sub-weight | Score (0-100) | Weighted Score |
|---|---|---|---|
| 2.1 Governance model maturity | 25% | _____ | _____ |
| 2.2 Governance participation | 20% | _____ | _____ |
| 2.3 Transparency & reporting | 20% | _____ | _____ |
| 2.4 Governance attack surface | 20% | _____ | _____ |
| 2.5 Key person dependency | 15% | _____ | _____ |
| **Pillar 2 Total** | **100%** | | **_____** |

### Pillar 3: Community Resilience (Weight: 20%)

| Sub-factor | Sub-weight | Score (0-100) | Weighted Score |
|---|---|---|---|
| 3.1 Member retention rate | 30% | _____ | _____ |
| 3.2 Net migration & growth | 25% | _____ | _____ |
| 3.3 Member economic quality | 20% | _____ | _____ |
| 3.4 Diversity & distribution | 15% | _____ | _____ |
| 3.5 Cultural cohesion | 10% | _____ | _____ |
| **Pillar 3 Total** | **100%** | | **_____** |

### Pillar 4: Infrastructure Robustness (Weight: 15%)

| Sub-factor | Sub-weight | Score (0-100) | Weighted Score |
|---|---|---|---|
| 4.1 Digital infrastructure | 25% | _____ | _____ |
| 4.2 Physical infrastructure quality | 20% | _____ | _____ |
| 4.3 Legal structure robustness | 25% | _____ | _____ |
| 4.4 Smart contract & protocol security | 15% | _____ | _____ |
| 4.5 Host country relationship stability | 15% | _____ | _____ |
| **Pillar 4 Total** | **100%** | | **_____** |

### Pillar 5: External Risk (Weight: 10%)

| Sub-factor | Sub-weight | Score (0-100) | Weighted Score |
|---|---|---|---|
| 5.1 Crypto market correlation | 25% | _____ | _____ |
| 5.2 Regulatory risk | 25% | _____ | _____ |
| 5.3 Concentration risk | 25% | _____ | _____ |
| 5.4 Reputational & competitive risk | 15% | _____ | _____ |
| 5.5 Black swan vulnerability | 10% | _____ | _____ |
| **Pillar 5 Total** | **100%** | | **_____** |

### Composite Credit Score

| Pillar | Weight | Score | Weighted Score |
|---|---|---|---|
| Treasury Health | 30% | _____ | _____ |
| Governance Quality | 25% | _____ | _____ |
| Community Resilience | 20% | _____ | _____ |
| Infrastructure Robustness | 15% | _____ | _____ |
| External Risk | 10% | _____ | _____ |
| **Composite Credit Score (CCS)** | **100%** | | **_____** |

### Rating Assignment

| CCS Range | Rating |
|---|---|
| 90-100 | NS-AAA |
| 80-89 | NS-AA |
| 70-79 | NS-A |
| 60-69 | NS-BBB (Investment Grade Floor) |
| 50-59 | NS-BB |
| 40-49 | NS-B |
| 30-39 | NS-CCC |
| 20-29 | NS-CC |
| 10-19 | NS-C |
| 0-9 | NS-D |

**Assigned Rating:** _____
**Rating Outlook:** Positive / Stable / Negative / Developing
**Date:** _____
**Analyst:** _____
**Next Review:** _____

---

*This methodology is designed for academic and analytical purposes. It represents the author's independent research and does not constitute investment advice, a solicitation, or an offer to buy or sell any securities or digital assets.*

*Copyright 2026 Kathleen Maree Grey. All rights reserved.*

---

As at 5 April 2026
Network State Credit Rating Framework (NSCRF) v1.0
Companion paper to:
- Network State Classification Framework (NSCF) v1.0
- Network State Economic Index (NSEI) v1.0
- SEZ to Network States: Historical Continuum v1.0
