import uuid
from enum import Enum

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

##############################
# BLOCK WITH DATABASE MODELS #
##############################


Base = declarative_base()


class PortalRole(str, Enum):
    ROLE_PORTAL_USER = 'ROLE_PORTAL_USER'
    ROLE_PORTAL_ADMIN = 'ROLE_PORTAL_ADMIN'
    ROLE_PORTAL_SUPERADMIN = 'ROLE_PORTAL_SUPERADMIN'


class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)



