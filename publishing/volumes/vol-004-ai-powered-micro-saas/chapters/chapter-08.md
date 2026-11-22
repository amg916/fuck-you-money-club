# Chapter 08: Tools, Observability Stack, Contextual Extensions & AI Search (GEO)

*LiteLLM / Helicone Token Telemetry, PostHog & Sentry, Manifest V3 Workflow Extensions, First-Party B2B Pixels & Generative Engine Optimization*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Build one paid workflow, not a museum of tools. Your stack must identify the tenant, finish the job, meter its cost, and explain why the customer stays. This directory connects those duties to a lean service menu and three acquisition surfaces: a contextual Chrome companion, bounded US business visitor resolution, and evidence that search assistants can cite. None replaces retention. Start with one provider per duty, measure cost per accepted result, and expand only when a measured bottleneck justifies another bill. Gross subscriptions are not owner profit.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Conservative | $50,000 gross |  |  |
| Base | $375,000 gross |  |  |
| Scaled | $700,000 gross |  |  |

## 1. Buy one tool per operating duty  `🏷️ OPERATING_FRAMEWORK`

Use Clerk when managed account flows save more time than their bill; use Auth.js when your team can own session security and account recovery. Neither choice grants access to customer records by itself. Resolve the tenant on the server and check membership on every read, write, and queued job. Choose Neon or Supabase Postgres for durable state, then add pgvector only when retrieval beats a plain query on a held out task set. Keep source records, vector references, and deletion state tied to the same tenant key. Index the fields the paid workflow actually uses. A founder who buys a vector store before proving retrieval quality has added a bill and a failure mode, not a moat. Test restores before trusting the first backup report.

Choose Trigger.dev for durable task runs or an Upstash queue service for a smaller delivery primitive, after checking the retry and scheduling behavior of the exact product. Store a job key before dispatch so a repeat event cannot bill twice or send two reports. Keep the task state in Postgres rather than trusting the browser to remember progress. Use Stripe when you want direct control of payment operations; consider Paddle when its merchant of record model fits your product and markets. Read the actual contract to establish who handles taxes, disputes, and refunds. In either case, verify webhook signatures and deduplicate event IDs. Grant paid access from verified billing state, not a success page. Reconcile local subscription state against the billing provider on a daily schedule.

Put LiteLLM or a small custom router between application code and model calls. Every request needs a tenant key, job key, model version, token usage, latency, and cost basis. Helicone can supply gateway observability, but avoid paying two vendors to retain the same raw content. PostHog owns product events such as first accepted result and weekly repeat use; Sentry owns exceptions and traces. Join them through opaque request IDs, not copied inbox text. Redact payloads before export and set short retention for diagnostic detail. A successful HTTP response can still contain an unusable answer, so record customer acceptance separately. Review the slowest and most expensive accepted jobs each week. Those two queues tell you whether to improve routing, trim context, repair retrieval, or simplify the workflow.

**Lean architecture: one accountable owner per duty**

| Duty | Shortlist | Acceptance test |
| --- | --- | --- |
| Auth | Clerk / Auth.js | Cross-tenant request denied |
| Data | Neon / Supabase + pgvector | Restore and tenant isolation |
| Jobs | Trigger.dev / Upstash | Duplicate event, one result |
| Models | LiteLLM / custom; Helicone | Cost reconciles by tenant |
| Signals | PostHog / Sentry | Trace links to accepted job |
| Billing | Stripe / Paddle | Replay cannot duplicate access |

## 2. Make token spend explain owner profit  `🏷️ ILLUSTRATIVE_MODEL`

Treat the three scenarios as annual planning cases, not observed results. Conservative means $50,000 gross subscription billings and 15% net owner profit, or $7,500, with 1 FT + 2 C. Base means $375,000 gross and 30% net, or $112,500, with 1 FT + 2 C. Scaled means $700,000 gross and 45% net, or $315,000, with 2 FT + 3 C. FT denotes full time operating roles; C denotes scoped contractors, not three hidden full time salaries. At the smallest case, the founder occupies the full time role and owner profit is their residual compensation before personal tax. It does not fund a market salary on top. State that limitation before presenting the model as an income replacement plan to any prospective operator.

