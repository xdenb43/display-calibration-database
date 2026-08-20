from pathlib import Path
import html


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
# Global generated metadata
# ============================================================

META_DIR = ROOT_DIR / ".meta"


# ============================================================
# Shields.io palette
#
# Source:
# https://github.com/badges/shields/blob/master/badge-maker/lib/color.js
#
# green      = #67AC09
# important  = #EA7233
# critical   = #DD4343
# inactive   = #9F9F9F
# ============================================================

SHIELDS_COLORS = {
    "green": "#67AC09",
    "important": "#EA7233",
    "critical": "#DD4343",
    "inactive": "#9F9F9F",
}


# ============================================================
# Color helpers
# ============================================================

def darken_color(
    hex_color: str,
    factor: float = 0.94,
) -> str:

    """
    Create a slightly darker version of a HEX color.

    factor:
        1.00 -> unchanged
        0.94 -> slightly darker
    """

    hex_color = hex_color.lstrip("#")

    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    red = round(red * factor)
    green = round(green * factor)
    blue = round(blue * factor)

    return (
        f"#{red:02X}"
        f"{green:02X}"
        f"{blue:02X}"
    )


def get_gradient_colors(
    shields_color: str,
) -> tuple[str, str]:

    """
    Return a very subtle vertical gradient.

    The top color is the exact Shields.io color.
    The bottom color is only slightly darker.
    """

    top_color = SHIELDS_COLORS[
        shields_color
    ]

    bottom_color = darken_color(
        top_color,
        0.94,
    )

    return (
        top_color,
        bottom_color,
    )


# ============================================================
# Badge generation
# ============================================================

def create_badge(
    label: str,
    message: str,
    color: tuple[str, str],
    label_width: int,
    message_width: int,
) -> str:

    total_width = (
        label_width
        + message_width
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{total_width}"
    height="20"
    role="img"
    aria-label="{html.escape(label)}: {html.escape(message)}">

    <title>{html.escape(label)}: {html.escape(message)}</title>

    <defs>

        <!--
            Very subtle Shields-inspired gradient
            for the label section.
        -->
        <linearGradient id="labelGradient"
                        x1="0"
                        y1="0"
                        x2="0"
                        y2="1">

            <stop offset="0%"
                  stop-color="#5A5A5A"/>

            <stop offset="100%"
                  stop-color="#505050"/>

        </linearGradient>


        <!--
            Very subtle status gradient.
            Keeps the Shields.io base color
            while avoiding a completely flat look.
        -->
        <linearGradient id="messageGradient"
                        x1="0"
                        y1="0"
                        x2="0"
                        y2="1">

            <stop offset="0%"
                  stop-color="{color[0]}"/>

            <stop offset="100%"
                  stop-color="{color[1]}"/>

        </linearGradient>


        <!--
            Very soft top highlight.
            Much weaker than the original version.
        -->
        <linearGradient id="highlightGradient"
                        x1="0"
                        y1="0"
                        x2="0"
                        y2="1">

            <stop offset="0%"
                  stop-color="#FFFFFF"
                  stop-opacity="0.08"/>

            <stop offset="60%"
                  stop-color="#FFFFFF"
                  stop-opacity="0.02"/>

            <stop offset="100%"
                  stop-color="#FFFFFF"
                  stop-opacity="0"/>

        </linearGradient>

    </defs>


    <!-- =====================================================
         Base badge
         ===================================================== -->

    <rect x="0"
          y="0"
          width="{total_width}"
          height="20"
          rx="3.5"
          fill="#555555"/>


    <!-- =====================================================
         Label section
         ===================================================== -->

    <path
        d="
            M 3.5 0
            H {label_width}
            V 20
            H 3.5
            A 3.5 3.5 0 0 1 0 16.5
            V 3.5
            A 3.5 3.5 0 0 1 3.5 0
            Z
        "
        fill="url(#labelGradient)"
    />


    <!-- =====================================================
         Message section
         ===================================================== -->

    <path
        d="
            M {label_width} 0
            H {total_width - 3.5}
            A 3.5 3.5 0 0 1 {total_width} 3.5
            V 16.5
            A 3.5 3.5 0 0 1 {total_width - 3.5} 20
            H {label_width}
            Z
        "
        fill="url(#messageGradient)"
    />


    <!-- =====================================================
         Soft highlight
         ===================================================== -->

    <rect x="0"
          y="0"
          width="{total_width}"
          height="10"
          rx="3.5"
          fill="url(#highlightGradient)"/>


    <!-- =====================================================
         Text
         ===================================================== -->

    <g fill="#FFFFFF"
       text-anchor="middle"
       font-family="Verdana,DejaVu Sans,sans-serif"
       font-size="11"
       font-weight="400">

        <text x="{label_width / 2}"
              y="14.5">

            {html.escape(label)}

        </text>


        <text x="{label_width + message_width / 2}"
              y="14.5">

            {html.escape(message)}

        </text>

    </g>


</svg>
'''


# ============================================================
# Standard availability badges
# ============================================================

def write_badge(
    path: Path,
    label: str,
    available: bool,
    label_width: int,
    message_width: int,
):

    message = (
        "available"
        if available
        else "unavailable"
    )

    if available:

        color = get_gradient_colors(
            "green"
        )

    else:

        color = get_gradient_colors(
            "critical"
        )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        create_badge(
            label,
            message,
            color,
            label_width,
            message_width,
        ),
        encoding="utf-8",
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

        color = get_gradient_colors(
            "important"
        )

        message_width = 50

    else:

        message = "validated"

        color = get_gradient_colors(
            "green"
        )

        message_width = 68

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        create_badge(
            "Page status",
            message,
            color,
            88,
            message_width,
        ),
        encoding="utf-8",
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

    0 Draft pages:
        inactive / grey

    1+ Draft pages:
        important / orange
    """

    if draft_count > 0:

        color = get_gradient_colors(
            "important"
        )

    else:

        color = get_gradient_colors(
            "inactive"
        )

    message = str(draft_count)

    message_width = max(
        32,
        22 + len(message) * 7,
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        create_badge(
            "Draft pages",
            message,
            color,
            76,
            message_width,
        ),
        encoding="utf-8",
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
    <title>File unavailable</title>
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

    # Global Draft page counter.
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
                    90,
                    84,
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
                    118,
                    91,
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
    #     inactive / grey
    #
    # 1+:
    #     important / orange
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