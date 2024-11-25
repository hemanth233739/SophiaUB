import os
import sys
import requests
from pytgcalls import PyTgCalls
import logging
from pyrogram import Client
from pyrogram import Client
from pymongo import MongoClient
from urllib.parse import urlparse
from motor.motor_asyncio import AsyncIOMotorClient
from subprocess import getoutput as r
from variables import *
from Restart import restart_program as rs_pg

# LOGGING
logging.basicConfig(
    format="[Sophia] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# VARIABLES

SESSION = os.environ.get("SESSION") or VAR_SESSION
API_ID = os.environ.get("API_ID") or VAR_API_ID
API_HASH = os.environ.get("API_HASH") or VAR_API_HASH
HANDLER = ["~",".","!","/","$","#"]
LOG_CHANNEL = -1002368269339
MONGO_DB_URI = os.environ.get("MONGO_DB_URI") or VAR_MONGO_DB_URI
REPO_URL = os.environ.get("YOUR_REPO_LINK") or VAR_REPO_URL
MY_VERSION = 511

if not SESSION or not API_ID or not API_HASH or not MONGO_DB_URI or not REPO_URL:
    logging.warn("You should enter the required details on variables.py or you need set env")
    exit()

# PRINT STUFFS
logging.info(f"Loaded version: {MY_VERSION}")

# GETTING REPO NAME USED FOR UPDATE MODULE
parsed_url = urlparse(REPO_URL)
path_parts = parsed_url.path.split('/')
repo_name = path_parts[2] if len(path_parts) > 2 else None

# CLIENT
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))

# DATABASE 
MONGO_DB = MongoClient(MONGO_DB_URI) # Special Thanks To KoraXD For Giving This Codes!!
DB = MONGO_DB.SOPHIA_UB
DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["SOPHIA_UB"]
GAME_DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["HYPER_GAMES"]
