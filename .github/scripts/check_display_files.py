from pathlib import Path
import html
import subprocess


ROOT_DIR = Path(".")

CATEGORIES = [
    "monitors",
    "laptops",
    "tablets",
    "tv",
    "smartphones",
]

FILE_BADGE_CATEGORIES = {
    "monitors",
    "laptops",
}


# ============================================================
# Paths
# ============================================================

SCRIPT_DIR = Path(__file__).resolve().parent

BADGE_GENERATOR = (
    SCRIPT_DIR / "generate_badge.js"
)

META_DIR = ROOT_DIR / ".meta"


# ============================================================
# Shields.io colors
#
# These names are passed directly to badge-maker.
# ============================================================

SHIELDS_COLORS = {
    "green": "green",
    "important": "important",
    "critical": "critical",
    "inactive": "inactive",
}


# ============================================================
# Badge generation
# ============================================================

def generate_badge(
    path: Path,
    label: str,
    message: str,
    color: str,
):
    """
    Generate an SVG badge using the official Shields.io
    badge-maker package through generate_badge.js.
    """

    if not BADGE_GENERATOR.exists():

        raise FileNotFoundError(
            "Badge generator not found: "
            f"{BADGE_GENERATOR}"
        )

    result = subprocess.run(
        [
            "node",
            str(BADGE_GENERATOR),
            label,
            message,
            color,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    if result.returncode != 0:

        print(
            "ERROR: badge generation failed."
        )

        if result.stderr:
            print(result.stderr)

        raise RuntimeError(
            "badge-maker returned "
            f"exit code {result.returncode}"
        )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        result.stdout,
        encoding="utf-8",
    )


# ============================================================
# Availability badges
# ============================================================

def write_badge(
    path: Path,
    label: str,
    available: bool,
):
    """
    Generate an availability badge.

    Available:
        green

    Unavailable:
        critical
    """

    if available:

        message = "available"

        color = SHIELDS_COLORS[
            "green"
        ]

    else:

        message = "unavailable"

        color = SHIELDS_COLORS[
            "critical"
        ]

    generate_badge(
        path,
        label,
        message,
        color,
    )


# ============================================================
# Page status
# ============================================================

def is_page_draft(
    readme_file: Path,
) -> bool:

    if not readme_file.exists():
        return False

    content = readme_file.read_text(
        encoding="utf-8",
        errors="ignore",
    )

    return (
        "<!-- PAGE_STATUS: DRAFT -->"
        in content
    )


def write_status_badge(
    path: Path,
    is_draft: bool,
):

    if is_draft:

        message = "draft"

        color = SHIELDS_COLORS[
            "important"
        ]

    else:

        message = "validated"

        color = SHIELDS_COLORS[
            "green"
        ]

    generate_badge(
        path,
        "Page status",
        message,
        color,
    )


# ============================================================
# Global Draft pages badge
# ============================================================

def write_draft_pages_badge(
    path: Path,
    draft_count: int,
):
    """
    Generate the global Draft pages badge.

    0:
        inactive / grey

    1+:
        important / orange
    """

    if draft_count > 0:

        color = SHIELDS_COLORS[
            "important"
        ]

    else:

        color = SHIELDS_COLORS[
            "inactive"
        ]

    generate_badge(
        path,
        "Draft pages",
        str(draft_count),
        color,
    )


# ============================================================
# ICC download redirect
# ============================================================

def create_redirect(
    redirect_path: Path,
    target_file: Path | None,
    unavailable_message: str,
):

    redirect_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if target_file is None:

        content = f"""<!doctype html>
<html lang="en">

<head>

    <meta charset="utf-8">

    <title>
        File unavailable
    </title>

</head>

<body>

<p>
    {html.escape(unavailable_message)}
</p>

</body>

</html>
"""

    else:

        target_url = (
            f"../{target_file.name}"
        )

        content = f"""<!doctype html>
<html lang="en">

<head>

    <meta charset="utf-8">

    <title>
        Download {html.escape(target_file.name)}
    </title>

</head>

<body>

<p>

    Downloading
    <strong>
        {html.escape(target_file.name)}
    </strong>...

</p>


<script>

(function () {{

    const url = {target_url!r};
    const filename = {target_file.name!r};

    const link =
        document.createElement("a");

    link.href = url;
    link.download = filename;

    document.body.appendChild(link);

    link.click();

    link.remove();

}})();

</script>


<noscript>

<p>

<a href="{html.escape(target_url, quote=True)}"
   download="{html.escape(target_file.name, quote=True)}">

    Download
    {html.escape(target_file.name)}

</a>

</p>

</noscript>


</body>

</html>
"""

    redirect_path.write_text(
        content,
        encoding="utf-8",
    )


# ============================================================
# Verification report redirect
# ============================================================

def create_page_redirect(
    redirect_path: Path,
    target_file: Path | None,
    unavailable_message: str,
):

    redirect_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if target_file is None:

        content = f"""<!doctype html>
<html lang="en">

<head>

    <meta charset="utf-8">

    <title>
        File unavailable
    </title>

</head>

<body>

<p>
    {html.escape(unavailable_message)}
</p>

</body>

</html>
"""

    else:

        target_url = (
            f"../{target_file.name}"
        )

        content = f"""<!doctype html>
<html lang="en">

<head>

    <meta charset="utf-8">

    <meta http-equiv="refresh"
          content="0; url={html.escape(target_url, quote=True)}">

    <title>
        Verification report
    </title>

</head>

<body>

<p>
    Opening verification report...
</p>

</body>

</html>
"""

    redirect_path.write_text(
        content,
        encoding="utf-8",
    )


# ============================================================
# File detection
# ============================================================

def find_first_file(
    device_dir: Path,
    extensions: set[str],
):

    for file in sorted(
        device_dir.iterdir()
    ):

        if (
            file.is_file()
            and file.suffix.lower()
            in extensions
        ):

            return file

    return None


# ============================================================
# Remove ICC/report badges from categories
# where they are not allowed
# ============================================================

def remove_file_badges(
    device_dir: Path,
):

    badges_dir = (
        device_dir / "badges"
    )

    if not badges_dir.is_dir():
        return

    for filename in (
        "icc.svg",
        "icc.html",
        "report.svg",
        "report.html",
    ):

        file = (
            badges_dir / filename
        )

        if file.exists():

            file.unlink()

            print(
                f"    Removed: {file}"
            )


# ============================================================
# Main
# ============================================================

def main():

    draft_pages = 0


    for category in CATEGORIES:

        category_dir = (
            ROOT_DIR / category
        )


        if not category_dir.is_dir():

            print(
                f"WARNING: category does not exist: "
                f"{category_dir}"
            )

            continue


        print(
            f"\nCategory: {category}"
        )


        for device_dir in sorted(
            category_dir.iterdir()
        ):

            if not device_dir.is_dir():
                continue


            device = (
                device_dir.name
            )


            print(
                f"  Checking: {device}"
            )


            badges_dir = (
                device_dir / "badges"
            )


            # ==================================================
            # Page status
            #
            # Generated for ALL categories.
            #
            # <!-- PAGE_STATUS: DRAFT -->
            #     -> important
            #
            # No marker
            #     -> green
            # ==================================================

            readme_file = (
                device_dir / "README.md"
            )


            is_draft = is_page_draft(
                readme_file
            )


            write_status_badge(
                badges_dir / "status.svg",
                is_draft,
            )


            if is_draft:

                draft_pages += 1


            print(
                f"    Status: "
                f"{'draft' if is_draft else 'validated'}"
            )


            # ==================================================
            # ICC / HTML badges
            #
            # Generated ONLY for:
            #
            #     monitors
            #     laptops
            # ==================================================

            if (
                category
                in FILE_BADGE_CATEGORIES
            ):

                # Only files directly inside
                # the device directory.

                icc_file = find_first_file(
                    device_dir,
                    {
                        ".icc",
                        ".icm",
                    },
                )


                report_file = find_first_file(
                    device_dir,
                    {
                        ".html",
                    },
                )


                # --------------------------------------------------
                # ICC badge
                # --------------------------------------------------

                write_badge(
                    badges_dir / "icc.svg",
                    "ICC profile",
                    icc_file is not None,
                )


                # --------------------------------------------------
                # ICC download redirect
                # --------------------------------------------------

                create_redirect(
                    badges_dir / "icc.html",
                    icc_file,
                    "ICC profile is not available.",
                )


                # --------------------------------------------------
                # Verification report badge
                # --------------------------------------------------

                write_badge(
                    badges_dir / "report.svg",
                    "Verification report",
                    report_file is not None,
                )


                # --------------------------------------------------
                # Verification report redirect
                # --------------------------------------------------

                create_page_redirect(
                    badges_dir / "report.html",
                    report_file,
                    "Verification report is not available.",
                )


                print(
                    f"    ICC: "
                    f"{icc_file.name if icc_file else 'unavailable'}"
                )


                print(
                    f"    HTML: "
                    f"{report_file.name if report_file else 'unavailable'}"
                )


            else:

                # --------------------------------------------------
                # Remove old ICC/report badges from categories
                # where they are not allowed.
                # --------------------------------------------------

                remove_file_badges(
                    device_dir
                )


    # ============================================================
    # Global Draft pages badge
    #
    # 0:
    #     inactive
    #
    # 1+:
    #     important
    #
    # Generated:
    #
    # .meta/draft-pages.svg
    # ============================================================

    write_draft_pages_badge(
        META_DIR / "draft-pages.svg",
        draft_pages,
    )


    print(
        f"\nTotal Draft pages: {draft_pages}"
    )


    print(
        f"Generated: "
        f"{META_DIR / 'draft-pages.svg'}"
    )


if __name__ == "__main__":
    main()