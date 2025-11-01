import inspect
import os


class _assets:
    @staticmethod
    def get_assets_file_path(rel_file_path: str) -> str:
        _src_dir_path = os.path.splitext(os.path.abspath(__file__))[0]

        stack = inspect.stack()
        caller_frame = stack[1]
        _dest_dir_path = os.path.splitext(os.path.abspath(caller_frame.filename))[0]
        _rel_dir_path = os.path.relpath(_dest_dir_path, _src_dir_path).lstrip(os.path.pardir + os.path.sep)

        dir_path = os.path.join(_src_dir_path, _rel_dir_path)
        file_path = os.path.join(dir_path, rel_file_path)
        return file_path


__all__ = [
    "_assets"
]
