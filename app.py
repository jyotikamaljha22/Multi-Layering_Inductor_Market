import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Global Multilayer Inductor Market (2025–2035)",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# BRAND SYSTEM
# -----------------------------
BURGUNDY = "#5B0F2E"
BURGUNDY_DARK = "#431024"
BURGUNDY_LIGHT = "#7A163F"
BURGUNDY_SOFT = "#F7EEF2"
ROSE = "#E8C7D5"
INK = "#0F172A"
SLATE = "#475569"
SLATE_LIGHT = "#64748B"
BORDER = "#E5E7EB"
BG = "#F6F2F4"
WHITE = "#FFFFFF"

PRIMARY_PASSWORD = "SMR2026"
CLIENT_NAME = "TDK Corporation"

QUICK_METRICS = {
    "Market Revenue 2035": "$2,115.25Mn",
    "Global CAGR": "3.87%",
    "TDK 2025 Proxied": "$318.27Mn",
    "Premium Growth Vector": "Automotive",
}

# -----------------------------
# DATA / CONTENT
# -----------------------------
CHAPTERS = {
    "1. Executive Summary & Strategic Imperatives": r'''
<div class="chapter-content">
<h1>1. Executive Summary & Strategic Imperatives</h1>
<p>The global multilayer inductor market is defined by the integration of high-frequency impedance matching and compact power filtering requirements across modern electronic architectures. Demand drivers stem fundamentally from the increasing complexity of radio frequency front-end modules and the rapid densification of electronic control units within automotive platforms. The underlying economics strongly favor manufacturers possessing advanced ceramic processing capabilities, extreme miniaturization techniques, and the ability to secure stringent automotive qualifications.</p>
<p>The market demonstrates resilient structural expansion, driven primarily by technological sophistication rather than sheer unit volume growth in end-devices. Value creation is migrating rapidly toward specialized applications, requiring suppliers to strategically navigate the divide between commoditized consumer electronics components and high-value, premium automotive subassemblies. The long-term forecast indicates sustained resilience against macroeconomic volatility due to the mandatory nature of radio frequency matching and power filtering in connected ecosystems. Total addressable market trajectories reveal a definitive shift toward environments prioritizing extreme reliability and miniaturization over pure cost-reduction.</p>
<table>
    <thead>
        <tr>
            <th>Market Metric</th>
            <th>2025 Value</th>
            <th>2030 Value</th>
            <th>2035 Value</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Total Market Revenue ($Mn)</td>
            <td>$1,446.68</td>
            <td>$1,727.53</td>
            <td>$2,115.25</td>
            <td>3.87%</td>
        </tr>
        <tr>
            <td>Total Volume Demand (Bn units)</td>
            <td>85.39 Bn</td>
            <td>112.51 Bn</td>
            <td>146.40 Bn</td>
            <td>5.53%</td>
        </tr>
        <tr>
            <td>Blended Average Selling Price ($/unit)</td>
            <td>$0.0169</td>
            <td>$0.0153</td>
            <td>$0.0144</td>
            <td>-1.58%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The growth pattern illustrates steady value expansion outpacing volume growth in critical segments, underscoring a structural shift toward premium components. The steady decline in blended average selling prices is heavily masked by the rising mix of high-value automotive components, preventing a complete commoditization of the global revenue pool.</div>
<p>Strategically, the landscape requires leading manufacturers to pivot away from volume-chasing strategies and anchor their portfolios in high-barrier segments. Competitors heavily reliant on legacy consumer electronics face mounting margin compression, whereas entities securing design wins in automotive power-over-coax and premium radio frequency modules stand to capture disproportionate value. The market ultimately rewards those capable of maintaining stringent process controls at microscopic dimensions.</p>
<div class="insight-highlight">The transition toward automotive-qualified components redefines the multilayer inductor value pool, shifting dependency away from consumer electronics cycles and toward sustained mobility investments.</div>
</div>
''',
    "2. Global Market Definition & Scope": r'''
<div class="chapter-content">
<h1>2. Global Market Definition & Scope</h1>
<p>The multilayer inductor segment is strictly defined by components formed through the microscopic layering of ceramic or ferrite materials interwoven with conductive coil patterns. Demand drivers for this specific architecture are anchored in the need for extreme miniaturization and high-density mounting, which alternative structures cannot easily achieve at scale. The economics of this defined boundary separate multilayer variants from wire-wound or macroscopic molded power inductors, establishing a unique competitive arena governed by sintering yields and advanced photolithography adjacent processes.</p>
<p>The market demonstrates a clear technological demarcation based on underlying material science, segmenting heavily into high-frequency dielectric ceramic applications and lower-frequency ferrite applications. High-frequency variants are imperative for radio frequency matching where ferrite materials become excessively lossy above several hundred megahertz. Conversely, ferrite-based multilayer inductors dominate compact power filtering and near-field communication applications. The boundary analysis strictly excludes thin-film and wire-wound equivalents, isolating the true multilayer chip inductor revenue pool to ensure precise strategic benchmarking and realistic total addressable market calculations.</p>
<table>
    <thead>
        <tr>
            <th>Technology Category</th>
            <th>Core Functionality</th>
            <th>Primary Material Base</th>
            <th>Inclusion Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>High-Frequency Multilayer</td>
            <td>Impedance matching, RF resonance</td>
            <td>Dielectric Ceramic</td>
            <td>Included (Core)</td>
        </tr>
        <tr>
            <td>Compact Signal / Power Multilayer</td>
            <td>Noise filtering, power line chokes</td>
            <td>Ferrite</td>
            <td>Included (Core)</td>
        </tr>
        <tr>
            <td>Thin-Film Inductors</td>
            <td>Ultra-high precision RF</td>
            <td>Photolithography / Ferrite</td>
            <td>Excluded (Adjacent)</td>
        </tr>
        <tr>
            <td>Wire-Wound Inductors</td>
            <td>High current, high Q-factor</td>
            <td>Wire over core</td>
            <td>Excluded (Substitute)</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The segmentation pattern establishes rigid boundaries necessary for accurate market sizing, isolating the specific capabilities required to compete in the multilayer arena. The explicit exclusion of adjacent technologies prevents the artificial inflation of the addressable market and clarifies the true competitive intensity within the ceramic chip ecosystem.</div>
<p>Strategically, this indicates that participation requires distinct material competencies that cannot be easily bridged by manufacturers operating exclusively in larger, wire-wound form factors. The market dictates that success in the radio frequency tier mandates mastery over ceramic dielectric properties, while success in power filtering necessitates advanced ferrite integration capabilities. This dual-material mandate acts as a natural barrier to entry, insulating top-tier incumbents from lower-cost manufacturers lacking integrated material development platforms.</p>
<div class="insight-highlight">The strict bifurcation between dielectric ceramic for radio frequency applications and ferrite for filtering prevents monolithic, one-size-fits-all manufacturing strategies from succeeding at a global scale.</div>
</div>
''',
    "3. Total Addressable Market (TAM) & Growth Forecast (2025–2035)": r'''
<div class="chapter-content">
<h1>3. Total Addressable Market (TAM) & Growth Forecast (2025–2035)</h1>
<p>The total addressable market for multilayer inductors reflects the aggregate value generated across all discrete device integrations requiring microscopic inductive components. Demand is driven by a combination of massive baseline volumes in consumer hardware and the exponential multiplication of content-per-device in premium mobility sectors. The economics of the total market rely on securing massive production scale to absorb capital expenditures while simultaneously advancing the technological frontier to capture high-margin early adoption cycles.</p>
<p>The market demonstrates a robust expansion from $1,446.68 million in 2025 to $2,115.25 million by 2035, securing a steady compound annual growth rate that defies the maturation of underlying hardware categories. This growth trajectory is sustained not by surging smartphone shipments, but by the relentless densification of electronic components within a relatively stable hardware base. The forecast highlights a fundamental decoupling of component demand from device shipments, as architectural complexities in connectivity and power management outpace end-user equipment sales. The aggregate revenue pool reflects a highly resilient industrial complex capable of weathering cyclical consumer downturns through specialized automotive and industrial growth vectors.</p>
<table>
    <thead>
        <tr>
            <th>Market Metric</th>
            <th>2025 Value</th>
            <th>2030 Value</th>
            <th>2035 Value</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Total Addressable Market ($Mn)</td>
            <td>$1,446.68 (100.0%)</td>
            <td>$1,727.53 (100.0%)</td>
            <td>$2,115.25 (100.0%)</td>
            <td>3.87%</td>
        </tr>
        <tr>
            <td>Total Device Anchors (Mn units)</td>
            <td>5,108.50 Mn</td>
            <td>6,518.08 Mn</td>
            <td>8,389.83 Mn</td>
            <td>5.07%</td>
        </tr>
        <tr>
            <td>Average Components per Device</td>
            <td>16.7 units</td>
            <td>17.2 units</td>
            <td>17.4 units</td>
            <td>0.41%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The growth pattern illustrates that overall revenue expansion is heavily predicated on volume scaling and content density improvements rather than price appreciation. The steady compound annual growth rate underscores a highly dependable, non-volatile market expansion that serves as a reliable anchor for long-term corporate manufacturing investments.</div>
<p>Strategically, this indicates that scale remains a prerequisite for baseline survival, but not a guarantee of premium profitability. The expanding addressable market demands aggressive capital allocation toward next-generation production lines to merely maintain current market share positions over the next decade. Competitors failing to match the baseline 3.8% market expansion rate will experience rapid dilution of their strategic relevance and a corresponding erosion of their pricing power across all major device categories.</p>
<div class="insight-highlight">Total market expansion is decoupled from consumer device shipment volumes, driven entirely by the architectural densification of radio frequency and power sub-systems.</div>
</div>
''',
    "4. Market Segmentation & Value Pools": r'''
<div class="chapter-content">
<h1>4. Market Segmentation & Value Pools</h1>
<p>The segmentation of the multilayer inductor market defines the internal distribution of profit pools and strategic battlegrounds. Demand drivers vary drastically across segments, with radio frequency variants tethered to wireless standards and automotive variants tied to electrification and autonomy mandates. The economics of segmentation reveal a stark divergence in average selling prices, where the value density of automotive-qualified components fundamentally eclipses the commoditized reality of standard compact ferrite filters.</p>
<p>The market demonstrates a commanding lead for radio frequency applications, which constitute the majority of revenue due to the extreme volume requirements of modern communication modules. However, the compact ferrite segment plays a critical role in defending manufacturing scale, absorbing fixed costs across vast consumer electronics portfolios. Automotive-qualified inductors represent the most critical strategic vector, operating from a smaller baseline but exhibiting growth rates that systematically cannibalize the relative share of consumer segments. The value pools within these categories require entirely divergent commercial strategies, engineering roadmaps, and customer engagement models.</p>
<table>
    <thead>
        <tr>
            <th>Segment Category</th>
            <th>2025 Revenue ($Mn)</th>
            <th>2030 Revenue ($Mn)</th>
            <th>2035 Revenue ($Mn)</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Radio Frequency (RF)</td>
            <td>$839.12 (58.0%)</td>
            <td>$973.82 (56.3%)</td>
            <td>$1,143.43 (54.0%)</td>
            <td>3.14%</td>
        </tr>
        <tr>
            <td>Compact Ferrite / NFC</td>
            <td>$474.80 (32.8%)</td>
            <td>$560.10 (32.4%)</td>
            <td>$672.21 (31.7%)</td>
            <td>3.53%</td>
        </tr>
        <tr>
            <td>Automotive-Qualified</td>
            <td>$132.75 (9.1%)</td>
            <td>$193.61 (11.2%)</td>
            <td>$299.60 (14.1%)</td>
            <td>8.48%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The segment evolution highlights a rapid structural rotation toward automotive dominance, with its relative revenue share expanding by five full percentage points over the decade. The radio frequency segment, while maintaining absolute dominance in total dollars, experiences a steady dilution in proportions as end-markets mature.</div>
<p>Strategically, this indicates that defending market share in the radio frequency segment is necessary to preserve absolute scale, but expanding aggressively into automotive applications is required to secure margin expansion. A portfolio overly concentrated in compact ferrite applications risks severe exposure to commoditization and aggressive pricing pressure from regional challengers. Long-term value capture requires continuous recalibration of capacity toward the high-growth, high-barrier automotive and specialized tiers.</p>
<div class="insight-highlight">The automotive-qualified segment operates as the ultimate margin multiplier, growing at more than double the rate of the broader multilayer inductor ecosystem.</div>
</div>
''',
    "5. Demand Engine: Device-Level Volume Modelling": r'''
<div class="chapter-content">
<h1>5. Demand Engine: Device-Level Volume Modelling</h1>
<p>The device-level demand engine quantifies the physical hardware shipments that pull multilayer inductors through the global supply chain. Demand is driven by an underlying base of billions of consumer endpoints, heavily augmented by emerging platforms operating at lower volumes but substantially higher component densities. The economics of device-level modelling dictate that absolute component demand is highly sensitive to minor fractional changes in attach rates within mega-volume categories such as smartphones and internet-of-things edge modules.</p>
<p>The market demonstrates that smartphones remain the indisputable anchor of global volume, shipping over 1.2 billion units annually and commanding the vast majority of physical component flow. However, emerging device categories exhibit superior shipment trajectories, with smartwatches and earwear expanding significantly faster than traditional handsets. Electric vehicle shipments, while representing a fraction of consumer electronics volumes, generate outsized component demand due to massively elevated content-per-vehicle metrics. Internet-of-things edge modules represent the ultimate long-tail volume driver, scaling rapidly as cellular connectivity penetrates industrial and environmental monitoring ecosystems.</p>
<table>
    <thead>
        <tr>
            <th>End-Device Category</th>
            <th>2025 Volume (Mn)</th>
            <th>2030 Volume (Mn)</th>
            <th>2035 Volume (Mn)</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Smartphones</td>
            <td>1,240.00 Mn (24.2%)</td>
            <td>1,316.20 Mn (20.1%)</td>
            <td>1,397.09 Mn (16.6%)</td>
            <td>1.20%</td>
        </tr>
        <tr>
            <td>Earwear / TWS</td>
            <td>360.00 Mn (7.0%)</td>
            <td>437.99 Mn (6.7%)</td>
            <td>532.88 Mn (6.3%)</td>
            <td>4.00%</td>
        </tr>
        <tr>
            <td>Smartwatches</td>
            <td>206.00 Mn (4.0%)</td>
            <td>262.88 Mn (4.0%)</td>
            <td>335.55 Mn (4.0%)</td>
            <td>5.00%</td>
        </tr>
        <tr>
            <td>Electric Vehicles (EVs)</td>
            <td>25.00 Mn (0.4%)</td>
            <td>39.00 Mn (0.5%)</td>
            <td>61.95 Mn (0.7%)</td>
            <td>9.51%</td>
        </tr>
        <tr>
            <td>ICE / HEV Vehicles</td>
            <td>67.50 Mn (1.3%)</td>
            <td>62.00 Mn (0.9%)</td>
            <td>56.28 Mn (0.6%)</td>
            <td>-1.80%</td>
        </tr>
        <tr>
            <td>IoT Edge Modules</td>
            <td>3,200.00 Mn (62.6%)</td>
            <td>4,400.00 Mn (67.5%)</td>
            <td>6,006.83 Mn (71.5%)</td>
            <td>6.50%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The device shipment profile underscores a rapid transition toward a highly distributed internet-of-things ecosystem, which systematically marginalizes the volumetric dominance of smartphones. The aggressive contraction of legacy combustion vehicles acts as a structural drag on broader automotive shipments, entirely offset by exponential electric vehicle adoption.</div>
<p>Strategically, this indicates that manufacturing supply chains must optimize for two completely divergent realities: extreme scale commodity supply for internet-of-things modules, and highly customized, rigorous supply for electric vehicles. Over-indexing commercial focus on smartphone shipments represents a strategic error, as growth entirely evaporates from that sector over the forecast period. Capturing the device-level demand engine requires a deeply bifurcated approach, prioritizing volume flexibility and extreme reliability simultaneously.</p>
<div class="insight-highlight">The volume anchor of the market permanently shifts from human-operated mobile devices toward distributed internet-of-things endpoints and autonomous mobility systems.</div>
</div>
''',
    "6. Application & Use-Case Expansion": r'''
<div class="chapter-content">
<h1>6. Application & Use-Case Expansion</h1>
<p>The application layer delineates how multilayer inductors are functionally deployed across complex electronic architectures, moving beyond simple device counts. Demand is driven by the internal densification of sub-systems, specifically radio frequency front-end modules, power management integrated circuits, and advanced driver assistance networks. The economics of use-case expansion allow manufacturers to capture higher value per device by securing design wins in performance-critical circuits where component failure leads to catastrophic system degradation.</p>
<p>The market demonstrates an intense proliferation of specialized applications, most notably within fifth-generation wireless environments where multiple inductors are required for precise impedance matching across vast frequency bands. The transition toward high-resolution automotive camera systems establishes a critical new use-case, demanding specialized inductors to manage power-over-coax transmission lines without corrupting high-speed video data. Near-field communication integrations represent another high-value expansion, pulling compact ferrite variants into wearable and mobile environments requiring secure, short-range coupling. These use-cases transform the component from a generic passive element into a critical system-enabling asset.</p>
<table>
    <thead>
        <tr>
            <th>Application Architecture</th>
            <th>Associated Device</th>
            <th>Functional Role</th>
            <th>Strategic Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>RF Front-End Matching</td>
            <td>5G Smartphones / Modules</td>
            <td>High-frequency impedance matching</td>
            <td>Volume Anchor</td>
        </tr>
        <tr>
            <td>Power-over-Coax (PoC)</td>
            <td>ADAS / In-Vehicle Networks</td>
            <td>Power / Signal isolation</td>
            <td>Premium Margin</td>
        </tr>
        <tr>
            <td>NFC Coupling</td>
            <td>Wearables / Mobile</td>
            <td>Short-range resonance</td>
            <td>Niche Defender</td>
        </tr>
        <tr>
            <td>PMIC Decoupling</td>
            <td>IoT / General Electronics</td>
            <td>Noise filtration</td>
            <td>Scale Defender</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The functional deployment matrix reveals that the highest strategic value is concentrated in applications requiring complex signal preservation, notably in automotive and advanced radio frequency architectures. Commoditized filtering applications serve purely as scale defenders, lacking the technical barriers required to sustain premium pricing.</div>
<p>Strategically, this indicates that commercial engineering teams must pivot from component-level selling toward module-level co-design, embedding products into the reference architectures of core semiconductor manufacturers. By aligning product development directly with the architectural roadmaps of power management and communication chipsets, manufacturers secure lock-in ahead of the broader market. Failure to align with emerging use-cases results in relegation to secondary, price-driven procurement channels.</p>
<div class="insight-highlight">Value capture relies entirely on penetrating highly complex sub-assemblies, transitioning the component from an interchangeable commodity to an application-specific enabler.</div>
</div>
''',
    "7. Pricing Dynamics & Value Realization": r'''
<div class="chapter-content">
<h1>7. Pricing Dynamics & Value Realization</h1>
<p>The pricing environment for multilayer inductors reflects a complex interplay between aggressive technological miniaturization and relentless commercial commoditization. Demand drivers naturally enforce continuous cost-down trajectories from original equipment manufacturers, forcing component providers to constantly innovate to maintain margin parity. The economics of value realization demand the continuous introduction of smaller, higher-performance form factors to offset the systemic price decay inherent to mature electronic components.</p>
<p>The market demonstrates persistent baseline price erosion across all major segments, acting as a structural headwind against top-line revenue expansion. The radio frequency segment faces moderate deflation as production yields for standard formats stabilize, while the compact ferrite segment endures heavier pressure from highly scaled regional competitors. Automotive-qualified components maintain the highest average selling prices, supported by stringent certification requirements and severe liability implications that deter aggressive cost-cutting. Blended value realization is ultimately protected by the shifting mix, as higher-priced automotive and advanced miniaturized components counterbalance the commoditization of legacy parts.</p>
<table>
    <thead>
        <tr>
            <th>Segment Category</th>
            <th>2025 ASP ($/unit)</th>
            <th>2030 ASP ($/unit)</th>
            <th>2035 ASP ($/unit)</th>
            <th>Pricing CAGR (2025-35)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Radio Frequency (RF)</td>
            <td>$0.0220</td>
            <td>$0.0215</td>
            <td>$0.0210</td>
            <td>-0.46%</td>
        </tr>
        <tr>
            <td>Compact Ferrite / NFC</td>
            <td>$0.0135</td>
            <td>$0.0130</td>
            <td>$0.0125</td>
            <td>-0.76%</td>
        </tr>
        <tr>
            <td>Automotive-Qualified</td>
            <td>$0.0350</td>
            <td>$0.0340</td>
            <td>$0.0330</td>
            <td>-0.58%</td>
        </tr>
        <tr>
            <td><strong>Blended Device Metric (Smartphone)</strong></td>
            <td><strong>$0.0186</strong></td>
            <td><strong>$0.0181</strong></td>
            <td><strong>$0.0176</strong></td>
            <td><strong>-0.55%</strong></td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The pricing trajectory confirms a universal deflationary environment, albeit at a highly controlled rate reflective of established oligopolistic manufacturing dynamics. Automotive components command a premium nearly triple that of compact ferrite equivalents, highlighting the extreme value of environmental and reliability certifications.</div>
<p>Strategically, this indicates that revenue growth models dependent solely on price stability are structurally flawed and destined to underperform. Sustained profitability requires the ruthless optimization of legacy production lines to match falling prices, coupled with aggressive capital diversion toward the premium automotive tier. Manufacturers unable to execute simultaneous cost-leadership in legacy formats and differentiation in premium formats will experience rapid margin compression.</p>
<div class="insight-highlight">Systemic price decay acts as an inescapable gravitational pull, navigable only by continuously shifting the portfolio mix toward reliability-critical automotive and ultra-miniaturized applications.</div>
</div>
''',
    "8. Regional Market Analysis: North America": r'''
<div class="chapter-content">
<h1>8. Regional Market Analysis: North America</h1>
<p>The North American multilayer inductor market operates as a preeminent hub for advanced architectural design and premium electronics consumption, despite lacking dominant domestic component production. Demand is driven by the world's most lucrative technology ecosystem, directing vast quantities of components into high-end smartphones, advanced wearable systems, and electric vehicle innovation centers. The economics of the region heavily leverage premium content factors, ensuring that devices consumed within this geography harbor significantly richer component bills of materials than global averages.</p>
<p>The market demonstrates robust revenue expansion within the United States, anchored by sustained consumption of premium-tier mobility hardware and heavy investments in autonomous automotive systems. While physical component manufacturing is largely off-shored, the engineering specification and procurement authority localized in California and Texas strictly dictate global supply chain behaviors. The regional value pool exhibits an outsized concentration in radio frequency variants, supporting the dense broadband infrastructure and complex cellular architectures demanded by North American carriers. Electric vehicle assembly networks in the region further establish a rapidly growing, high-margin consumption base insulated from pure consumer electronics cycles.</p>
<table>
    <thead>
        <tr>
            <th>Country / Sub-Region</th>
            <th>2025 Revenue ($Mn)</th>
            <th>2030 Revenue ($Mn)</th>
            <th>2035 Revenue ($Mn)</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>United States</td>
            <td>$146.58 (10.1%)</td>
            <td>$177.30 (10.2%)</td>
            <td>$214.83 (10.1%)</td>
            <td>3.89%</td>
        </tr>
        <tr>
            <td>Mexico (Production Hub)</td>
            <td>$17.68 (1.2%)</td>
            <td>$21.41 (1.2%)</td>
            <td>$25.91 (1.2%)</td>
            <td>3.89%</td>
        </tr>
        <tr>
            <td>Canada / Rest of NA</td>
            <td>$22.40 (1.5%)</td>
            <td>$26.10 (1.5%)</td>
            <td>$31.10 (1.4%)</td>
            <td>3.33%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The geographic concentration highlights the United States as an indispensable pillar of premium component demand, maintaining a rigid proportional share of the global market over the decade. Mexico operates distinctly as a near-shored production conduit, capturing manufacturing volume directly responsive to United States end-market demand.</div>
<p>Strategically, this indicates that securing design wins within North American corporate ecosystems is mandatory for dictating global production volumes, regardless of where physical assembly occurs. Manufacturers must maintain high-touch application engineering teams situated proximate to major technology campuses to influence early-stage reference designs. Relying solely on Asian manufacturing channels without establishing deep technical authority in North America relinquishes control over the highest-margin product lifecycles.</p>
<div class="insight-highlight">North America exerts a gravitational influence over global component specifications, acting as the primary theater for securing premium radio frequency and automotive design wins.</div>
</div>
''',
    "9. Regional Market Analysis: Europe": r'''
<div class="chapter-content">
<h1>9. Regional Market Analysis: Europe</h1>
<p>The European multilayer inductor market is defined by unparalleled rigor in industrial automation standards and a globally dominant, legacy-rich automotive manufacturing complex. Demand is driven unequivocally by the systematic transition of the European mobility sector toward full electrification and the dense integration of advanced driver assistance systems. The economics of the region prioritize extreme reliability, environmental compliance, and secure supply chain sourcing over aggressive short-term cost reduction, creating a highly stable value pool.</p>
<p>The market demonstrates sustained, highly profitable expansion anchored primarily in Germany, which acts as the gravitational center for continental automotive component specification. European demand profiles skew heavily toward the automotive-qualified segment, contrasting sharply with the consumer-electronics dominance observed in Asian markets. The regulatory environment surrounding emissions and vehicle safety features structurally mandates the inclusion of complex power-over-coax and premium radio frequency architectures within the European fleet. This environment structurally favors incumbent Japanese component manufacturers that possess proven decades-long track records of zero-defect quality systems.</p>
<table>
    <thead>
        <tr>
            <th>Country / Sub-Region</th>
            <th>2025 Revenue ($Mn)</th>
            <th>2030 Revenue ($Mn)</th>
            <th>2035 Revenue ($Mn)</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Germany</td>
            <td>$41.97 (2.9%)</td>
            <td>$52.54 (3.0%)</td>
            <td>$65.75 (3.1%)</td>
            <td>4.59%</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td>$18.10 (1.2%)</td>
            <td>$21.40 (1.2%)</td>
            <td>$25.80 (1.2%)</td>
            <td>3.61%</td>
        </tr>
        <tr>
            <td>France & Italy</td>
            <td>$26.40 (1.8%)</td>
            <td>$31.20 (1.8%)</td>
            <td>$37.90 (1.7%)</td>
            <td>3.68%</td>
        </tr>
        <tr>
            <td>Eastern Europe (Assembly)</td>
            <td>$14.20 (0.9%)</td>
            <td>$17.80 (1.0%)</td>
            <td>$22.50 (1.0%)</td>
            <td>4.71%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The regional architecture displays Germany commanding the highest growth trajectory among mature economies, entirely propelled by its electric vehicle transition. Eastern European zones exhibit adjacent high-growth metrics as automotive manufacturing and industrial assembly operations systematically migrate eastward seeking cost optimization within the trading bloc.</div>
<p>Strategically, this indicates that defending market share in Europe requires an uncompromising commitment to automotive quality standards and localized engineering support. Component manufacturers must align their product roadmaps intimately with the multi-year development cycles of European Tier-1 automotive suppliers, securing integration into core vehicle platforms well ahead of production. Failure to maintain zero-defect credentials or achieve necessary AEC-Q200 qualifications immediately disqualifies suppliers from participating in the region's most lucrative growth vector.</p>
<div class="insight-highlight">European market dynamics operate structurally independent of consumer electronics volatility, establishing a fortress environment for high-margin, automotive-qualified component supply.</div>
</div>
''',
    "10. Regional Market Analysis: Asia Pacific (Ex-Japan) & Japan": r'''
<div class="chapter-content">
<h1>10. Regional Market Analysis: Asia Pacific (Ex-Japan) & Japan</h1>
<p>The Asia Pacific landscape dictates the global equilibrium of the multilayer inductor market, housing the absolute majority of physical component production and device assembly. Demand is driven by the colossal, integrated Chinese consumer electronics machine and the rapidly advancing technological infrastructure across the broader Asian continent. The economics are deeply bifurcated, contrasting Japan's role as the elite technological progenitor against China's role as the unparalleled master of manufacturing scale and domestic consumption.</p>
<p>The market demonstrates overwhelming revenue dominance by China, which alone accounts for over a quarter of the global value pool and serves as both the primary assembly hub and a massive end-market. Japan maintains critical strategic relevance not through volume, but through its operation as a mother-factory ecosystem, driving miniaturization techniques and premium material science. India emerges as the breakout growth vector, accelerating rapidly as smartphone assembly and industrial modernization policies take root. Taiwan and South Korea maintain formidable positions as centers of excellence for compact component manufacturing, enforcing intense regional pricing pressure and technological competition.</p>
<table>
    <thead>
        <tr>
            <th>Country / Sub-Region</th>
            <th>2025 Revenue ($Mn)</th>
            <th>2030 Revenue ($Mn)</th>
            <th>2035 Revenue ($Mn)</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>China</td>
            <td>$398.24 (27.5%)</td>
            <td>$470.83 (27.2%)</td>
            <td>$559.87 (26.4%)</td>
            <td>3.46%</td>
        </tr>
        <tr>
            <td>India</td>
            <td>$124.96 (8.6%)</td>
            <td>$180.37 (10.4%)</td>
            <td>$253.32 (11.9%)</td>
            <td>7.31%</td>
        </tr>
        <tr>
            <td>Japan</td>
            <td>$51.70 (3.5%)</td>
            <td>$61.35 (3.5%)</td>
            <td>$72.97 (3.4%)</td>
            <td>3.50%</td>
        </tr>
        <tr>
            <td>South Korea</td>
            <td>$32.54 (2.2%)</td>
            <td>$38.16 (2.2%)</td>
            <td>$44.80 (2.1%)</td>
            <td>3.25%</td>
        </tr>
        <tr>
            <td>Taiwan</td>
            <td>$8.45 (0.5%)</td>
            <td>$10.03 (0.5%)</td>
            <td>$11.89 (0.5%)</td>
            <td>3.47%</td>
        </tr>
        <tr>
            <td>Vietnam</td>
            <td>$17.15 (1.1%)</td>
            <td>$21.90 (1.2%)</td>
            <td>$27.98 (1.3%)</td>
            <td>5.02%</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The regional trajectories reveal a significant redistribution of volume growth toward India and Vietnam, reflecting a systemic geopolitical derisking of the global supply chain away from monolithic Chinese concentration. Despite this dispersion, China's absolute revenue scale remains unassailable, ensuring its position as the ultimate battleground for component volume and aggressive cost competitiveness.</div>
<p>Strategically, this indicates that navigating the Asian theater requires a highly nuanced localization strategy, defending premium technology nodes in Japan while aggressively matching cost structures in China. Manufacturers must establish dual-track operations, insulating advanced research and development within Japanese and Korean strongholds while expanding footprint flexibility across Southeast Asia. Underestimating the technical ascent of domestic Chinese manufacturers within this region invites rapid market share erosion across all but the most specialized, high-barrier automotive segments.</p>
<div class="insight-highlight">The gravitational center of global electronics volume remains deeply entrenched in Asia, but the structural layout shifts rapidly toward a decentralized, China-plus-one manufacturing paradigm.</div>
</div>
''',
    "11. Competitive Landscape & Market Share": r'''
<div class="chapter-content">
<h1>11. Competitive Landscape & Market Share</h1>
<p>The competitive landscape of the multilayer inductor market operates as an established oligopoly, dominated by a concentrated cadre of Japanese and Korean technology conglomerates facing aggressive insurgencies from highly capitalized Chinese and Taiwanese challengers. Demand is captured by entities demonstrating proven scale, absolute reliability, and the financial endurance to fund continuous miniaturization capital expenditures. The economics strongly favor incumbents possessing integrated material science platforms, creating substantial barriers against pure assembly-oriented entrants lacking internal ceramic formulation capabilities.</p>
<p>The market demonstrates the enduring supremacy of Japanese manufacturers, with Murata and TDK collectively commanding over half of the global revenue pool. This dominance is heavily predicated on their monopolization of the ultra-miniaturized radio frequency segment and the highly lucrative automotive-qualified tier. Samsung Electro-Mechanics occupies a formidable position as a scale competitor wielding significant leverage across compact consumer and standard automotive arenas. Conversely, entities such as Sunlord and YAGEO exhibit aggressive share capture trajectories, utilizing localized advantages, aggressive pricing strategies, and immense domestic scale to relentlessly compress the margins of legacy Japanese manufacturers in commoditized formats.</p>
<table>
    <thead>
        <tr>
            <th>Primary Competitor</th>
            <th>2025 Market Share (%)</th>
            <th>2025 Proxied Revenue ($Mn)</th>
            <th>2035 Market Share (%)</th>
            <th>Strategic Trajectory</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Murata</td>
            <td>31.0%</td>
            <td>$448.47 Mn</td>
            <td>28.0%</td>
            <td>Defend Premium Core</td>
        </tr>
        <tr>
            <td>TDK Corporation</td>
            <td>22.0%</td>
            <td>$318.27 Mn</td>
            <td>21.0%</td>
            <td>Expand Automotive Niche</td>
        </tr>
        <tr>
            <td>Samsung Electro-Mechanics</td>
            <td>9.0%</td>
            <td>$130.20 Mn</td>
            <td>10.0%</td>
            <td>Scale Consumer & Auto</td>
        </tr>
        <tr>
            <td>Taiyo Yuden</td>
            <td>8.0%</td>
            <td>$115.73 Mn</td>
            <td>8.0%</td>
            <td>Defend High-Reliability</td>
        </tr>
        <tr>
            <td>Sunlord</td>
            <td>7.0%</td>
            <td>$101.26 Mn</td>
            <td>10.0%</td>
            <td>Aggressive Localization</td>
        </tr>
        <tr>
            <td>YAGEO / Chilisin</td>
            <td>6.0%</td>
            <td>$86.80 Mn</td>
            <td>8.0%</td>
            <td>Consolidate & Scale</td>
        </tr>
        <tr>
            <td>TAI-TECH</td>
            <td>3.0%</td>
            <td>$43.40 Mn</td>
            <td>3.0%</td>
            <td>Maintain Regional Niche</td>
        </tr>
        <tr>
            <td>Others (Fragmented)</td>
            <td>14.0%</td>
            <td>$202.53 Mn</td>
            <td>12.0%</td>
            <td>Consolidation Risk</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The structural evolution of market share indicates a systematic dilution of Japanese dominance, as domestic Chinese champions capture the baseline volume growth of the massive Asian consumer apparatus. The consolidation of the "Others" category signals an increasingly hostile environment for sub-scale manufacturers unable to fund the transition toward automotive standards and extreme miniaturization.</div>
<p>Strategically, this indicates that top-tier incumbents cannot rely on scale alone to defend their positions against rapidly accelerating regional adversaries. Preserving market share requires the intentional abandonment of highly commoditized, low-barrier product lines in favor of aggressive expansion into specialized formats where challengers lack material science credibility. Success dictates operating the portfolio with extreme duality: matching the cost efficiency of Taiwanese manufacturers on legacy lines while aggressively distancing from them via sub-millimeter automotive innovation.</p>
<div class="insight-highlight">The oligopoly structure remains intact, but the base of the pyramid is systematically surrendering to aggressively capitalized, localization-driven challengers from the greater China ecosystem.</div>
</div>
''',
    "12. Competitor Benchmarking: Deep Dive Profiles": r'''
<div class="chapter-content">
<h1>12. Competitor Benchmarking: Deep Dive Profiles</h1>
<p>The benchmarking analysis decomposes the strategic posture, technological capability, and operational footprint of the foremost entities operating within the multilayer inductor arena. Demand capture profiles range from entities utilizing complete vertical integration of material science to those leveraging massive capacity footprints and horizontal portfolio breadth. The economics of benchmarking reveal that true competitive separation is achieved exclusively through the mastery of proprietary ceramic sintering techniques and successful penetration of global automotive qualification regimes.</p>
<p>The market demonstrates distinct archetypes among the leadership cohort. Murata acts as the undeniable premium benchmark, dictating the frontier of extreme miniaturization (01005 formats) and dominating high-Q radio frequency integrations. TDK operates as the comprehensive broad-spectrum powerhouse, wielding immense automotive relevance through highly specialized applications like power-over-coax components alongside robust consumer filtering architectures. Conversely, Sunlord exemplifies the aggressive localization archetype, weaponizing its immense domestic footprint and sophisticated central laboratories to systematically displace foreign suppliers within the expansive Chinese communications infrastructure.</p>
<table>
    <thead>
        <tr>
            <th>Competitor</th>
            <th>RF / High-Freq Competence</th>
            <th>Miniaturization Frontier</th>
            <th>Auto Qualification (AEC-Q200)</th>
            <th>China Localization Scale</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Murata</td>
            <td>Very High</td>
            <td>High (01005 leadership)</td>
            <td>High</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>TDK Corporation</td>
            <td>High</td>
            <td>High</td>
            <td>High</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>Taiyo Yuden</td>
            <td>Medium</td>
            <td>High</td>
            <td>High</td>
            <td>Low</td>
        </tr>
        <tr>
            <td>Samsung E-M</td>
            <td>Medium</td>
            <td>Medium</td>
            <td>High</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>Sunlord</td>
            <td>Medium</td>
            <td>Medium</td>
            <td>Medium</td>
            <td>High</td>
        </tr>
        <tr>
            <td>YAGEO / Chilisin</td>
            <td>Medium</td>
            <td>Medium</td>
            <td>Medium</td>
            <td>High</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The capability matrix explicitly maps the technological chasm separating top-tier Japanese innovators from scale-oriented regional challengers, particularly concerning the miniaturization frontier. However, the matrix also highlights the severe localization advantage possessed by domestic Chinese entities, representing a critical systemic threat to foreign incumbents within the world's largest volume market.</div>
<p>Strategically, this indicates that head-to-head competition across all metrics is functionally impossible, requiring manufacturers to lean heavily into their archetypal strengths. TDK must ruthlessly exploit its breadth and automotive credibility to secure deeply integrated module wins, neutralizing the aggressive pricing tactics of Sunlord and YAGEO. Meanwhile, the persistent technological thrust of Murata requires TDK to continuously invest in its fundamental material science capabilities to prevent the commoditization of its own premium radio frequency portfolio.</p>
<div class="insight-highlight">Competitive survival dictates acknowledging that technological superiority in Japan does not automatically translate to commercial defense against aggressive footprint localization in China.</div>
</div>
''',
    "13. Customer & OEM Concentration": r'''
<div class="chapter-content">
<h1>13. Customer & OEM Concentration</h1>
<p>The customer ecosystem governing the multilayer inductor market is characterized by extreme consolidation among a highly select cohort of original equipment manufacturers and tier-one automotive suppliers. Demand is dictated by the architectural roadmaps forged within the campuses of dominant smartphone brands, major semiconductor foundries, and legacy European automotive conglomerates. The economics of customer engagement mandate massive upfront engineering investments to secure placement on reference designs, yielding massive volume lock-ins that sustain factory utilization for years.</p>
<p>The market demonstrates that commercial power is highly asymmetric, concentrated heavily among top-tier consumer electronics giants whose procurement decisions instantly validate or obsolete massive tranches of component capacity. However, the structural rise of electric vehicles introduces a powerful counterbalance, elevating the purchasing authority of automotive tier-one module builders. This bifurcation forces component manufacturers to support wildly different customer profiles: smartphone brands demanding absolute lowest-cost commodity availability, versus automotive integrators demanding zero-defect traceability and comprehensive lifecycle support.</p>
<table>
    <thead>
        <tr>
            <th>Customer Category</th>
            <th>Procurement Priority</th>
            <th>Volume Profile</th>
            <th>Margin Profile</th>
            <th>Strategic Lock-in</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Smartphone OEMs (Top 5)</td>
            <td>Extreme scale, cost-down</td>
            <td>Massive, highly cyclical</td>
            <td>Low / Commoditized</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>RF Module / PMIC Integrators</td>
            <td>Size reduction, impedance precision</td>
            <td>High</td>
            <td>Medium-High</td>
            <td>High (Reference Design)</td>
        </tr>
        <tr>
            <td>Automotive Tier-1s</td>
            <td>AEC-Q200, zero-defect quality</td>
            <td>Moderate, stable growth</td>
            <td>High / Premium</td>
            <td>Very High</td>
        </tr>
        <tr>
            <td>IoT Device Integrators</td>
            <td>Standardized availability, scale</td>
            <td>Highly fragmented</td>
            <td>Low</td>
            <td>Low</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The customer topology reveals that margin capture is fundamentally inversely correlated with sheer device volume, exposing the hazard of over-indexing on smartphone procurement cycles. Penetrating the rigid supply networks of automotive tier-one suppliers offers the ultimate defensive perimeter against the extreme pricing pressure wielded by consolidated consumer electronics giants.</div>
<p>Strategically, this indicates that commercial organizations must completely bifurcate their sales and application engineering strategies based on the target customer architecture. Securing high-margin automotive business requires patient, multi-year engineering engagements embedded deeply within the customer's design lifecycle. Conversely, maintaining consumer volume requires aggressive distribution management and relentless capacity optimization to survive the brutal procurement practices characteristic of the consolidated mobile device sector.</p>
<div class="insight-highlight">The true arbiter of market value is no longer the final device manufacturer, but the specialized module integrator constructing the complex radio frequency and power architectures operating within the device.</div>
</div>
''',
    "14. Trade, Import–Export & Tariff Analysis": r'''
<div class="chapter-content">
<h1>14. Trade, Import–Export & Tariff Analysis</h1>
<p>The global trade environment surrounding passive electronic components acts as a critical external variable, manipulating physical supply routes and severely distorting baseline component economics. Demand distribution is fundamentally altered by geopolitical trade restrictions, tariff volatility, and aggressive nationalistic policies favoring domestic semiconductor supply chains. The economics of production footprint strategy are no longer dictated solely by labor arbitrage, but by the necessity of constructing tariff-resilient manufacturing networks capable of bypassing localized trade barriers.</p>
<p>The market demonstrates high sensitivity to macroeconomic trade volatility, heavily impacting the massive trans-Pacific flow of technology hardware. The structural reality of the market dictates that while end-demand is globally distributed, physical component production remains hyper-concentrated in East Asia. The persistent threat of tariff impositions accelerates the regionalization of manufacturing, driving defensive footprint expansions across Southeast Asia. Consequently, the fluidity of global component export flows is being rapidly replaced by rigid, bloc-oriented supply chains designed specifically to navigate punitive import duties and national security restrictions.</p>
<table>
    <thead>
        <tr>
            <th>Trade Metric / Phenomenon</th>
            <th>Impact Vector</th>
            <th>Targeted Geography</th>
            <th>Strategic Consequence</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Tariff Volatility on Hardware</td>
            <td>Demand suppression, inventory whipsaw</td>
            <td>US / China Corridor</td>
            <td>Smartphone forecast degradation</td>
        </tr>
        <tr>
            <td>China Localization Mandates</td>
            <td>Displacement of foreign incumbents</td>
            <td>Domestic China Market</td>
            <td>Accelerates Sunlord / local challengers</td>
        </tr>
        <tr>
            <td>China+1 Manufacturing Migration</td>
            <td>Footprint diversification, cost increase</td>
            <td>Vietnam / Philippines</td>
            <td>Forces redundant capacity investments</td>
        </tr>
        <tr>
            <td>Automotive Subsidy Structures</td>
            <td>End-market distortion</td>
            <td>Europe / North America</td>
            <td>Accelerates localized EV architectures</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The trade dynamic illustrates that geopolitical friction acts as a systemic accelerant for supply chain duplication, permanently elevating the structural cost base of the entire industry. The localization mandates within China present the most immediate existential threat to legacy incumbents, effectively weaponizing the world's largest end-market against foreign component dependency.</div>
<p>Strategically, this indicates that manufacturing footprint agility is paramount, requiring top-tier entities to rapidly establish robust operational capacity outside the immediate Chinese mainland. Relying on centralized mega-factories creates unacceptable exposure to sudden trade restrictions and retaliatory tariffs. Manufacturers must construct decentralized, resilient supply webs capable of seamlessly routing automotive and premium components into restricted markets without triggering punitive economic penalties.</p>
<div class="insight-highlight">Geopolitical tariff volatility permanently dismantles the era of the centralized global mega-factory, mandating highly redundant, regionalized production architectures.</div>
</div>
''',
    "15. Product Benchmarking & Miniaturization (0402 to 01005)": r'''
<div class="chapter-content">
<h1>15. Product Benchmarking & Miniaturization (0402 to 01005)</h1>
<p>The evolution of product specifications within the multilayer inductor ecosystem is characterized by a relentless, physically demanding march toward extreme miniaturization. Demand is driven by the severe spatial constraints inherent to sophisticated smartphone architectures and densely packed automotive communication modules. The economics of product benchmarking establish sub-millimeter manufacturing capability not merely as a premium feature, but as the absolute minimum requirement to participate in the highest-margin radio frequency allocations.</p>
<p>The market demonstrates a profound technological stratification based purely on physical dimensions, with the bleeding edge represented by the mass commercialization of 01005 (imperial) formats. Achieving stable production yields at these microscopic dimensions requires unprecedented precision in ceramic layering, pattern printing, and high-temperature sintering. Furthermore, the market demands that extreme miniaturization is achieved without degrading high-frequency performance or sacrificing stringent automotive reliability (AEC-Q200) standards. Manufacturers incapable of stabilizing yields below the legacy 0402 threshold face permanent exclusion from the critical path of next-generation hardware development.</p>
<table>
    <thead>
        <tr>
            <th>Package Dimension (Imperial)</th>
            <th>Primary Application Domain</th>
            <th>Manufacturing Barrier</th>
            <th>Strategic Value Profile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0805 / Larger</td>
            <td>Legacy power, basic filtering</td>
            <td>Very Low</td>
            <td>Commodity / Scale Defender</td>
        </tr>
        <tr>
            <td>0402</td>
            <td>Standard RF, mobile signal</td>
            <td>Medium</td>
            <td>Baseline Industry Standard</td>
        </tr>
        <tr>
            <td>0201</td>
            <td>Advanced 5G RF modules</td>
            <td>High (Yield sensitivity)</td>
            <td>Premium Consumer Focus</td>
        </tr>
        <tr>
            <td>01005</td>
            <td>Ultra-compact RF, Auto communication</td>
            <td>Extreme (Patterning precision)</td>
            <td>Bleeding-Edge Leadership</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The miniaturization matrix confirms that profit pools reside exclusively at the smallest physical dimensions, effectively filtering out technologically deficient competitors. The ability to push automotive-qualified components down to the 01005 format, as demonstrated by Murata, establishes the definitive benchmark for market dominance over the next decade.</div>
<p>Strategically, this indicates that research and development capital must be overwhelmingly directed toward overcoming the fundamental physics limiting sub-millimeter ceramic manipulation. Component size acts as an absolute commercial binary; components exceeding the spatial budget of modern integrated modules are not discounted—they are entirely rejected. Sustaining market relevance requires an institutional commitment to pushing the boundaries of material science and optical inspection technology.</p>
<div class="insight-highlight">Extreme miniaturization operates as a ruthless technical discriminator, permanently segregating true innovators from commoditized regional assemblers.</div>
</div>
''',
    "16. Capacity & Supply-Demand Balance": r'''
<div class="chapter-content">
<h1>16. Capacity & Supply-Demand Balance</h1>
<p>The capacity architecture of the global multilayer inductor market represents a delicate equilibrium between massive capital expenditure requirements and the persistent threat of cyclical oversupply. Demand fluctuations driven by macroeconomic consumer hardware cycles routinely test the financial resilience of the supply base. The economics of capacity management dictate that profitability relies entirely on maintaining exceptionally high factory utilization rates, forcing manufacturers to carefully throttle capacity expansion against highly unpredictable end-market pull.</p>
<p>The market demonstrates significant recent investments in geographic capacity diversification, notably characterized by aggressive facility expansions in Vietnam, the Philippines, and localized Japanese technological centers. The industry operates under the constant specter of localized supply constraints, particularly regarding specialized high-frequency and automotive-qualified components that cannot be rapidly substituted by generic equivalents. Conversely, the rapid scale-up of domestic Chinese manufacturing capability threatens to flood the legacy compact ferrite segment, threatening severe margin compression through structural oversupply. This dynamic forces a bifurcated capacity strategy: extreme agility for volume components and careful, long-term provisioning for premium tiers.</p>
<table>
    <thead>
        <tr>
            <th>Capacity Node / Geography</th>
            <th>Dominant Product Profile</th>
            <th>Strategic Expansion Logic</th>
            <th>Risk Profile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Japan (Mother-Factories)</td>
            <td>Premium RF, Automotive PoC</td>
            <td>Process leadership, intellectual property defense</td>
            <td>High fixed operational costs</td>
        </tr>
        <tr>
            <td>China (Scale Centers)</td>
            <td>Compact Ferrite, Consumer RF</td>
            <td>Mass volume matching, local demand defense</td>
            <td>Intense domestic oversupply</td>
        </tr>
        <tr>
            <td>ASEAN (Vietnam/Philippines)</td>
            <td>Broad passive portfolio</td>
            <td>China+1 diversification, cost arbitrage</td>
            <td>Logistics and talent scaling</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The geographic capacity map highlights a deliberate strategic fracturing of the supply base, intentionally separating premium intellectual property development from commoditized mass production. The expansion of ASEAN facilities serves as a critical pressure release valve, mitigating the existential risks associated with over-concentration in any single geopolitical theater.</div>
<p>Strategically, this indicates that capital must not be deployed homogenously across the manufacturing network. High-value investments in capacity must be strictly tethered to the automotive and ultra-miniaturized tiers where supply-demand mechanics remain highly favorable to the manufacturer. Deploying new capital into legacy format capacity, particularly within highly contested regions, constitutes an unacceptable destruction of corporate value.</p>
<div class="insight-highlight">Profitability is determined less by total global capacity, and more by the deliberate isolation of premium manufacturing capability from the gravitational pull of commoditized oversupply.</div>
</div>
''',
    "17. Value Chain & Profit Pool Analysis": r'''
<div class="chapter-content">
<h1>17. Value Chain & Profit Pool Analysis</h1>
<p>The multilayer inductor value chain represents a highly integrated industrial process where profit pools are aggressively concentrated at the extremes of material science formulation and module integration. Demand requirements mandate that physical manufacturing processes remain tightly coupled, limiting the viability of highly fragmented, outsourced production models. The economics of the value chain establish that margin capture is inextricably linked to the possession of proprietary ceramic formulations and the attainment of stringent, zero-defect quality validation protocols.</p>
<p>The market demonstrates that fundamental material integration—specifically the formulation of low-loss dielectric ceramics and high-permeability ferrites—acts as the primary barrier preventing the commoditization of the sector. The patterning, layering, and high-temperature sintering of these materials constitute the core manufacturing crucible, dictating absolute product yield and consequent financial viability. The highest density of value capture, however, occurs downstream during the integration of these discrete components into complex sub-assemblies, such as radio frequency front-end modules and automotive power management circuits. Entities incapable of influencing this module-level integration are relegated to operating as interchangeable, low-margin raw material providers.</p>
<table>
    <thead>
        <tr>
            <th>Value Chain Stage</th>
            <th>Core Activity</th>
            <th>Barrier to Entry</th>
            <th>Profit Pool Concentration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Material Formulation</td>
            <td>Ceramic / Ferrite synthesis</td>
            <td>Very High (Proprietary IP)</td>
            <td>High</td>
        </tr>
        <tr>
            <td>Patterning & Sintering</td>
            <td>Micro-layering, yield management</td>
            <td>High (Capital intensive)</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>Testing & Qualification</td>
            <td>AEC-Q200 / RF Validation</td>
            <td>High (Time / Rigor)</td>
            <td>High (Margin protector)</td>
        </tr>
        <tr>
            <td>Module Integration</td>
            <td>Placement in RF/Power packages</td>
            <td>Very High (Reference designs)</td>
            <td>Very High (Value realization)</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The profit pool architecture reveals that pure physical manufacturing is secondary in value creation to the mastery of fundamental material science and the control of downstream integration pathways. Qualification regimes act as the ultimate margin defense, establishing a temporal and financial moat that shields incumbents from aggressive capacity-dumping by regional scale competitors.</div>
<p>Strategically, this indicates that the pursuit of cost leadership through manufacturing efficiency alone is insufficient to secure long-term profitability. Corporations must fiercely protect their upstream material intellectual property while simultaneously establishing deep, collaborative engineering relationships with downstream module integrators. Capturing the full profit pool requires operating not merely as a component manufacturer, but as an indispensable architectural partner within the semiconductor ecosystem.</p>
<div class="insight-highlight">The ultimate profit pools reside not in the physical assembly of the inductor, but in the proprietary material science that makes it possible and the module architecture that makes it necessary.</div>
</div>
''',
    "18. Strategic Scenarios (Base, Upside, Downside) & Sensitivity": r'''
<div class="chapter-content">
<h1>18. Strategic Scenarios (Base, Upside, Downside) & Sensitivity</h1>
<p>The strategic scenario modeling quantifies the highly elastic nature of the multilayer inductor market, stress-testing foundational assumptions against macroeconomic volatility and accelerated technological adoption. Demand trajectories are fundamentally bound to the velocity of electric vehicle penetration and the resilience of the global consumer hardware replacement cycle. The economics of scenario planning demand that organizational strategy remains highly fluid, capable of absorbing significant demand destruction or rapidly capitalizing on unexpected architectural densification.</p>
<p>The market demonstrates substantial volatility across projected time horizons, revealing an upside scenario capturing $2,308.58 million by 2035 versus a downside reality constraining the market to $1,908.16 million. The delta between these outcomes is primarily dictated by the sensitivity to device-level content multiplication, specifically regarding the aggressiveness of automotive electrification and advanced radio frequency integration. Total market revenue is demonstrably more sensitive to shifts in absolute device demand than to proportional shifts in component pricing, underscoring the absolute necessity of maintaining exposure to high-volume end markets even under adverse pricing conditions.</p>
<table>
    <thead>
        <tr>
            <th>Strategic Scenario</th>
            <th>2025 Revenue ($Mn)</th>
            <th>2030 Revenue ($Mn)</th>
            <th>2035 Revenue ($Mn)</th>
            <th>CAGR (2025-2035)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Base Case Reality</td>
            <td>$1,446.68</td>
            <td>$1,727.53</td>
            <td>$2,115.25</td>
            <td>3.87%</td>
        </tr>
        <tr>
            <td>Optimized Upside</td>
            <td>$1,578.90</td>
            <td>$1,885.43</td>
            <td>$2,308.58</td>
            <td>3.87%</td>
        </tr>
        <tr>
            <td>Constrained Downside</td>
            <td>$1,305.05</td>
            <td>$1,558.41</td>
            <td>$1,908.16</td>
            <td>3.87%</td>
        </tr>
        <tr>
            <td><strong>Sensitivity: +/- 10% Demand</strong></td>
            <td><strong>--</strong></td>
            <td><strong>--</strong></td>
            <td><strong>$2,326.77 / $1,903.72</strong></td>
            <td><strong>--</strong></td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The scenario variance highlights the critical reliance on macroeconomic hardware stability, with demand destruction scenarios severely retarding the trajectory toward a two-billion-dollar market. The sensitivity analysis confirms that while pricing defense is critical, absolute physical volume loss represents the most catastrophic threat to the aggregate revenue pool.</div>
<p>Strategically, this indicates that manufacturing organizations must construct highly elastic operational models capable of throttling capital expenditures synchronously with rapid demand deviations. Over-committing to rigid capacity expansion based purely on upside projections invites severe financial exposure during cyclical drawdowns. Conversely, maintaining a purely defensive posture guarantees the relinquishment of massive high-margin revenue pools during periods of unexpected technological acceleration.</p>
<div class="insight-highlight">The market's ultimate scale is dictated not by the aggressive proliferation of new hardware, but by the relentless, invisible densification of components within existing hardware paradigms.</div>
</div>
''',
    "19. TDK Strategy: Opportunity Mapping & Win/Loss Matrix": r'''
<div class="chapter-content">
<h1>19. TDK Strategy: Opportunity Mapping & Win/Loss Matrix</h1>
<p>The strategic positioning of TDK Corporation within the multilayer inductor environment relies upon weaponizing its massive portfolio breadth and unparalleled credibility across high-reliability automotive architectures. Demand capture requires TDK to navigate aggressively against the extreme miniaturization prowess of Murata and the relentless localization scale of domestic Chinese competitors. The economics of TDK's strategy dictate isolating its premium capabilities within impregnable technological fortresses while systematically defending its necessary baseline scale in commoditized segments.</p>
<p>The market demonstrates that TDK holds a highly defensible core position, proxied at over $318 million in 2025 revenue, supported by strategic assets such as the Ouchi factory acting as a primary capability anchor. The opportunity map clearly identifies automotive power-over-coax architectures and specialized compact near-field communication applications as high-probability win zones where TDK's material science acts as a definitive moat. Conversely, pure-play commodity filtering within Chinese domestic consumer electronics represents a structural loss zone, requiring defensive holding patterns rather than aggressive, margin-dilutive capital deployment. TDK's ultimate success depends on systematically abandoning low-ground volume battles to dictate the high-ground terms of premium reliability.</p>
<table>
    <thead>
        <tr>
            <th>Competitive Vector</th>
            <th>TDK Strategic Posture</th>
            <th>Primary Challenger</th>
            <th>Projected Outcome (Win/Loss)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ultra-Miniature RF (01005)</td>
            <td>Defensive parity</td>
            <td>Murata</td>
            <td>Contested / Partial Loss</td>
        </tr>
        <tr>
            <td>Automotive Niche (PoC)</td>
            <td>Aggressive expansion</td>
            <td>Taiyo Yuden / Samsung</td>
            <td>Clear Win Zone</td>
        </tr>
        <tr>
            <td>Domestic China Scale</td>
            <td>Managed retreat / defense</td>
            <td>Sunlord / YAGEO</td>
            <td>Structural Loss Zone</td>
        </tr>
        <tr>
            <td>Advanced Material IP</td>
            <td>Unassailable stronghold</td>
            <td>Broad market</td>
            <td>Clear Win Zone</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The win/loss matrix brutally isolates TDK's absolute necessity to migrate portfolio weight toward the automotive tier, conceding the impossibility of out-scaling localized Chinese manufacturers on their own terrain. Establishing technological parity with Murata at the extreme edges of miniaturization is required merely to maintain strategic relevance in the premium smartphone sector.</div>
<p>Strategically, this indicates that TDK must treat advanced internal nodes, specifically the integrated operations spanning Akita and Ouchi, as the foundational bedrock of its global margin defense. The corporation must fiercely protect its status as a primary partner for European and North American automotive tier-ones, utilizing that status to insulate itself against Asian price warfare. The comprehensive strategy is not one of universal dominance, but of surgical value extraction from the most technically demanding segments of the market.</p>
<div class="insight-highlight">TDK's optimal strategic posture eschews pure volume supremacy in favor of dominating the specialized intersections of premium radio frequency and absolute automotive reliability.</div>
</div>
''',
    "20. Strategic Recommendations & Investment Roadmap": r'''
<div class="chapter-content">
<h1>20. Strategic Recommendations & Investment Roadmap</h1>
<p>The culmination of global market data, structural segmentation shifts, and competitive benchmarking mandates a highly disciplined, automotive-first investment doctrine for top-tier component manufacturers. Demand realities explicitly invalidate historical growth models dependent upon surging consumer electronics volumes, necessitating a brutal reallocation of organizational resources. The economics of the recommended roadmap demand that all future capital expenditures are subjected to stringent return-on-investment hurdles heavily biased toward high-barrier, zero-defect applications.</p>
<p>The market demonstrates that sustained leadership over the next decade requires the immediate execution of a tripartite strategic offensive: absolute prioritization of automotive radio frequency dominance, structural defense of compact manufacturing scale through targeted China-plus-one diversification, and the relentless advancement of sub-millimeter ceramic sintering capabilities. Investment roadmaps must fundamentally pivot away from raw capacity expansion and toward extreme technological differentiation. The mitigation of localized competitive risks requires Japanese incumbents to permanently intertwine their proprietary material science with the deeply integrated hardware roadmaps of global semiconductor architectures, making component substitution functionally impossible.</p>
<table>
    <thead>
        <tr>
            <th>Strategic Priority</th>
            <th>Primary Action Vector</th>
            <th>Capital Allocation Target</th>
            <th>Risk Mitigation Metric</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Automotive Dominance</td>
            <td>Secure AEC-Q200 for extreme RF</td>
            <td>Japanese Mother-Factories</td>
            <td>High-margin revenue insulation</td>
        </tr>
        <tr>
            <td>Geopolitical Resilience</td>
            <td>Accelerate China+1 expansion</td>
            <td>ASEAN (Vietnam/Philippines)</td>
            <td>Tariff & trade volatility defense</td>
        </tr>
        <tr>
            <td>Miniaturization Parity</td>
            <td>Commercialize 01005 capabilities</td>
            <td>R&D / Advanced Sintering</td>
            <td>Smartphone reference design lock-in</td>
        </tr>
        <tr>
            <td>Portfolio Optimization</td>
            <td>Divest/deprioritize legacy filtering</td>
            <td>Shift focus to PoC / Specialty</td>
            <td>Avoid pure commodity price wars</td>
        </tr>
    </tbody>
</table>
<div class="post-table-insight">The investment roadmap definitively shifts the corporate center of gravity away from generic capacity generation and toward specialized, application-specific engineering authority. By executing this prioritized allocation, manufacturers ensure their survival against both aggressive localized cost-cutting and the massive structural disruption of global supply chains.</div>
<p>Strategically, this indicates that the next era of multilayer inductor competition will not be won on the factory floor alone, but within the advanced research laboratories dictating the future of ceramic dielectric properties. Executive leadership must possess the discipline to reject low-margin volume contracts that dilute operational focus from the critical automotive and premium radio frequency mandates. Success is ultimately determined by the corporation's ability to evolve from a vendor of interchangeable parts into an indispensable architect of advanced electronic connectivity.</p>
<div class="insight-highlight">The ultimate strategic mandate requires the complete abandonment of the commodity component mindset in favor of dominating the highly specialized, high-liability intersection of mobility and connectivity.</div>
</div>
''',
}

