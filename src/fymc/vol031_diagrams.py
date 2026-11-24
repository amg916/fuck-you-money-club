"""Volume 031 diagrams: Uber & Commercial Fleet Arbitrage."""

from typing import Any, Dict, List

VOLUME_031_SUBTITLE: str = (
    "Uber Fleet Partner SUVs at $600 a Week, Black-Car Private Clienteles at "
    "$100 an Hour, $350-$450 Weekly Gig Rentals, Co-Hosting Off the Gross, and "
    "the Plate, Insurance, Kill-Switch, and Booking-Software Gates That Guard "
    "the Margin"
)


def build_volume_031_diagrams_data() -> List[Dict[str, Any]]:
    """Return the eight structured diagram dicts for Volume 031."""
    diagrams: List[Dict[str, Any]] = []

    # Diagram 01: Uber Fleet launch sequence (Chapter 1).
    diagrams.append(
        {
            "diagram_id": "diag-01-uber-fleet-launch-sequence",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "Launching an Uber Fleet One SUV at a Time",
            "subtitle": "Account setup, VIN-first insurance, one vehicle, renter vetting, weekly pricing",
            "caption": (
                "Fleet operators sequence the launch so the costly mistakes happen on paper, "
                "not after the truck is bought: quote insurance on the VIN, start with one "
                "vehicle, and refuse renters who arrive without a limousine license and full "
                "payment."
            ),
            "assumptions_note": (
                "Step order follows the practitioner gates as reported. The $600 Suburban "
                "rate and $794 Houston permit stickers are single-operator figures, not "
                "market-wide rates."
            ),
            "note": (
                "Sources are Norman Tutorials (70EXcECzC70 @ 00:01:33), TJackk "
                "(GBM9d0WqM-0 @ 00:20:42, 9mwQox6xtqw @ 00:02:56, 4NPuQA-V4ZA @ 00:04:57, "
                "UTnHLaPqh1s @ 00:04:02), and Rideshare Professor (tKKCFcEvdl4 @ 00:05:29, "
                "7e3yD_HEDec @ 00:01:28, 4Y5_eWf85tM @ 00:13:13)."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Open the Fleet account",
                    "value": "Step 1",
                    "detail": (
                        "Sign up for Uber Fleet and submit tax information carefully, "
                        "double-checking it before continuing (Norman Tutorials)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Quote insurance on the exact VIN",
                    "value": "Step 2",
                    "detail": (
                        "Get the commercial auto quote off the VIN before buying, because once "
                        "the vehicle is bought the owner is stuck with it (TJackk)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Buy one large black SUV",
                    "value": "Step 3",
                    "detail": (
                        "Start with one vehicle, not five (Rideshare Professor). Keep a reserve "
                        "for licensing, permits such as $794 Houston stickers per SUV, insurance, "
                        "and a surprise repair week (TJackk)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Vet the renter before handoff",
                    "value": "Step 4",
                    "detail": (
                        "No limousine license and no full payment up front means no car; a "
                        "repeating action-needed flag is a red alert for a bought account (TJackk)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Charge weekly and monitor driving",
                    "value": "Step 5",
                    "detail": (
                        "Suburbans lease at $600 per week, Cadillacs $100 more; speeding over 80 "
                        "earns one warning and the second time the driver is out "
                        "(Rideshare Professor)."
                    ),
                },
            ],
        }
    )

    # Diagram 02: Gig rental gross-to-net funnel (Chapter 6).
    diagrams.append(
        {
            "diagram_id": "diag-02-gig-rental-gross-to-net-funnel",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "From $1,600 Gross to About $700 Real Net Per Car",
            "subtitle": "Monthly economics of a cheap economy car rented weekly to gig drivers",
            "caption": (
                "Etienne Elsaesser strips the influencer math on a $3,000-$6,000 Corolla-class "
                "rental down to about $700 net per car per month once insurance, maintenance, "
                "a total-loss reserve, processing, and cleaning are paid."
            ),
            "assumptions_note": (
                "Gross and net endpoints are as stated by Etienne Elsaesser; intermediate "
                "stages are simple subtraction of the stated deductions, and insurance is "
                "reported as $300 or more, so the post-insurance stage is an upper bound."
            ),
            "note": (
                "Etienne Elsaesser (amfsF8yd5hg @ 00:06:15, l8b3Oi2g48I @ 00:00:00); "
                "$400+ per week yielding a $1,600 monthly minimum per Alex Auto "
                "(Sukdr8-ecMM @ 00:05:14)."
            ),
            "stages": [
                {
                    "label": "Monthly gross at $400+ per week",
                    "value": 1600,
                    "display": "$1,600",
                    "conversion": "Starting gross",
                    "detail": "Weekly rent of $350-$450 paid upfront; Alex Auto cites a $1,600 monthly minimum.",
                },
                {
                    "label": "After insurance",
                    "value": 1300,
                    "display": "About $1,300",
                    "conversion": "Less $300+ insurance",
                    "detail": "Insurance runs $300 or more per car per month.",
                },
                {
                    "label": "After maintenance",
                    "value": 1100,
                    "display": "About $1,100",
                    "conversion": "Less about $200 maintenance",
                    "detail": "Routine maintenance runs about $200 per car per month.",
                },
                {
                    "label": "After total-loss reserve",
                    "value": 900,
                    "display": "About $900",
                    "conversion": "Less $200 total-loss reserve",
                    "detail": "A $200 monthly reserve funds the car that eventually gets totaled.",
                },
                {
                    "label": "Real net per car",
                    "value": 700,
                    "display": "About $700",
                    "conversion": "Less processing and cleaning",
                    "detail": "Payment processing and cleaning close the gap to about $700 net.",
                },
            ],
        }
    )

    # Diagram 03: Weekly fleet-car margin waterfall (Chapter 3).
    diagrams.append(
        {
            "diagram_id": "diag-03-fleet-car-weekly-margin-waterfall",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "Where $1,500 in Weekly Fares Goes on a Fleet Car",
            "subtitle": "Uber commission and driver share leave the owner $225 per vehicle",
            "caption": (
                "Owners Risk models a small fleet where $1,500 in weekly fares loses 25% to "
                "Uber and $900 to the driver, leaving $225 per car and about $4,500 per month "
                "across five cars, with the warning that Uber's algorithm controls the margin."
            ),
            "assumptions_note": (
                "Gross, commission rate, driver share, per-car net, and five-car monthly net "
                "are as stated by Owners Risk; the $375 commission and $1,125 subtotal are "
                "arithmetic on those figures. The final bar is on a monthly, five-car basis."
            ),
            "note": "Owners Risk (oDmpBy9CTek @ 00:07:27).",
            "bars": [
                {"label": "Weekly gross fares", "value": 1500, "display": "$1,500", "kind": "total"},
                {"label": "Uber commission at 25%", "value": -375, "display": "-$375", "kind": "deduction"},
                {"label": "After Uber commission", "value": 1125, "display": "$1,125", "kind": "total"},
                {"label": "Driver keeps", "value": -900, "display": "-$900", "kind": "deduction"},
                {"label": "Owner net per car per week", "value": 225, "display": "$225", "kind": "result"},
                {"label": "Five-car owner net per month", "value": 4500, "display": "About $4,500", "kind": "result"},
            ],
        }
    )

    # Diagram 04: Monthly cost of revenue vehicles (Chapter 2).
    diagrams.append(
        {
            "diagram_id": "diag-04-revenue-vehicle-monthly-cost",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "The Monthly Nut on a Revenue Vehicle",
            "subtitle": "Black SUV all-in costs versus the components and a WAV minivan route",
            "caption": (
                "Stack the full monthly cost before signing: a 100 percent financed Navigator "
                "runs $3,000 to $3,300 all in, a 2025 Escalade at a 620 credit score lands "
                "near $3,500, and a used Sienna WAV runs about $1,300 while still qualifying "
                "for XL."
            ),
            "assumptions_note": (
                "Where a speaker gave a single figure, min, max, and typical are set equal. "
                "Navigator typical uses the almost-$3,000 figure cited when renting out the "
                "former Tesla. Escalade figures reflect one caller's credit profile."
            ),
            "note": (
                "ESCAPE THE MATRIX (fPh6slkW9Tk @ 00:05:15, fPh6slkW9Tk @ 00:06:08, "
                "fPh6slkW9Tk @ 00:09:45, Y8ppyxLqw9E @ 00:02:13) and Yusuf Benallal "
                "(xrJ-xGav6Xo @ 00:03:19)."
            ),
            "unit": "USD per month",
            "bars": [
                {
                    "label": "2025 Escalade at a 620 credit score",
                    "min": 2993.81,
                    "max": 3500,
                    "typical": 3500,
                    "display": "$2,993.81 note, about $3,500 with insurance",
                },
                {
                    "label": "Lincoln Navigator all-in, NYC Black",
                    "min": 3000,
                    "max": 3300,
                    "typical": 3000,
                    "display": "$3,000 to $3,300",
                },
                {
                    "label": "Navigator car note at 0% APR",
                    "min": 1733,
                    "max": 1733,
                    "typical": 1733,
                    "display": "$1,733",
                },
                {
                    "label": "Used Toyota Sienna WAV all-in",
                    "min": 1300,
                    "max": 1300,
                    "typical": 1300,
                    "display": "About $1,300",
                },
                {
                    "label": "Navigator commercial liability",
                    "min": 370,
                    "max": 370,
                    "typical": 370,
                    "display": "$370",
                },
            ],
        }
    )

    # Diagram 05: Going-private gate check (Chapter 5).
    diagrams.append(
        {
            "diagram_id": "diag-05-private-black-car-gate-check",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Ready to Move From Uber Black to Private Clients",
            "subtitle": "Four gates before taking direct bookings",
            "caption": (
                "Operators who left the app agree Uber Black is a launchpad, not a business. "
                "Black Truck Mick grossed $15,070 in month one on a rented SUV, but only after "
                "pricing for the day and moving direct work to $100 an hour."
            ),
            "assumptions_note": (
                "Gate order is an editorial sequence of practitioner gates; rates and the "
                "$300 daily break-even reflect one rented SUV costing $1,250 a week."
            ),
            "note": (
                "Fares and Frustrations (_UpXw8QDal8 @ 00:06:26), Business with Mide "
                "(4TzKcRuyrHY @ 00:00:44), Black Truck Mick (uODRGjORQF4 @ 00:10:28, "
                "uODRGjORQF4 @ 00:14:11), My Chauffeur Life (Y-1AudoR8JA @ 00:04:09), and "
                "Luxury Transportation Academy / Podcast (yg-RtCxYcG8 @ 00:09:02)."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Are the TCP, permits, and airport credentials locked in?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Hold launch; operating without the TCP is illegal and the wrong airport "
                        "permit or credential means lost bookings."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Does pricing cover the day, not just the ride?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Reprice; Black Truck Mick needed $300 a day to cover a rented SUV and "
                        "admits $40 for six riders was too little."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Is a weekly reserve funded with every expense tracked?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Build the reserve first, before a luxury repair costing thousands parks "
                        "the car for weeks."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Do reservations live in a CRM or booking system?",
                    "pass_next": (
                        "Take direct work at $100 an hour, $80 for affiliates, fed by hotel "
                        "concierges, event planners, and corporate assistants."
                    ),
                    "fail_action": (
                        "Pull bookings out of WhatsApp and text threads, where nine times out "
                        "of 10 they get lost."
                    ),
                },
            ],
        }
    )

    # Diagram 06: Off-platform software stack (Chapter 11).
    diagrams.append(
        {
            "diagram_id": "diag-06-owned-booking-pipe-stack",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "Own the Booking Pipe",
            "subtitle": "The software spokes around an off-Turo rental operator",
            "caption": (
                "After Turo revoked the unofficial API access Fleetwire and CarSync relied on, "
                "operators converged on a direct website plus automated contracts, payment "
                "links, e-signatures, and double-booking blocks."
            ),
            "assumptions_note": (
                "Pricing is as quoted by each speaker at the time; Brandon Duff reported a "
                "$34 Fleetwire entry plan versus the roughly $20 tier cited by Alex Auto."
            ),
            "note": (
                "Alex Auto (0Q8BZGkkigM @ 00:01:39, 0Q8BZGkkigM @ 00:05:17), "
                "Mike_Thebusinessman (1Va2FwAMf2A @ 00:05:18, 1Va2FwAMf2A @ 00:06:27, "
                "1Va2FwAMf2A @ 00:17:13), and Fleet Brothers (VCL-xD3r5VU @ 00:01:08)."
            ),
            "center": {
                "role": "Off-Turo rental operator",
                "headcount": "Owner plus two staff accounts on the Fleetwire entry tier",
                "focus": "Direct bookings that survive a Turo sync shutdown",
            },
            "spokes": [
                {
                    "role": "Fleetwire",
                    "type": "Booking site and payment links",
                    "kpi": "About $20 per month for 5 cars, roughly $240-$250 at 150 cars",
                },
                {
                    "role": "Fleet Finesse",
                    "type": "Booking engine with no car caps",
                    "kpi": "$69 per month standard, $197 deluxe with custom domain",
                },
                {
                    "role": "Stripe deposit holds",
                    "type": "Payment layer",
                    "kpi": "Avoids the 2.7%-2.8% fee; hold falls off on day 7",
                },
                {
                    "role": "HQ Rentals",
                    "type": "Rental management suite",
                    "kpi": "Near $90 plus a $450-$500 setup fee; car caps forced a migration",
                },
            ],
        }
    )

    # Diagram 07: Credential and cover outlay stack (Chapter 4).
    diagrams.append(
        {
            "diagram_id": "diag-07-tcp-credential-cover-stack",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "What a TCP Black-Car Credential and Cover Cost Up Front",
            "subtitle": "Khushnud Numonov's EPN, TCP filing, commercial premium, and card fee",
            "caption": (
                "The TCP belongs inside an LLC or corporation and dies on sequencing errors; "
                "the bigger bill is the commercial premium, which Khushnud Numonov paid "
                "upfront on a 0 percent APR card instead of a 23.8 percent APR loan."
            ),
            "assumptions_note": (
                "Bucket figures are as reported by Khushnud Numonov; the total range is the "
                "arithmetic sum of the buckets, with the low end on Class B and the high end "
                "on Class A. Airport permits are excluded because no cost was given."
            ),
            "note": (
                "Khushnud Numonov (67saVKNzHxc @ 00:07:16, 67saVKNzHxc @ 00:10:24, "
                "IqvMzwtwzrI @ 00:05:26, IqvMzwtwzrI @ 00:10:07)."
            ),
            "total_range": "About $9,516 to $10,016",
            "buckets": [
                {
                    "label": "DMV EPN",
                    "low": 15,
                    "high": 15,
                    "notes": "About $15, takes one to two weeks, and stalls the TCP portal until it clears.",
                },
                {
                    "label": "TCP filing fee",
                    "low": 1000,
                    "high": 1500,
                    "notes": "$1,000 Class B with a 125-mile limit; $1,500 Class A for unlimited runs.",
                },
                {
                    "label": "Uber Black sedan commercial premium",
                    "low": 8161,
                    "high": 8161,
                    "notes": "Lancer Insurance cash price per year; financing meant $2,155 down and 23.8% APR.",
                },
                {
                    "label": "Card fee to pay the premium upfront",
                    "low": 340,
                    "high": 340,
                    "notes": "Offset by $170 cash back, saving about $441 versus the financed loan.",
                },
            ],
        }
    )

    # Diagram 08: Fix-before-scale roadmap (Chapter 12).
    diagrams.append(
        {
            "diagram_id": "diag-08-fix-before-scale-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Fix the Process Before Adding Cars",
            "subtitle": "Four weeks of systems before the fleet grows",
            "caption": (
                "Operators running 15 to 300+ cars agree scale only works once systems exist; "
                "King of Rentals warns that adding cars to a bad process just adds fuel to "
                "the fire."
            ),
            "assumptions_note": (
                "The four-week grouping is an editorial sequence of practitioner gates and "
                "pro-tips, not a timeline any single operator reported."
            ),
            "note": (
                "King of Rentals (706e4cdleYQ @ 00:00:22, OBbGsDAi0xA @ 00:08:08), Etienne "
                "Elsaesser (3dvvSrh_cus @ 00:06:44, VUKM00PHEmI @ 00:25:20, "
                "3dvvSrh_cus @ 00:09:28, VUKM00PHEmI @ 00:07:36), and Car Rental Coach "
                "(lOTgf5qQVJ8 @ 00:02:35)."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Audit the operating process",
                    "deliverable": "Timestamped check-in and check-out evidence on every rental",
                    "gate": "No new cars added onto a process that is no bueno",
                },
                {
                    "week": "Week 2",
                    "title": "Lock payment and guest insurance",
                    "deliverable": (
                        "Phone each guest's insurer, confirm the policy is not brand new, ask "
                        "about exclusions, and pull a binder"
                    ),
                    "gate": "No reservation without payment, with the deposit taken on rental day",
                },
                {
                    "week": "Week 3",
                    "title": "Staff with per-job vendors",
                    "deliverable": "Per-job 1099 vendors for cleaning, delivery, and turnaround",
                    "gate": "Do not get employees",
                },
                {
                    "week": "Week 4",
                    "title": "Protect the asset and the account",
                    "deliverable": (
                        "OBD2 tracker concealed behind a splitter, plus an oil, coolant, washer "
                        "fluid, and wiper check on every returned car"
                    ),
                    "gate": "Never cancel from the host side; call Turo to cancel instead",
                },
            ],
        }
    )

    return diagrams


VOLUME_031_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Black-Car Fleet Ladder",
        "subtitle": (
            "From a $600-a-Week Uber Fleet Suburban to $100-an-Hour Private Chauffeur Work"
        ),
        "audience": (
            "Drivers and small investors weighing Uber Black SUVs, Fleet Partner rentals, "
            "and a private black-car clientele"
        ),
        "research_basis": (
            "Rideshare Professor's $600 weekly Suburban rate and 15-month payoff, ESCAPE THE "
            "MATRIX's $1,733 Navigator note, Black Truck Mick's $15,070 first month, and "
            "Fares and Frustrations' 80-percent-versus-100-percent framing."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=7e3yD_HEDec&t=88s",
            "https://www.youtube.com/watch?v=4Y5_eWf85tM&t=351s",
            "https://www.youtube.com/watch?v=fPh6slkW9Tk&t=315s",
            "https://www.youtube.com/watch?v=uODRGjORQF4&t=0s",
            "https://www.youtube.com/watch?v=TxZA7z6wXLg&t=54s",
        ],
        "validation_status": "Grounded strictly in Vol. 031 YouTube practitioner transcripts.",
    },
    {
        "title": "The $400-a-Week Rental Machine",
        "subtitle": (
            "Cheap Paid-Off Economy Cars, Gig-Driver Renters, Kill Switches, and a 90-Day Payback"
        ),
        "audience": (
            "Operators renting $3,000-$6,000 economy cars to Uber, Lyft, and DoorDash drivers "
            "by the week"
        ),
        "research_basis": (
            "Etienne Elsaesser's $350-$450 weekly rate and about $700 real net, King of "
            "Rentals' $1,000 private net versus roughly $500 on Turo, Kel King's 90-day "
            "golden rule, and Alex Auto's tracker and kill-switch mandate."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=l8b3Oi2g48I&t=0s",
            "https://www.youtube.com/watch?v=amfsF8yd5hg&t=375s",
            "https://www.youtube.com/watch?v=DOrgMXhPDXs&t=456s",
            "https://www.youtube.com/watch?v=7l7A5buuie0&t=2491s",
            "https://www.youtube.com/watch?v=bHUp-OA4bH8&t=520s",
        ],
        "validation_status": "Grounded strictly in Vol. 031 YouTube practitioner transcripts.",
    },
    {
        "title": "Other People's Cars, Plates, and Permits",
        "subtitle": (
            "Co-Hosting Splits Off the Gross, NYC TLC Plate Rentals, and California TCP Sequencing"
        ),
        "audience": (
            "Operators scaling without owning every vehicle, through co-hosted cars or "
            "scarce for-hire credentials"
        ),
        "research_basis": (
            "Delano Green's over-$100k monthly profit near 99 cars, Peak Auto Academy's 23% "
            "owner return on a Yukon, Demario Mccowan's cut-off-the-gross rule, Khushnud "
            "Numonov's $1,000-$1,500 TCP fees, and FastTrack's $289 weekly plate-plus-insurance."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=SPoQzQlFhXg&t=533s",
            "https://www.youtube.com/watch?v=3kqux9OEEfY&t=167s",
            "https://www.youtube.com/watch?v=b4HG8nxaQlU&t=377s",
            "https://www.youtube.com/watch?v=67saVKNzHxc&t=624s",
            "https://www.youtube.com/watch?v=DiLCf_drK0E&t=511s",
        ],
        "validation_status": "Grounded strictly in Vol. 031 YouTube practitioner transcripts.",
    },
]
