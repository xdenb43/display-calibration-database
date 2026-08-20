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


def create_badge(
    label: str,
    message: str,
    color: str,
    label_width: int,
    message_width: int,
) -> str:

    total_width = label_width + message_width

    return f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{total_width}"
    height="20"
    role="img"
    aria-label="{html.escape(label)}: {html.escape(message)}">

    <title>{html.escape(label)}: {html.escape(message)}</title>

    <rect width="{total_width}" height="20" rx="3" fill="#555"/>

    <rect x="{label_width}"
          width="{message_width}"
          height="20"
          fill="{color}"/>

    <g fill="#fff"
       text-anchor="middle"
       font-family="Verdana,DejaVu Sans,sans-serif"
       font-size="11">

        <text x="{label_width / 2}"
              y="15">
            {html.escape(label)}
        </text>

        <text x="{label_width + message_width / 2}"
              y="15">
            {html.escape(message)}
        </text>

    </g>
</svg>
'''


def write_badge(
    path: Path,
    label: str,
    available: bool,
    label_width: int,
    message_width: int,
):

    message = "available" if available else "unavailable"
    color = "#2ea44f" if available else "#d73a49"

    path.parent.mkdir(parents=True, exist_ok=True)

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


def create_redirect(
    redirect_path: Path,
    target_file: Path | None,
    unavailable_message: str,
):

    redirect_path.parent.mkdir(parents=True, exist_ok=True)

    if target_file is None:

        content = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>File unavailable</title>
</head>
<body>
    <p>{html.escape(unavailable_message)}</p>
</body>
</html>
"""

    else:

        # Target file is located one directory above "badges".
        target_url = f"../{target_file.name}"

        content = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Download {html.escape(target_file.name)}</title>
</head>

<body>

<p>
    Downloading
    <strong>{html.escape(target_file.name)}</strong>...
</p>

<script>
(function () {{
    const url = {target_url!r};
    const filename = {target_file.name!r};

    const link = document.createElement("a");
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
            Download {html.escape(target_file.name)}
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


def find_first_file(device_dir: Path, extensions: set[str]):

    for file in sorted(device_dir.iterdir()):

        if (
            file.is_file()
            and file.suffix.lower() in extensions
        ):
            return file

    return None


def main():

    for category in CATEGORIES:

        category_dir = ROOT_DIR / category

        if not category_dir.is_dir():

            print(
                f"WARNING: category does not exist: "
                f"{category_dir}"
            )

            continue

        print(f"\nCategory: {category}")

        for device_dir in sorted(category_dir.iterdir()):

            if not device_dir.is_dir():
                continue

            device = device_dir.name

            print(f"  Checking: {device}")

            # Only files directly inside the device directory.
            icc_file = find_first_file(
                device_dir,
                {".icc", ".icm"},
            )

            report_file = find_first_file(
                device_dir,
                {".html"},
            )

            badges_dir = device_dir / "badges"

            # ICC badge
            write_badge(
                badges_dir / "icc.svg",
                "ICC profile",
                icc_file is not None,
                90,
                84,
            )

            # ICC redirect
            create_redirect(
                badges_dir / "icc.html",
                icc_file,
                "ICC profile is not available.",
            )

            # Verification badge
            write_badge(
                badges_dir / "report.svg",
                "Verification report",
                report_file is not None,
                118,
                91,
            )

            # Verification redirect
            create_redirect(
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


if __name__ == "__main__":
    main()