Build the annual bridge explicitly. Conservative allocates $10,000 to inference and hosting COGS and $32,500 to other operating costs. Base allocates $56,250 and $206,250 respectively. Scaled allocates $84,000 and $301,000. Subtract both buckets from gross billings to reach the stated net amounts. Other costs include payment fees, refunds, tools, contractor invoices, acquisition, support, and paid staff where present. Exclude sales taxes collected for authorities from gross subscriptions and explain that owner personal taxes remain outside these net figures. These are illustrative envelopes, not vendor quotes or staffing benchmarks. Break each envelope into actual quotes before hiring. If labor exceeds the envelope, reduce the net forecast rather than quietly labeling unpaid work as efficiency. The scaled case assumes materially better automation and retention, not merely more customers.

At $99 per month, a worked account with 200 completed jobs, $0.06 inference per job, and $3 allocated hosting produces $15 in monthly COGS and $84 before all other expenses. These are chosen assumptions, not current provider prices. Failed attempts and retries must be included in the cost numerator even when the customer sees only one result. Meter input, output, cached input, retrieval, and tool charges where applicable. Set a soft tenant budget that routes simple tasks cheaply and a hard spend ceiling that pauses new expensive work with a clear status. Never silently replace a promised result with lower quality output. Track accepted jobs per paid account alongside cancellation by cohort. A cheap model that doubles rework can be more expensive than the stronger model it replaced.

## 3. Put the free companion inside the paid workflow  `🏷️ OPERATING_FRAMEWORK`

The chrome_extension_contextual_arbitrage play starts with a narrow moment inside a daily CRM, inbox, or ERP tab. A free Manifest V3 Chrome companion can turn a selected account note into three useful next actions, then offer the $99 monthly SaaS tier for saved workflows, team history, and higher usage. Ship one supported host first. Ask for the minimum host permissions, prefer a user initiated selection, and show the exact material being sent. Do not scrape the entire inbox because it is technically reachable. The extension is a contextual entry point, not a second product with its own billing state. Keep model credentials on your server and exchange short lived authenticated requests. Bind each request to the tenant and validate message origins before reading page context or launching work.

Manifest V3 service workers can stop between events, so persist pending job references and recover state on the next interaction. Bundle executable extension code rather than downloading remote scripts; call your server for data and inference. Treat page text as untrusted input that cannot change tool permissions or reveal another tenant's records. Use a structured extraction boundary and cap context length before dispatch. Test the companion against changing CRM layouts, expired sessions, duplicate clicks, and network loss. A selector that silently reads the wrong account is worse than an explicit unavailable state. Offer a manual selection fallback when the host layout changes. Keep the core paid workflow usable on the web so a browser review delay or host redesign does not disable the business overnight.

Measure the extension funnel from eligible active users to first accepted insight, repeat weekly use, upgrade, and retained paid accounts. Installs alone do not establish distribution. For an illustrative cohort, 1,000 activated free users at a 3% paid conversion rate produce 30 accounts and $2,970 monthly gross subscriptions at $99 each. If every free account consumes $0.50 of monthly inference, that cohort also creates $500 of recurring free inference cost before support or paid usage. Charge that cost to acquisition economics rather than hiding it in infrastructure. Limit free volume by server enforced tenant and account budgets, not a local counter that resets on reinstall. Compare retained contribution against the ongoing free cohort bill. Remove features that generate curiosity clicks but never help a customer complete the paid job.

**SOP — Standard Operating Procedure**

1. Select context
   - Support one host and task.
   - Document selected fields and permissions.
2. Secure execution
   - Authenticate server calls.
   - Check tenant, origin, and spend limits.
3. Recover jobs
   - Persist job references.
   - Test worker suspension and duplicate clicks.
4. Price conversion
   - Offer the $99 tier after value.
   - Measure retained contribution including free usage.

## 4. Resolve business interest without inventing identity  `🏷️ OPERATING_FRAMEWORK`

