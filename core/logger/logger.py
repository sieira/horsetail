"""
Copyright © 2016 Luis Sieira Garcia
This file is part of horsetail.
    Horsetail is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Horsetail is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with along with horsetail. If not, see <http://www.gnu.org/licenses/>.
"""
from functools import partial
from django.utils import timezone


from core.core_module import CoreModule


class Logger(CoreModule):
    class Color(object):
        BLUE_FG = '\x1b[34m'
        GREEN_FG = '\x1b[32m'
        MAGENTA_FG = '\x1b[35m'
        RED_FG = '\x1b[31m'
        RESET = '\x1b[0m'
        YELLOW_FG = '\x1b[33m'

    @classmethod
    def ANSI_logger(tag, color, *args):
        print('{color} [{tag}] {message} [{timestamp}]'.format(color=color,
                                                               tag=tag,
                                                               message=' '.join(*args),
                                                               timestamp=timezone.now()))

Logger.info = partial(Logger.ANSI_logger('i', Logger.Color.YELLOW_FG))
Logger.error = partial(Logger.ANSI_logger('x', Logger.Color.RED_FG))
Logger.http = partial(Logger.ANSI_logger('ǁ', Logger.Color.BLUE_FG))
# TODO log stacktraces
# TODO decorator for http logger
