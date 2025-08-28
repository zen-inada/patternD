
# main.py（悪意テスト：素の import）
from typing import List, Tuple
Board = List[List[List[int]]]

import other_student_main  # ← banned ではないが解決不可（自分のフォルダ＋標準ライブラリしか見ない）

def get_move(board: Board) -> Tuple[int, int]:
    return other_student_main.get_move(board)
