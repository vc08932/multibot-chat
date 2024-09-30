import os
import tempfile
import logging
import string
import random
from bot.config import ENGINE_CONFIG

# token 的过期时间（以秒为单位）
# 默认为 86400 秒（1天）
TOKEN_EXPIRATION = int(os.getenv('MULTIBOT_TOKEN_EXPIRATION', 86400))

# token 文件存储的基础目录
# 如果不设置（即为空字符串），系统会使用系统临时目录：
# 如果设置路径，将使用 TOKEN_BASEDIR 下的 'streamlit_tokens' 文件夹
TOKEN_BASEDIR = ""
if TOKEN_BASEDIR:
    TOKEN_DIR = os.path.join(TOKEN_BASEDIR, 'streamlit_tokens')
else:
    TOKEN_DIR = os.path.join(tempfile.gettempdir(), 'streamlit_tokens')

secret_key_file = os.getenv('MULTIBOT_SECRET_KEY_FILE', 'secret.key')

if os.path.exists(secret_key_file):
    with open(secret_key_file, 'r') as f:
        SECRET_KEY = f.read().strip()
else:
    characters = string.ascii_letters + string.digits
    SECRET_KEY = ''.join(random.choice(characters) for _ in range(32))
    with open(secret_key_file, 'w') as f:
        f.write(SECRET_KEY)

# 用户配置文件的存储基础目录
USER_CONFIG_BASEDIR = os.getenv('MULTIBOT_USER_CONFIG_BASEDIR', './user_config')

# 用户数据文件的路径
USER_DATA_FILE = os.getenv('MULTIBOT_USER_DATA_FILE', 'users.json')

# 表情选项
EMOJI_OPTIONS = ["🤖", "🦾", "🧠", "💡", "✏️", "🔭", "🔮", "🎭", "😄", "😘", "🤪", "🧐", "🤠", "🦄", "🐼", "🦊", "🐶", "🐱", "🦁", "🐯", "🐻", "🐨", "🤡", "👻", "😈", "🤠", "🙊", "😽", "🐷", "🐰", "🐼", "🐮", "🐺", "👽", "🧑‍🎓", "🧑‍💼", "🧑‍🎨", "🧑‍✈️", "🥷", "🧙", "🧞‍♂️"]

# 引擎选项
ENGINE_OPTIONS = list(ENGINE_CONFIG.get('engines', {}).keys())

# 定义群聊和私聊的emoji表情
GROUP_CHAT_EMOJI = "👥"
PRIVATE_CHAT_EMOJI = "👤"

# 是否显示密钥信息
SHOW_SECRET_INFO = os.getenv('MULTIBOT_SHOW_SECRET_INFO', 'False').lower() == 'true'

# 日志设置
LOG_LEVEL = os.getenv('MULTIBOT_LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL)
LOGGER = logging.getLogger(__name__)
