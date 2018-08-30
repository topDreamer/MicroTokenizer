from typing import (
    List
)

from MicroTokenizer import default_model_dir


class BaseTokenizer(object):
    def __init__(self, model_dir=None, *args, **kwargs):
        if model_dir is None:
            model_dir = default_model_dir

        self.model_dir = model_dir

    def load_model(self):
        raise NotImplemented

    def segment(self, message: str) -> List[str]:
        raise NotImplemented

    def train_one_line(self, token_list: List[str]):
        raise NotImplemented

    def do_train(self):
        raise NotImplemented

    def persist_to_dir(self, output_dir: str):
        raise NotImplemented
