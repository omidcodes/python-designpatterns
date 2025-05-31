# Target
class Logger:
    def log_info(self, message: str) -> None:
        """Log an informational message."""
        raise NotImplementedError

    def log_warning(self, message: str) -> None:
        """Log a warning message."""
        raise NotImplementedError

    def log_error(self, message: str) -> None:
        """Log an error message."""
        raise NotImplementedError
    
# Adaptee
class MetricLogger:
    def send_metric(self, level: str, payload: dict) -> None:
        """
        Sends a metric with a specified level and payload.

        - level: one of "INFO", "WARN", "ERR"
        - payload: a dict with arbitrary keys, e.g. {"msg": "..." }
        """
        print(f"[{level}] {payload['msg']}")

# Adapter
class Adapter(Logger):
    
    def __init__(self, _logger: MetricLogger):
        self._logger = _logger
    

    def log_info(self, message: str) -> None:
        """Log an informational message."""
        self._logger.send_metric(level="INFO", payload={"msg": message} )

    def log_warning(self, message: str) -> None:
        """Log a warning message."""
        self._logger.send_metric(level="WARN", payload={"msg": message} )

    def log_error(self, message: str) -> None:
        """Log an error message."""
        self._logger.send_metric(level="ERR", payload={"msg": message} )
    

metric_logger = MetricLogger()
logger = Adapter(_logger = metric_logger)

logger.log_error(message="this is a message")