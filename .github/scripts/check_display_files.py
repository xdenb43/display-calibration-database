from pathlib import Path
import sys
import html
import yaml


CONFIG_FILE = Path(".github/display-file-check.yml")
ROOT_DIR = Path(".")
BADGES_DIR = ROOT_DIR / "badges"


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
    target_path: Path | None,
    unavailable_message: str,
):
    redirect_path.parent.mkdir(parents=True, exist_ok=True)

    if target_path is None:
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
        # Calculate the relative URL from the redirect HTML
        # to the target file.
        relative_target = (
            target_path
            .relative_to(redirect_path.parent)
            if target_path.is_relative_to(redirect_path.parent)
            else None
        )

        if relative_target is None:
            import os

            relative_target = Path(
                os.path.relpath(
                    target_path,
                    redirect_path.parent,
                )
            )

        target_url = str(relative_target).replace("\\", "/")

        content = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={html.escape(target_url, quote=True)}">
    <title>Redirecting...</title>
</head>
<body>
    <p>
        Redirecting to
        <a href="{html.escape(target_url, quote=True)}">
            {html.escape(target_path.name)}
        </a>
    </p>

    <script>
        window.location.replace({target_url!r});
    </script>
</body>
</html>
"""

    redirect_path.write_text(content, encoding="utf-8")


def find_first_file(device_dir: Path, extensions: set[str]):
    """
    Search ONLY directly inside device_dir.
    No recursive search.
    """
    for file in sorted(device_dir.iterdir()):
        if file.is_file() and file.suffix.lower() in extensions:
            return file

    return None


def main():
    if not CONFIG_FILE.exists():
        print(f"ERROR: configuration file not found: {CONFIG_FILE}")
        sys.exit(1)

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    categories = config.get("categories", [])

    if not categories:
        print("ERROR: no categories configured")
        sys.exit(1)

    BADGES_DIR.mkdir(parents=True, exist_ok=True)

    for category in categories:
        category_dir = ROOT_DIR / category

        if not category_dir.is_dir():
            print(f"WARNING: category does not exist: {category_dir}")
            continue

        print(f"\nCategory: {category}")

        # Only immediate subdirectories are treated as devices.
        for device_dir in sorted(category_dir.iterdir()):

            if not device_dir.is_dir():
                continue

            device = device_dir.name

            print(f"  Checking: {device}")

            icc_file = find_first_file(
                device_dir,
                {".icc", ".icm"},
            )

            report_file = find_first_file(
                device_dir,
                {".html"},
            )

            badge_dir = BADGES_DIR / category / device

            # --------------------------------------------------
            # ICC
            # --------------------------------------------------

            write_badge(
                badge_dir / "icc.svg",
                "ICC profile",
                icc_file is not None,
                90,
                84,
            )

            create_redirect(
                badge_dir / "icc.html",
                icc_file,
                "ICC profile is not available.",
            )

            # --------------------------------------------------
            # Verification report
            # --------------------------------------------------

            write_badge(
                badge_dir / "report.svg",
                "Verification report",
                report_file is not None,
                118,
                91,
            )

            create_redirect(
                badge_dir / "report.html",
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