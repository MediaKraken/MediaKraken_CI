'''
  Copyright (C) 2019 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

import os

from common import common_network_email
from dotenv import load_dotenv

# load .env stats
load_dotenv()

common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        'metaman@beaverbay.local',
                                        'Build images',
                                        'waffles',
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])
