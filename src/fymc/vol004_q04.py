from __future__ import annotations

CHAPTER_4 = {
    "id": "Q4",
    "chapter_id": "Q4",
    "chapter_number": 4,
    "question_number": 4,
    "slug": "product-hunt-launch-postgresql-multi-tenant-rls",
    "question_prompt": "What do these videos teach about launching an app on Product Hunt, isolating tenant data in PostgreSQL, building multi-tenant APIs with EF Core or Claude Code and Prisma, and enabling, creating, and applying basic and advanced Supabase RLS policies—including AI-generated policies—to control access and prevent data leaks?",
    "kicker": "Q4 / THE BIG MONEY PLAYBOOKS",
    "title": "Launching on Product Hunt and Securing Multi-Tenant Apps with PostgreSQL RLS",
    "subtitle": "An app launch on Product Hunt, plus PostgreSQL tenant isolation and row-level authorization using Supabase, EF Core, Prisma, Claude Code, and AI-generated policies.",
    "layout_template": "comparison_matrix",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Jack Smith's Product Hunt launch finished with 17 upvotes after late social promotion "
        "and a bespoke video that received two views. Their next attempt would emphasize a "
        "clearer tagline, earlier outreach, and more engaging content. Across the database "
        "demonstrations, practitioners move row authorization into PostgreSQL rather than trusting "
        "every application query to remember its filter. The mechanics are enabling RLS, defining "
        "policies, supplying caller context, and testing through the actual application role. "
        "Milan Jovanović uses an EF Core connection interceptor; Alex Rusin builds transaction-scoped "
        "Prisma access with Claude Code. Supabase demonstrates dashboard templates, AI-generated "
        "policies, and relational authorization. Alternatives differ on policy granularity, session "
        "handling, and encryption architecture. Repeated traps include owner bypass, privileged "
        "views, unrestricted policies, missing write permissions, and misleadingly successful interfaces."
    ),
    "key_metrics": [
        {
            "label": "First Product Hunt launch result",
            "metric": "First Product Hunt launch result",
            "value": "17 upvotes",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Jack Smith reports the first launch's result and adopts that result as the "
                "benchmark to beat on the next attempt."
            ),
            "source": "Jack Smith ([hJtOsLAfxxE @ 00:12:20])",
        },
        {
            "label": "Bespoke launch video audience",
            "metric": "Bespoke launch video audience",
            "value": "2 views",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Jack Smith spent hours scripting and producing a Product Hunt-specific video, "
                "then reported two views and wished the time had gone into outbound content."
            ),
            "source": "Jack Smith ([hJtOsLAfxxE @ 00:09:04])",
        },
        {
            "label": "Prisma concurrency exercise",
            "metric": "Prisma concurrency exercise",
            "value": "800 concurrent requests; no contamination",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Alex Rusin reports this result from the generated hammer script, explicitly "
                "limiting the finding to the tested configuration and failure mode."
            ),
            "source": "Alex Rusin ([ctJy5AxgVXM @ 00:07:51])",
        },
        {
            "label": "Product Hunt hidden-vote opening",
            "metric": "Product Hunt hidden-vote opening",
            "value": "First 4 hours",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Jack Smith describes upvotes being hidden and products appearing in randomized "
                "order before vote totals become visible and ordering changes."
            ),
            "source": "Jack Smith ([hJtOsLAfxxE @ 00:01:13])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Jack Smith describes Product Hunt as a place to reach early adopters, feedback, "
                    "and sometimes press, primarily among people already in technology. Products receive "
                    "a homepage listing for 24 hours; the opening four hours hide votes and randomize "
                    "ordering, after which vote totals determine placement. Their launch strategy separates "
                    "inbound votes from people browsing the platform and outbound votes from people brought "
                    "there through an existing audience. The execution starts with the icon, product name, "
                    "and especially the tagline, because those are the pieces visible before someone opens "
                    "the listing. Smith's mobile app, Quotable, did not solve a pain point shared by much "
                    "of that audience, and their retrospective focuses on making its relevant benefits "
                    "clearer rather than abandoning the platform [hJtOsLAfxxE @ 00:07:21]. On the application "
                    "side, Alex Rusin demonstrates an equally concrete dependency: a family-tree endpoint "
                    "returns another account's person when its account filter disappears "
                    "[ctJy5AxgVXM @ 00:00:00]. Milan Jovanović reproduces the same failure with notes "
                    "belonging to two users after removing an EF Core filter. Both developers move the "
                    "authorization condition into PostgreSQL so the omitted application filter no longer "
                    "exposes the other user's rows [OwCgDPa0DnA @ 00:02:22]."
                ),
                (
                    "The database consensus is an authorization rule attached to the data, not a promise "
                    "that every caller will remember the right condition. Paul Copplestone, speaking on "
                    "Microsoft Developer, explains RLS as an implicit WHERE clause: a profile query can "
                    "omit its own user filter while the policy still evaluates which rows the caller "
                    "may access. Their distinction is precise: authentication determines whether a user "
                    "or role can enter; authorization determines what that caller can access afterward "
                    "[vZT1Qx2xUCo @ 00:02:05]. Past The Diagram applies the same mechanism to unpaid "
                    "invoices, with the database comparing tenant_id against the current session's "
                    "tenant rather than relying on the developer to add that comparison. The application "
                    "must supply the tenant resolved after authentication, and the policy needs attention "
                    "to both existing rows and incoming values [h1KAW_izGl8 @ 00:00:43]. updownx adds "
                    "the operating prerequisites: enabled RLS without a policy denies rows by default, "
                    "while superusers and BYPASSRLS roles bypass enforcement. Their recommended application "
                    "connection uses a dedicated non-superuser role with the required table privileges. "
                    "They also use the pg_policies view to inspect policy names, roles, commands, and "
                    "USING and WITH CHECK expressions, making the configured rules visible rather than "
                    "assuming that a table toggle explains every permission [MEkM0aC1JaI @ 00:02:46]."
                ),
                (
                    "The dashboard walkthroughs agree that enabling RLS is a table-specific operation "
                    "and that allowing the intended actions is a separate task. Money Tools Academy "
                    "starts by choosing the correct project, opening Table Editor, selecting the actual "
                    "table, and checking that its RLS status remains enabled afterward. They emphasize "
                    "that changing one table does not change every related table in the project "
                    "[OBXv-uTBD7A @ 00:01:01]. SmartMoneyTutorials takes the authentication, configuration, "
                    "and policies route, finds a table marked disabled, and enables it. Their important "
                    "qualification is that enabling alone grants nothing: without policies, access is "
                    "denied, so the intended reads and writes still need rules "
                    "[Sctm5VrwWTw @ 00:02:09]. Shortcut Academy reaches the same controls from the "
                    "database and tables area and says a table created in the dashboard may already "
                    "have RLS enabled. Check the current toggle rather than assuming its state "
                    "[4ncm-XBGErs @ 00:00:55]. Codewithguillaume demonstrates the consequence: enabling "
                    "a read-all template makes orders appear in Postman, including another user's "
                    "orders. They then remove that broad policy and choose the own-data template. "
                    "Getting data back establishes that a policy permits the query; their demonstration "
                    "then narrows the permission to the intended owner [Vx1q8Nfp0BE @ 00:01:48]."
                ),
            ],
            "table": {
                "caption": "Baseline mechanics the practitioners actually put into operation",
                "headers": ["Operating baseline", "What the practitioner does", "Expert Source"],
                "rows": [
                    [
                        "Separate Product Hunt discovery from the audience you bring to the launch.",
                        "Smith distinguishes inbound platform browsers from outbound supporters, then works on listing appeal, audience outreach, and the launch date.",
                        "Jack Smith ([hJtOsLAfxxE @ 00:02:33])",
                    ],
                    [
                        "Move the forgotten user filter into a database authorization policy instead.",
                        "Jovanović removes the application filter, exposes both users' notes, and demonstrates PostgreSQL applying the missing restriction through row-level security.",
                        "Milan Jovanović ([OwCgDPa0DnA @ 00:02:22])",
                    ],
                    [
                        "Treat identity verification and row authorization as separate questions to answer.",
                        "Copplestone distinguishes entering the database from deciding which particular data the admitted user or role may subsequently access.",
                        "Microsoft Developer ([vZT1Qx2xUCo @ 00:02:05])",
                    ],
                    [
                        "Inspect the actual table because related tables do not inherit this toggle.",
                        "The walkthrough selects the project and table individually, then checks the status indicator to confirm that RLS remains enabled.",
                        "Money Tools Academy ([OBXv-uTBD7A @ 00:01:01])",
                    ],
                    [
                        "Expect missing policies to deny requests rather than automatically restore functionality.",
                        "The enabling guide explicitly separates activating RLS from adding policies that permit the exact reads and writes the application needs.",
                        "SmartMoneyTutorials ([Sctm5VrwWTw @ 00:02:09])",
                    ],
                    [
                        "Use policy metadata and an application role subject to the configured rules.",
                        "updownx recommends inspecting pg_policies and running application queries as a dedicated non-superuser with the necessary privileges on the protected tables.",
                        "updownx ([MEkM0aC1JaI @ 00:04:28])",
                    ],
                ],
            },
        },
        {
            "id": "exact-street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Build the first policy around an explicit operation and condition. SmartMoneyTutorials "
                    "opens the chosen table's policy creation screen, selects a template or starts from "
                    "scratch, gives the policy a clear name and description, selects the operation, and "
                    "compares the row's user identifier with the authenticated user. They finish by saving "
                    "and testing through the application's authenticated calls "
                    "[sfzubTrNiiU @ 00:02:00]. Shortcut Academy separates the expressions: USING controls "
                    "accessible rows and the rows targeted by update or delete, while WITH CHECK validates "
                    "new or changed rows for insert and update. Their ownership example mirrors the "
                    "condition in both places [4ncm-XBGErs @ 00:01:53]. Supabase demonstrates the AI "
                    "version without changing those mechanics: ask the SQL assistant to enable RLS, "
                    "accept the generated change, and run it; then request read access only when the "
                    "published column is true. The policy editor displays a diff before acceptance and "
                    "saving. Next, switch from the dashboard's privileged postgres role to anonymous or "
                    "a specific authenticated user and inspect the resulting rows "
                    "[hu2SQjvCXIw @ 00:02:44]. Codewithguillaume's orders example shows why the selected "
                    "template matters: read-all returns other users' orders, so their replacement is "
                    "the template for viewing only one's own data [Vx1q8Nfp0BE @ 00:02:09]."
                ),
                (
                    "Milan Jovanović implements caller context with an EF Core database connection "
                    "interceptor. Their API extracts the user identifier from JWT claims, and the "
                    "interceptor overrides ConnectionOpenedAsync so the session setting is established "
                    "before EF Core continues executing the query. They inject the HTTP context accessor, "
                    "read the name-identifier claim, create a database command, and set the application "
                    "user value. Registration includes the accessor, the interceptor service, and the "
                    "database context's interceptor configuration [OwCgDPa0DnA @ 00:07:44]. Alex Rusin "
                    "uses Claude Code to generate Prisma migrations and a transaction-scoped account "
                    "wrapper instead. The sequence is enable RLS, create the account policy, discover "
                    "owner bypass, force enforcement, and then supply account context. Their wrapper "
                    "uses set_config with its local flag true so the setting reverts at transaction "
                    "end rather than following a pooled connection into another request "
                    "[ctJy5AxgVXM @ 00:05:31]. Rusin then replaces repeated route-level wrapping with "
                    "a Prisma client extension: the raw client stays inside db.ts, while the exported "
                    "account-scoped interface wraps every model operation in a scoped transaction. "
                    "Past The Diagram likewise requires transaction-local context and warns that ordinary "
                    "SET survives on the connection after it returns to the pool "
                    "[h1KAW_izGl8 @ 00:02:09]."
                ),
                (
                    "Supabase's advanced email client starts with an identity mismatch: application users "
                    "have integer IDs, while auth.users has UUIDs. The implementation adds a nullable, "
                    "unique supabase_id foreign key, producing a one-to-one link without deleting the "
                    "application user's email history when the authentication user disappears. A trigger "
                    "function inserts the public user or updates the existing email match with the new "
                    "authentication ID [PdEutzhsrws @ 00:02:17]. The email read policy then resolves "
                    "the public user ID through that link and allows emails where the user is sender "
                    "or recipient. Folder visibility follows email visibility with an EXISTS subquery, "
                    "so the referenced email policy governs which folder records contribute to the "
                    "display. Supabase's blog walkthrough uses the same relational technique: a comment "
                    "is readable when its associated post can be selected, avoiding a duplicate "
                    "implementation of the post's visibility rules [Ow_Uzedfohk @ 00:10:45]. Write "
                    "permissions remain separate: the email example checks that the authenticated user "
                    "is the sender, and the blog example combines post visibility with comment ownership. "
                    "Copplestone also explains USING as checking existing values and WITH CHECK as "
                    "checking incoming values, including preventing an update from changing ownership "
                    "to another user [vZT1Qx2xUCo @ 00:10:59]."
                ),
            ],
            "table": {
                "caption": "Execution paths, concrete tools, and the settings that carry the work",
                "headers": ["Execution task", "Exact practitioner workflow", "Expert Source"],
                "rows": [
                    [
                        "Prepare the launch listing and bring existing followers into the launch day.",
                        "Smith works on icon, name, tagline, description, images, video, and first comment, then links the launch from X and LinkedIn.",
                        "Jack Smith ([hJtOsLAfxxE @ 00:03:34])",
                    ],
                    [
                        "Create a named table policy with the intended action and ownership condition.",
                        "Choose a template or start from scratch, select the operation, define the condition, save the policy, and test authenticated application calls.",
                        "SmartMoneyTutorials ([sfzubTrNiiU @ 00:02:00])",
                    ],
                    [
                        "Use the AI editor to generate published-post visibility and inspect its change.",
                        "Supabase requests published-only reads, examines the generated policy and diff, accepts the change, and saves it against the database.",
                        "Supabase ([hu2SQjvCXIw @ 00:02:09])",
                    ],
                    [
                        "Set the claims-derived user before EF Core executes the application query.",
                        "Jovanović overrides the connection-opened method, reads the HTTP user's claim, executes the session-setting command, and registers the interceptor with the context.",
                        "Milan Jovanović ([OwCgDPa0DnA @ 00:07:44])",
                    ],
                    [
                        "Keep Prisma access scoped without asking every route to remember a wrapper.",
                        "Rusin keeps the raw client private inside db.ts and exports account-scoped access whose extension wraps every model operation in a transaction.",
                        "Alex Rusin ([ctJy5AxgVXM @ 00:09:22])",
                    ],
                    [
                        "Make related-table visibility follow the authorization already enforced on its parent.",
                        "Supabase selects the associated post inside a comment policy and uses EXISTS so comments are visible only when their post is visible.",
                        "Supabase ([Ow_Uzedfohk @ 00:11:00])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small implementation choices with concrete practitioner payoffs",
                "body": "Use the specific lever each practitioner demonstrated, including the conditions around it.",
                "items": [
                    (
                        "Smith used Max Blade's live-updating Product Hunt stats and comments stream "
                        "to remain at the top of followers' X feeds; their next idea was to alternate "
                        "that stream with a live coding session and more interaction. "
                        "[Jack Smith — hJtOsLAfxxE @ 00:10:55]"
                    ),
                    (
                        "Copplestone recommends wrapping an RLS function call in SELECT so the planner "
                        "can obtain the value once instead of evaluating the function for every row. "
                        "[Microsoft Developer — vZT1Qx2xUCo @ 00:13:04]"
                    ),
                    (
                        "Inspect pg_policies for the policy name, affected roles, command, USING, "
                        "WITH CHECK, and whether the policy is permissive or restrictive. "
                        "[updownx — MEkM0aC1JaI @ 00:02:46]"
                    ),
                    (
                        "Use the table editor's authenticated role and choose a specific user to test "
                        "actual permitted actions, not only the rows visible to the privileged dashboard role. "
                        "[Supabase — hu2SQjvCXIw @ 00:03:43]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Prepare the listing and outbound promotion",
                    "action": "Work on the homepage tagline and prepare audience-facing launch content before launch day.",
                    "detail": (
                        "Smith identifies the tagline as the missed opportunity to communicate features "
                        "and regrets posting only on launch day rather than building interest beforehand. "
                        "[Jack Smith — hJtOsLAfxxE @ 00:08:30] "
                        "[Jack Smith — hJtOsLAfxxE @ 00:10:25]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Enable the intended table and create explicit permissions",
                    "action": "Confirm the project and table, enable RLS, and save the policies for the intended operations.",
                    "detail": (
                        "Verify the selected table's enabled indicator; then select the action and role, "
                        "and define the USING and WITH CHECK conditions appropriate to that action. "
                        "[Money Tools Academy — OBXv-uTBD7A @ 00:02:11] "
                        "[Shortcut Academy — 4ncm-XBGErs @ 00:01:34]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Connect enforcement to caller context",
                    "action": "Use an application role subject to RLS and supply the authenticated tenant in transaction-local scope.",
                    "detail": (
                        "Past The Diagram says to derive tenant context after authentication, not from a "
                        "caller-chosen header, and to use SET LOCAL inside the transaction. Rusin's "
                        "Prisma wrapper uses the equivalent local flag in set_config. "
                        "[Past The Diagram — h1KAW_izGl8 @ 00:01:49] "
                        "[Alex Rusin — ctJy5AxgVXM @ 00:05:31]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Exercise both allowed and forbidden access",
                    "action": "Test another tenant's known row through the real application role and test the write operations too.",
                    "detail": (
                        "Past The Diagram expects zero rows for the cross-tenant read and extends testing "
                        "to insert, update, and delete. Rusin also deliberately removes FORCE to make "
                        "the isolation test fail and checks pooled requests under concurrency. "
                        "[Past The Diagram — h1KAW_izGl8 @ 00:03:52] "
                        "[Alex Rusin — ctJy5AxgVXM @ 00:14:30]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-and-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Policy granularity is a genuine difference in implementation style. Milan Jovanović "
                    "creates one user-isolation policy for all commands in the notes example, explicitly "
                    "choosing SELECT, UPDATE, INSERT, and DELETE together "
                    "[OwCgDPa0DnA @ 00:04:01]. Supabase's introductory blog walkthrough also begins "
                    "with an all-actions ownership policy, then adds a separate published-post read "
                    "policy and later a moderation policy. That demonstration uses additional permissions "
                    "to expand what the application can do without granting another user ownership "
                    "of the post [Ow_Uzedfohk @ 00:04:25]. Copplestone recommends the opposite "
                    "organizational default: avoid FOR ALL, create one policy per operation and role, "
                    "and place the relevant conditions inside that policy. Their reason is the mental "
                    "model of multiple policies: permissive policies combine with OR, while restrictive "
                    "policies combine with AND. They find the combination harder to reason about "
                    "than a granular policy containing its own logic [vZT1Qx2xUCo @ 00:12:01]. "
                    "updownx teaches both mechanisms as available controls, illustrating a permissive "
                    "admin rule alongside a restrictive local-socket requirement. The alternatives are "
                    "not competing claims about whether authorization belongs in PostgreSQL; they are "
                    "different ways to arrange and reason about the conditions that admit a row "
                    "[MEkM0aC1JaI @ 00:01:22]."
                ),
                (
                    "Caller context is where the implementations diverge more sharply. Jovanović obtains "
                    "the user from authenticated claims and sets the session value after opening the "
                    "EF Core connection. They prefer establishing it once per API request rather than "
                    "repeating the database round trip for every query. They also explicitly identify "
                    "the boundary of their helper: an HTTP context accessor returns no user in a "
                    "message consumer or background job, so those paths require another way to supply "
                    "identity [OwCgDPa0DnA @ 00:12:32]. Rusin's demonstration obtains the account from "
                    "a request header and feeds it to the account-scoped Prisma client, with transaction "
                    "locality handling pooled-connection reuse [ctJy5AxgVXM @ 00:09:56]. Past The "
                    "Diagram draws a stricter trust boundary: a tenant header is caller-chosen, so "
                    "the application must use the tenant it resolved after authentication and must "
                    "not simply trust client input. They also reject connection-persistent SET in "
                    "favor of SET LOCAL inside a transaction [h1KAW_izGl8 @ 00:01:49]. These are "
                    "specific differences in provenance and lifetime, not interchangeable recipes. "
                    "Jovanović demonstrates where EF Core can inject context; Rusin demonstrates "
                    "how to make scoped access the exported interface; Past The Diagram specifies "
                    "which source of tenant identity their isolation model accepts."
                ),
                (
                    "The Postgres Conference playbook pursues cryptographic isolation rather than only "
                    "row authorization. Rajan, presenting Baffle's architecture, describes shared tables "
                    "or logical databases whose tenants' data is encrypted with different keys. The "
                    "proposed system combines a SQL proxy, database extensions, and a management console. "
                    "Applications connect to the proxy, which identifies protected values and transforms "
                    "them before forwarding queries to PostgreSQL [VRoHkeV_-iI @ 00:15:17]. Tenant "
                    "determination can use a tenant column, a SQL comment, or a session variable; "
                    "separate logical databases instead allow the database name in the connection "
                    "to select the tenant key. Their bring-your-own-key model places management with "
                    "the SaaS provider, while hold-your-own-key retains the tenant's own key-management "
                    "environment and its associated burden. Copplestone's database-centric alternative "
                    "focuses on SQL authorization and the security posture inherited by applications "
                    "above PostgreSQL [vZT1Qx2xUCo @ 00:04:41]. Product Hunt timing also has "
                    "competing choices in Smith's account: they wanted a weekend for less competition, "
                    "chose Monday under a deadline using Mark Lou's advice, and afterward questioned "
                    "whether Monday morning outreach had hurt participation. Their next move is to "
                    "try a weekend, not claim that the alternate day has already produced a better "
                    "result [hJtOsLAfxxE @ 00:10:25]."
                ),
            ],
            "table": {
                "caption": "Different approaches, with their actual boundaries left intact",
                "headers": ["Decision with alternatives", "Practitioner positions and distinctions", "Expert Source"],
                "rows": [
                    [
                        "Choose between an all-commands ownership policy and granular operation-specific policy organization.",
                        "Jovanović selects all commands for the notes example; Copplestone recommends one policy per operation and role to simplify the authorization mental model.",
                        "Milan Jovanović ([OwCgDPa0DnA @ 00:04:01]); Microsoft Developer ([vZT1Qx2xUCo @ 00:12:23])",
                    ],
                    [
                        "Decide whether to combine policies or consolidate their conditions into one rule.",
                        "updownx explains permissive OR and restrictive AND combinations; Copplestone calls combinations complicated and prefers keeping conditions together within granular policies.",
                        "updownx ([MEkM0aC1JaI @ 00:01:22]); Microsoft Developer ([vZT1Qx2xUCo @ 00:12:01])",
                    ],
                    [
                        "Distinguish the demo's header-supplied account from a tenant resolved after authentication.",
                        "Rusin passes the account header into scoped Prisma access; Past The Diagram explicitly rejects trusting caller-chosen tenant headers as the identity source.",
                        "Alex Rusin ([ctJy5AxgVXM @ 00:09:56]); Past The Diagram ([h1KAW_izGl8 @ 00:01:49])",
                    ],
                    [
                        "Separate automatic authorization filtering from the query filters used for performance.",
                        "Rusin removes manual account filters after adding scoped access; Copplestone still recommends explicit WHERE clauses to reduce work before RLS evaluation.",
                        "Alex Rusin ([ctJy5AxgVXM @ 00:06:25]); Microsoft Developer ([vZT1Qx2xUCo @ 00:15:54])",
                    ],
                    [
                        "Compare provider-managed tenant keys with keys retained in each tenant's environment.",
                        "Rajan describes bring-your-own-key as reducing tenant management burden, while hold-your-own-key keeps management in the tenant's chosen environment with additional responsibility.",
                        "Postgres Conference ([VRoHkeV_-iI @ 00:25:37]); Postgres Conference ([VRoHkeV_-iI @ 00:27:40])",
                    ],
                    [
                        "Weigh the desired lower-competition weekend against the deadline-driven Monday launch choice.",
                        "Smith preferred a weekend, launched Monday under the hackathon deadline, questioned that timing afterward, and planned to try a weekend next.",
                        "Jack Smith ([hJtOsLAfxxE @ 00:05:35]); Jack Smith ([hJtOsLAfxxE @ 00:12:03])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-and-economics",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Smith's launch economics are an allocation-of-effort story with a visible result: "
                    "17 upvotes, not the product-of-the-day win teased in the opening. They spent "
                    "hours writing and producing a bespoke video aimed at Product Hunters, but it "
                    "received two views. Their retrospective redirects that effort toward more engaging "
                    "outbound content instead of treating an elaborate listing video as essential "
                    "[hJtOsLAfxxE @ 00:09:04]. The social posts mostly requested support without "
                    "providing something funny, interesting, or valuable, and promotion began on the "
                    "day rather than building interest earlier. Their small following also constrained "
                    "the number of people who could encounter those posts. Rusin reports a different "
                    "operating cost after isolation works: row policies add evaluation overhead, may "
                    "change query plans, and need measurement on the application's own data. Logging "
                    "the claimed and resolved account IDs improves debugging, but their implementation "
                    "adds a round trip, so they discuss putting it behind a production debug flag "
                    "[ctJy5AxgVXM @ 00:11:37]. Copplestone likewise revises the attractive idea of "
                    "blanket SELECT queries: explicit WHERE conditions remain useful for reducing "
                    "the data considered before policy evaluation. Their performance advice keeps "
                    "the database-enforced rule while still writing selective application queries "
                    "[vZT1Qx2xUCo @ 00:15:54]."
                ),
                (
                    "Several demonstrations show enforcement appearing present while the actual access "
                    "path escapes it. Jovanović enables the notes policy and still receives every "
                    "row because the current postgres connection has elevated privileges. The result "
                    "changes after creating and using the less-privileged application role "
                    "[OwCgDPa0DnA @ 00:04:51]. Rusin encounters a related but distinct failure: "
                    "their Prisma role is not a superuser, yet owns the protected tables, so the "
                    "first migration does not stop the leak. FORCE makes that owner subject to "
                    "the policy; missing account context then produces empty results "
                    "[ctJy5AxgVXM @ 00:03:40]. Supabase's advanced email client exposes another "
                    "path: enabling RLS on emails does not hide the displayed emails because the "
                    "application reads a view. Setting security_invoker true fixes that path, but "
                    "folder counts remain wrong until the related email_folders table and its "
                    "policy are addressed [PdEutzhsrws @ 00:09:50]. Codewithguillaume's orders "
                    "walkthrough adds the broad-policy trap: the read-all template restores visible "
                    "data but includes orders belonging to another user. They delete it before "
                    "installing the own-data rule. These demonstrations identify different causes "
                    "behind apparently working requests: elevated roles, table ownership, view "
                    "execution, related-table coverage, and permission conditions that admit too "
                    "many rows [Vx1q8Nfp0BE @ 00:01:48]."
                ),
                (
                    "Test the denied action, not just the successful screen. Past The Diagram asks "
                    "for a test that establishes tenant A's session, queries a known tenant B "
                    "row, and receives zero rows through the real application role and connection "
                    "path. They extend that exercise to insert, update, and delete rather than "
                    "stopping at a read assertion [h1KAW_izGl8 @ 00:03:52]. CyberSecurityTV "
                    "similarly calls for allow and deny assertions against two seeded tenants "
                    "in a temporary CI database, plus checks of REST endpoints, views, and RPCs. "
                    "Their warning is that ordinary functional tests can succeed while another "
                    "tenant's data remains accessible [3yDr4mrZXAw @ 00:04:45]. Rusin runs "
                    "a generated concurrency script and reports 800 concurrent requests without "
                    "contamination, explicitly describing that as a result for the tested "
                    "configuration rather than proof of every property. They also insist on "
                    "reading generated tests and making the isolation test fail by removing "
                    "FORCE [ctJy5AxgVXM @ 00:07:51]. Supabase demonstrates a smaller negative "
                    "test directly in the table editor: selecting as an authenticated user works, "
                    "but inserting a post with a blank ownership column fails. Supplying that "
                    "user's ID succeeds. The exercised action and supplied identity expose whether "
                    "the intended permission actually exists [hu2SQjvCXIw @ 00:05:33]."
                ),
            ],
            "table": {
                "caption": "Observed failures and the checks practitioners used to expose them",
                "headers": ["Failure or operating cost", "Observed result and practitioner response", "Expert Source"],
                "rows": [
                    [
                        "Hours spent producing a bespoke launch video did not produce meaningful viewing.",
                        "Smith reports two video views and wishes that production time had instead supported more engaging content for bringing outbound visitors.",
                        "Jack Smith ([hJtOsLAfxxE @ 00:09:04])",
                    ],
                    [
                        "Enabling a table policy did not constrain the elevated demonstration database connection.",
                        "Jovanović still selected every note as postgres, then created a less-privileged application role and changed the application's connection to use it.",
                        "Milan Jovanović ([OwCgDPa0DnA @ 00:05:07])",
                    ],
                    [
                        "A non-superuser connection still bypassed policies because it owned the protected table.",
                        "Rusin's first migration left the unsafe route leaking; forcing RLS exposed the next issue, which was missing account context.",
                        "Alex Rusin ([ctJy5AxgVXM @ 00:03:40])",
                    ],
                    [
                        "The email interface continued showing data after RLS was enabled on emails.",
                        "Supabase traced the reads through a view, enabled security_invoker, and then investigated related tables when folder counts continued showing other data.",
                        "Supabase ([PdEutzhsrws @ 00:09:50])",
                    ],
                    [
                        "A successful read-all template returned another user's orders alongside the current user's.",
                        "Codewithguillaume removed the broad read policy and replaced it with the template intended to let users view only their own data.",
                        "Codewithguillaume ([Vx1q8Nfp0BE @ 00:02:09])",
                    ],
                    [
                        "Working functional flows did not establish that cross-tenant requests were actually denied.",
                        "CyberSecurityTV recommends a temporary CI database with two tenants, explicit allow and deny assertions, and failures when the deny checks permit access.",
                        "CyberSecurityTV ([3yDr4mrZXAw @ 00:04:45])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks grounded in the demonstrations and their reported reversals",
                "body": "Check the actual outcome, execution role, access path, and denied operation.",
                "items": [
                    (
                        "Compare launch effort with the observed response: Smith's bespoke video "
                        "received two views after hours of work, and their preferred reallocation "
                        "was more engaging outbound content. "
                        "[Jack Smith — hJtOsLAfxxE @ 00:09:04]"
                    ),
                    (
                        "Run isolation checks as the actual application role; table owners, superusers, "
                        "and BYPASSRLS roles can make an apparently configured policy ineffective. "
                        "[Past The Diagram — h1KAW_izGl8 @ 00:02:48]"
                    ),
                    (
                        "Check views and related-table counts after enabling a base table: Supabase "
                        "had to change view execution and address email_folders before the email "
                        "client's visible data and counts followed the intended rules. "
                        "[Supabase — PdEutzhsrws @ 00:10:37]"
                    ),
                    (
                        "Make the negative test fail deliberately, then exercise pooled access: Rusin "
                        "removes FORCE to check the test and separately reports the concurrency "
                        "script's configuration-specific result. "
                        "[Alex Rusin — ctJy5AxgVXM @ 00:14:30] "
                        "[Alex Rusin — ctJy5AxgVXM @ 00:07:51]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        "\"Isolation that depends on every query remembering a filter is not a security model, "
        "it is a hope.\" — Past The Diagram (h1KAW_izGl8 @ 00:00:03)."
    ),
    "diagram_id": "diag-07",
    "action_checklist": [
        (
            "Refine the Product Hunt tagline around features the audience can recognize, and "
            "prepare engaging outbound posts before the launch rather than only asking for "
            "support on the day. [Jack Smith — hJtOsLAfxxE @ 00:08:30] "
            "[Jack Smith — hJtOsLAfxxE @ 00:09:35]"
        ),
        (
            "Open the correct project and table, confirm the RLS toggle, and add the policies "
            "needed for the intended reads and writes instead of stopping after enabling it. "
            "[Money Tools Academy — OBXv-uTBD7A @ 00:01:01] "
            "[SmartMoneyTutorials — Sctm5VrwWTw @ 00:02:09]"
        ),
        (
            "Name each policy clearly, choose its action and role, define existing-row and "
            "incoming-value conditions where applicable, and test authenticated calls after saving. "
            "[Shortcut Academy — 4ncm-XBGErs @ 00:01:34] "
            "[SmartMoneyTutorials — sfzubTrNiiU @ 00:02:34]"
        ),
        (
            "Use the authenticated tenant as context, keep pooled-connection context transaction-local, "
            "and inspect whether the application role owns tables or bypasses enforcement. "
            "[Past The Diagram — h1KAW_izGl8 @ 00:01:49] "
            "[updownx — MEkM0aC1JaI @ 00:03:26]"
        ),
        (
            "Review AI-generated policy changes, test as a selected authenticated user, and "
            "inspect views and related-table policies when visible rows or counts remain wrong. "
            "[Supabase — hu2SQjvCXIw @ 00:02:44] "
            "[Supabase — PdEutzhsrws @ 00:11:22]"
        ),
        (
            "Add cross-tenant read and write denials, inspect generated tests, make an isolation "
            "test fail deliberately, and run the concurrent account-access exercise. "
            "[CyberSecurityTV — 3yDr4mrZXAw @ 00:04:45] "
            "[Alex Rusin — ctJy5AxgVXM @ 00:11:18] "
            "[Alex Rusin — ctJy5AxgVXM @ 00:14:30]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Jack Smith — Launching My App on Product Hunt [00:09:04]",
            "url": "https://www.youtube.com/watch?v=hJtOsLAfxxE&t=544s",
            "relevance": "Primary practitioner testimony on bespoke launch-video effort, two views, and reallocating effort toward outbound content.",
        },
        {
            "title": "Past The Diagram — Postgres Row-Level Security for Multi-Tenant SaaS [00:03:52]",
            "url": "https://www.youtube.com/watch?v=h1KAW_izGl8&t=232s",
            "relevance": "Primary practitioner testimony on proving tenant isolation with a known foreign-tenant row and the real application connection.",
        },
        {
            "title": "Alex Rusin — Claude Code + Prisma: Multi-Tenant Postgres API That Can't Leak Data [00:05:31]",
            "url": "https://www.youtube.com/watch?v=ctJy5AxgVXM&t=331s",
            "relevance": "Primary practitioner testimony on transaction-local tenant context and avoiding identity persistence on pooled connections.",
        },
        {
            "title": "Supabase — Advanced Row Level Security (RLS) Policies // Authorization Deep Dive [00:10:37]",
            "url": "https://www.youtube.com/watch?v=PdEutzhsrws&t=637s",
            "relevance": "Primary practitioner testimony on changing view execution to security_invoker so underlying row policies govern results.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "hJtOsLAfxxE",
            "title": "Launching My App on Product Hunt",
            "channel": "Jack Smith",
            "author": "Jack Smith",
            "text": "I spent hours and hours doing this; in the end it got two views.",
            "tip": "I spent hours and hours doing this; in the end it got two views.",
            "timestamp": 544,
            "timestamp_seconds": 544,
            "timestamp_label": "[00:09:04]",
            "url": "https://www.youtube.com/watch?v=hJtOsLAfxxE&t=544s",
            "markdown": "[00:09:04](https://www.youtube.com/watch?v=hJtOsLAfxxE&t=544s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on launch-content effort and the observed audience for the bespoke video.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "h1KAW_izGl8",
            "title": "Postgres Row-Level Security for Multi-Tenant SaaS",
            "channel": "Past The Diagram",
            "author": "Past The Diagram",
            "text": "Write a test that sets the session to tenant A, queries for a row you know belongs to tenant B, and asserts it gets nothing back.",
            "tip": "Write a test that sets the session to tenant A, queries for a row you know belongs to tenant B, and asserts it gets nothing back.",
            "timestamp": 232,
            "timestamp_seconds": 232,
            "timestamp_label": "[00:03:52]",
            "url": "https://www.youtube.com/watch?v=h1KAW_izGl8&t=232s",
            "markdown": "[00:03:52](https://www.youtube.com/watch?v=h1KAW_izGl8&t=232s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on negative testing against a known cross-tenant row.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "vZT1Qx2xUCo",
            "title": "Everything you need to know about Postgres Row Level Security | POSETTE 2024",
            "channel": "Microsoft Developer",
            "author": "Microsoft Developer",
            "text": "If you were calling a function inside your RLS policy, then you should try to wrap it in a SELECT statement.",
            "tip": "If you were calling a function inside your RLS policy, then you should try to wrap it in a SELECT statement.",
            "timestamp": 784,
            "timestamp_seconds": 784,
            "timestamp_label": "[00:13:04]",
            "url": "https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=784s",
            "markdown": "[00:13:04](https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=784s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on reducing repeated function evaluation within RLS policies.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "MEkM0aC1JaI",
            "title": "PostgreSQL Row-Level Security Explained with Multi-Tenancy",
            "channel": "updownx",
            "author": "updownx",
            "text": "The pg_policies view in PostgreSQL provides metadata for each row security policy, including the policy name, roles it applies to, command type, and USING and WITH CHECK expressions.",
            "tip": "The pg_policies view in PostgreSQL provides metadata for each row security policy, including the policy name, roles it applies to, command type, and USING and WITH CHECK expressions.",
            "timestamp": 166,
            "timestamp_seconds": 166,
            "timestamp_label": "[00:02:46]",
            "url": "https://www.youtube.com/watch?v=MEkM0aC1JaI&t=166s",
            "markdown": "[00:02:46](https://www.youtube.com/watch?v=MEkM0aC1JaI&t=166s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on inspecting the actual policy configuration.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "VRoHkeV_-iI",
            "title": "Data Isolation in Multitenant PostgreSQL",
            "channel": "Postgres Conference",
            "author": "Postgres Conference",
            "text": "Different tenants' data will be encrypted with different keys, so that it provides strong cryptographic data isolation.",
            "tip": "Different tenants' data will be encrypted with different keys, so that it provides strong cryptographic data isolation.",
            "timestamp": 571,
            "timestamp_seconds": 571,
            "timestamp_label": "[00:09:31]",
            "url": "https://www.youtube.com/watch?v=VRoHkeV_-iI&t=571s",
            "markdown": "[00:09:31](https://www.youtube.com/watch?v=VRoHkeV_-iI&t=571s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the tenant-specific encryption-key alternative.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "OwCgDPa0DnA",
            "title": "Building Multi-Tenant APIs Using EF Core and Row-Level Security",
            "channel": "Milan Jovanović",
            "author": "Milan Jovanović",
            "text": "If I were using this from a message consumer or a background job, this is going to return null. So I'd need a different approach to set who is the current user.",
            "tip": "If I were using this from a message consumer or a background job, this is going to return null. So I'd need a different approach to set who is the current user.",
            "timestamp": 781,
            "timestamp_seconds": 781,
            "timestamp_label": "[00:13:01]",
            "url": "https://www.youtube.com/watch?v=OwCgDPa0DnA&t=781s",
            "markdown": "[00:13:01](https://www.youtube.com/watch?v=OwCgDPa0DnA&t=781s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the HTTP context accessor's boundary outside HTTP requests.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "PdEutzhsrws",
            "title": "Advanced Row Level Security (RLS) Policies // Authorization Deep Dive",
            "channel": "Supabase",
            "author": "Supabase",
            "text": "We can actually use this little trick to enforce policies from another table.",
            "tip": "We can actually use this little trick to enforce policies from another table.",
            "timestamp": 944,
            "timestamp_seconds": 944,
            "timestamp_label": "[00:15:44]",
            "url": "https://www.youtube.com/watch?v=PdEutzhsrws&t=944s",
            "markdown": "[00:15:44](https://www.youtube.com/watch?v=PdEutzhsrws&t=944s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on deriving email-folder visibility from the emails table's policies.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ctJy5AxgVXM",
            "title": "Claude Code + Prisma: Multi-Tenant Postgres API That Can't Leak Data",
            "channel": "Alex Rusin",
            "author": "Alex Rusin",
            "text": "It has to be a transaction and this flag true in set_config, that's the local flag. It makes this the equivalent of SET LOCAL. The value gets reverted when the transaction ends.",
            "tip": "It has to be a transaction and this flag true in set_config, that's the local flag. It makes this the equivalent of SET LOCAL. The value gets reverted when the transaction ends.",
            "timestamp": 348,
            "timestamp_seconds": 348,
            "timestamp_label": "[00:05:48]",
            "url": "https://www.youtube.com/watch?v=ctJy5AxgVXM&t=348s",
            "markdown": "[00:05:48](https://www.youtube.com/watch?v=ctJy5AxgVXM&t=348s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on transaction-scoped tenant context for pooled Prisma connections.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Ow_Uzedfohk",
            "title": "Implement Authorization using Row Level Security (RLS) with Supabase (Step By Step Guide)",
            "channel": "Supabase",
            "author": "Supabase",
            "text": "If we can see a post it makes sense that we can see all of its comments.",
            "tip": "If we can see a post it makes sense that we can see all of its comments.",
            "timestamp": 629,
            "timestamp_seconds": 629,
            "timestamp_label": "[00:10:29]",
            "url": "https://www.youtube.com/watch?v=Ow_Uzedfohk&t=629s",
            "markdown": "[00:10:29](https://www.youtube.com/watch?v=Ow_Uzedfohk&t=629s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on inheriting comment visibility from the associated post.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Vx1q8Nfp0BE",
            "title": "Row Level Security with @Supabase — Course part 10 (2025)",
            "channel": "Codewithguillaume",
            "author": "Codewithguillaume",
            "text": "What I would like to do is just to query my own orders and not the orders from other users.",
            "tip": "What I would like to do is just to query my own orders and not the orders from other users.",
            "timestamp": 108,
            "timestamp_seconds": 108,
            "timestamp_label": "[00:01:48]",
            "url": "https://www.youtube.com/watch?v=Vx1q8Nfp0BE&t=108s",
            "markdown": "[00:01:48](https://www.youtube.com/watch?v=Vx1q8Nfp0BE&t=108s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony motivating replacement of read-all with owner-specific access.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "sfzubTrNiiU",
            "title": "How To Create RLS Policies In Supabase [Step-By-Step 2026]",
            "channel": "SmartMoneyTutorials",
            "author": "SmartMoneyTutorials",
            "text": "Always test with your app's authenticated calls to confirm the behavior matches your expectations.",
            "tip": "Always test with your app's authenticated calls to confirm the behavior matches your expectations.",
            "timestamp": 154,
            "timestamp_seconds": 154,
            "timestamp_label": "[00:02:34]",
            "url": "https://www.youtube.com/watch?v=sfzubTrNiiU&t=154s",
            "markdown": "[00:02:34](https://www.youtube.com/watch?v=sfzubTrNiiU&t=154s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on verifying a saved policy through authenticated application requests.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "hu2SQjvCXIw",
            "title": "Use AI to enable and generate RLS policies for Postgres with Supabase",
            "channel": "Supabase",
            "author": "Supabase",
            "text": "We've written a policy to enable the select action but the insert action is still being denied by RLS.",
            "tip": "We've written a policy to enable the select action but the insert action is still being denied by RLS.",
            "timestamp": 237,
            "timestamp_seconds": 237,
            "timestamp_label": "[00:03:57]",
            "url": "https://www.youtube.com/watch?v=hu2SQjvCXIw&t=237s",
            "markdown": "[00:03:57](https://www.youtube.com/watch?v=hu2SQjvCXIw&t=237s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on testing separate operation permissions after AI-assisted policy creation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Sctm5VrwWTw",
            "title": "How To Enable Row Level Security In Supabase [RLS Guide 2026]",
            "channel": "SmartMoneyTutorials",
            "author": "SmartMoneyTutorials",
            "text": "Enabling RLS by itself doesn't grant access. If there are no policies, all access is denied by default.",
            "tip": "Enabling RLS by itself doesn't grant access. If there are no policies, all access is denied by default.",
            "timestamp": 129,
            "timestamp_seconds": 129,
            "timestamp_label": "[00:02:09]",
            "url": "https://www.youtube.com/watch?v=Sctm5VrwWTw&t=129s",
            "markdown": "[00:02:09](https://www.youtube.com/watch?v=Sctm5VrwWTw&t=129s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony separating the RLS toggle from explicit permission policies.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "3yDr4mrZXAw",
            "title": "Supabase RLS Security Explained: How to Protect Your Database From Data Leaks | CyberSecurityTV",
            "channel": "CyberSecurityTV",
            "author": "CyberSecurityTV",
            "text": "Add a CI job that spins up a temporary database, seeds two tenants, and runs both allow and deny assertions.",
            "tip": "Add a CI job that spins up a temporary database, seeds two tenants, and runs both allow and deny assertions.",
            "timestamp": 285,
            "timestamp_seconds": 285,
            "timestamp_label": "[00:04:45]",
            "url": "https://www.youtube.com/watch?v=3yDr4mrZXAw&t=285s",
            "markdown": "[00:04:45](https://www.youtube.com/watch?v=3yDr4mrZXAw&t=285s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on continuous allow-and-deny testing for tenant isolation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "4ncm-XBGErs",
            "title": "How to Create Policy (rls) in Supabase [2026 Full Guide]",
            "channel": "Shortcut Academy",
            "author": "Shortcut Academy",
            "text": "The USING expression filters which rows are accessible for SELECT and also controls which rows a user can target with UPDATE or DELETE.",
            "tip": "The USING expression filters which rows are accessible for SELECT and also controls which rows a user can target with UPDATE or DELETE.",
            "timestamp": 113,
            "timestamp_seconds": 113,
            "timestamp_label": "[00:01:53]",
            "url": "https://www.youtube.com/watch?v=4ncm-XBGErs&t=113s",
            "markdown": "[00:01:53](https://www.youtube.com/watch?v=4ncm-XBGErs&t=113s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the existing-row side of a policy's authorization expressions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "OBXv-uTBD7A",
            "title": "How to Turn On Row Level Security in Supabase (Full Guide 2026)",
            "channel": "Money Tools Academy",
            "author": "Money Tools Academy",
            "text": "Look for the toggle to remain on or any status indicator that shows RLS is active.",
            "tip": "Look for the toggle to remain on or any status indicator that shows RLS is active.",
            "timestamp": 131,
            "timestamp_seconds": 131,
            "timestamp_label": "[00:02:11]",
            "url": "https://www.youtube.com/watch?v=OBXv-uTBD7A&t=131s",
            "markdown": "[00:02:11](https://www.youtube.com/watch?v=OBXv-uTBD7A&t=131s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on confirming the selected table's RLS state after enabling it.",
        },
    ],
}
