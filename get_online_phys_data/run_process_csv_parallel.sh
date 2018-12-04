# run_process_csv_parallel.sh
for year in `seq 2001 2018`; do
  python process_csv_files.py -y $year &
done
