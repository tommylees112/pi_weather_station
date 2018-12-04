# assert_all_done.sh
for year in `seq 2001 2018`; do
  ls oxford_weather_station/$year | grep ".pkl";

done
