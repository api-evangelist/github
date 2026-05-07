#!/usr/bin/env python3
"""Build the GitHub API tube-style map.

42 of GitHub's APIs grouped onto 8 product lines. Mixed shapes:
arcs, sine waves, an L-shape (Identity & Org), a vertical drop
(Deploy & Codespaces), and a closed heptagonal loop for the
"Resources" family of static helper APIs.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Repository Invitations": "Repo Invitations",
    "Code of Conduct": "Code of Conduct",
}

LINES = [
    {
        "name": "Repositories — Core",
        "color": "#E0245E",
        # Concave-up arc — middle stations sit higher than the endpoints.
        "stations": [
            ("Repos",    (260, 195)),
            ("Branches", (400, 170)),
            ("Tags",     (540, 160)),
            ("Commits",  (680, 165)),
            ("Pulls",    (820, 180)),
            ("Webhooks", (960, 200)),
        ],
    },
    {
        "name": "Repositories — Collaboration",
        "color": "#E68B1F",
        # Short concave-up arc.
        "stations": [
            ("Collaborators",          (430, 280)),
            ("Repository Invitations", (640, 260)),
            ("Reactions",              (850, 280)),
        ],
    },
    {
        "name": "Code Quality & Security",
        "color": "#0B7956",
        # Sine wave.
        "stations": [
            ("Actions",         (260, 365)),
            ("Checks",          (430, 345)),
            ("Code Scanning",   (610, 365)),
            ("Secret Scanning", (790, 345)),
            ("Dependabot",      (970, 365)),
        ],
    },
    {
        "name": "Issues & Activity",
        "color": "#0E9D6E",
        # Concave-up arc with 7 stations.
        "stations": [
            ("Issues",        (270, 470)),
            ("Projects",      (400, 440)),
            ("Search",        (510, 425)),
            ("Notifications", (620, 425)),
            ("Events",        (730, 425)),
            ("Feeds",         (840, 440)),
            ("Gists",         (970, 470)),
        ],
    },
    {
        "name": "Identity & Org",
        "color": "#1E5BD0",
        # J-shape — vertical drop on the left, then 45° bend right.
        "stations": [
            ("Users",   (260, 545)),
            ("Org",     (260, 605)),
            ("Teams",   (290, 660)),
            ("Auth",    (350, 695)),
            ("SCIM",    (420, 720)),
        ],
    },
    {
        "name": "Apps",
        "color": "#7B3FE4",
        # Short concave-down arc dipping in the middle.
        "stations": [
            ("App",          (510, 545)),
            ("Installation", (620, 535)),
            ("Copilot",      (730, 535)),
            ("Models",       (840, 545)),
        ],
    },
    {
        "name": "Deploy & Codespaces",
        "color": "#C5318B",
        # Vertical drop on the right edge.
        "stations": [
            ("Releases",    (1020, 460)),
            ("Pages",       (1020, 530)),
            ("Deployments", (1020, 600)),
            ("Packages",    (1020, 670)),
            ("Codespaces",  (1020, 740)),
        ],
    },
    {
        "name": "Resources",
        "color": "#5A6275",
        # Closed heptagonal loop centered on (820, 760), radius 50.
        # 7 evenly-spaced points around a circle (51.4° apart).
        "closed": True,
        "stations": [
            ("Licenses",        (870, 760)),  # 0°
            ("Gitignore",       (851, 799)),  # 51.4°
            ("Markdown",        (809, 808)),  # 102.9°
            ("Emojis",          (770, 781)),  # 154.3°
            ("Octocat",         (770, 738)),  # 205.7°
            ("Zen",             (809, 712)),  # 257.1°
            ("Code of Conduct", (851, 721)),  # 308.6°
        ],
    },
]

# Stations whose canonical apis.yml aid doesn't follow {provider}-{slug(name)}-api.
URL_OVERRIDES = {
    "Pulls":     "https://apis.apis.io/apis/github/github-pull-requests-api/",
    "Users":     "https://apis.apis.io/apis/github/github-user-api/",
    "Gitignore": "https://apis.apis.io/apis/github/github-gitignore-templates-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)

    build_subway(
        title="The GitHub API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · "
                 f"click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: github/openapi/*.yml · github.com/api-evangelist/github",
        out_dir=Path(__file__).resolve().parent,
        out_basename="github-subway-map",
        provider_id="github",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