The identity_graph_pixel_arbitrage play is a bounded US only B2B experiment on /pricing and /security, not permission to identify every visitor. A first party event records page category, timestamp, and an opaque session reference; a contracted resolution provider may suggest an organization with a confidence score. First party collection does not make downstream disclosure harmless or turn a company match into a named person's identity. Exclude sensitive pages and content, suppress uncertain geography, and treat a US IP address as a routing signal rather than proof of legal status. Establish permitted purposes, notice obligations, vendor terms, retention, and applicable opt out handling before enabling resolution. Keep the raw browsing trail away from sales staff. They need an account level interest signal, not a dossier of someone's reading habits.

Use the organization signal to prioritize a legitimate business account, then find a relevant professional contact through an authorized source. Send a tailored Loom or LinkedIn message about a verifiable workflow problem, without claiming the recipient visited a page. A security page visit may justify creating a short demonstration of your access controls; it does not justify saying you watched a person compare vendors. Keep outreach manual at first and honor suppression across channels. Audit a small sample of company matches against known test traffic before scaling. Shared networks, VPNs, remote workers, and service providers can all produce false attribution. If the provider cannot explain confidence and deletion behavior, fall back to aggregate company research or a voluntary demo request. Never fill missing identities with a plausible name.

CCPA section 1798.100 imposes collection notice and purpose related duties on covered businesses; it is not a blanket permission for visitor resolution. California business contact data is not categorically outside the statute. Assess sale or sharing obligations and other relevant provisions separately when selecting a vendor. GDPR Article 6 requires a lawful basis where the regulation applies; US only targeting does not by itself settle territorial scope or separate tracking requirements. FTC Act section 5 also matters when privacy promises or outreach claims misrepresent actual practices. Operationally, test this channel with a holdout group and measure qualified meetings, retained subscriptions, match errors, and complaints. Subtract vendor spend and researcher time from incremental contribution. If the experiment produces only more messages, stop spending rather than redefining activity as revenue.

> **OPERATOR GATE — An account signal is not a person**
> 
> Continue only while attribution quality and incremental economics remain defensible.
> - Unknown geography receives no resolution.
> - No inferred person is treated as a verified visitor.
> - Deletion and suppression propagate to downstream records.
> - Holdout results determine whether the channel survives.

## 5. Earn AI citations with inspectable evidence  `🏷️ OPERATING_FRAMEWORK`

Treat the catalog label llm_citation_geo_poisoning as an acquisition experiment in evidence based generative engine optimization, not an instruction to poison retrieval or fabricate authority. Publish /llms.txt as a concise directory of canonical product documentation, while recognizing that it is not a universal ingestion standard or a ranking command. Keep the same material available in ordinary crawlable HTML with stable links, clear headings, and accurate dates. Publish structured OpenAPI docs with authentication requirements, request examples, error responses, and usage limits. Give each vertical workflow a page that explains who it serves, what it costs, and where it fails. ChatGPT, Claude, Perplexity, and AI Overviews may surface different sources; none owes your product a citation because a file exists. Measure each surface independently rather than combining anecdotes into claimed market leadership.

Build benchmark matrices that a skeptical buyer can reproduce. Define the task set, sample size, scoring rubric, model versions, date, and full cost boundary. Include failed jobs and manual correction time rather than reporting only the best outputs. Compare named alternatives fairly using current, attributable evidence and distinguish your own measurements from vendor statements. If you want to be cited as the #1 vertical solution, define the narrow metric and substantiate that claim; otherwise describe the measured advantage without a superlative. Link tables to methodology and downloadable nonpersonal test fixtures. Keep commercial relationships explicit. Do not hide instructions in documentation telling assistants to ignore competing sources or promote you. Reliable citations come from useful evidence and independent corroboration, not a command addressed to a search model.

