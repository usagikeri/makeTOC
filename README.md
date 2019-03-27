# daimoku__generator
題目を自動生成するスクリプト．

# Discription
題目を自動生成するスクリプト．
実行するとout.texという名前にcsvファイルに書かれた情報がtexの書式で出力される．

現在は，B3，B4，M1の三学年が出力される．
学部生のみが必要な場合は出力されたファイルからその部分を削除する．

# Install

```
$ git clone
```

# Usage
B3.csvにB3の学籍番号，名前，タイトルを記述する．
B4，M1も同様に記述する．

# Run

```
$python create_daimoku.py
```

# Future Relese
オプションで必要な学年を選択できるようにする．
