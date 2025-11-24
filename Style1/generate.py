#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
江苏大学课程报告封面生成脚本
运行后输入信息，自动生成PDF并清理临时文件
"""

import subprocess
import os

def main():
    print("=" * 40)
    print("  江苏大学课程报告封面生成器")
    print("=" * 40)
    print()

    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # 获取用户信息
    student_id = input("请输入学号: ").strip()
    class_name = input("请输入班级: ").strip()
    name = input("请输入姓名: ").strip()
    title = input("请输入题目: ").strip()
    report_type = input("请输入报告类型 (如: 智能通信技术基础 XX 任务): ").strip()
    date = input("请输入日期 (如: 2025年11月): ").strip() or "2025年11月"

    # 读取模板
    template = r'''\documentclass[a4paper,12pt]{article}
\usepackage{ctex}
\usepackage{graphicx}
\usepackage{geometry}

% 页面设置
\geometry{left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm}

% 字体设置 - 全部使用黑体
\setCJKfamilyfont{hei}{SimHei}
\newcommand{\hei}{\CJKfamily{hei}}

% 字号定义
\newcommand{\yihao}{\fontsize{26pt}{39pt}\selectfont}
\newcommand{\sanhao}{\fontsize{16pt}{24pt}\selectfont}

% 固定宽度标签
\newcommand{\infolabel}[1]{\makebox[5em][s]{#1}}

\begin{document}
\pagestyle{empty}

\begin{center}

% 标题
\vspace*{1cm}
{\yihao\hei 江\ 苏\ 大\ 学\ 课\ 程\ 报\ 告}

\vspace{2cm}

% 校徽
\includegraphics[width=5cm]{UJS-source/jsulogo绿色.pdf}

\vspace{2cm}

% 题目
{\sanhao\hei TITLE_STR}

\vspace{1.5cm}

\end{center}

% 信息区域
\begin{flushleft}
\hspace{3cm}
\begin{minipage}{12cm}
{\sanhao\hei
\infolabel{学号}：\underline{\makebox[7.5cm]{STUDENT_ID}}\\[0.8cm]
\infolabel{班级}：\underline{\makebox[7.5cm]{CLASS_NAME}}\\[0.8cm]
\infolabel{姓名}：\underline{\makebox[7.5cm]{STUDENT_NAME}}\\[0.8cm]
\infolabel{报告类型}：\underline{\makebox[7.5cm]{REPORT_TYPE}}
}
\end{minipage}
\end{flushleft}

\vfill

% 底部日期
\begin{center}
{\sanhao\hei DATE_STR}
\end{center}

\vspace{1cm}

\end{document}
'''

    # 生成 tex 文件
    content = template.replace('STUDENT_ID', student_id)
    content = content.replace('CLASS_NAME', class_name)
    content = content.replace('STUDENT_NAME', name)
    content = content.replace('TITLE_STR', title)
    content = content.replace('REPORT_TYPE', report_type)
    content = content.replace('DATE_STR', date)

    output_tex = "cover.tex"
    output_pdf = "cover.pdf"

    with open(output_tex, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n正在编译...")

    # 编译
    result = subprocess.run(
        ['xelatex', '-interaction=nonstopmode', output_tex],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )

    if result.returncode == 0 and os.path.exists(output_pdf):
        print(f"✓ 生成成功: {output_pdf}")
    else:
        print("✗ 编译失败，请检查错误信息")
        print(result.stdout)
        return

    # 清理临时文件
    for ext in ['.aux', '.log']:
        temp_file = f"cover{ext}"
        if os.path.exists(temp_file):
            os.remove(temp_file)

    print("✓ 临时文件已清理")

if __name__ == "__main__":
    main()