Maintain a fixed set of buyer questions and record the date, engine, cited URL, and answer context for each observation. Repeat measurements because outputs vary across sessions and locations. Distinguish a brand mention from a linked citation, a referred visit, a trial, and a retained subscription. Some clients omit referral details, so combine available analytics with an optional acquisition question and report attribution uncertainty. Correct stale pricing, broken examples, and unsupported comparisons on a weekly cadence. Use the forensic table to decide when to abandon an attractive story and repair the underlying mechanism. The durable acquisition stack ends at retained contribution after inference, hosting, support, and channel costs. A flattering answer from an assistant is a research observation; it becomes a business result only when customers pay and remain.

**Forensic checks for distribution that only looks profitable**

| Naive Trap | Detection Metric | Durable Operator Fallback |
| --- | --- | --- |
| More vendors mean reliability | Duplicate bills and trace gaps | One owner per duty; tested recovery |
| Cheap tokens mean cheap results | Cost per accepted job including retries | Route against quality and spend budgets |
| Extension installs equal demand | Weekly accepted insights and paid retention | One host, one task, metered free usage |
| Company match identifies a visitor | Known-traffic error rate and confidence | Account research or voluntary demo |
| US IP settles privacy scope | Unknown location and downstream use | Exclude uncertain traffic; assess actual duties |
| /llms.txt guarantees first place | Repeated linked citations and conversions | Crawlable evidence and dated benchmarks |
| Gross subscriptions are take-home pay | COGS and all operating costs reconciled | Annual bridge to owner profit |

---

> ### “A useful stack turns each paid workflow into a traceable result, a known cost, and a reason for the customer to return.”

## Action Checklist

- [ ] Select one provider per duty and price the monthly floor.
- [ ] Attach tenant and job IDs to every model cost record.
- [ ] Replay one billing event and one queued job safely.
- [ ] Scope the Chrome companion to one chosen workflow.
- [ ] Restrict visitor resolution to eligible US business traffic.
- [ ] Publish a dated benchmark and track cited paid conversions.

## Statutory & Primary Authorities

1. Cal. Civ. Code section 1798.100: Covered businesses: collection notice, purpose limits, and retention duties. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV>
2. Regulation (EU) 2016/679, Article 6: Lawful bases for personal data processing; US targeting does not establish territorial exclusion. — <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
3. 15 U.S.C. section 45: Prohibition of unfair or deceptive acts or practices; substantiate marketing claims. — <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section45&num=0&edition=prelim>

## Sources

