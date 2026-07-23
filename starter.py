"""B2 Password Checker starter (CLI).

専門学校1年生向けのシンプルなスターターです。
標準ライブラリだけで動作します。
"""

import re
import random
import string
from commonPattern import COMMON_PATTERNS
from language import LANG

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

def check_length(password, text):

    length = len(password)

    if length >= 16:
        return 4, text["length_16"]

    if length >= 12:
        return 3, text["length_12"]

    if length >= 8:
        return 2, text["length_8"]

    return 0, text["length_short"]
def check_character_types(password, text):

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    type_count = sum([has_lower, has_upper, has_digit, has_symbol])

    if type_count >= 4:
        return 4, text["type_4"]

    if type_count == 3:
        return 3, text["type_3"]

    if type_count == 2:
        return 1, text["type_2"]

    return 0, text["type_1"]

def check_common_patterns(password, text):

    lower = password.lower()

    for pattern in COMMON_PATTERNS:
        if pattern in lower:
            return -2, text["common_pattern"].format(pattern=pattern)

    if re.search(r"(.)\1\1", password):
        return -1, text["repeat"]

    return 1, text["safe_pattern"]

def check_passphrase(password, text):

    words = password.split()

    if len(words) >= 3:
        return 2, text["passphrase_yes"]

    return 0, text["passphrase_no"]

def evaluate_password(password, language="English"):

    text = LANG[language]

    if password == "":
        raise ValueError(text["empty"])

    total_score = 0
    messages = []

    checkers = [
        check_length,
        check_character_types,
        check_common_patterns,
        check_passphrase,
    ]

    for checker in checkers:
        score, message = checker(password, text)
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