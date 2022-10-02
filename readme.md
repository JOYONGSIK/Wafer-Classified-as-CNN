## NOTICE
- <b>용민아, 최우수상 축하한다</b> 👋  

<hr>

# Wafer-Classified-as-CNN

- 반도체 웨이퍼를 분류하기 위한 CNN Repo.<br>
*(Repo, Classifying Semiconductor Wafers)*

- 버전 관리 및 배포를 편하게 하기 위해서, docker 사용.<br>
*(Use docker, For ease of Vesion management & deployment)*
    - (용민이가 팀원에게 배포 편하게 하라고. :D)

- Docker Build *(default port 8080)*
    - 오류나면, --recv-keys {Your Key} 기입.
```
cd docker

docker build -t wafer-classified-as-cnn:latest . 
or 
Check -> scripts/build :D 
```

- Docker Run
```
cd .. 

docker run --name wafer-classified-as-cnn --gpus all -v $(pwd):/Wafer-Classified-as-CNN -dit --ipc=host wafer-classified-as-cnn:latest 
```

- Docker Attach
```
docker attach wafer-classified-as-cnn
```

- Create venv Environment
```
python -m venv venv
source ./venv/bin/activate
```

- Create Development Package 
    - 이 부분 오류나면, 그냥 pip instll 으로 깔아서 써 :D (requirements.cpu-dev.txt 참고.)
    - 수정하고 싶으면, setup extras 부분 check.
```
pip install -e "."
```

<hr>

- Data 준비 ? 
    - data 폴더에서 image_data(Folder)를 넣고, 아래 코드 실행!
    ```sh 
    sh scripts/split.sh
    ```

- 평균과 표준편차로 이미지 normalization을 진행하는 코드? [dataset.py](src/wafer/dataset/dataset.py)에서 `get_mean_std` 확인 가능! 

<br>

# 정리는 내일..