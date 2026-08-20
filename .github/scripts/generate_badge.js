import { makeBadge } from "badge-maker";

const label = process.argv[2];
const message = process.argv[3];
const color = process.argv[4];

if (!label || !message || !color) {
    console.error(
        "Usage: node generate_badge.js <label> <message> <color>"
    );

    process.exit(1);
}

const svg = makeBadge({
    label,
    message,
    labelColor: "#555",
    color,
    style: "flat",
});

process.stdout.write(svg);