<h1><b>Password Strength Checker (B2 Password Checker) - TEAM WH</b></h1>

<h2>課題概要</h2>

これはコマンドラインインターフェース（CLI）およびWebブラウザ上で動作するパスワード強度チェッカーです。
AIシステム学科の「プログラミング基礎」クラスを代表して、私たち Team WH の初めてのチームプロジェクトとして作成しました。

パスワードの長さをはじめ、文字種の複雑さやよく使われる危険なパターンを検出し、安全性を評価します。

<h2>主な機能</h2>

リアルタイム強度診断: 入力されたパスワードを Weak / Medium / Strong の3段階で総合評価し、スコアを算出します。

セキュアなパスワード生成機能: random および string ライブラリを活用し、大文字・小文字・数字・記号を組み合わせた強力な16文字のパスワードをワンクリックで自動生成します。

選べるインターフェース: 軽量でサクサク動くCLI版（starter.py）と、グラフィカルで直感的なWeb UI版（app.py）の両方を利用可能です。

<h2>使用技術</h2>

Python 3.10

<h2>標準ライブラリ</h2>
import re<br>
import string<br>
import random

<h2>サードパーティライブラリ</h2>
Streamlit (Web GUI構築用)

<h2>ファイル構成</h2>

WH_PJ
├── README.md            # このファイル
├── starter.py           # CLI版およびコア判定ロジック
├── common_pattern.py    # 危険パターン定義リスト
├── language.py          # 多言語対応用テキストデータ（想定）
└── GUI.py               # Streamlit Webアプリケーション


<h2>セットアップと実行準備</h2>

<h3>1. リポジトリのクローン</h3>

お使いのPCにプロジェクトをダウンロードします。

git clone https://github.com/khinkyaw1011/WH1.git

<h3>2. 必要なライブラリのインストール</h3>

Streamlit<br>
Python3


<h2>実行方法</h2>

Webアプリ版（Streamlit）の起動

ブラウザ上で直感的にチェックしたい場合はこちらを使用します。

streamlit run app.py


<h2>CLI版の起動</h2>

ターミナル上で素早くチェックしたい場合、またはパスワードを自動生成したい場合はこちらを使用します。

python starter.py


<h2>実行例とスコアリング</h2>

<h3>Example 1: 弱いパスワード</h3>

入力: helloworld

強度: Weak

スコア: 3

判定理由: 小文字のみで構成されており、推測されやすい単語パターンが含まれています。

<h3>Example 2: 普通のパスワード</h3>

入力: Hello World

強度: Medium

スコア: 6

判定理由: 文字長は十分にありますが、構成文字種が少なく改善の余地があります。

<h3>Example 3: 強力なパスワード</h3>

入力: Guido van Rossum@BD-31011956

強度: Strong

スコア: 8

判定理由: 12文字以上で、大文字・小文字・数字・記号が全て含まれる安全な構成です。

<h4>パスワード自動生成の実行例 (CLI)</h4>

<h4>おすすめのパスワードを生成しますか？ (y/n): y</h4>

<h4>おすすめパスワード: g#2uH!A#3rvKWU*j</h4>

<h4>強度: Strong</h4>

<h4>スコア: 9</h4>

*********************

<h2>Team WH</h2>

<h2>AIシステム学科 プログラミング基礎 チームプロジェクト</h2>
