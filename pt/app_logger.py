import json
import logging  # ✅ Required for logger to work

SENSITIVE_FIELDS = ["password", "token", "email", "ssn", "credit_card"]

# Mask function
def mask_sensitive(data):
    masked = {}
    for k, v in data.items():
        if k.lower() in SENSITIVE_FIELDS:
            masked[k] = "****"
        else:
            masked[k] = v
    return masked

# Custom formatter that filters sensitive fields
class JsonFilterFormatter(logging.Formatter):
    def format(self, record):
        try:
            parsed = json.loads(record.msg)  # msg is expected to be a JSON string
            filtered = mask_sensitive(parsed)
            record.msg = json.dumps(filtered)
        except Exception:
            pass  # If msg is not JSON, do nothing
        return super().format(record)

# Logger setup
def get_logger():
    logger = logging.getLogger("secureLogger")
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers on repeated calls
    if not logger.handlers:
        handler = logging.FileHandler("secure_app.log")
        formatter = JsonFilterFormatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

