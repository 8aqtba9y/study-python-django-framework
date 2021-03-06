### command


##### 設置されているライブラリーのリストを出力し、現在のディレクトリに保存

```
$ pip3 freeze > requirements/dev.txt
```


##### ライブラリーリストを設置

```
$ pip3 install -r requrements/dev.txt
```


##### 開発環境毎に必要なライブラリーのリストが違う場合、以下の表に示したような定義ができる

|No|ファイル名|内容|
|:-:|:-:|:-:|
|1|requirements/dev.txt|ローカル開発用|
|2|requirements/stg.txt|ステージング用|
|3|requirements/prod.txt|本番用|
|4|requirements/prod_aws.txt|AWS EC2配布用|
|5|requirements/prod_aws_lambda.txt|AWS Lambda配布用|


##### 仮装環境ライブラリー **venv**

1. 仮装環境のディレクトリ生成

`python3 -m venv ./myvenv`

2. 仮装環境の活性化

`source ./mvvenv/bin/activate`

3. 現在の仮装環境非活性化

`deactivate`


##### djangoインストール

```
$ pip3 install --upgrade pip
$ pip install "django<2"
```

