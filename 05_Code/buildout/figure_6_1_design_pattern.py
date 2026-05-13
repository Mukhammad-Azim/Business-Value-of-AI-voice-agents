"""
figure_6_1_design_pattern.py
============================

Generate Figure 6.1 — the four-prerequisite Voice-AI-in-Regulated-Workflow
design pattern, anchored to the Better.com / Tinman / Betsy / ElevenLabs case.
Saves a publication-quality PNG to outputs/figures/design_pattern/.

Layout
------

The redesigned figure organises the diagram into four horizontal lanes so
that no text or arrow ever overlaps a coloured prerequisite box:

    +------------------+--------------------------------------------------+
    |  TITLE / SUBTITLE                                                   |
    +---------------------------------------------------------------------+
    |  CHANNEL LANE   :  Borrower (voice channel)  ←→  Voice infra        |
    |                    (top-of-figure entry/exit point)                 |
    +---------------------------------------------------------------------+
    |  FOUR-BOX LANE  :  [1 Tinman] [2 Betsy] [3 Voice infra] [4 Human]   |
    |                    (each with title / subtitle / case anchor)       |
    +---------------------------------------------------------------------+
    |  FLOW LANE      :  inter-prerequisite arrows + labels in dedicated  |
    |                    horizontal corridors above and below the boxes   |
    +---------------------------------------------------------------------+
    |  EVIDENCE BAND  :  Governance & multidimensional measurement        |
    +---------------------------------------------------------------------+

The boxes are spaced so that arrow labels live in the gaps *between*
boxes, and the "agent ↔ human" escalation/handback loop is routed below
the boxes in a dedicated corridor, far from any other text. Each box is
labelled with a 1–2 line caption and a one-line case-evidence anchor.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, ".")
from _helpers import FIG_DESIGN  # noqa: E402

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def build_figure(out_path: str) -> None:
    fig, ax = plt.subplots(figsize=(13.0, 8.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Colour palette (academic-neutral)
    color_platform = "#1F4E79"  # deep navy
    color_agent = "#2E6F40"  # forest green
    color_voice = "#7A4D9D"  # plum
    color_human = "#C0504D"  # muted red
    color_text = "white"
    text_dark = "#222222"
    arrow_color = "#333333"

    # ---------------------------------------------------------------- title
    ax.text(
        50, 95.5,
        "Figure 6.1. Voice-AI-in-Regulated-Workflow Design Pattern",
        ha="center", va="bottom",
        fontsize=15.5, fontweight="bold", color=text_dark,
    )
    ax.text(
        50, 92.4,
        "Four prerequisites observed in the Better.com / Tinman / Betsy / "
        "ElevenLabs case",
        ha="center", va="top",
        fontsize=10.8, color=text_dark, style="italic",
    )

    # ------------------------------------------------------- borrower lane
    # Borrower box sits above the Voice-infra box (box #3) so the channel
    # arrow can drop straight down into the voice prerequisite without
    # crossing any other element.
    borrower_x = 60
    borrower_y = 84
    ax.text(
        borrower_x, borrower_y,
        "Borrower (voice channel)",
        ha="center", va="center",
        fontsize=11.0, fontweight="bold", color=text_dark,
        bbox=dict(
            boxstyle="round,pad=0.55",
            facecolor="#F4F1E4",
            edgecolor="#444444",
            linewidth=1.0,
        ),
    )

    # Vertical arrows: borrower -> voice (down) and voice -> borrower (up)
    ax.add_patch(FancyArrowPatch(
        (57, 80.5), (57, 70),
        arrowstyle="-|>", lw=1.6, color=arrow_color, mutation_scale=14,
    ))
    ax.add_patch(FancyArrowPatch(
        (63, 70), (63, 80.5),
        arrowstyle="-|>", lw=1.6, color=arrow_color, mutation_scale=14,
    ))
    ax.text(
        49, 75.3, "speech in",
        fontsize=9.2, color=text_dark, style="italic",
        ha="right", va="center",
    )
    ax.text(
        71, 75.3, "speech out",
        fontsize=9.2, color=text_dark, style="italic",
        ha="left", va="center",
    )

    # ------------------------------------------------------- four boxes
    # Box width = 18; gap between boxes = 6 (so that arrow corridors are
    # visible between adjacent prerequisites).
    box_w, box_h = 18, 22
    box_y = 48
    gap_x = 4
    box_xs = [4, 4 + box_w + gap_x,
              4 + 2 * (box_w + gap_x), 4 + 3 * (box_w + gap_x)]

    boxes = [
        # (x, color, title, subtitle, evidence-anchor)
        (
            box_xs[0], color_platform,
            "1. Process-aware\noperating platform",
            "Exposes structured\nworkflow & document state",
            "Case anchor: Tinman\n(Better Home & Finance, 2025)",
        ),
        (
            box_xs[1], color_agent,
            "2. Coordination-layer\nagent scope",
            "LLM scoped to routine\nborrower communication",
            "Case anchor: Betsy\n(Better Home & Finance, 2024a, 2026)",
        ),
        (
            box_xs[2], color_voice,
            "3. Low-latency\nvoice infrastructure",
            "STT \u2192 LLM \u2192 TTS\n(low-latency target)",
            "Case anchor: ElevenLabs Agents\n(Better & ElevenLabs, 2026)",
        ),
        (
            box_xs[3], color_human,
            "4. Auditable human\nescalation",
            "Licensed consultant at\nthe regulated boundary",
            "Case anchor: SAFE Act,\nTILA, CFPB UDAAP",
        ),
    ]

    for (x, color, title, subtitle, evidence) in boxes:
        patch = FancyBboxPatch(
            (x, box_y), box_w, box_h,
            boxstyle="round,pad=0.45,rounding_size=1.1",
            linewidth=1.5,
            edgecolor=color,
            facecolor=color,
            alpha=0.92,
        )
        ax.add_patch(patch)
        # Title (top of box)
        ax.text(
            x + box_w / 2, box_y + box_h - 3.8,
            title, ha="center", va="top",
            fontsize=11.0, fontweight="bold", color=color_text,
        )
        # Subtitle (centre of box)
        ax.text(
            x + box_w / 2, box_y + box_h / 2 - 1.0,
            subtitle, ha="center", va="center",
            fontsize=9.6, color=color_text,
        )
        # Evidence anchor (just below box, dark italic)
        ax.text(
            x + box_w / 2, box_y - 1.8,
            evidence, ha="center", va="top",
            fontsize=8.7, color=text_dark, style="italic",
        )

    # ----------------------------------------------- inter-box arrow lanes
    # The centre of each gap (corridor) is where labels sit. Y-corridors
    # are well above (y_top) and well below (y_bot) the boxes' midline so
    # arrows have room to be drawn.
    arrow_kw = dict(
        arrowstyle="-|>", lw=1.55, color=arrow_color, mutation_scale=14,
    )

    # ----- Box 3 (Voice infra) <-> Box 2 (Agent), short horizontal pair.
    x3_left = box_xs[2]                  # left edge of box 3
    x2_right = box_xs[1] + box_w         # right edge of box 2
    # Arrow: box 2 -> box 3 (transcripts), drawn slightly above midline.
    ax.add_patch(FancyArrowPatch(
        (x2_right, box_y + box_h * 0.62),
        (x3_left,  box_y + box_h * 0.62),
        **arrow_kw,
    ))
    # Arrow: box 3 -> box 2 (response audio), drawn slightly below.
    ax.add_patch(FancyArrowPatch(
        (x3_left,  box_y + box_h * 0.38),
        (x2_right, box_y + box_h * 0.38),
        **arrow_kw,
    ))
    mid_23 = (x2_right + x3_left) / 2
    ax.text(
        mid_23, box_y + box_h + 1.4,
        "transcripts",
        fontsize=9.0, color=text_dark, style="italic",
        ha="center", va="bottom",
    )
    ax.text(
        mid_23, box_y - 5.7,
        "response audio",
        fontsize=9.0, color=text_dark, style="italic",
        ha="center", va="top",
    )

    # ----- Box 1 (Tinman) <-> Box 2 (Agent).
    x1_right = box_xs[0] + box_w
    x2_left = box_xs[1]
    ax.add_patch(FancyArrowPatch(
        (x1_right, box_y + box_h * 0.62),
        (x2_left,  box_y + box_h * 0.62),
        **arrow_kw,
    ))
    ax.add_patch(FancyArrowPatch(
        (x2_left,  box_y + box_h * 0.38),
        (x1_right, box_y + box_h * 0.38),
        **arrow_kw,
    ))
    mid_12 = (x1_right + x2_left) / 2
    ax.text(
        mid_12, box_y + box_h + 1.4,
        "workflow state",
        fontsize=9.0, color=text_dark, style="italic",
        ha="center", va="bottom",
    )
    ax.text(
        mid_12, box_y - 5.7,
        "actions",
        fontsize=9.0, color=text_dark, style="italic",
        ha="center", va="top",
    )

    # ----- Box 2 (Agent) <-> Box 4 (Human escalation), routed BELOW the
    # box-bottom italic labels via two clearly separated horizontal lanes
    # that do not touch box 3's interior, the box-bottom labels, or the
    # evidence band.
    x2_centre = box_xs[1] + box_w / 2
    x4_centre = box_xs[3] + box_w / 2

    # Two horizontal lanes (top: escalation; bottom: handback) with stub
    # verticals from each box's bottom edge.
    esc_y = box_y - 9.5    # y = 38.5
    hand_y = box_y - 14.5  # y = 33.5

    # Outbound: agent -> human (escalation), top lane.
    ax.add_patch(FancyArrowPatch(
        (x2_centre - 2, box_y),
        (x2_centre - 2, esc_y),
        arrowstyle="-", lw=1.55, color=arrow_color, mutation_scale=14,
    ))
    ax.add_patch(FancyArrowPatch(
        (x2_centre - 2, esc_y),
        (x4_centre - 2, esc_y),
        arrowstyle="-", lw=1.55, color=arrow_color, mutation_scale=14,
    ))
    ax.add_patch(FancyArrowPatch(
        (x4_centre - 2, esc_y),
        (x4_centre - 2, box_y - 0.2),
        **arrow_kw,
    ))

    # Inbound: human -> agent (handback / decision artefact), bottom lane.
    ax.add_patch(FancyArrowPatch(
        (x4_centre + 2, box_y),
        (x4_centre + 2, hand_y),
        arrowstyle="-", lw=1.55, color=arrow_color, mutation_scale=14,
    ))
    ax.add_patch(FancyArrowPatch(
        (x4_centre + 2, hand_y),
        (x2_centre + 2, hand_y),
        arrowstyle="-", lw=1.55, color=arrow_color, mutation_scale=14,
    ))
    ax.add_patch(FancyArrowPatch(
        (x2_centre + 2, hand_y),
        (x2_centre + 2, box_y - 0.2),
        **arrow_kw,
    ))

    # Lane labels (centred over each lane).
    label_x = (x2_centre + x4_centre) / 2
    ax.text(
        label_x, esc_y + 1.0,
        "regulated-step escalation",
        fontsize=9.4, color=text_dark, style="italic",
        ha="center", va="bottom",
    )
    ax.text(
        label_x, hand_y + 1.0,
        "handback / decision artefact",
        fontsize=9.4, color=text_dark, style="italic",
        ha="center", va="bottom",
    )

    # --------------------------------------------- evidence / governance band
    band_y = 14.0
    band_h = 16.0
    ax.add_patch(FancyBboxPatch(
        (4, band_y), 92, band_h,
        boxstyle="round,pad=0.5,rounding_size=1.0",
        linewidth=1.2,
        edgecolor="#888888",
        facecolor="#F8F4E3",
        alpha=0.95,
    ))
    ax.text(
        50, band_y + band_h - 2.6,
        "Governance & multidimensional measurement (Chapter 6 \u00a76.5)",
        ha="center", va="top",
        fontsize=11.2, fontweight="bold", color=text_dark,
    )
    ax.text(
        50, band_y + band_h - 7.0,
        "Audited financials (10-K; expense ratio, RPE, net loss)   \u2022   "
        "Management-reported KPIs (NPS; CSAT; call volume)",
        ha="center", va="top",
        fontsize=9.4, color=text_dark,
    )
    ax.text(
        50, band_y + band_h - 11.0,
        "Independent customer discourse (Trustpilot ratings, VADER, "
        "BERTopic, keyword prevalence)   \u2022   Vendor materials (flagged)",
        ha="center", va="top",
        fontsize=9.4, color=text_dark,
    )

    # ---------------------------------------------------------- footer
    ax.text(
        50, 4.5,
        "Source: author, derived from Chapters 4 and 5 of this thesis. "
        "Each coloured box represents a prerequisite condition; arrows "
        "show the dataflow and",
        ha="center", va="bottom",
        fontsize=8.3, color=text_dark, style="italic",
    )
    ax.text(
        50, 1.7,
        "regulated-step escalation paths observed in the case-study evidence.",
        ha="center", va="bottom",
        fontsize=8.3, color=text_dark, style="italic",
    )

    plt.tight_layout(rect=(0, 0, 1, 1))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Save at 300 dpi for thesis-quality embedding (~3900 x 2550 px). The
    # PNG writer uses lossless deflate compression so embedding in Word
    # does not introduce additional compression artefacts.
    plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    out_path = os.path.join(FIG_DESIGN, "fig_6_1_design_pattern.png")
    build_figure(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
