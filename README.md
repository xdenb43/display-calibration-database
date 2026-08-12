# Display Configuration Database

Database of display configurations, calibration data and measurements focused on long-term visual comfort and accurate image reproduction.

This repository contains display settings, ICC/ICM color profiles, verification reports, measurements and engineering documentation for monitors, laptops, smartphones, tablets and TVs.

[![ReadMe](https://img.shields.io/badge/ReadMe-018EF5?logo=readme&logoColor=fff)](README.md)
[![Latest Release](https://img.shields.io/github/v/release/xdenb43/display-configuration-database)](https://github.com/xdenb43/display-configuration-database/releases)
[![License](https://img.shields.io/github/license/xdenb43/display-configuration-database)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/xdenb43/display-configuration-database)](https://github.com/xdenb43/display-configuration-database/commits/main)

## Table of Contents

- [Repository structure](#repository-structure)
- [Device categories](#device-categories)
- [Configuration and calibration philosophy](#configuration-and-calibration-philosophy)
- [Disclaimer](#disclaimer)
- [License](#license)

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
├── tablets/
└── tv/
```

Each device directory is self-contained and may include:  
- Device documentation (`README.md`)  
- Display configuration and recommended settings  
- ICC/ICM color profile (if applicable)
- Display verification report (if applicable)
- Additional measurements, notes or images (optional)

## Device categories

| Category           | Description                              |
| ------------------ | ---------------------------------------- |
| 🖥️ **Monitors**   | External LCD, Mini LED and OLED displays |
| 💻 **Laptops**     | Built-in notebook displays               |
| 📱 **Smartphones** | Mobile device displays                   |
| 📱 **Tablets**     | Tablet displays                          |
| 📺 **TVs**         | Television displays                      |


## Configuration and calibration philosophy

The repository follows a physics-first and verification-first approach.  

- Display behavior is determined primarily by the physical characteristics of the display.  
- Settings are selected based on the display's hardware characteristics and, where available, real measurements.  
- Monitor calibration is performed through the display's hardware controls whenever possible.  
- ICC/ICM profiles complement display calibration and color management; they do not change the physical properties of the display.  
- Smartphone and tablet entries primarily document Daily Use configurations optimized for long-term visual comfort, readability and appropriate luminance.  
- Verification reports and measurements are provided whenever available to document the resulting display behavior.  
- Changes to calibration or configuration parameters are made only after verification rather than by assumption.  

## Disclaimer

Calibration and display configuration results are device-specific.  

Even identical display models may differ due to manufacturing tolerances, panel revisions, aging, firmware, display modes and user settings. Published configurations and profiles should therefore be considered reference configurations and may not provide identical results on another unit.  

## License

Unless otherwise stated, all documentation is released under the MIT License.  

Calibration profiles, verification reports, measurements and configuration recommendations are provided for educational and research purposes.  

[⬆️ Back to TOC](#table-of-contents)