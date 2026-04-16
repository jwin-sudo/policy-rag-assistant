from __future__ import annotations

import logging

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.sampling import ParentBased, TraceIdRatioBased

from src.config import Settings

logger = logging.getLogger(__name__)


def setup_telemetry(settings: Settings) -> bool:
    if not settings.otel_enabled:
        return False

    if not settings.otel_exporter_otlp_endpoint:
        return False

    try:
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    except (ImportError, ModuleNotFoundError) as exc:
        logger.warning("Telemetry enabled but OTLP exporter import failed: %s", exc)
        return False

    try:
        provider = TracerProvider(
            resource=Resource.create({"service.name": settings.otel_service_name}),
            sampler=ParentBased(TraceIdRatioBased(settings.otel_sample_ratio)),
        )
        exporter = OTLPSpanExporter(endpoint=settings.otel_exporter_otlp_endpoint)
        provider.add_span_processor(BatchSpanProcessor(exporter))
        trace.set_tracer_provider(provider)
    except Exception as exc:
        logger.warning("Telemetry setup failed and was disabled: %s", exc)
        return False

    return True


def get_tracer(name: str):
    return trace.get_tracer(name)
