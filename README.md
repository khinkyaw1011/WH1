# B2 Password Checker (Starter)

## 課題概要
CLIで動くパスワード強度チェッカーを作る課題です。
まずは標準ライブラリだけで、基本的な判定ロジックを実装します。

この課題は完成品ではありません。TODO と challenge を進めながら、
自分たちで改善していく前提です。

## 学習目標
- 文字列処理と条件分岐の基本を身につける
- 「長さ」「文字種」「推測されやすい文字列」の観点で強度評価できる
- CLIアプリの入出力を実装できる
- private GitHub repository でチーム開発できる

## 使用技術
- Python 3.10+
- 標準ライブラリのみ

## ファイル構成
- `README.md`: 課題説明と実行方法
- `starter.py`: CLIスターターコード
- `requirements.txt`: 外部依存の有無

## セットアップ
### 1) private repository から clone

```bash
git clone <YOUR_PRIVATE_REPOSITORY_URL>
cd ai-programming-2026-team-project-1-starter/B_app_development/B2_password_checker
```

### 2) 実行準備
- Python 3.10以上があれば実行できます。
- このstarterは標準ライブラリのみなので、追加インストールは不要です。

## 実行方法

```bash
python3 starter.py
```

## 期待される出力例
- 入力: `password`
	- 強度: Weak
	- 理由: 長さ不足、小文字のみ、よく使われる語に近い

- 入力: `G7!m2#Qx9`
	- 強度: Strong
	- 理由: 長さ十分、複数文字種を含む

## 評価ルール（starter版）
- 長さ
- 文字種（小文字・大文字・数字・記号）
- 推測されやすいパターン（`password`, `123456`, `qwerty` など）

## TODO（学生が実装する項目）
- [ ] 連続文字（`abc`, `123`）の検出を改善する
- [ ] 日本語メッセージをもっと分かりやすくする
- [ ] スコア計算の基準をチームで再設計する
- [ ] 判定結果をログに保存する

## Challenge（発展課題）
- Challenge 1: 複数パスワードをまとめて評価するモードを追加する
- Challenge 2: 使ってはいけない単語リストを外部ファイルで管理する
- Challenge 3: パスワード生成機能を追加する
- Challenge 4: Streamlit版を別ファイル（app.py）として作る
- Challenge 5: pytestで判定関数のテストを作る

## 使いやすさ・実行しやすさの指針（課題B共通）
- 実行コマンドをREADMEに必ず記載する
- 入力例を表示して、初めてでも試しやすくする
- エラー時は「次に何を入力すればよいか」を示す

## GitHub運用（private repository 推奨）
- private repository に限定メンバーを追加して運用する
- `main` を安定版、日々の作業は `develop` や作業ブランチで進める
- Issue / Pull Request を使って、変更理由を残す
- READMEは常に最新の実行方法へ更新する

## 提出時チェック
- [ ] CLIが起動する
- [ ] 2種類以上のパスワードで強度判定が確認できる
- [ ] TODOを最低3項目進めた
- [ ] READMEの実行方法が最新
