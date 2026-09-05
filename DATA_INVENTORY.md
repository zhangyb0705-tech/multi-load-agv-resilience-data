# Data inventory and release scope

This inventory records what was found during a local audit of the surviving manuscript materials and working files. It distinguishes published data from information that is not present in the surviving sources. No missing values were reconstructed from figure pixels or generated synthetically.

## Published and source-verified

| Data group | Published location | Scope |
| --- | --- | --- |
| Initial benchmark dimensions | `data/initial_case.json` | 50 cargo types, 25 normal orders, 9 AGVs, and per-cargo demand range of 15–50 pallets |
| Vehicle and handling parameters | `data/initial_case.json` | 1,800 kg maximum load, 1 m/s speed, 10 s loading/unloading time, 15 kg empty-pallet tare mass, and 5 s additional acceleration/deceleration time per stop |
| Unloading capacity | `data/initial_case.json` | Five positions per unloading point, counting full and empty pallets together |
| Urgent-order scenario | `data/initial_case.json` | Insertion after normal order 12 and priority sequence `[3, 2, 1, 1, 2, 3]` |
| SAC hyperparameters and computing environment | `data/initial_case.json` | Discount factor, soft-update coefficient, entropy temperature, learning rate, software, processor, and memory |
| Six strategy-level outcomes | `data/strategy_results.json` | Exact aggregate values reported in manuscript Table 3 |

The 5 s additional stop delay is reported in both surviving source Chapter 4 materials. The final manuscript does not repeat it explicitly in the experimental-design paragraph, so this provenance distinction is recorded in `data/initial_case.json` and the README.

## Checked but not available in the surviving local materials

- Individual cargo weights.
- Complete order-by-cargo demand matrix.
- Exact warehouse or task-point coordinates.
- Random seeds and repeated-run identifiers.
- Raw SAC loss, entropy, and makespan arrays.
- Trained model checkpoints.
- Complete task-level simulation event logs and AGV trajectories.

The local audit found no research-data spreadsheets, CSV/TSV files, NumPy arrays, model checkpoints, serialized training objects, databases, or other machine-readable raw simulation outputs outside this release. The surviving Word sources contain benchmark constants, formulas, figures, narrative descriptions, and the aggregate strategy table. Figure-processing scripts only crop, relabel, or redraw presentation graphics; they do not contain recoverable raw event-level or training-series data.

## Interpretation

This repository therefore publishes all source-verified, shareable machine-readable benchmark values and aggregate outcome values recoverable from the surviving local materials. It is not a complete computational-reproduction package because the raw instance matrix, event log, training arrays, checkpoints, and seeds are not present and have not been imputed.
