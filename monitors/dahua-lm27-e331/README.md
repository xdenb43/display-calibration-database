# Dahua DHI-LM27-E331A   

Consumer 27-inch IPS gaming monitor featuring a PFS E-LED backlight.

Calibration optimized for visual comfort using Spyder X and DisplayCAL.

Official product page:  <https://www.dahuasecurity.com/mena/products/All-Products/Display--Control/Monitors/Gaming-Series/LM27-E331A>  

## Specifications  

| Parameter          | Value           |
| ------------------ | --------------- |
| Screen size        | 27"             |
| Panel type         | IPS             |
| Aspect Ratio       | 16:9            |
| Resolution         | 2560 × 1440     |
| Backlight          | E-LED WCG (PFS) |
| Refresh rate       | 180 Hz          |
| Typical brightness | 300 nits        |
| Contrast Ratio     | 1000:1          |
| Viewing Angle(H/V) | 178°(H)/178°(V) |
| Response time      | 1 ms            |


### Color characteristics
- Wide Color Gamut (WCG) declared by manufacturer
- Known color gamut:  
    - sRGB: ~ 99%  
    - NTSC: 85%  
    - DCI-P3: Not specified  
- Color depth: 8 bit + FRC  

## Calibration  

Calibration objective: **Visual comfort with reduced eye strain during prolonged use.**  

### Calibration environment  

| Parameter          | Value        |
| ------------------ | ------------ |
| Calibration date   | 2026-06-30   |
| Instrument         | Spyder X     |
| Software           | DisplayCAL   |
|                    |              |  
| Target white point | D65 (6500 K) |
| Target gamma       | 2.2          |
| Target luminance   | 120 cd/m²    |

### OSD settings  

- Display menu:  
    - Brightness: 22  
    - Contrast: 50  
    - Black level: 50  
    - Sharpness: 50  
- Colors menu:  
    - Red 50  
    - Green 49  
    - Blue 43  
- Gaming menu:  
    - FreeSync OFF  
    - Overdrive OFF  
    - DCR OFF  
    - MPRT OFF  
- Advanced menu:  
    - HDR OFF  
- Refresh Rate: 120 Hz fixed

## Downloads

> [!IMPORTANT]
> The ICC profile was created using the OSD settings listed above.
> Different monitor settings (brightness, RGB gain, contrast, etc.) may reduce color accuracy.

### Calibration
- [ICC profile](https://xdenb43.github.io/display-configuration-database/monitors/dahua-lm27-e331/DHI-LM27-E331_120cdm2_D6500_2.2_M-S_XYZLUT_MTX.icm)

### Reports  
- [Verification report (HTML)](https://xdenb43.github.io/display-configuration-database/monitors/dahua-lm27-e331/Measurement_Report_DHI-LM27-E331.html)
- [Verification report (PDF)](Measurement_Report_DHI-LM27-E331.pdf)

## Brightness Response Curve  

![Brightness vs. Luminance](brightness_vs_luminance_dhi_lm27_e331.png) 

> [!NOTE]
> Recommended luminance levels:
>
> - Night: 80–100 cd/m²
> - Evening: 100–120 cd/m²
> - Daylight: 120–140 cd/m²
> - Bright daylight: 140–160 cd/m²

|  OSD Brightness (%)  | Luminance (cd/m²) |
| :------------------: | :---------------: |
|          0           |        28         |
|          4           |        40         |
|          10          |        60         |
|          13          |        70         |
|        **16**        |      **80**       |
|          17          |        85         |
|          19          |        90         |
|        **22**        |      **100**      |
|        **27**        |      **120**      |
|        **33**        |      **140**      |
|          36          |        150        |
|          50          |        197        |
|          75          |        276        |
|         100          |        351        |
