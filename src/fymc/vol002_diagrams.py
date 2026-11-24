VOLUME_002_SUBTITLE: str = (
    "Find the Funds, Prove the Claim, Reach Owners and Heirs, "
    "and Build a Repeatable Recovery Pipeline"
)


def build_volume_002_diagrams_data() -> list[dict]:
    return [
        {
            "diagram_id": "diag-01-find-verify-contact-document-track",
            "chapter_number": 1,
            "title": "From Auction Record to Recovery Claim",
            "subtitle": (
                "Connect the sale, the available funds, the entitled claimant, "
                "and the holding office's requirements."
            ),
            "caption": (
                "Ted Thomas describes narrowing auction results to excess proceeds. "
                "Eric Richardson of Money Making Juggernaut emphasizes county "
                "procedures, while Bob Diamond emphasizes identity and agreements."
            ),
            "assumptions_note": (
                "Richardson's accessible-county approach requires knowing the "
                "local claim process. Diamond's agreement examples are not "
                "universal filing requirements."
            ),
            "note": (
                "SurplusFundsRiches warns that old balances may already be claimed. "
                "Diamond identifies signing the wrong person as a recurring failure."
            ),
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Find sold-auction candidates",
                    "value": "Step 1",
                    "detail": (
                        "Ted Thomas starts with auction results and narrows to "
                        "properties sold for more than the county originally asked."
                    ),
                },
                {
                    "step": "02",
                    "label": "Verify funds and competing debt",
                    "value": "Step 2",
                    "detail": (
                        "SurplusFundsRiches checks list age, continuing availability, "
                        "ownership, and debt as they stood at the sale."
                    ),
                },
                {
                    "step": "03",
                    "label": "Locate the entitled claimant",
                    "value": "Step 3",
                    "detail": (
                        "Richardson uses locating research and repeatable outreach. "
                        "Diamond checks that the person is the intended claimant "
                        "rather than a relative or namesake."
                    ),
                },
                {
                    "step": "04",
                    "label": "Agree and assemble documents",
                    "value": "Step 4",
                    "detail": (
                        "Diamond describes a fee agreement, power of attorney, "
                        "assignment, and payment direction. Richardson first "
                        "establishes how the selected county accepts claims."
                    ),
                },
                {
                    "step": "05",
                    "label": "Submit and track the claim",
                    "value": "Step 5",
                    "detail": (
                        "Richardson follows the county's filing route. Unclaimed CEO "
                        "identifies the actual holding office and timing, while "
                        "Diamond warns against discovering deadlines after signing."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-overseas-recovery-balance",
            "chapter_number": 6,
            "title": "An Overseas Recovery Through Contact and Paperwork",
            "subtitle": (
                "Danielle reports $97,000 reduced to $87,000 before negotiating "
                "a 20% fee."
            ),
            "caption": (
                "Danielle, appearing on Money Making Juggernaut, describes an "
                "overseas recovery using WhatsApp, Google Translate, and "
                "translated notarizations."
            ),
            "assumptions_note": (
                "Danielle reports a balance reduction, not a lead-conversion funnel. "
                "The $87,000 repeated through contact, documentation, and agreement "
                "is the same after-tax reference balance, not a separately measured "
                "balance at each milestone."
            ),
            "note": (
                "Danielle's 20% is a negotiated fee, not a conversion rate. "
                "The $87,000 is not the owner's net receipt after that fee. "
                "Contact and documentation milestones do not establish an exact "
                "chronology for every exchange."
            ),
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Initial reported funds",
                    "value": 97000,
                    "display": "$97,000",
                    "conversion": "Not a lead-conversion measure",
                    "detail": (
                        "Danielle identifies this amount before the reduction "
                        "for back taxes."
                    ),
                },
                {
                    "label": "After back taxes",
                    "value": 87000,
                    "display": "$87,000",
                    "conversion": "Back-tax adjustment",
                    "detail": (
                        "Danielle reports that back taxes reduced the funds "
                        "to this amount before the fee discussion."
                    ),
                },
                {
                    "label": "Overseas communication",
                    "value": 87000,
                    "display": "$87,000 reference balance",
                    "conversion": "No separate balance change reported",
                    "detail": (
                        "Danielle uses WhatsApp and Google Translate to communicate "
                        "with the overseas owner. The amount remains a reference "
                        "to the reported after-tax funds."
                    ),
                },
                {
                    "label": "Translated notarizations",
                    "value": 87000,
                    "display": "$87,000 reference balance",
                    "conversion": "No separate balance change reported",
                    "detail": (
                        "Translated notarizations support Danielle's recovery work. "
                        "No separate documentation-stage balance is reported."
                    ),
                },
                {
                    "label": "Negotiated recovery agreement",
                    "value": 87000,
                    "display": "$87,000 before the recovery fee",
                    "conversion": "20% negotiated fee, not conversion",
                    "detail": (
                        "Danielle reports negotiating a 20% fee and completing "
                        "the overseas recovery. This amount is not the operator's "
                        "fee or the owner's net distribution."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-sale-minus-debt-examples",
            "chapter_number": 3,
            "title": "Reconstruct the Surplus Before Pursuing It",
            "subtitle": (
                "Separate sale proceeds from the debt being collected, then "
                "investigate whether additional deductions remain."
            ),
            "caption": (
                "Nicole of Next Level VA reports the Tarrant reconstruction. "
                "Overage Acquisition supplies a separate introductory tax-sale "
                "illustration."
            ),
            "assumptions_note": (
                "Nicole's Tarrant figures and Overage Acquisition's illustration "
                "are independent examples. Each sale total begins a separate "
                "calculation; neither result establishes a claimant's final payout."
            ),
            "note": (
                "Nicole groups unpaid taxes, penalties, interest, and attorney "
                "fees in the reported deduction. Mark of Texas FundFinding "
                "warns that additional taxes can reduce preliminary proceeds."
            ),
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Tarrant sale price",
                    "value": 41000,
                    "display": "$41,000",
                    "kind": "total",
                },
                {
                    "label": "Tarrant taxes and charges",
                    "value": 13251.08,
                    "display": "-$13,251.08",
                    "kind": "deduction",
                },
                {
                    "label": "Tarrant reported surplus",
                    "value": 27748.92,
                    "display": "$27,748.92",
                    "kind": "result",
                },
                {
                    "label": "Separate illustrated sale",
                    "value": 100000,
                    "display": "$100,000",
                    "kind": "total",
                },
                {
                    "label": "Illustrated back taxes",
                    "value": 10000,
                    "display": "-$10,000",
                    "kind": "deduction",
                },
                {
                    "label": "Illustrated overage",
                    "value": 90000,
                    "display": "$90,000",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-reported-operating-expenses",
            "chapter_number": 2,
            "title": "Keep Operating Costs Separate From Recovery Volume",
            "subtitle": (
                "Reported mailing, document, notarization, and judicial-work "
                "expenses have different purchase units."
            ),
            "caption": (
                "Eric Richardson's student on Money Making Juggernaut reports "
                "mailing costs. Greg of Overage Acquisition reports a deed-copy "
                "cost, Nick Fullmer reports remote notarization, and Bob Diamond "
                "reports a judicial-work budget."
            ),
            "assumptions_note": (
                "Each entry is a quoted point amount, so its bounds and reference "
                "value are identical. These are not market distributions or "
                "independently established typical prices. Approximate quotes "
                "remain approximate."
            ),
            "note": (
                "Richardson's student's letter and campaign figures describe the "
                "same mailing economics at different quantities and must not be "
                "added together. Diamond's legal budget is not a list-purchase cost."
            ),
            "chart_type": "horizontal_bars",
            "unit": "USD per stated purchase or budget",
            "bars": [
                {
                    "label": "Student's single letter",
                    "min": 0.85,
                    "max": 0.85,
                    "typical": 0.85,
                    "display": "$0.85 per letter",
                },
                {
                    "label": "Student's mailing campaign",
                    "min": 850,
                    "max": 850,
                    "typical": 850,
                    "display": "$850 for 1,000 letters",
                },
                {
                    "label": "Greg's online grant-deed copy",
                    "min": 4,
                    "max": 4,
                    "typical": 4,
                    "display": "About $4 per copy",
                },
                {
                    "label": "Fullmer's remote notarization",
                    "min": 25,
                    "max": 25,
                    "typical": 25,
                    "display": "$25 for the reported affidavit notarization",
                },
                {
                    "label": "Diamond's judicial-work budget",
                    "min": 2500,
                    "max": 2500,
                    "typical": 2500,
                    "display": "$2,500 reported legal-work budget",
                },
            ],
        },
        {
            "diagram_id": "diag-05-mortgage-surplus-qualification",
            "chapter_number": 5,
            "title": "Qualify the Mortgage-Foreclosure Claim",
            "subtitle": (
                "A sale-price gap does not establish available funds, claimant "
                "priority, or a complete filing."
            ),
            "caption": (
                "Eric Richardson of Money Making Juggernaut checks actual debt, "
                "trustee disbursements, and prior claims. Friscia & Associates "
                "describes service and authority checks for a New Jersey motion."
            ),
            "assumptions_note": (
                "Richardson distinguishes county-held judicial funds from "
                "trustee-held nonjudicial funds. Friscia & Associates' motion "
                "requirements describe the New Jersey procedure discussed, "
                "not a universal filing packet."
            ),
            "note": (
                "Sternberg Law Group distinguishes a third-party winning bid "
                "from a bank-owned outcome. Richardson warns that an opening "
                "bid may not represent the amount actually owed."
            ),
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Did the sale produce a candidate after checking the "
                        "final judgment or writ rather than only the opening bid?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Retrieve the sale result and actual debt record. "
                        "Do not treat a bank-owned outcome as proven surplus."
                    ),
                },
                {
                    "gate": "G2",
                    "question": (
                        "Does the holding office's disbursement breakdown "
                        "establish that money remains after creditor payments?"
                    ),
                    "pass_next": "G3",
                    "fail_action": (
                        "Request the trustee's disbursement history. Pause "
                        "owner-recovery pursuit until remaining funds are established."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "Has prior contact and existing claim activity been checked?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Ask the claimant about prior recovery contact and "
                        "submitted claims, and resolve the existing-claim status."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Are ownership, authority, relevant liens, and the "
                        "applicable filing requirements established?"
                    ),
                    "pass_next": (
                        "Proceed through the applicable court or trustee claim route."
                    ),
                    "fail_action": (
                        "Resolve missing authority or filing defects. For Friscia's "
                        "New Jersey motion, check party service, estate authority "
                        "when needed, and agreement between the proposed order "
                        "and court amounts."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-fund-specific-recovery-responsibilities",
            "chapter_number": 11,
            "title": "One Recovery Operation, Distinct Claim Routes",
            "subtitle": (
                "Coordinate availability research, claimant authority, "
                "fund-specific documentation, and payment tracking."
            ),
            "caption": (
                "Scott White begins with availability and entitlement. "
                "Eric Richardson of Money Making Juggernaut explains bankruptcy "
                "research and entity authority. David Wilkerson and Pierce Law "
                "Group describe state-funds agreement requirements."
            ),
            "assumptions_note": (
                "These responsibilities do not establish a reported team size or "
                "require separate hires. Unclaimed CEO recommends proving the "
                "process repeatedly before delegating it to a virtual assistant."
            ),
            "note": (
                "Richardson's bankruptcy guest distinguishes four filings from "
                "one payout. A filed or accepted case is not collected revenue, "
                "and state-property requirements do not substitute for court requirements."
            ),
            "chart_type": "org_architecture",
            "center": {
                "role": "Recovery operator",
                "headcount": "Not specified",
                "focus": (
                    "Match the fund type, money holder, entitled claimant, "
                    "required agreement, and actual payment status."
                ),
            },
            "spokes": [
                {
                    "role": "Availability and case research",
                    "type": "Research responsibility",
                    "kpi": (
                        "Availability, existing claims, payment history, and the "
                        "origin of the funds checked before pursuit, following "
                        "Scott White and Richardson."
                    ),
                },
                {
                    "role": "Claimant and entity authority",
                    "type": "Entitlement responsibility",
                    "kpi": (
                        "Authorized corporate signatory identified and entitlement "
                        "supported, following Richardson's entity-research guidance."
                    ),
                },
                {
                    "role": "Agreement and claim preparation",
                    "type": "Fund-specific documentation responsibility",
                    "kpi": (
                        "Applicable timing, fee, disclosure, and signature "
                        "requirements checked, following Wilkerson and "
                        "Pierce Law Group."
                    ),
                },
                {
                    "role": "Submission and payment tracking",
                    "type": "Processing responsibility",
                    "kpi": (
                        "Filed, accepted, and paid cases tracked separately, "
                        "following Richardson's bankruptcy case discussion."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-competing-debt-allocation",
            "chapter_number": 4,
            "title": "The Listed Surplus Is Not the Owner's Remainder",
            "subtitle": (
                "Alfred Taren's worked example reduces $180,000 to $55,000 "
                "after competing debt."
            ),
            "caption": (
                "Alfred Taren illustrates a $95,000 second mortgage, $8,000 "
                "HOA debt, and $22,000 judgment against a $180,000 listed surplus."
            ),
            "assumptions_note": (
                "Taren gives fixed illustrative amounts, not low and high "
                "estimates. Equal bounds preserve those amounts without "
                "introducing an unsupported range."
            ),
            "note": (
                "Taren advises checking what the actual case or sale file has "
                "already paid and keeping owner-facing amounts estimated. "
                "The $55,000 remainder is not a promised payment or a stated "
                "net amount after recovery fees."
            ),
            "chart_type": "stacked_comparison",
            "total_range": "$180,000 illustrated listed surplus",
            "buckets": [
                {
                    "label": "Second mortgage",
                    "low": 95000,
                    "high": 95000,
                    "notes": (
                        "Taren's illustrated competing mortgage deduction."
                    ),
                },
                {
                    "label": "HOA debt",
                    "low": 8000,
                    "high": 8000,
                    "notes": (
                        "Taren's illustrated homeowners association deduction."
                    ),
                },
                {
                    "label": "Judgment",
                    "low": 22000,
                    "high": 22000,
                    "notes": (
                        "Taren's illustrated judgment deduction."
                    ),
                },
                {
                    "label": "Illustrated remainder",
                    "low": 55000,
                    "high": 55000,
                    "notes": (
                        "Taren's reported remainder after the listed deductions; "
                        "not an established claimant payout."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-08-repeatable-recovery-milestones",
            "chapter_number": 12,
            "title": "Build the Pipeline Around Verified Milestones",
            "subtitle": (
                "Choose a market, verify the opportunity, prepare the conversation, "
                "and maintain a documented handoff."
            ),
            "caption": (
                "Eric Richardson of Money Making Juggernaut, Spencer Vann, "
                "Surplus Funds List, and Surplus Systems emphasize repeatable "
                "execution, follow-up, case status, and operating references."
            ),
            "assumptions_note": (
                "The weekly cadence is a planning framework, not a four-week "
                "completion or payout schedule reported by these practitioners. "
                "Advance only when each verification gate is satisfied."
            ),
            "note": (
                "Richardson cautions against leaving employment before the "
                "pipeline can support delayed payments. Full Circle on Surplus "
                "Funds Secrets checks client information before a paid attorney "
                "handoff because a bad case can still incur the retainer."
            ),
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Commit to a market and process",
                    "deliverable": (
                        "A selected market and a repeatable operating reference, "
                        "following Vann's focus guidance and Surplus Systems' "
                        "master-SOP approach."
                    ),
                    "gate": (
                        "Avoid repeated niche switching before completing deals; "
                        "Vann describes that pattern as a source of lost months."
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Qualify the recovery opportunity",
                    "deliverable": (
                        "A researched case with actual debt checked and questions "
                        "about second mortgages and liens addressed, following "
                        "Richardson."
                    ),
                    "gate": (
                        "Do not equate the opening bid with everything owed or "
                        "proceed on an apparent surplus that has not been verified."
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Practice contact and maintain follow-up",
                    "deliverable": (
                        "Call practice using recorded wins and losses, following "
                        "Jordan Tejeda Marketing, with outreach and next actions "
                        "tracked through the Surplus Funds List CRM approach."
                    ),
                    "gate": (
                        "Keep replies actionable and claimant status current. "
                        "Richardson describes prompt calls after reply alerts; "
                        "Surplus Funds List maintains claimant portal status."
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Verify the handoff and track progress",
                    "deliverable": (
                        "Checked client information, an applicable processing "
                        "handoff, and ongoing tasks and claimant updates, following "
                        "Full Circle and Surplus Funds List."
                    ),
                    "gate": (
                        "Check the case before incurring an attorney retainer. "
                        "Maintain follow-up rather than treating a signed agreement "
                        "as a completed recovery."
                    ),
                },
            ],
        },
    ]


VOLUME_002_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Find the Funds. Prove the Claim.",
        "subtitle": (
            "Build a county-focused recovery practice with free records, "
            "verified balances, claimant research, and complete filing packets."
        ),
        "audience": (
            "New recovery operators who want a research-led starting point "
            "rather than expensive preparation or unsupported payout promises."
        ),
        "research_basis": (
            "Eric Richardson recommends starting where county results and filing "
            "procedures are understood. Alfred Taren prioritizes doing the work "
            "over preparation and warns that an auction gap is only a research "
            "starting point. Overage Acquisition checks for existing claims "
            "before working a case."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=_vsvjD8JvgU&t=131s",
            "https://www.youtube.com/watch?v=8-8koApqnYA&t=358s",
            "https://www.youtube.com/watch?v=YCb5jYZX_A8&t=242s",
            "https://www.youtube.com/watch?v=bpxSOg1_xbE&t=125s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 002 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Reach the Claimant Others Could Not",
        "subtitle": (
            "Use family research, patient follow-up, accessible paperwork, "
            "and verified authority to move difficult recovery cases."
        ),
        "audience": (
            "Operators prepared to work deceased-owner, displaced-owner, "
            "overseas, and communication-constrained cases."
        ),
        "research_basis": (
            "David Church describes reaching relatives through retained phone "
            "numbers and funeral providers, and switching to paper when email "
            "stalls. Danielle reports an overseas recovery supported by translation. "
            "Pierce Law Group distinguishes estate authority from an heir's "
            "eventual distribution."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=hA6VJ_GqGyc&t=39s",
            "https://www.youtube.com/watch?v=hA6VJ_GqGyc&t=314s",
            "https://www.youtube.com/watch?v=V_ycS3i_CMY&t=239s",
            "https://www.youtube.com/watch?v=WEohyFOyk2M&t=74s",
            "https://www.youtube.com/watch?v=ErS3fgilrDY&t=33s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 002 YouTube practitioner transcripts."
        ),
    },
    {
        "title": "Build a Recovery Pipeline, Not a Payout Promise",
        "subtitle": (
            "Separate signing, filing, acceptance, and payment with verified "
            "handoffs, recurring follow-up, and fund-specific procedures."
        ),
        "audience": (
            "Working recovery operators building a repeatable operation across "
            "foreclosure surplus, state property, or bankruptcy distributions."
        ),
        "research_basis": (
            "Surplus Funds List connects outreach, tasks, documents, and claimant "
            "updates. Eric Richardson distinguishes delayed payments from signed "
            "business, while the bankruptcy guest separates filings from actual "
            "payouts. Unclaimed CEO recommends proving a process before delegating, "
            "and Full Circle checks cases before paid attorney processing."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=lOnYUxDdOdI&t=250s",
            "https://www.youtube.com/watch?v=DK8BPV7WVvI&t=107s",
            "https://www.youtube.com/watch?v=waps0YmW8BI&t=150s",
            "https://www.youtube.com/watch?v=XdU7CVOntKk&t=237s",
            "https://www.youtube.com/watch?v=c2vik3KCA5g&t=1995s",
        ],
        "validation_status": (
            "Grounded strictly in Vol. 002 YouTube practitioner transcripts."
        ),
    },
]
