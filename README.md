
# Yosys Tool Automation
## Directory structure
``` tree
yosys_automation
├── designs
│   ├── design1_top
│   │   └── design1_top.v
│   ├── design2_top
│   │   └── design2_top.v
│   └── designs.txt
├── logs
│   ├── design1_top.log
│   └── design2_top.log
├── Makefile
├── README.md
├── Reports
│   └── designs_info.csv
└── scripts
    ├── run_flow.py
    ├── script_csv_info.py
    └── ys_script.ys
```

## Instructions

1. Copy your all designs in the `designs/` directory. The design folder name should be same as the top module name of the design.
2. Enter comma-separated design file name as well as design top module name in the `designs.txt` file.

## Sample for designs.txt
```txt
design1_top.v,design1_top
design2_top.v,design2_top
```

> **Note:** Name of each design folder should be same as the top module name of the design.

# Usage
Run the following command in the terminal to clean all the previous logs.
```bash
make clean
```
Run the following command in the terminal to run the complete yosys flow and generate csv report.
```bash
make all
```
> **Note:** `make all` will clean all the previous design logs in the `logs/` directory and new logs will be generated.


All the design logs will be generated in the `logs/` directory.
The CSV file `designs_info.csv` will be generated at the end in the `Reports/` directory.