# -----------------------------
# CONFIDENTIALITY OVERRIDES
# -----------------------------
COMPETITOR_ALIAS_MAP = {
    "Murata": "Player 1",
    "TDK Corporation": "Player 2",
    "Samsung Electro-Mechanics": "Player 3",
    "Samsung E-M": "Player 3",
    "Taiyo Yuden": "Player 4",
    "Sunlord": "Player 5",
    "YAGEO / Chilisin": "Player 6",
}

CH11_TITLE = "11. Competitive Landscape & Market Share"

def anonymize_chapter_11(html: str) -> str:
    for original, alias in COMPETITOR_ALIAS_MAP.items():
        html = html.replace(original, alias)
    html = html.replace(
        "Japanese manufacturers, with Player 1 and Player 2 collectively commanding over half of the global revenue pool.",
        "leading manufacturers, with Player 1 and Player 2 collectively commanding over half of the global revenue pool."
    )
    html = html.replace("legacy Japanese manufacturers", "legacy incumbents")
    return html

CHAPTERS[CH11_TITLE] = anonymize_chapter_11(CHAPTERS[CH11_TITLE])

# -----------------------------
# DATA FOR VISUALS
# -----------------------------
market_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Revenue": [1446.68, 1727.53, 2115.25],
    "Volume": [85.39, 112.51, 146.40],
    "ASP": [0.0169, 0.0153, 0.0144],
})

