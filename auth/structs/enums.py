# app/auth/structs/enums.py
from enum import Enum

class Role(str, Enum):
    seeker = "seeker"
    helper = "helper"
    both = "both"

class Capacity(str, Enum):
    personal = "personal"
    institutional = "institutional"