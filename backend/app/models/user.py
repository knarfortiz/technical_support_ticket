

from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.message import Message
    from app.models.ticket import Ticket

class User(Base):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    email: str = Field(unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    full_name: str
    is_active: bool
    role: str = Field(default="client") # client, technician, admin (Enum)
    
    #relationships
    tickets: list["Ticket"] = Relationship(back_populates="client", foreign_keys="[Ticket.user_id]")
    assigned_tickets: list["Ticket"] = Relationship(back_populates="technician", foreign_keys="[Ticket.assigned_technician_id]")
    messages: list["Message"] = Relationship(back_populates="author", foreign_keys="[Message.author_id]")