tam_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Device Anchors": [5108.50, 6518.08, 8389.83],
    "Components per Device": [16.7, 17.2, 17.4],
})

segment_df = pd.DataFrame({
    "Segment": ["Radio Frequency (RF)", "Compact Ferrite / NFC", "Automotive-Qualified"],
    "2025": [839.12, 474.80, 132.75],
    "2030": [973.82, 560.10, 193.61],
    "2035": [1143.43, 672.21, 299.60],
})

device_df = pd.DataFrame({
    "Device": ["Smartphones", "Earwear / TWS", "Smartwatches", "Electric Vehicles (EVs)", "ICE / HEV Vehicles", "IoT Edge Modules"],
    "2025": [1240.00, 360.00, 206.00, 25.00, 67.50, 3200.00],
    "2030": [1316.20, 437.99, 262.88, 39.00, 62.00, 4400.00],
    "2035": [1397.09, 532.88, 335.55, 61.95, 56.28, 6006.83],
})

pricing_df = pd.DataFrame({
    "Segment": ["Radio Frequency (RF)", "Compact Ferrite / NFC", "Automotive-Qualified", "Blended Device Metric (Smartphone)"],
    "2025": [0.0220, 0.0135, 0.0350, 0.0186],
    "2030": [0.0215, 0.0130, 0.0340, 0.0181],
    "2035": [0.0210, 0.0125, 0.0330, 0.0176],
})

