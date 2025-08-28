# === main.py（テンプレ準拠・悪意テストD）===
from abc import ABC, abstractmethod
from typing import Tuple, List
Board = List[List[List[int]]]

class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]: ...

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        import other_student_main  # ← 自分フォルダ＋標準ライブラリ以外は解決不可
        return other_student_main.get_move(board)

_ai = MyAI()
def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
