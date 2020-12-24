#coding=utf-8

import difflib


def get_equal_rate_1(str1, str2):
    '''用于对比两端字符串的相似度'''
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

print(get_equal_rate_1('你好','好1你'))