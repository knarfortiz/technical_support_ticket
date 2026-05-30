from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.message import Message
    from app.models.user import User


class Ticket(Base):
    __tablename__ = "tickets"

    id: int = Field(primary_key=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    status: str = Field(default="open") # open, in_progress, closed (Enum)
    priority: str = Field(default="medium") # low, medium, high
    user_id: int = Field(foreign_key="users.id", nullable=False)
    assigned_technician_id: int = Field(foreign_key="users.id")

    # relationships
    client: "User" = Relationship(back_populates="tickets", foreign_keys="[user_id]")
    technician: "User" = Relationship(back_populates="assigned_tickets", foreign_keys="[assigned_technician_id]")
    messages: list["Message"] = Relationship(back_populates="ticket", cascade_delete=True)