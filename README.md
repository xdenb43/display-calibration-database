<a id="top"></a>
# Display Configuration Database

Database of display configurations, calibration data and measurements focused on long-term visual comfort and accurate image reproduction.

This repository contains display settings, ICC/ICM color profiles, verification reports, measurements and engineering documentation for monitors, laptops, smartphones, tablets and TVs.

[![Monitors](https://img.shields.io/github/directory-file-count/xdenb43/display-configuration-database/monitors?type=dir&label=Monitors&color=informational)](https://github.com/xdenb43/display-configuration-database/tree/main/monitors)
[![Laptops](https://img.shields.io/github/directory-file-count/xdenb43/display-configuration-database/laptops?type=dir&label=Laptops&color=informational)](https://github.com/xdenb43/display-configuration-database/tree/main/laptops)
[![Smartphones](https://img.shields.io/github/directory-file-count/xdenb43/display-configuration-database/smartphones?type=dir&label=Smartphones&color=informational)](https://github.com/xdenb43/display-configuration-database/tree/main/smartphones)
[![Tablets](https://img.shields.io/github/directory-file-count/xdenb43/display-configuration-database/tablets?type=dir&label=Tablets&color=informational)](https://github.com/xdenb43/display-configuration-database/tree/main/tablets)
[![TVs](https://img.shields.io/github/directory-file-count/xdenb43/display-configuration-database/tv?type=dir&label=TVs&color=informational)](https://github.com/xdenb43/display-configuration-database/tree/main/tv)
<sup align="right">[![Draft pages](.meta/draft-pages.svg)](.meta/draft-pages/)</sup>

## Table of contents

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

| Category       | Description                              |
| -------------- | ---------------------------------------- |
| 🖥️ Monitors    | External LCD, Mini LED and OLED displays |
| 💻 Laptops     | Built-in notebook displays               |
| 📱 Smartphones | Mobile device displays                   |
| 📱 Tablets     | Tablet displays                          |
| 📺 TVs         | Television displays                      |


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

<p align="right">
  <a href="#top">⬆️ Top</a>
</p>