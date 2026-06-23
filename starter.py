
専門学校1年生向けのシンプルなスターターです。
標準ライブラリだけで動作します。
"""

import re


COMMON_PATTERNS = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein",
]


def check_length(password):
    """長さによる点数とコメントを返す。"""
    length = len(password)
    if length >= 12:
        return 3, "長さは十分です。"
    if length >= 8:
        return 2, "長さは最低ラインです。"
    return 0, "8文字未満です。もっと長くしましょう。"


def check_character_types(password):
    """文字種の数を点数化する。"""
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    type_count = sum([has_lower, has_upper, has_digit, has_symbol])

    if type_count >= 4:
        return 4, "小文字・大文字・数字・記号を含んでいます。"
    if type_count == 3:
        return 3, "文字種は3種類です。もう1種類あるとより強くなります。"
    if type_count == 2:
        return 1, "文字種が少なめです。大文字や記号を追加しましょう。"
    return 0, "1種類の文字しか使っていません。"


def check_common_patterns(password):
    """よく使われる危険パターンをチェックする。"""
    lower = password.lower()

    for pattern in COMMON_PATTERNS:
        if pattern in lower:
            return -2, f"推測されやすい語 '{pattern}' が含まれています。"

    # 同じ文字が続くケースを簡易チェック
    if re.search(r"(.)\1\1", password):
        return -1, "同じ文字の繰り返しが多いです。"

    return 1, "危険なパターンは見つかりませんでした。"


def evaluate_password(password):
    """パスワード強度を評価し、スコアとコメントを返す。"""
    if password == "":
        raise ValueError("空のパスワードは評価できません。")

    total_score = 0
    messages = []

    for checker in [check_length, check_character_types, check_common_patterns]:
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
    print("終了したいときは 'q' を入力してください。")

    while True:
        language = input("Choose language (en/jp): ").strip().lower()
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
