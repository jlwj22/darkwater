# Roadmap

Each milestone ends with at least one decision record in `docs/decisions/`.

| Week | Milestone | DSLC stage | Deliverable |
|---|---|---|---|
| 1 | Problem framing | Business understanding | `docs/problem_statement.md`, decision 0001 |
| 2–3 | Ingestion | Data acquisition | AIS download → partitioned Parquet for chosen region/window |
| 3–4 | Data quality | Cleaning | pandera schemas, documented cleaning rules |
| 4–6 | EDA | Exploration | Coverage, traffic density, and gap-distribution notebooks |
| 6–7 | Modeling layer | Feature engineering | dbt models: port visits, transmission gaps, vessel encounters |
| 8–9 | Baselines | Modeling | Rule-based detectors, Isolation Forest, MLflow tracking |
| 10–11 | Core models | Modeling | Coverage-adjusted gap model, rendezvous clustering |
| 12 | Evaluation | Validation | Weak-label evaluation (GFW, OFAC), error analysis |
| 13–14 | Extension | Modeling | Port congestion forecasting *or* trajectory autoencoder |
| 15 | Write-up | Communication | Final README with findings and limitations |

## Week 1 — problem framing

Write `docs/problem_statement.md` answering:

1. **Who cares?** Name a concrete user (e.g., a Coast Guard analyst, a marine insurer). What
   decision would this help them make?
2. **What counts as "anomalous"?** Define going dark, loitering, and rendezvous precisely enough
   that two people would label the same track the same way.
3. **Why is this hard?** No ground truth, and most AIS gaps are receiver coverage, not intent.
   How will you tell the difference?
4. **What does success look like?** Pick metrics you could compute without full labels
   (precision@k against weak labels, analyst-review hit rate, stability over time).
5. **Scope:** which region(s) and time window, and why? Keep it within ~50 GB of raw data.
6. **Out of scope:** what you're deliberately *not* doing.

Then write `docs/decisions/0001-region-and-window.md` using the template.
