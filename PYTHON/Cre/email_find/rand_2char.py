import random

def rand_2char():
    words = [
        "东风", "何处", "人间", "风流", "归去", "春风", "西风", "归来", "江南", "相思", "梅花", "千里",
        "回首", "明月", "多少", "如今", "阑干", "年年", "万里", "一笑", "黄昏", "当年", "天涯", "相逢",
        "芳草", "尊前", "一枝", "风雨", "流水", "依旧", "风吹", "风月", "多情", "故人", "当时", "无人",
        "斜阳", "不知", "不见", "深处", "时节", "平生", "凄凉", "春色", "匆匆", "功名", "一点", "无限",
        "今日", "天上", "杨柳", "西湖", "桃花", "扁舟", "消息", "憔悴", "何事", "芙蓉", "神仙", "一片",
        "桃李", "人生", "十分", "心事", "黄花", "一声", "佳人", "长安", "东君", "断肠", "而今", "鸳鸯",
        "为谁", "十年", "去年", "少年", "海棠", "寂寞", "无情", "不是", "时候", "肠断", "富贵", "蓬莱",
        "昨夜", "行人", "今夜", "谁知", "不似", "江上", "悠悠", "几度", "青山", "何时", "天气", "惟有",
        "一曲", "月明", "往事"
    ]
    num = random.randint(0, 98)
    print(words[num])

rand_2char()