north_america_df = pd.DataFrame({
    "Region": ["United States", "Mexico (Production Hub)", "Canada / Rest of NA"],
    "2025": [146.58, 17.68, 22.40],
    "2030": [177.30, 21.41, 26.10],
    "2035": [214.83, 25.91, 31.10],
})

europe_df = pd.DataFrame({
    "Region": ["Germany", "United Kingdom", "France & Italy", "Eastern Europe (Assembly)"],
    "2025": [41.97, 18.10, 26.40, 14.20],
    "2030": [52.54, 21.40, 31.20, 17.80],
    "2035": [65.75, 25.80, 37.90, 22.50],
})

apac_df = pd.DataFrame({
    "Region": ["China", "India", "Japan", "South Korea", "Taiwan", "Vietnam"],
    "2025": [398.24, 124.96, 51.70, 32.54, 8.45, 17.15],
    "2030": [470.83, 180.37, 61.35, 38.16, 10.03, 21.90],
    "2035": [559.87, 253.32, 72.97, 44.80, 11.89, 27.98],
})

competitive_df = pd.DataFrame({
    "Competitor": ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Others"],
    "2025": [31.0, 22.0, 9.0, 8.0, 7.0, 6.0, 3.0, 14.0],
    "2035": [28.0, 21.0, 10.0, 8.0, 10.0, 8.0, 3.0, 12.0],
})

