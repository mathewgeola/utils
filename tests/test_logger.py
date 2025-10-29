from utils import logger as _logger


def test_logger():
    logger = _logger.logger
    logger = _logger.get_logger(__name__, to_console=True, to_file=True, file_max_bytes=10, file_backup_count=3)

    logger.debug("debug message")
    logger.info("info message")
    logger.success("success message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    logger.framework("framework message")


if __name__ == '__main__':
    test_logger()
