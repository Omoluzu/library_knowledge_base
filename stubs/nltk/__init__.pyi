from typing import Any
import sys


class Downloader:

    def download(
        self,
        info_or_id: Any = None,
        download_dir: Any = None,
        quiet: bool = False,
        force: bool = False,
        prefix: str = "[nltk_data] ",
        halt_on_error: bool = True,
        raise_on_error: bool = False,
        print_error_to: Any = sys.stderr,
    ) -> bool: ...


_downloaded = Downloader()
download = _downloaded.download