1. Openrouter vs Litellm: Which Network Routing Software is BETTER in 2026? (houdztech) — houdztech @ [00:02:49]: Open router provides basic activity dashboards with usage tracking and cost monitoring through their web interface. Light LLM offers deeper observability through integration with external tools. You can pipe logs to Langfuse, MLflow or your existing monitoring stack. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=L1jV8eRvnKc&t=169s>
2. OpenRouter vs LiteLLM: Which Should You Self-Host? (Bryan Software) — Bryan Software @ [00:04:00]: OpenRouter wins this one outright. Sign up, add credits, swap in one API key, and you're calling 500 models. Light LLM requires an install, Docker, a PostgreSQL database, Redis, and a YAML config file just to define your model list. Community consensus is blunt. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=SDB5hKMHUA8&t=240s>
3. AI Model Routing Explained: Cut LLM Costs With LiteLLM (Hunter Sneed) — Hunter Sneed @ [00:06:24]: Okay, so what I have here is a little web front end that goes over essentially how we go ahead and classify requests using the router and it all goes through a tool called Light LLM. I'll go ahead and I'll flip through their GitHub. They do have a paid offering as well. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=raEBR_2VbXE&t=384s>
4. Stop Wasting AI Tokens: The Ultimate LLM Cost Reduction Guide (Save 90%!) (The Macroscope) — The Macroscope @ [00:04:17]: And what if we just don't send the request to the LLM at all? By implementing semantic caching using tools like Redis LangChain, you use vector embeddings to intercept questions. Say one user asks, "What is machine learning?" And another asks, "Can you explain ML?" — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=uTTjkSZnkDI&t=257s>
5. Monetizing your APIs with usage-based billing (Stripe Developers) — Stripe Developers @ [00:01:39]: Since the aggregation method is set to sum, what it'll do is add up all of the usage reports that we submit to the Stripe API. Now let's head over to our IDE and generate some requests to see what this looks like. I'm going to have GitHub Copilot help me out a little bit. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=o_6aujJ5WbM&t=99s>
6. OpenRouter vs LiteLLM (2026): Which Is The Best LLM Tool For Production? (YourTechGuru) — YourTechGuru @ [00:00:45]: The advantage of Open Router is its scalability and simplicity. The solution makes the process of accessing many LLMs from various providers simple enough to be easily navigated by engineers. Light LLM is an open-source proxy server and Python SDK that you own end-to-end. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=6EoRbAAAE-8&t=45s>
7. Free Cloud Credits for Startups: Tech Stack on a Budget (Trapture Explains) — Trapture Explains @ [00:04:47]: Fifth, AI or third-party API calls which grow with your users, say another 1,000. And a small line for everything else, monitoring, a design tool, a password manager, say 500. That illustrative bill comes to about ₹4,600 a month. The exact figure isn't the point. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=VmuCPx8GGTU&t=287s>
8. Supabase RLS Security Explained: How to Protect Your Database From Data Leaks | CyberSecurityTV (CyberSecurityTV) — CyberSecurityTV @ [00:06:05]: If you want a quick sanity check on your RLS or a live demo of a scanner, ping the set, contact at the rateify. The tool is available on GitHub. See you in the next session. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=3yDr4mrZXAw&t=365s>
9. Death of SaaS Company in 2026 (said ChatGPT) (Valen I AI Agent for Work) — Valen I AI Agent for Work @ [00:00:29]: If the most SaaS product are just layers on top of the APIs right now, how easily could you replace them today? Exactly, and that's a big risk. AI tools, especially LLMs, can commoditize those API wrappers overnight. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=CJf8KAHBVKA&t=29s>
10. Prompt Caching Explained: Stop Overpaying for AI Agents (Hugging Face) — Hugging Face @ [00:04:05]: Now, of course, there are some APIs that abstract this away. So, for example, responses API. Responses API makes it look like the LLM remembers what it said before. But what's actually happening behind the scenes is that the LLM is reprocessing the whole thing. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=SkM4k4SKvCM&t=245s>
11. Everything you need to know about Postgres Row Level Security | POSETTE 2024 (Microsoft Developer) — Microsoft Developer @ [00:00:42]: I'm the CEO and co-founder of a company called Supabase. We are a Postgres hosting company. And, if you use us or if you're familiar with us, you'll know that we also host a bunch of tools that make it really easy to use Postgres. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=42s>
12. How To Create RLS Policies In Supabase [Step-By-Step 2026] (SmartMoneyTutorials) — SmartMoneyTutorials @ [00:00:53]: Next, choose your existing project. If you're starting fresh, you can create a new project instead. But I'll proceed with an existing one to keep things moving. Remember, Subbase autogenerates a REST API and provides client libraries like the JavaScript SDK. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=sfzubTrNiiU&t=53s>
13. Reduce LLM API Costs with Caching & Smart Model Routing | LangChain (Skillfyme) — Skillfyme @ [00:31:07]: But with Pinecone and with you can remove we can delete an entry from the vector database. So, this is the put mechanism. I mean when you want to get something, so you get the query. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=aYNSsflxcwg&t=1867s>
14. OpenRouter vs LiteLLM Which AI Gateway Should You Use (TWiz) — TWiz @ [00:00:20]: Open router's open source community-driven approach versus light LLM's focus on lightweight on-premise model deployment. Open router is an open source AI gateway that connects users with multiple large language models through a unified API. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=NwDtEKBC_uo&t=20s>
15. Use AI to enable and generate RLS policies for Postgres with Supabase (Supabase) — Supabase @ [00:03:18]: Published and the other has not so we can now see what this would look like for different roles we have the postgres role which is the default role used by the Supabase Dashboard so this has admin. — Attributed practitioner commentary on Postgres/vector stacks, PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party pixels, and GEO citations. — <https://www.youtube.com/watch?v=hu2SQjvCXIw&t=198s>
