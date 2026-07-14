"""B2 Password Checker starter (CLI).

専門学校1年生向けのシンプルなスターターです。
標準ライブラリだけで動作します。
"""

import re
import random
import string

COMMON_PATTERNS = [
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
    "password",
    "0123456789",
    "qwerty",
    "admin",
    "letmein",
    "apple",
    "red"
    ]
def generate_password():
    length=16
    """Generate a strong random password."""
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols="!@#$%^&*"

    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    all_characters = lowercase + uppercase + digits + symbols
    while len(password) <length:
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return "".join(password)

def check_length(password):
    """長さによる点数とコメントを返す。"""
    length = len(password)
    if length >= 16:
        return 4, "16文字以上で非常に安全です。"
    if length >= 12:
        return 3, "十分な長さがあります。"
    if length >= 8:
        return 2, "長さは最低限ありますが、もう少し長くするとより安全です。"
    return 0, "文字数が足りません。8文字以上をおすすめします。"


def check_character_types(password):
    """文字種の数を点数化する。"""
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    type_count = sum([has_lower, has_upper, has_digit, has_symbol])

    if type_count >= 4:
        return 4, "小文字・大文字・数字・記号が全て含んでいます。"
    if type_count == 3:
        return 3, "3種類の文字を使っています。もう1種類追加するとさらに安全です。"
    if type_count == 2:
        return 1, "文字種が少なめです。大文字や記号を追加しましょう。"
    return 0, "1種類の文字しか使っていません。"


def check_common_patterns(password):
    """よく使われる危険パターンをチェックする。"""
    lower = password.lower()

    for pattern in COMMON_PATTERNS:
        if pattern in lower:
            return -2, f"'{pattern}' のような推測されやすい単語が含まれています。"

    # 同じ文字が続くケースを簡易チェック
    if re.search(r"(.)\1\1", password):
        return -1, "同じ文字を3回以上続けて使っています。"

    return 1, "よく使われる危険なパターンは見つかりませんでした。"

def check_passphrase(password):
    """3つ以上の単語からなるパスフレーズをチェックする。"""

    # Split the password by spaces
    words = password.split()

    # Check if there are 3 or more words
    if len(words) >= 3:
        return 2, "3つ以上の単語を使ったパスフレーズです。"

    return 0, "3つ以上の単語で構成されたパスフレーズではありません。"


def evaluate_password(password):
    """パスワード強度を評価し、スコアとコメントを返す。"""
    if password == "":
        raise ValueError("パスワードが入力されていません。入力してください。")

    total_score = 0
    messages = []

    for checker in [check_length, check_character_types, check_common_patterns, check_passphrase]:
        score, message = checker(password)
        total_score += score
        messages.append(message)

    if total_score >= 7:
        level = "Strong"
    elif total_score >= 4:
        level = "Medium"
    else:
        level = "Weak"

    return {
        "score": total_score,
        "level": level,
        "messages": messages,
    }


def print_result(result):
    """評価結果を見やすく表示する。"""
    print("\n--- 判定結果 ---")
    print(f"強度: {result['level']}")
    print(f"スコア: {result['score']}")
    print("理由:")
    for message in result["messages"]:
        print(f"- {message}")


def main():
    print("=== B2 Password Checker (CLI Starter) ===")
    print("パスワード強度を簡易チェックします。")
    print("【入力例】")
    print("Hello123!")
    print("Blue Tiger Pizza")
    print("CorrectHorseBatteryStaple")
    print("終了するには「q」を入力してください。")

    while True:
        user_input = input("\nパスワードを入力: ").strip()
        if user_input.lower() == "q":
            print("終了します。")
            break
        else:
            resultCheck = evaluate_password(user_input)
            print_result(resultCheck)

        choice = input("\nおすすめのパスワードを生成しますか？ (y/n): ").lower()

        if choice == "y":
            print("おすすめパスワード:", generate_password())
        elif choice == "n":
            user_input = input("\nパスワードを入力: ").strip()
        if user_input.lower() == "q":
            print("終了します。")
            break

        try:
            result = evaluate_password(user_input)
            print_result(result)
        except ValueError as error:
            print(f"エラー: {error}")


# TODO:
# - 連続文字列（abc, 123, qwerty）の判定を強化する
# - 強度ごとに改善提案メッセージを分ける
# - スコア配点をチームで見直し、理由をREADMEに書く

# challenge:
# - 16文字以上の推奨ルールを導入する
# - パスフレーズ（単語3つ以上）の判定を追加する
# - Streamlit版を別ファイルで作る


if __name__ == "__main__":
    main()
