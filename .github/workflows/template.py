def build_prompt(data, mode, prev):
    header = f"""
━━━━━━━━━━━━━━━━━━
【米国株 市場レビュー】{ '18:07' if mode=='1807' else '6:07' } JST
（米国株 / 半導体・NVDA中心）
━━━━━━━━━━━━━━━━━━
"""

    rules = """
制約：
・数値判断は禁止
・与えられたデータのみ使用
・NVDAとSOXは同量・同粒度
・投資助言禁止
"""

    payload = f"""
データ：
{data}

前回シナリオ：
{prev}
"""

    return header + rules + payload
