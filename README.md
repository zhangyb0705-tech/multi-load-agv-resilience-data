# Resilience-oriented multi-load AGV scheduling data

This repository contains the anonymized benchmark configuration and aggregate experimental results reported in the manuscript **Resilience-Oriented Scheduling of Multi-Load AGVs for Warehouse Unloading with Urgent Order Insertion: A Soft Actor-Critic Approach**.

## Repository contents

- `data/initial_case.json`: initial benchmark configuration, urgent-order insertion rule, SAC hyperparameters, and computing environment.
- `data/strategy_results.json`: aggregate results for the six priority-control strategies reported in Table 3 of the manuscript.
- `DATA_INVENTORY.md`: audit of the data that were found, published, and unavailable in the surviving local materials.
- `metadata.json`: dataset-level metadata and provenance.
- `scripts/validate_data.py`: a standard-library validation script for checking the published values and required fields.
- `CITATION.cff`: citation metadata for this dataset.

## Initial benchmark

The shareable benchmark contains 50 cargo types, 25 normal orders, and 9 multi-load AGVs. Demand for each cargo type is between 15 and 50 pallets. Each AGV has a maximum load of 1,800 kg and travels at 1 m/s. Loading and unloading each require 10 s, an empty pallet has a tare mass of 15 kg, and each stop adds 5 s for acceleration and deceleration. Each unloading point can hold at most five full or empty pallets. Urgent work is inserted immediately after completion of the 12th normal order, with priority sequence `[3, 2, 1, 1, 2, 3]`.

The SAC settings are a discount factor of 0.99, soft-update coefficient of 0.005, initial entropy temperature of 0.2, and learning rate of 0.0003.

## Data provenance

The values in `data/initial_case.json` are transcribed from the experimental-design section of the manuscript and its source Chapter 4 materials. The values in `data/strategy_results.json` are transcribed from Table 3 of the manuscript. No values have been inferred from chart pixels.

The 5 s acceleration/deceleration delay per stop appears in both surviving source Chapter 4 materials. It is included for source completeness, although the final manuscript does not repeat this parameter explicitly in its experimental-design paragraph.

The company-specific operational records underlying the warehouse scenario are confidential. The surviving source materials do not contain the individual cargo weights, the complete order-by-cargo demand matrix, exact warehouse coordinates, random seeds, trained model checkpoints, raw training arrays, or the complete event log. These unavailable fields have not been reconstructed or imputed. Consequently, this release supports inspection of the initial benchmark specification and verification of the reported aggregate results, but it does not by itself reproduce a full training run.

## Validation

Run the following command with Python 3.10 or later:

```bash
python scripts/validate_data.py
```

The validator checks the benchmark dimensions, priority sequence, hyperparameters, strategy coverage, units, and the exact Table 3 values.

## Suggested data-availability statement

The anonymized initial benchmark configuration and aggregate experimental results are available in this repository. Company-specific operational records and the complete simulation event log are not publicly available because of confidentiality restrictions.

## Dataset title for submission systems

Anonymized benchmark data for resilience-oriented multi-load AGV scheduling

## License

The dataset and accompanying documentation in this repository are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (`CC-BY-4.0`). Users may share and adapt the material, including for commercial purposes, provided that appropriate credit is given, a link to the license is supplied, and any changes are indicated. See `LICENSE` for the complete legal text and `CITATION.cff` for the dataset authors and suggested citation metadata.
