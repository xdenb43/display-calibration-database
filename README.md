# Display Calibration Database

Database of display calibration settings focused on visual comfort and eye health.

This repository contains ICC/ICM color profiles, display verification reports and engineering documentation for monitors, laptops, smartphones and TVs.

---

## Repository structure

```text
project/
├── monitors/
│   └── device-name/
│       ├── README.md
│       ├── profile.icc / profile.icm
│       └── verification-report.html
│
├── laptops/
├── smartphones/
└── tv/
```

Each device directory is self-contained and may include:

- Device documentation (`README.md`)
- ICC/ICM color profile
- Display verification report
- Additional notes, measurements or images (optional)

---

## Device categories

| Category | Description |
|----------|-------------|
| 🖥️ Monitors | External LCD, Mini LED and OLED displays |
| 💻 Laptops | Built-in notebook displays |
| 📱 Smartphones | Mobile device displays |
| 📺 TVs | Television displays |

---

## Calibration philosophy

The repository is based on several engineering principles:

- Display behavior is determined by its physical characteristics.
- Calibration settings are derived from measurements, not assumptions.
- ICC/ICM profiles complement hardware calibration and do not change the physical properties of a display.
- Verification reports are provided whenever available to document calibration quality.

---

## Disclaimer

Calibration results are device-specific.

Even identical display models may differ due to manufacturing tolerances, panel revisions, aging and user settings. The published profiles should be considered reference configurations and may not provide identical accuracy on another unit.

---

## License

Unless otherwise stated, all documentation is released under the MIT License.

Calibration profiles, verification reports and documentation are provided for educational and research purposes.