"""
Audit logging model.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.mixins import TimestampMixin
from app.models.mixins import UUIDMixin


class AuditLog(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "audit_logs"

    user_id: Mapped[str | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    action: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    resource: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(64),
    )

    user_agent: Mapped[str | None] = mapped_column(
        String(255),
    )

    event_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    user = relationship(
        "User",
        back_populates="audit_logs",
    )