scenario_df = pd.DataFrame({
    "Year": [2025, 2030, 2035],
    "Base Case Reality": [1446.68, 1727.53, 2115.25],
    "Optimized Upside": [1578.90, 1885.43, 2308.58],
    "Constrained Downside": [1305.05, 1558.41, 1908.16],
})

roadmap_df = pd.DataFrame({
    "Priority": ["Automotive Dominance", "Geopolitical Resilience", "Miniaturization Parity", "Portfolio Optimization"],
    "Priority Score": [95, 86, 89, 78],
    "Time Horizon": ["Near-term", "Near-term", "Mid-term", "Immediate"],
})

miniaturization_df = pd.DataFrame({
    "Package": ["0805 / Larger", "0402", "0201", "01005"],
    "Barrier Score": [1, 2, 3, 4],
    "Strategic Value Score": [1, 2, 3, 4],
})

capacity_df = pd.DataFrame({
    "Node": ["Japan (Mother-Factories)", "China (Scale Centers)", "ASEAN (Vietnam/Philippines)"],
    "Barrier": [5, 2, 3],
    "Risk": [3, 5, 4],
    "Reward": [5, 3, 4],
})

win_loss_df = pd.DataFrame({
    "Vector": ["Ultra-Miniature RF (01005)", "Automotive Niche (PoC)", "Domestic China Scale", "Advanced Material IP"],
    "Outcome Score": [2, 5, 1, 5],
    "Label": ["Contested / Partial Loss", "Clear Win Zone", "Structural Loss Zone", "Clear Win Zone"],
})

