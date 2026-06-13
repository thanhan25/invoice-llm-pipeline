class InvoicePipelineError(Exception):
    """Base structural exception class for all errors inside the invoice pipeline framework."""

    pass


class DocumentIngestionError(InvoicePipelineError):
    """Raised when an asset payload fails data extraction, storage, or validation rules."""

    pass


class LLMInferenceError(InvoicePipelineError):
    """Raised when structured prompting generation or inference output layers fail formatting constraints."""

    pass


class FeedbackLoggingError(InvoicePipelineError):
    """Raised when human-in-the-loop compliance records cannot be written to persistent storage layers."""

    pass
