Author: Yoohyuk Chang

1. util_data/simul_settings.yaml 에 보면 time 하고 city 정할 수 있음. 여기에 designate 해놓으면 모든 세팅이 이걸로 되는거니까 참고하삼.

2. city_info.py 를 먼저 돌린다. 돌리면 util_data 파일 안에 세팅한 도시의 관련된 파일이 safegraph 로부터 extract 해서 생성될 것임.
3. move.py 를 돌린다. results_data 파일에 지정된 도시 관련된 poi 파일과 household 파일이 각각 생성된다.
4. determine_movement_by_poi_timestep.py 를 돌린다. Simulations 팀에게 주기 적합한 포맷으로 convert 한다.



TODO: Make a driver file to run all these at once. (But need to await each of the files.)

<Driver program (Assume that {City Name}.yaml file is already created by running city_info.py)>
먼저 {city name}.yaml 을 만들어 놔야함.
그리고 driver.py 를 돌린다.
