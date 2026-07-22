Password Strength Checker (B2 Password Checker)

課題概要

これはコマンドラインインターフェース（CLI）およびWebブラウザ上で動作するパスワード強度チェッカーです。
AIシステム学科の「プログラミング基礎」クラスを代表して、私たち Team WH の初めてのチームプロジェクトとして作成しました。

パスワードの長さをはじめ、文字種の複雑さやよく使われる危険なパターンを検出し、安全性を評価します。

主な機能

リアルタイム強度診断: 入力されたパスワードを Weak / Medium / Strong の3段階で総合評価し、スコアを算出します。

セキュアなパスワード生成機能: random および string ライブラリを活用し、大文字・小文字・数字・記号を組み合わせた強力な16文字のパスワードをワンクリックで自動生成します。

選べるインターフェース: 軽量でサクサク動くCLI版（starter.py）と、グラフィカルで直感的なWeb UI版（app.py）の両方を利用可能です。

使用技術

Python 3.10

標準ライブラリ: re, string, random

サードパーティライブラリ: Streamlit (Web GUI構築用)

ファイル構成

WH_PJ
├── README.md            # このファイル
├── starter.py           # CLI版およびコア判定ロジック
├── common_pattern.py    # 危険パターン定義リスト
├── language.py          # 多言語対応用テキストデータ（想定）
└── app.py               # Streamlit Webアプリケーション


セットアップと実行準備

1. リポジトリのクローン

お使いのPCにプロジェクトをダウンロードします。

git clone https://github.com/khinkyaw1011/WH_PJ.git
cd WH_PJ


2. 必要なライブラリのインストール

Streamlit
Python3


実行方法

Webアプリ版（Streamlit）の起動

ブラウザ上で直感的にチェックしたい場合はこちらを使用します。

streamlit run app.py


CLI版の起動

ターミナル上で素早くチェックしたい場合、またはパスワードを自動生成したい場合はこちらを使用します。

python starter.py


実行例とスコアリング

Example 1: 弱いパスワード

入力: helloworld

強度: Weak

スコア: 3

判定理由: 小文字のみで構成されており、推測されやすい単語パターンが含まれています。

Example 2: 普通のパスワード

入力: Hello World

強度: Medium

スコア: 6

判定理由: 文字長は十分にありますが、構成文字種が少なく改善の余地があります。

Example 3: 強力なパスワード

入力: Guido van Rossum@BD-31011956

強度: Strong

スコア: 8

判定理由: 12文字以上で、大文字・小文字・数字・記号が全て含まれる安全な構成です。

パスワード自動生成の実行例 (CLI)

おすすめのパスワードを生成しますか？ (y/n): y

おすすめパスワード: g#2uH!A#3rvKWU*j

強度: Strong

スコア: 9

Team WH

AIシステム学科 プログラミング基礎 チームプロジェクト
