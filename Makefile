all: 	clean run_flow csv_report

run_flow:
	python3 scripts/run_flow.py

run_fpga_flow:
	python3 scripts/run_fpga_flow.py

csv_report:
	python3 scripts/script_csv_info.py

clean:
	rm  -rf logs/*.log

