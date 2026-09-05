#!/usr/bin/env python3
"""Validate the published benchmark configuration and aggregate results."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str) -> dict:
    with (ROOT / relative_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_initial_case(case: dict) -> None:
    problem = case["problem"]
    assert problem["cargo_type_count"] == 50
    assert problem["normal_order_count"] == 25
    assert problem["demand_per_cargo_type_pallets"] == {
        "minimum": 15,
        "maximum": 50,
    }
    assert problem["agvs"] == {
        "count": 9,
        "maximum_load_kg": 1800,
        "travel_speed_m_per_s": 1,
    }
    assert problem["handling"] == {
        "loading_or_unloading_time_s": 10,
        "empty_pallet_tare_mass_kg": 15,
    }
    assert problem["unloading_points"]["capacity_per_point_pallet_positions"] == 5
    assert problem["urgent_order_insertion"]["priority_sequence"] == [3, 2, 1, 1, 2, 3]
    assert case["sac_training"] == {
        "discount_factor": 0.99,
        "soft_update_coefficient": 0.005,
        "initial_entropy_temperature": 0.2,
        "learning_rate": 0.0003,
    }


def validate_results(results: dict) -> None:
    records = results["records"]
    assert len(records) == 6
    expected = {
        ("exponential", "probabilistic_selection"): (22182.4, 3.14, 4333.5, 6.4, 13572.9, -1.668),
        ("exponential", "reward_selection"): (21672.5, 3.22, 3283.9, 5.9, 12377.7, -1.668),
        ("linear", "probabilistic_selection"): (22338.7, 3.12, 5086.2, 2.2, 13876.5, -0.816),
        ("linear", "reward_selection"): (21375.8, 3.26, 4018.6, 8.1, 11379.1, -0.715),
        ("logarithmic", "probabilistic_selection"): (22244.5, 3.13, 2888.6, 4.1, 12581.0, -0.518),
        ("logarithmic", "reward_selection"): (21813.3, 3.20, 3673.9, 2.7, 13150.0, -1.773),
    }
    observed = {}
    for record in records:
        key = (record["priority_weight"], record["allocation_method"])
        assert key not in observed
        observed[key] = (
            record["total_handling_time_s"],
            record["throughput_pallets_per_min"],
            record["urgent_order_insertion_time_s"],
            record["maximum_decline_percent"],
            record["priority_task_duration_s"],
            record["normalized_load_balance_score"],
        )
    assert observed == expected


def main() -> None:
    validate_initial_case(load_json("data/initial_case.json"))
    validate_results(load_json("data/strategy_results.json"))
    print("Data validation passed: initial benchmark and six strategy records are consistent.")


if __name__ == "__main__":
    main()
