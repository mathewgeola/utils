import os
import platform
import zipfile
from typing import Literal, cast


class _file:
    COMPRESS_TYPE = Literal["zip"]

    @staticmethod
    def compress(
            dir_path: str,
            compress_file_path: str | None = None,
            compress_type: COMPRESS_TYPE = "zip"
    ) -> str | None:
        dir_path = os.path.abspath(dir_path)
        if not os.path.isdir(dir_path):
            return None

        if compress_file_path is None:
            compress_file_path = os.path.join(
                os.path.dirname(dir_path), os.path.basename(dir_path) + "." + compress_type
            )
        else:
            compress_file_path = os.path.abspath(compress_file_path)

        if compress_type == "zip":
            with zipfile.ZipFile(compress_file_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        if os.path.abspath(file_path) == compress_file_path:
                            continue

                        rel_file_path = os.path.relpath(file_path, dir_path)
                        zf.write(file_path, arcname=rel_file_path)
            return compress_file_path

        return None

    @staticmethod
    def decompress(
            compress_file_path: str,
            dir_path: str | None = None,
            compress_type: COMPRESS_TYPE = "zip"
    ) -> str | None:
        compress_file_path = os.path.abspath(compress_file_path)
        if not os.path.isfile(compress_file_path):
            return None

        if dir_path is None:
            dir_path = os.path.splitext(compress_file_path)[0]
        else:
            dir_path = os.path.abspath(dir_path)

        os.makedirs(dir_path, exist_ok=True)

        if compress_type == "zip":
            with zipfile.ZipFile(compress_file_path, "r") as zf:
                zf.extractall(dir_path)
            return dir_path

        return None

    @staticmethod
    def get_file_paths_and_dir_paths(path: str) -> tuple[list[str], list[str]]:
        file_paths = []
        dir_paths = []

        path = os.path.abspath(path)

        with os.scandir(path) as entries:
            for entry in entries:
                System = Literal["Windows", "Linux", "Darwin"]
                system: System = cast(System, platform.system())
                if system == "Windows":
                    from nt import DirEntry
                elif system == "Linux":
                    from posix import DirEntry
                elif system == "Darwin":
                    from posix import DirEntry
                else:
                    raise TypeError(
                        f"Invalid type for 'system': "
                        f"Expected `Literal[\"Windows\",\"Linux\",\"Darwin\"]`, "
                        f"but got {type(system).__name__!r} (value: {system!r})"
                    )

                entry: DirEntry
                if entry.is_file():
                    file_paths.append(entry.path)
                elif entry.is_dir():
                    dir_paths.append(entry.path)
                    sub_file_paths, sub_dir_paths = _file.get_file_paths_and_dir_paths(entry.path)
                    file_paths.extend(sub_file_paths)
                    dir_paths.extend(sub_dir_paths)

        return file_paths, dir_paths


__all__ = [
    "_file"
]
