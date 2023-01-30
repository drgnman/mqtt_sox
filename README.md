# mqtt_sox
git cloneして使ってください

```
pip install -r requirements.txt
```

sox_mqtt.pyをimportすることでmqttのpublishとsubscribeを支援します。

## Create
メタノードとしてそのトピックが扱う情報をretainerに登録します。
メタノード名はpublishの宛先となるノード名_metaとして定義されます。

## Publish
パブリッシャはNodeオブジェクトにデータをセットした上で、publishメソッドを用いてデータを配信します

## Subscribe
サブスクライバはsubscribeメソッドでnode_nameを指定してサブスクライブ登録をする
setProcessOnMessageメソッドでデータ受信時の処理を定義する。
runメソッドでサブスクライブを開始

## Node
|要素名|説明|
|----|----|
|node_name|ノード名|
|location|位置情報(緯度,経度)の順で指定|
|transducers|ノードが扱うtransducer群|
|description|備考|

## Transducer
|要素名|説明|
|----|----|
|transducer_name|Transducer名|
|unit|単位|
|min_value|想定される最小値|
|max_value|想定される最大値|
|description|備考|
