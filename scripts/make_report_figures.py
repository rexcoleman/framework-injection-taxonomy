#!/usr/bin/env python3
"""Generate FP-21 report figures."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INPUT_DIR = Path("outputs/experiments")
OUT_DIRS = [Path("blog/images"), Path("outputs/figures")]

def ensure_dirs():
    for d in OUT_DIRS:
        d.mkdir(parents=True, exist_ok=True)

def save(fig, name):
    for d in OUT_DIRS:
        fig.savefig(d / f"{name}.png", dpi=150, bbox_inches="tight")
    print(f"  Saved: {name}.png")

def fig_e1():
    with open(INPUT_DIR / "e1_results.json") as f:
        data = json.load(f)["results"]
    fws = ["langchain", "crewai", "autogen", "direct_api"]
    labels = ["LangChain", "CrewAI", "AutoGen", "Direct API"]
    colors = ["#2563eb", "#dc2626", "#16a34a", "#9ca3af"]
    rates = [data[fw]["success_rate"]*100 for fw in fws]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, rates, color=colors, alpha=0.8)
    ax.set_ylabel("Injection Success Rate (%)")
    ax.set_title("Prompt Injection Success by Framework\n(20 payloads x 5 seeds)")
    ax.set_ylim(0, 100)
    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f"{rate:.0f}%", ha="center", va="bottom", fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    save(fig, "e1_framework_comparison")
    plt.close()

def fig_e2():
    with open(INPUT_DIR / "e2_results.json") as f:
        data = json.load(f)["results"]
    fws = ["langchain", "crewai", "autogen", "direct_api"]
    labels = ["LangChain", "CrewAI", "AutoGen", "Direct API"]
    direct = [data[fw]["direct_rate"]*100 for fw in fws]
    indirect = [data[fw]["indirect_rate"]*100 for fw in fws]
    x = np.arange(len(fws))
    w = 0.35
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(x - w/2, direct, w, label="Direct Injection", color="#2563eb", alpha=0.8)
    ax.bar(x + w/2, indirect, w, label="Indirect (Tool Output)", color="#dc2626", alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Success Rate (%)")
    ax.set_title("Direct vs Indirect Injection by Framework\n(5 payloads per type x 5 seeds)")
    ax.set_ylim(0, 100)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    save(fig, "e2_direct_vs_indirect")
    plt.close()

def main():
    ensure_dirs()
    print("Generating FP-21 figures...")
    fig_e1()
    fig_e2()
    print("Done.")

if __name__ == "__main__":
    main()
