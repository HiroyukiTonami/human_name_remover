
HNR
====

csvファイルを読み込み、含まれる人名を全て`'人名'`へ変換します。

## Usage

- mecab本体をインストールします。文字コード指定がある場合utf-8にしてください。[参考](https://qiita.com/yukinoi/items/990b6933d9f21ba0fb43)
- インストールしたmecab.exeにPATHを通します。Windowsにデフォルトでインストールした場合`C:\Program Files\MeCab\bin`とかにあります。
- `pip install -r requirements.txt`します。
- human_name_removerと処理したいcsvファイルを同じフォルダに入れ、実行します。
- 人名部分が全て置換されたresult.csvが出力されます。