# -----------------------------
# SESSION STATE
# -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "visitor_name" not in st.session_state:
    st.session_state.visitor_name = ""
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "Overview"

# -----------------------------
# CSS
# -----------------------------
def inject_css(login_mode: bool = False) -> None:
    sidebar_login_hide = "section[data-testid='stSidebar'] {display:none !important;}" if login_mode else ""
    st.markdown(
        f"""
        <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
            button[kind="secondary"] {{display:none;}}
            [data-testid="stToolbar"] {{display:none !important;}}
            [data-testid="stDecoration"] {{display:none !important;}}
            .stDeployButton {{display:none !important;}}
            button[data-testid="baseButton-headerNoPadding"] {{display:none !important;}}
            {sidebar_login_hide}

            .stApp {{
                background:
                    radial-gradient(circle at top left, rgba(232,199,213,0.18), transparent 28%),
                    linear-gradient(180deg, #FBF8F9 0%, #F5F1F3 100%);
            }}

            html, body, [class*="css"] {{
                font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: {INK};
            }}

            section[data-testid="stSidebar"] {{
                background: linear-gradient(180deg, #2E0A18 0%, #431024 100%);
                border-right: 1px solid rgba(255,255,255,0.07);
            }}

            section[data-testid="stSidebar"] * {{
                color: #FFF7FA !important;
            }}

            [data-testid="stSidebarNav"] {{
                display:none !important;
            }}

            div[data-baseweb="select"] > div,
            div[data-baseweb="input"] > div {{
                border-radius: 14px !important;
            }}

            .main-shell {{
                max-width: 1360px;
                margin: 0 auto;
                padding-bottom: 2rem;
            }}

            .hero-card {{
                position: relative;
                overflow: hidden;
                background: linear-gradient(135deg, rgba(91,15,46,1) 0%, rgba(67,16,36,1) 72%);
                border-radius: 28px;
                padding: 34px 38px;
                color: white;
                box-shadow: 0 18px 40px rgba(91,15,46,0.22);
                border: 1px solid rgba(255,255,255,0.08);
                margin-bottom: 18px;
            }}

            .hero-card:before {{
                content: "";
                position: absolute;
                right: -120px;
                top: -80px;
                width: 320px;
                height: 320px;
                background: radial-gradient(circle, rgba(255,255,255,0.10) 0%, transparent 65%);
            }}

            .hero-kicker {{
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 0.16em;
                text-transform: uppercase;
                color: #F6DDE6;
                margin-bottom: 12px;
            }}

            .hero-title {{
                font-size: 2.8rem;
                line-height: 1.14;
                font-weight: 800;
                margin-bottom: 12px;
            }}

            .hero-subtitle {{
                font-size: 1.15rem;
                color: #F8E8EF;
                max-width: 780px;
            }}

            .metric-card {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 20px;
                padding: 18px 18px 16px 18px;
                min-height: 150px;
                box-shadow: 0 10px 26px rgba(15,23,42,0.06);
            }}

            .metric-label {{
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                color: #64748B;
                font-weight: 800;
                margin-bottom: 10px;
            }}

            .metric-value {{
                font-size: 1.95rem;
                line-height: 1.1;
                color: {BURGUNDY};
                font-weight: 800;
                margin-bottom: 8px;
            }}

            .metric-note {{
                font-size: 14px;
                line-height: 1.55;
                color: #6B7280;
            }}

            .sidebar-brand {{
                background: rgba(255,255,255,0.06);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 18px;
                padding: 16px 16px 14px 16px;
                margin-bottom: 10px;
                box-shadow: 0 10px 24px rgba(0,0,0,0.18);
            }}

            .sidebar-kicker {{
                font-size: 11px;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                color: #E9C7D5 !important;
                margin-bottom: 6px;
            }}

            .sidebar-title {{
                font-size: 20px;
                line-height: 1.25;
                font-weight: 800;
                margin-bottom: 6px;
            }}

            .sidebar-sub {{
                font-size: 12px;
                color: #F1DDE5 !important;
            }}

            .sidebar-user {{
                background: rgba(255,255,255,0.05);
                border-radius: 14px;
                padding: 12px 14px;
                border: 1px solid rgba(255,255,255,0.06);
                margin: 10px 0 14px;
                color: #FDEEF5;
                font-size: 13px;
            }}

            .section-title {{
                font-size: 1.32rem;
                font-weight: 800;
                color: {INK};
                margin: 0 0 0.35rem 0;
            }}

            .section-subtitle {{
                color: {SLATE};
                font-size: 0.96rem;
                margin-bottom: 1rem;
            }}

            .report-shell {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 24px;
                box-shadow: 0 14px 32px rgba(15,23,42,0.06);
                overflow: hidden;
                margin-top: 16px;
            }}

            .report-banner {{
                background: linear-gradient(135deg, #FFF6F9 0%, #FAEDF2 100%);
                border-bottom: 1px solid #EED7E1;
                padding: 18px 26px;
            }}

            .report-title {{
                font-size: 1.6rem;
                font-weight: 800;
                color: {INK};
            }}

            .report-card {{
                padding: 26px 30px 30px 30px;
            }}

            .chapter-content h1 {{
                font-size: 2.15rem;
                font-weight: 800;
                color: #0F172A;
                margin-top: 0;
                margin-bottom: 1.5rem;
                border-bottom: 2px solid #E2E8F0;
                padding-bottom: 0.55rem;
            }}

            .chapter-content h2 {{
                font-size: 1.5rem;
                font-weight: 700;
                color: #1E293B;
                margin-top: 2rem;
                margin-bottom: 1rem;
            }}

            .chapter-content h3 {{
                font-size: 1.2rem;
                font-weight: 700;
                color: #334155;
                margin-top: 1.5rem;
                margin-bottom: 0.75rem;
            }}

            .chapter-content p {{
                margin-bottom: 1.25rem;
                line-height: 1.8;
                color: #334155;
                text-align: justify;
                font-size: 0.99rem;
            }}

            .chapter-content table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1.5rem 0;
                background-color: #ffffff;
                box-shadow: 0 1px 3px rgba(0,0,0,0.08);
                border-radius: 0.6rem;
                overflow: hidden;
                border: 1px solid #E2E8F0;
            }}

            .chapter-content th {{
                background: linear-gradient(180deg, #5B0F2E 0%, #431024 100%);
                color: #ffffff;
                font-weight: 700;
                text-align: left;
                padding: 0.85rem 1rem;
                border-bottom: 2px solid #6E2341;
                font-size: 0.88rem;
            }}

            .chapter-content td {{
                padding: 0.8rem 1rem;
                border-bottom: 1px solid #E2E8F0;
                color: #334155;
                font-size: 0.88rem;
                vertical-align: top;
            }}

            .chapter-content tr:last-child td {{
                border-bottom: none;
            }}

            .chapter-content tr:hover td {{
                background-color: #FBF5F7;
            }}

            .insight-highlight {{
                background-color: #FAF2F5;
                border-left: 4px solid #8A1E4F;
                padding: 1rem 1.25rem;
                margin: 1.5rem 0;
                font-style: italic;
                color: #7A163F;
                font-weight: 600;
                border-radius: 0 0.5rem 0.5rem 0;
            }}

            .post-table-insight {{
                background-color: #FCFAFB;
                border: 1px solid #E8DCE2;
                padding: 1rem;
                margin-top: -1rem;
                margin-bottom: 1.5rem;
                font-size: 0.88rem;
                color: #5B4B54;
                border-radius: 0 0 0.5rem 0.5rem;
            }}

            .small-callout {{
                background: rgba(255,255,255,0.96);
                border: 1px solid {BORDER};
                border-radius: 18px;
                padding: 16px 18px;
                box-shadow: 0 10px 26px rgba(15,23,42,0.05);
            }}

            .chapter-note {{
                background: #FFF8FB;
                border: 1px solid #F0D6E1;
                border-radius: 16px;
                padding: 14px 16px;
                color: #6B213E;
                font-size: 14px;
                margin-bottom: 14px;
            }}
            
            [data-testid="stForm"] {{
                border: none !important;
                padding: 0 !important;
            }}

            [data-testid="stTextInput"] label,
            [data-testid="stRadio"] label {{
                font-weight: 700 !important;
                color: {INK} !important;
            }}
            
            .stButton > button {{
                background: linear-gradient(135deg, {BURGUNDY} 0%, {BURGUNDY_DARK} 100%);
                color: white;
                border: none;
                border-radius: 14px;
                padding: 0.7rem 1rem;
                font-weight: 700;
                box-shadow: 0 10px 20px rgba(91,15,46,0.18);
            }}

            .stButton > button:hover {{
                filter: brightness(1.04);
                transform: translateY(-1px);
            }}

            @media (max-width: 768px) {{
                .report-card {{
                    padding: 20px 18px 22px 18px;
                }}
                .hero-card {{
                    padding: 26px 22px;
                    border-radius: 22px;
                }}
                .metric-value {{
                    font-size: 1.65rem;
                }}
            }}
        </style>
        <meta http-equiv="refresh" content="300">
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# HELPERS
# -----------------------------
def metric_card(label: str, value: str, note: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def section_intro(title: str, subtitle: str) -> None:
    st.markdown(f'<div class="section-title">{title}</div><div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)

def style_plot(fig: go.Figure, title: str, height: int = 360) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0, xanchor="left", font=dict(size=18, color=INK)),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter, sans-serif", color=SLATE),
        margin=dict(l=18, r=18, t=58, b=18),
        height=height,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hoverlabel=dict(bgcolor="white", font_color=INK),
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor="rgba(148,163,184,0.18)", zeroline=False)
    return fig

# -----------------------------
# MATPLOTLIB INLINE CHARTS 
# -----------------------------
def market_revenue_chart():
    years = ["2025", "2030", "2035"]
    revenue = [1446.7, 1727.5, 2115.3]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(years, revenue, color='#5B0F2E')
    ax.set_ylabel("Revenue ($Mn)")
    ax.set_title("Market Expansion ($Mn)")
    st.pyplot(fig)

def market_volume_chart():
    years = ["2025", "2030", "2035"]
    volume = [85.4, 112.5, 146.4]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(years, volume, color='#7A163F')
    ax.set_ylabel("Volume (Bn Units)")
    ax.set_title("Volume Scaling (Bn Units)")
    st.pyplot(fig)

def tam_combo_chart():
    years = ["2025", "2030", "2035"]
    devices = [5108.5, 6518.0, 8389.8]
    components = [16.7, 17.2, 17.4]

    fig, ax1 = plt.subplots(figsize=(6, 4))
    ax1.bar(years, devices, color='#5B0F2E')
    ax1.set_ylabel("Device Anchors (Mn)")
    ax1.set_title("Total Device Anchors")
    st.pyplot(fig)

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.plot(years, components, marker='o', color='#7A163F', linewidth=2)
    ax2.set_ylabel("Components per Device")
    ax2.set_title("Density Metrics")
    st.pyplot(fig2)

def segment_stacked_chart():
    years = ["2025", "2030", "2035"]
    rf = [839, 973, 1143]
    ferrite = [474, 560, 672]
    auto = [132, 193, 299]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(years, rf, label="RF", color='#5B0F2E')
    ax.bar(years, ferrite, bottom=rf, label="Ferrite", color='#7A1C3A')
    bottom2 = [rf[i] + ferrite[i] for i in range(3)]
    ax.bar(years, auto, bottom=bottom2, label="Automotive", color='#B07A92')

    ax.set_title("Segment Evolution ($Mn)")
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    plt.tight_layout()
    st.pyplot(fig)

def pricing_chart():
    years = ["2025", "2030", "2035"]
    rf = [0.0220, 0.0215, 0.0210]
    auto = [0.0350, 0.0340, 0.0330]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(years, rf, marker='o', label='RF', color='#5B0F2E', linewidth=2)
    ax.plot(years, auto, marker='s', label='Auto', color='#7A163F', linewidth=2)
    ax.set_ylabel("ASP ($)")
    ax.set_title("Pricing Erosion & Premium Resistance")
    ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9))
    st.pyplot(fig)

def scenario_chart():
    years = ["2025", "2030", "2035"]
    base = [1446.68, 1727.53, 2115.25]
    upside = [1578.90, 1885.43, 2308.58]
    downside = [1305.05, 1558.41, 1908.16]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(years, upside, linestyle='--', color='#7A163F', label='Upside')
    ax.plot(years, base, marker='o', color='#5B0F2E', linewidth=3, label='Base')
    ax.plot(years, downside, linestyle=':', color='#A4456F', label='Downside')
    ax.set_title("Strategic Scenarios ($Mn)")
    ax.set_ylabel("Revenue ($Mn)")
    ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))
    st.pyplot(fig)

def render_hero() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">Boardroom Preview Dashboard</div>
            <div class="hero-title">Global Multilayer Inductor Market (2025–2035)</div>
            <div class="hero-subtitle">Demand expansion, RF complexity, automotive qualification, and portfolio strategy — translated into a dynamic executive dashboard for TDK.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_overview() -> None:
    render_hero()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Market Revenue 2035", QUICK_METRICS["Market Revenue 2035"], "Global multilayer inductor market")
    with c2:
        metric_card("Global CAGR", QUICK_METRICS["Global CAGR"], "2025–2035 base case")
    with c3:
        metric_card("TDK 2025 Proxied", QUICK_METRICS["TDK 2025 Proxied"], "Illustrative revenue position")
    with c4:
        metric_card("Premium Growth Vector", QUICK_METRICS["Premium Growth Vector"], "High-barrier value pool")

    st.markdown("")
    tab1, tab2, tab3, tab4 = st.tabs(["Market trajectory", "Value pools", "Regional architecture", "Competition & scenarios"])

    with tab1:
        section_intro("Trajectory and pricing", "The overview layer concentrates the most decision-critical variables: revenue, volume, and ASP compression.")
        col_a, col_b = st.columns([1.35, 1])
        with col_a:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Scatter(
                x=market_df["Year"], y=market_df["Revenue"],
                mode="lines+markers",
                name="Revenue ($Mn)",
                line=dict(color=BURGUNDY, width=4),
                marker=dict(size=10, color=BURGUNDY)
            ), secondary_y=False)
            fig.add_trace(go.Bar(
                x=market_df["Year"], y=market_df["Volume"],
                name="Volume (Bn units)",
                marker_color="#D7B2C0",
                opacity=0.78
            ), secondary_y=True)
            fig.update_yaxes(title_text="Revenue ($Mn)", secondary_y=False)
            fig.update_yaxes(title_text="Volume (Bn units)", secondary_y=True)
            style_plot(fig, "Revenue expansion vs. volume scale", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            asp_fig = go.Figure()
            asp_fig.add_trace(go.Scatter(
                x=market_df["Year"], y=market_df["ASP"],
                mode="lines+markers+text",
                text=[f"${x:.4f}" for x in market_df["ASP"]],
                textposition="top center",
                line=dict(color=BURGUNDY_LIGHT, width=4),
                marker=dict(size=10, color=BURGUNDY_LIGHT),
                fill="tozeroy",
                fillcolor="rgba(122,22,63,0.08)",
                name="ASP ($/unit)"
            ))
            asp_fig.update_yaxes(title_text="ASP ($/unit)")
            style_plot(asp_fig, "Blended ASP compression", 380)
            st.plotly_chart(asp_fig, use_container_width=True)

    with tab2:
        section_intro("Segment structure and device pull", "Value creation is migrating toward automotive-qualified components even while RF maintains scale leadership.")
        col_a, col_b = st.columns([1.25, 1])
        with col_a:
            melt = segment_df.melt(id_vars="Segment", var_name="Year", value_name="Revenue")
            fig = px.bar(
                melt, x="Year", y="Revenue", color="Segment", barmode="group",
                color_discrete_sequence=[BURGUNDY, "#B07A92", "#E7C7D5"]
            )
            style_plot(fig, "Segment revenue by year", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            fig = go.Figure(data=[go.Pie(
                labels=["RF", "Compact Ferrite / NFC", "Automotive-Qualified"],
                values=[54.0, 31.7, 14.1],
                hole=0.62,
                marker=dict(colors=[BURGUNDY, "#B07A92", "#E7C7D5"]),
                sort=False
            )])
            fig.update_traces(textinfo="label+percent")
            style_plot(fig, "2035 mix shift toward automotive", 380)
            st.plotly_chart(fig, use_container_width=True)

        device_melt = device_df.melt(id_vars="Device", value_vars=["2025", "2035"], var_name="Year", value_name="Volume")
        fig = px.bar(
            device_melt,
            x="Device",
            y="Volume",
            color="Year",
            barmode="group",
            color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
        )
        fig.update_layout(xaxis_tickangle=-18)
        style_plot(fig, "Device-level demand engine: 2025 vs. 2035", 390)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        section_intro("Regional architecture", "Asia remains the volume center of gravity while Europe and North America protect premium automotive value pools.")
        col_a, col_b = st.columns([1.1, 1.2])
        with col_a:
            region_rollup = pd.DataFrame({
                "Region": ["North America", "Europe", "Asia Pacific + Japan"],
                "2025": [north_america_df["2025"].sum(), europe_df["2025"].sum(), apac_df["2025"].sum()],
                "2035": [north_america_df["2035"].sum(), europe_df["2035"].sum(), apac_df["2035"].sum()],
            })
            melt = region_rollup.melt(id_vars="Region", var_name="Year", value_name="Revenue")
            fig = px.bar(
                melt, x="Region", y="Revenue", color="Year", barmode="group",
                color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
            )
            style_plot(fig, "Regional value pools: 2025 vs. 2035", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            country_2035 = pd.concat([
                north_america_df.assign(Group="North America"),
                europe_df.assign(Group="Europe"),
                apac_df.assign(Group="Asia Pacific + Japan")
            ], ignore_index=True).sort_values("2035", ascending=True)
            fig = px.bar(
                country_2035,
                x="2035",
                y="Region",
                color="Group",
                orientation="h",
                color_discrete_sequence=[BURGUNDY, "#B07A92", "#E7C7D5"]
            )
            style_plot(fig, "2035 country / sub-region stack", 380)
            st.plotly_chart(fig, use_container_width=True)

    with tab4:
        section_intro("Competitive positioning and scenario stress-testing", "Competitive share is anonymized, while the scenario view highlights upside and downside sensitivity.")
        col_a, col_b = st.columns([1.05, 1.15])
        with col_a:
            melt = competitive_df.melt(id_vars="Competitor", var_name="Year", value_name="Share")
            fig = px.bar(
                melt, x="Competitor", y="Share", color="Year", barmode="group",
                color_discrete_sequence=[BURGUNDY, "#D7B2C0"]
            )
            style_plot(fig, "Anonymized market share view", 380)
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            fig = go.Figure()
            for name, color in [
                ("Base Case Reality", BURGUNDY),
                ("Optimized Upside", "#A4456F"),
                ("Constrained Downside", "#D8B5C3"),
            ]:
                fig.add_trace(go.Scatter(
                    x=scenario_df["Year"], y=scenario_df[name],
                    mode="lines+markers", name=name,
                    line=dict(width=4, color=color),
                    marker=dict(size=9, color=color)
                ))
            fig.update_yaxes(title_text="Revenue ($Mn)")
            style_plot(fig, "Scenario sensitivity through 2035", 380)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("")
    st.markdown(
        """
        <div class="small-callout">
            <div class="section-title" style="margin-bottom:8px;">Executive interpretation</div>
            <div class="section-subtitle" style="margin-bottom:0;">
                The dashboard confirms a structural market rotation: RF remains the scale engine, automotive becomes the premium margin engine, and Asia remains the manufacturing gravity center. The strategic implication is not to chase all volume equally — it is to defend scale where necessary while concentrating investment in zero-defect, miniaturized, automotive-qualified architectures.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_prev_next(options: list[str], current: str) -> None:
    idx = options.index(current)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if idx > 0:
            if st.button("⬅ Previous"):
                st.session_state["nav_choice"] = options[idx - 1]
                st.rerun()

    with col2:
        if idx < len(options) - 1:
            if st.button("Next ➡"):
                st.session_state["nav_choice"] = options[idx + 1]
                st.rerun()

def render_chapter_page(title: str, nav_options: list[str]) -> None:
    st.markdown(
        f"""
        <div class="report-shell">
            <div class="report-banner">
                <div class="report-title">{title}</div>
            </div>
            <div class="report-card">
        """,
        unsafe_allow_html=True,
    )
    
    html_content = CHAPTERS[title]
    
    # 1. Inject placeholders for storytelling charts
    if title.startswith("1. "):
        html_content = html_content.replace("</p>\n<table>", "</p>\n\n<table>")
    elif title.startswith("3. "):
        html_content = html_content.replace("</div>\n<p>", "</div>\n\n<p>")
    elif title.startswith("4. "):
        html_content = html_content.replace("</div>\n<p>", "</div>\n\n<p>")
    elif title.startswith("7. "):
        html_content = html_content.replace("</div>\n<p>", "</div>\n\n<p>")
    elif title.startswith("18. "):
        html_content = html_content.replace("</div>\n<p>", "</div>\n\n<p>")

    # 2. SAFELY SPLIT BY THE EXACT MARKER
    parts = html_content.split("")
    
    st.markdown(parts[0], unsafe_allow_html=True)
    
    if len(parts) > 1:
        colA, colB = st.columns([1, 1]) if title.startswith("1. ") or title.startswith("3. ") else (st, st)
        
        # Render the specific inline chart
        if title.startswith("1. "):
            with colA:
                market_revenue_chart()
            with colB:
                market_volume_chart()
        elif title.startswith("3. "):
            with colA:
                tam_combo_chart()
        elif title.startswith("4. "):
            segment_stacked_chart()
        elif title.startswith("7. "):
            pricing_chart()
        elif title.startswith("18. "):
            scenario_chart()

        st.markdown(parts[1], unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
    render_prev_next(nav_options, title)

    st.markdown("""
    ---
    **Confidential & Proprietary** © 2026 Strategic Market Research  

    To access the full report:  
    📩 info@strategicmarketresearch.com
    """)

def render_login() -> None:
    inject_css(login_mode=True)
    
    # Center the login form using columns
    _, col, _ = st.columns([1, 1.2, 1])
    
    with col:
        # Add some top margin to push it down
        st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
        
        # Use a native Streamlit container so the inputs actually stay inside
        with st.container(border=True):
            st.markdown("""
                <h2 style='text-align: center; color: #5B0F2E; padding-bottom: 15px;'>
                    SMR BOARDROOM ACCESS
                </h2>
            """, unsafe_allow_html=True)
            
            name = st.text_input("Name", placeholder="Enter your name")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # CRITICAL FIX: type="primary" prevents the CSS from hiding the button
            if st.button("Enter Dashboard", type="primary", use_container_width=True):
                if password == "SMR2026":
                    st.session_state.authenticated = True
                    st.session_state.visitor_name = name.strip()
                    st.session_state.nav_choice = "Overview"
                    st.rerun()
                else:
                    st.error("Incorrect password")

# -----------------------------
# APP
# -----------------------------
if not st.session_state.authenticated:
    render_login()
    st.stop()

inject_css(login_mode=False)

nav_options = ["Overview"] + list(CHAPTERS.keys())

st.sidebar.markdown(
    f"""
    <div class="sidebar-brand">
        <div class="sidebar-kicker">Strategic Market Research</div>
        <div class="sidebar-title">Global Multilayer Inductor Market</div>
        <div class="sidebar-sub">Client: {CLIENT_NAME}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div class="sidebar-user">
        Viewing as <strong>{st.session_state.visitor_name}</strong><br>
        Premium preview mode · Tier 3 dashboard
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.radio(
    "Navigate",
    nav_options,
    key="nav_choice",
    label_visibility="collapsed",
)

st.sidebar.caption("Confidential & Proprietary")
st.sidebar.caption("© 2026 Strategic Market Research")
if st.sidebar.button("Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.visitor_name = ""
    st.session_state.nav_choice = "Overview"
    st.rerun()

st.markdown('<div class="main-shell">', unsafe_allow_html=True)
if st.session_state.nav_choice == "Overview":
    render_overview()
else:
    render_chapter_page(st.session_state.nav_choice, nav_options)
st.markdown('</div>', unsafe_allow_html=True)
