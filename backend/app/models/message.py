from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.ticket import Ticket
    from app.models.user import User


class Message(Base):
    __tablename__ = "messages"

    id: int = Field(primary_key=True)
    content: str = Field(nullable=False)
    ticket_id: int = Field(foreign_key="tickets.id", nullable=False, ondelete="CASCADE")
    author_id: int = Field(foreign_key="users.id", nullable=False)

    # relationships
    ticket: "Ticket" = Relationship(back_populates="messages", foreign_keys="[ticket_id]")
    author: "User" = Relationship(back_populates="messages", foreign_keys="[author_id]")
