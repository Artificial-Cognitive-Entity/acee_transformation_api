
class Error(Exception):
    """Base class for other exceptions"""
    pass

class BucketAccessError(Error):
    """Raised when there is an issue accessing the GCP bucket"""
    pass

class DataProcessingError(Error):
    """Raised when there is an issue processing the data"""
    pass

# You can define more custom exceptions as needed
